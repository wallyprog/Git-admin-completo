# Generated by Django 2.0.2 on 2019-11-23 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proprietario',
            name='nome',
            field=models.CharField(default='sem nome', max_length=50),
            preserve_default=False,
        ),
    ]
