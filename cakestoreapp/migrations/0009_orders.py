# Generated by Django 4.2.1 on 2023-07-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakestoreapp', '0008_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cakename', models.CharField(max_length=30)),
                ('amount', models.BigIntegerField()),
                ('address', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
