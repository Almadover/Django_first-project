# Generated by Django 5.0.2 on 2024-02-18 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('subject', models.CharField(max_length=10, verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('group', models.CharField(max_length=10, verbose_name='Класс')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.teacher')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
            },
        ),
    ]
