# Generated by Django 4.0.5 on 2022-09-21 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='offset',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]