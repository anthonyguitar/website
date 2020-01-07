# Generated by Django 2.2 on 2020-01-07 21:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_musiclink'),
    ]

    operations = [
        migrations.AddField(
            model_name='musiclink',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='musiclink',
            name='email',
            field=models.EmailField(default='notset', max_length=200),
        ),
    ]
