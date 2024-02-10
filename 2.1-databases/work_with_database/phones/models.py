from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='photos/%/%/%/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=300, unique=True, db_index=True)
