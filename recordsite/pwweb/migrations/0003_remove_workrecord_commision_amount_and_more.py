# Generated by Django 5.0.1 on 2024-01-28 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pwweb', '0002_alter_workrecord_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workrecord',
            name='commision_amount',
        ),
        migrations.AlterField(
            model_name='workrecord',
            name='commission_rate',
            field=models.FloatField(default=0.75),
        ),
    ]
