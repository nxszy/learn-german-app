# Generated by Django 5.0 on 2024-03-10 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verbs', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='conjverb',
            unique_together={('translation', 'infinitive')},
        ),
        migrations.AlterField(
            model_name='conjverb',
            name='translation',
            field=models.CharField(max_length=30),
        )
    ]
