# Generated by Django 4.2.10 on 2024-03-21 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0084_tipbox_dashboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='total_comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='total_earnings',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='total_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='total_uploads',
            field=models.IntegerField(default=0),
        ),
    ]
