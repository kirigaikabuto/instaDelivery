# Generated by Django 2.2.6 on 2019-12-19 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curier', '0003_auto_20191219_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curier',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mycurier', to=settings.AUTH_USER_MODEL),
        ),
    ]
