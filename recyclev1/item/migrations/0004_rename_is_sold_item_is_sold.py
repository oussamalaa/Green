# Generated by Django 4.2.1 on 2023-05-18 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_category_options_alter_category_name_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='is_Sold',
            new_name='is_sold',
        ),
    ]
