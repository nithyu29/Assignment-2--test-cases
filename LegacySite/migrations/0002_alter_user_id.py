# Generated by Django 4.1.7 on 2023-03-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LegacySite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
