# Generated by Django 4.2.11 on 2024-05-14 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_review_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
    ]
