# Generated by Django 3.0.5 on 2020-06-20 00:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_auto_20200620_0538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('basic_rate', models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('hsn_sac', models.CharField(blank=True, max_length=100)),
                ('gst_percentage', models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('manufacturer', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manufacturer', to='myapi.Vendor')),
            ],
        ),
    ]
