# Generated by Django 2.2.5 on 2021-04-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio_App', '0002_about_banner_experience_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='site_pics', verbose_name='Image')),
                ('name', models.CharField(max_length=220, verbose_name='Put Clinet Name!!')),
                ('description', models.TextField(max_length=220, verbose_name='client Thougths!!')),
                ('prof_name', models.CharField(max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('cupon', models.CharField(max_length=120, null=True, verbose_name='put Discount!')),
                ('details', models.TextField(max_length=220, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=120, null=True)),
                ('subscription', models.CharField(max_length=120, null=True)),
                ('price_description', models.CharField(max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=120, null=True)),
                ('title', models.CharField(max_length=120, null=True)),
                ('filter', models.CharField(max_length=120, null=True)),
                ('service_image', models.ImageField(upload_to='site_pics', verbose_name='Image')),
                ('servie_text', models.CharField(max_length=120, null=True)),
            ],
        ),
    ]
