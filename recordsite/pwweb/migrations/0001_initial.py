# Generated by Django 5.0.1 on 2024-01-28 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkRecord',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('game_type', models.CharField(max_length=200)),
                ('customer_name', models.CharField(max_length=200)),
                ('is_challenger_rank', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=5)),
                ('paid_amount', models.FloatField()),
                ('commission_rate', models.FloatField()),
                ('commision_amount', models.FloatField()),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('status', models.IntegerField(choices=[('1', 'Pending'), ('2', 'Approved'), ('3', 'Denied'), ('4', 'Removed')], default='1')),
            ],
        ),
    ]
