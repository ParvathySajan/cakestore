# Generated by Django 4.2.1 on 2023-07-05 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakestoreapp', '0003_cakes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cakes',
            name='cakeimage',
            field=models.ImageField(null=True, upload_to='cakeimgs'),
        ),
    ]
