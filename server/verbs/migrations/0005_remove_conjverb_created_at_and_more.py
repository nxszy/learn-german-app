# Generated by Django 5.0 on 2024-03-21 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verbs', '0004_remove_conjverb_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conjverb',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='conjverb',
            name='updated_at',
        ),
    ]
