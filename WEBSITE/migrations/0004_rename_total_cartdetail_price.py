# Generated by Django 3.2.4 on 2021-07-05 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WEBSITE', '0003_auto_20210705_0938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartdetail',
            old_name='total',
            new_name='price',
        ),
    ]
