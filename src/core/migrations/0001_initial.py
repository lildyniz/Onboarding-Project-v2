# Generated by Django 5.0.4 on 2024-05-01 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_type', models.CharField(choices=[('Общепит', 'Catering'), ('Ритейл', 'Retail'), ('Туризм', 'Tourism')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Directions', to='core.business')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Users', to='core.business')),
            ],
        ),
    ]
