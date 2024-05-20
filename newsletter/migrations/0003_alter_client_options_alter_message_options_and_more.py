# Generated by Django 4.2.7 on 2024-05-16 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_remove_client_blank_client_full_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'клиент', 'verbose_name_plural': 'клиенты'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'сообщение', 'verbose_name_plural': 'сообщения'},
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
        migrations.AlterField(
            model_name='client',
            name='comment',
            field=models.TextField(verbose_name='комментарий'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='почта'),
        ),
        migrations.AlterField(
            model_name='client',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='message',
            name='topic',
            field=models.CharField(max_length=50, verbose_name='заголовок'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter.client', verbose_name='клиенты'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='frequency',
            field=models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly')], default='W', max_length=2, verbose_name='частота рассылки'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='initial',
            field=models.DateTimeField(verbose_name='начало рассылки'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='message',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='newsletter.message', verbose_name='сообщение'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='status',
            field=models.CharField(choices=[('S', 'Successful'), ('P', 'In Process'), ('F', 'Failed')], default='P', max_length=2, verbose_name='статус'),
        ),
    ]
