# Generated by Django 4.2 on 2024-04-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, verbose_name='пароль'),
        ),
    ]