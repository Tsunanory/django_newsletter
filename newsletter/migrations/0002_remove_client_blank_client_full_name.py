# Generated by Django 4.2.7 on 2024-05-16 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='blank',
        ),
        migrations.AddField(
            model_name='client',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]