# Generated by Django 2.1.2 on 2019-02-05 18:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customaccount',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customaccount',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='CustomAccount',
        ),
    ]
