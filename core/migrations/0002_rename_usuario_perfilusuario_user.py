# Generated by Django 4.2.7 on 2024-04-03 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfilusuario',
            old_name='usuario',
            new_name='user',
        ),
    ]
