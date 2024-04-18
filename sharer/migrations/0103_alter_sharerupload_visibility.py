# Generated by Django 4.2.10 on 2024-03-27 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0102_remove_sharer_followers_tier1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharerupload',
            name='visibility',
            field=models.CharField(choices=[('ALL', 'All (followers and non-followers)'), ('NON_FOLLOWER', 'Preview Content'), ('FOLLOWERS_TIER1', 'BRONZE - Tier'), ('FOLLOWERS_TIER2', 'SILVER - Tier'), ('FOLLOWERS_TIER3', 'GOLD - Tier')], default='ALL', max_length=100),
        ),
    ]
