# Generated by Django 3.2 on 2021-04-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210423_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request_detail',
            name='requested_on',
        ),
        migrations.AlterField(
            model_name='request_detail',
            name='duration',
            field=models.DurationField(),
        ),
    ]