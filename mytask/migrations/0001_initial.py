# Generated by Django 4.2 on 2023-05-01 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avalue', models.IntegerField()),
                ('bvalue', models.IntegerField()),
            ],
        ),
    ]