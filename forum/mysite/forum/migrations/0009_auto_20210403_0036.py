# Generated by Django 3.0.5 on 2021-04-02 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_answerm_postm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postm',
            old_name='text',
            new_name='tresc',
        ),
        migrations.RemoveField(
            model_name='postm',
            name='subject',
        ),
    ]
