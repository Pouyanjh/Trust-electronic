# Generated by Django 5.0.1 on 2024-01-27 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_popproduct_topproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='electronicalParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ElectronicEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ReceiverandRemote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='touchKeys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
