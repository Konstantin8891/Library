from rest_framework import serializers

from events.models import Organization, Event
from users.models import CustomUser


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationForEventSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    users = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = (
            'title',
            'description',
            'address',
            'users'
        )

    def get_address(self, obj):
        return obj.postcode + ' ' + obj.address

    def get_users(self, obj):
        organization_id = obj.id
        users = CustomUser.objects.filter(
            organization_id=organization_id
        ).values_list('username', flat=True)
        return users


class EventCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        organizations = validated_data.pop("organizations")
        event = Event.objects.create(
            title=validated_data.pop("title"),
            description=validated_data.pop("description"),
            image=validated_data.pop("image"),
            date=validated_data.pop("date"),
        )
        event.organizations.set(organizations)
        return event


class EventReturnedViewSerializer(serializers.ModelSerializer):
    organizations = OrganizationSerializer(read_only=True, many=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'title',
            'description',
            'organizations',
            'image',
            'date'
        )

    def get_image(self, obj):
        # print(dir(obj.image))
        request = self.context.get('request')
        uri = obj.image.url
        return request.build_absolute_uri(uri)


class EventViewSerializer(serializers.ModelSerializer):
    organizations = OrganizationForEventSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = '__all__'
