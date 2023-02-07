# Generated by Django 4.1.5 on 2023-02-06 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='productdata',
            fields=[
                
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_descrition', models.CharField(max_length=500)),
                ('product_prize', models.IntegerField()),
                ('product_image', models.ImageField(default='media/file/photos/OIP_1.jfif', upload_to='media/files/photos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
