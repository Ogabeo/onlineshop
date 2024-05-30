# Generated by Django 4.2.13 on 2024-05-29 13:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_about_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailReviewModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=250)),
                ('comment', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
