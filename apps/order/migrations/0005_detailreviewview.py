# Generated by Django 4.2.13 on 2024-05-26 11:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_status_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailReviewView',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
