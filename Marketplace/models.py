from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
from django.db.models.signals import pre_save
from SwapPlants.util import unique_slug_generator


class Plant(models.Model):
    PLANT_CATEGORIES = [
        ('O', 'Obst'),
        ('G', 'Gemüse'),
        ('Z', 'Zierpflanze'),
        ('K', 'Kraut'),
    ]

    MARKET_CATEGORIES = [
        ('V', 'Verschenken'),
        ('T', 'Tauschen'),
    ]

    LOCATION_CATEGORIES = [
        ('Sc', 'Schatten'),
        ('H', 'Halbschatten'),
        ('So', 'Sonne'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    # TODO only offer months to the customer:
    # https://stackoverflow.com/questions/30017229/how-to-represent-month-as-field-on-django-model
    flowering_time = models.DateField(auto_now_add=False, blank=True, null=True)
    harvest_time = models.DateField(auto_now_add=False, blank=True, null=True)

    perennial = models.BooleanField(blank=True, null=True)
    hardy = models.BooleanField(blank=True, null=True)
    location_type = models.CharField(max_length=2, choices=LOCATION_CATEGORIES, blank=True, null=True)

    user = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='users',
                                related_query_name='user')

    image = models.ImageField(null=True)
    plant_type = models.CharField(max_length=1, choices=PLANT_CATEGORIES)
    market_type = models.CharField(max_length=1, choices=MARKET_CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    reserved = models.BooleanField(default=False)
    city = models.CharField(max_length=30)
    zip_code = models.IntegerField(blank=True, null=True)

    slug = models.SlugField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ['created_at', 'title']
        index_together = ('title', 'slug')
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Plant)
