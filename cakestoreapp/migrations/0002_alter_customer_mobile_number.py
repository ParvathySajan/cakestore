# Generated by Django 4.2.1 on 2023-06-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakestoreapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile_number',
            field=models.CharField(max_length=15),
        ),
    ]
