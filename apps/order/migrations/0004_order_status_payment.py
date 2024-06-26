# Generated by Django 4.2.11 on 2024-05-15 09:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('country', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('order', models.ManyToManyField(related_name='payment', to='order.order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
