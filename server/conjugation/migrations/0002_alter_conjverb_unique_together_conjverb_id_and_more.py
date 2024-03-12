# Generated by Django 5.0 on 2024-03-10 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conjugation', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='conjverb',
            unique_together={('translation', 'infinitive')},
        ),
        migrations.AddField(
            model_name='conjverb',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conjverb',
            name='translation',
            field=models.CharField(max_length=30),
        )
    ]