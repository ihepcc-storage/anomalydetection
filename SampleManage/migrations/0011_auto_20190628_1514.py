# Generated by Django 2.1.1 on 2019-06-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SampleManage', '0010_auto_20190611_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictmethod',
            name='paramvalue',
            field=models.CharField(max_length=3000),
        ),
    ]
