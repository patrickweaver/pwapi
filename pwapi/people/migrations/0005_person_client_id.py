# Generated by Django 2.1.5 on 2019-04-13 01:45

from django.db import migrations, models
import people.models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20180927_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='client_id',
            field=models.CharField(blank=True, default=people.models.generate_api_key, max_length=255, unique=True),
        ),
    ]
