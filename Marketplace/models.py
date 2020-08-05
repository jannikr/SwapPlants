from django.db import models


# Create your models here.

class Plant(models.Model):
    PLANT_CATEGORIES = [
        ('O', 'Obst'),
        ('G', 'Gemüse'),
        ('Z', 'Zierpflanze'),
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

    # user = models.ForeignKey(ShopUser,
    #                             on_delete=models.CASCADE,
    #                             related_name='user',
    #                             related_query_name='users')

    image = models.ImageField(null=True)
    plant_type = models.CharField(max_length=1, choices=PLANT_CATEGORIES)
    market_type = models.CharField(max_length=1, choices=MARKET_CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    reserved = models.BooleanField(default=False)
    city = models.CharField(max_length=30)
    zip_code = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['created_at', 'title']
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'
