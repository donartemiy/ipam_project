# Generated by Django 4.2.17 on 2024-12-15 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ips', '0002_alter_ipaddressmodel_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipaddressmodel',
            name='last_seen',
            field=models.DateTimeField(null=True),
        ),
    ]