# Generated by Django 3.2.12 on 2022-03-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_event_drupal_node_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='website',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
