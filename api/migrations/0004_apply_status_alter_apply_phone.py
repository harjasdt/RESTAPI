# Generated by Django 4.0.5 on 2022-09-21 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_apply_offset'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='status',
            field=models.CharField(choices=[('1', 'PENDING'), ('2', 'ACCEPTED'), ('3', 'REJECTED')], default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='apply',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
