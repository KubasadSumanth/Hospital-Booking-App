# Generated by Django 3.2.2 on 2021-06-09 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_hospitals_patients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitals',
            name='noOfSeats',
            field=models.IntegerField(),
        ),
    ]