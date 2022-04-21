# Generated by Django 4.0.4 on 2022-04-21 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_car_car_user_alter_car_car_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_user',
        ),
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.CharField(choices=[('Coupes', 'Coupes'), ('Van', 'Van'), ('Minivans', 'Minivans'), ('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('Convertible', 'Convertible'), ('SUVs', 'SUVs'), ('Crossovers', 'Crossovers'), ('Trucks', 'Trucks')], max_length=100),
        ),
    ]
