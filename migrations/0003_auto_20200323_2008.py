# Generated by Django 3.0.4 on 2020-03-23 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dblog', '0002_auto_20200323_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='subcategory',
            new_name='parent',
        ),
    ]
