# Generated by Django 2.2.6 on 2020-02-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricelist', '0005_auto_20200222_0809'),
    ]

    operations = [
        migrations.CreateModel(
            name='unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=5)),
            ],
        ),
    ]
