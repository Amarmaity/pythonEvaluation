# Generated by Django 5.2.4 on 2025-07-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='user_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
