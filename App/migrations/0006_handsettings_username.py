# Generated by Django 3.1.4 on 2022-01-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20220110_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='handsettings',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
