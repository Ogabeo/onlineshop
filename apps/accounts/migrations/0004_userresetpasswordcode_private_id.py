# Generated by Django 4.2.11 on 2024-04-19 05:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresetpasswordcode',
            name='private_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]