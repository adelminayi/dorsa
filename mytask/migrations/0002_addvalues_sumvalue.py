# Generated by Django 4.2 on 2023-05-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytask', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addvalues',
            name='sumvalue',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]