# Generated by Django 4.2.1 on 2023-12-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
