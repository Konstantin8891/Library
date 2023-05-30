from django.db import models
from django.utils.safestring import mark_safe


class Organization(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    address = models.TextField()
    postcode = models.CharField(max_length=15)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    organizations = models.ManyToManyField(Organization, related_name='events')
    image = models.ImageField(upload_to='images')
    date = models.DateField()

    def __str__(self):
        return self.title

    def get_organizations(self):
        return ",".join([str(p) for p in self.organizations.all()])

    def image_icon(self):
        if self.image:
            return mark_safe(
                u'<a href="{0}" target="_blank">'
                u'<img src="{0}" width="100"/></a>'.format(self.image.url)
            )
        else:
            return '(Нет изображения)'


class EventOrganization(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
