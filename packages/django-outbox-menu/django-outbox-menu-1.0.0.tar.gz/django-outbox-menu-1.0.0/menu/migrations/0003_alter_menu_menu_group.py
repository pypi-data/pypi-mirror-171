# Generated by Django 4.1.1 on 2022-10-05 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_menu_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_group',
            field=models.ManyToManyField(blank=True, to='menu.menugroup'),
        ),
    ]
