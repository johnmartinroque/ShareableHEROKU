# Generated by Django 4.2.4 on 2024-02-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0009_remove_sharerupload_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharerupload',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/images'),
        ),
    ]
