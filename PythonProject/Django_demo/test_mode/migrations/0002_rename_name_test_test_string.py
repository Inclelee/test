# Generated by Django 4.1.4 on 2023-01-11 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_mode', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='name',
            new_name='test_string',
        ),
    ]
