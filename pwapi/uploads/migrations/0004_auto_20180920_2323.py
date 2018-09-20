# Generated by Django 2.1 on 2018-09-20 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0003_auto_20180916_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='url',
            field=models.CharField(default='', max_length=2048, unique=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='uuid',
            field=models.CharField(blank=True, default='', max_length=1024, unique=True),
        ),
    ]
