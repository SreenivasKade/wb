# Generated by Django 3.1.4 on 2021-08-11 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='movement',
            field=models.CharField(choices=[('up', 'up'), ('down', 'down'), ('left', 'left'), ('right', 'right'), ('stop', 'stop')], max_length=10),
        ),
    ]
