# Generated by Django 2.1.2 on 2018-11-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20181020_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
