# Generated by Django 2.2.6 on 2019-11-19 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Lallog', '0007_auto_20191113_1112'),
        ('curier', '0002_auto_20191119_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_orders', to='curier.Curier')),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myorders', to='Lallog.Lalo')),
            ],
        ),
    ]
