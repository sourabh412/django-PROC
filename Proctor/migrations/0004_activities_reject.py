# Generated by Django 3.2.2 on 2022-02-15 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proctor', '0003_auto_20220213_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='Reject',
            field=models.TextField(default='N', max_length=1),
        ),
    ]
