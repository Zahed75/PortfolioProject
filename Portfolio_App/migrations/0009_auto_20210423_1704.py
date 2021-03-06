# Generated by Django 2.2.5 on 2021-04-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio_App', '0008_auto_20210423_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_image',
            field=models.ImageField(blank=True, upload_to='portfolio_pics', verbose_name='about picture'),
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(blank=True, max_length=220),
        ),
        migrations.AlterField(
            model_name='about',
            name='heading',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='about',
            name='percentage',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='about',
            name='skill_name',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
