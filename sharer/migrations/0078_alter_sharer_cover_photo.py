# Generated by Django 4.2.10 on 2024-03-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0077_sharer_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharer',
            name='cover_photo',
            field=models.ImageField(blank=True, default='uploads/default/default_cover.jpg', null=True, upload_to='cover_photos'),
        ),
    ]
