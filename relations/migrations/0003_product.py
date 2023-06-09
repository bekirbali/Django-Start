# Generated by Django 4.2.1 on 2023-05-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0002_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=128)),
                ('product', models.CharField(max_length=128)),
                ('account', models.ManyToManyField(to='relations.account')),
            ],
        ),
    ]
