# Generated by Django 2.1.5 on 2019-06-07 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name_plural': 'Services'},
        ),
        migrations.AlterModelOptions(
            name='whyus',
            options={'verbose_name_plural': 'WhyUs'},
        ),
    ]
