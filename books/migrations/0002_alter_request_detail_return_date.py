# Generated by Django 3.2 on 2021-04-23 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_detail',
            name='return_date',
            field=models.DateField(default=datetime.date(2021, 4, 30)),
        ),
    ]
