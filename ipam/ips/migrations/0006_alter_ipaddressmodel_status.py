# Generated by Django 4.2.17 on 2024-12-15 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ips', '0005_alter_ipaddressmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipaddressmodel',
            name='status',
            field=models.CharField(choices=[('free', 'free'), ('used', 'used')], default='free', max_length=4),
        ),
    ]