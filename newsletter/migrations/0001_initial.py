# Generated by Django 4.2.7 on 2024-05-16 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_attempt_time', models.DateTimeField()),
                ('last_attempt_status', models.CharField(choices=[('S', 'Successful'), ('P', 'In Process'), ('F', 'Failed')], default='S', max_length=2)),
                ('server_response', models.IntegerField(default=200)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('blank', models.CharField(max_length=50, verbose_name='null')),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial', models.DateTimeField()),
                ('frequency', models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly')], default='W', max_length=2)),
                ('status', models.CharField(choices=[('S', 'Successful'), ('P', 'In Process'), ('F', 'Failed')], default='P', max_length=2)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter.client')),
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='newsletter.message')),
            ],
        ),
    ]