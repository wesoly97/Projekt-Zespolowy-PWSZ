# Generated by Django 3.0.5 on 2021-05-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_dzial_matematyki_userstats'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstats',
            name='algebra',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userstats',
            name='zdobyte',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]
