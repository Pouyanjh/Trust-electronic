# Generated by Django 5.0.1 on 2024-01-22 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popproduct',
            fields=[
                ('title', models.CharField(blank=True, max_length=100, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.URLField(blank=True, max_length=500)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'popproduct',
                'verbose_name_plural': 'popproducts',
            },
        ),
        migrations.CreateModel(
            name='Topproduct',
            fields=[
                ('title', models.CharField(blank=True, max_length=100, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.URLField(blank=True, max_length=500)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'topproduct',
                'verbose_name_plural': 'topproducts',
            },
        ),
    ]
