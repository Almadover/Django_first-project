# Generated by Django 5.0.2 on 2024-02-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='photos/%/%/%/')),
                ('release_date', models.DateField()),
                ('lte_exists', models.CharField(max_length=5)),
                ('slug', models.SlugField(max_length=300, unique=True)),
            ],
        ),
    ]
