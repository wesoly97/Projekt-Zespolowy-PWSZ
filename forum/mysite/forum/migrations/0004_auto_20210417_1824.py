# Generated by Django 3.0.5 on 2021-04-17 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_score_data_testu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='data_testu',
            field=models.DateTimeField(),
        ),
    ]