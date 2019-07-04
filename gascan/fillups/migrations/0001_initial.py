# Generated by Django 2.2.2 on 2019-06-28 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fillup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fillup_date', models.DateTimeField()),
                ('odometer', models.DecimalField(decimal_places=1, max_digits=20)),
                ('gas_gallons', models.DecimalField(decimal_places=3, max_digits=5)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=12, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=12, null=True)),
                ('car', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cars.Car')),
            ],
            options={
                'verbose_name_plural': 'fillups',
            },
        ),
    ]
