# Generated by Django 4.1.1 on 2022-10-07 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_menu_menu_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucustom',
            name='menu_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='menu.menugroup'),
        ),
    ]
