# Generated by Django 4.0.4 on 2022-04-21 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_car_car_user_alter_car_car_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='location',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.CharField(choices=[('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('Trucks', 'Trucks'), ('Coupes', 'Coupes'), ('Minivans', 'Minivans'), ('Crossovers', 'Crossovers'), ('Convertible', 'Convertible'), ('Van', 'Van'), ('SUVs', 'SUVs')], max_length=100),
        ),
    ]