# Generated by Django 5.0 on 2023-12-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accountapp', '0002_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]