# Generated by Django 5.0.1 on 2024-01-29 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pwweb', '0004_alter_workrecord_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workrecord',
            name='is_challenger_rank',
            field=models.CharField(choices=[('True', '是'), ('False', '否')], default='True', max_length=5),
        ),
    ]
