# Generated by Django 4.2.13 on 2024-05-26 11:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('work_hours', models.CharField(max_length=50)),
                ('facebook', models.CharField(max_length=50)),
                ('youtube', models.CharField(max_length=350)),
                ('twitter', models.CharField(max_length=250)),
                ('instagram', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]