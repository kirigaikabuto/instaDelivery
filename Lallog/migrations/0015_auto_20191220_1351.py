# Generated by Django 2.2.6 on 2019-12-20 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lallog', '0014_auto_20191219_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='testorder',
            name='nal',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1000),
        ),
        migrations.AddField(
            model_name='testorder',
            name='raschet',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1000),
        ),
    ]