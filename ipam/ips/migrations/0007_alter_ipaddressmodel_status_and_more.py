# Generated by Django 4.2.17 on 2024-12-15 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ips', '0006_alter_ipaddressmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipaddressmodel',
            name='status',
            field=models.CharField(choices=[('free', 'free'), ('used', 'used')], max_length=4),
        ),
        migrations.AlterField(
            model_name='ipaddressmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ip_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
