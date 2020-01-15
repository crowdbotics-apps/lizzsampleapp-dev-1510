# Generated by Django 2.2.9 on 2020-01-15 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel', models.CharField(max_length=256)),
                ('bhp', models.BigIntegerField()),
                ('torque', models.FloatField()),
                ('description', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='engine_description', to='home.CustomText')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=256)),
                ('year', models.DateField()),
                ('brand', models.CharField(max_length=256)),
                ('doors', models.BigIntegerField()),
                ('description', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_description', to='home.CustomText')),
                ('engine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_engine', to='home.Engine')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
