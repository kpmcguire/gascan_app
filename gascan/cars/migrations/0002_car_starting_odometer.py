# Generated by Django 2.2.2 on 2019-07-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='starting_odometer',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=20),
        ),
    ]
