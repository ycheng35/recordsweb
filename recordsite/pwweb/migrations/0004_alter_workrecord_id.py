# Generated by Django 5.0.1 on 2024-01-29 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pwweb', '0003_remove_workrecord_commision_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workrecord',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
