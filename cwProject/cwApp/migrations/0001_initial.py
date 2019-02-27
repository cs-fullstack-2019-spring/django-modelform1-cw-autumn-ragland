# Generated by Django 2.0.6 on 2019-02-27 21:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=1000)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 2, 27, 21, 54, 40, 481320, tzinfo=utc))),
            ],
        ),
    ]