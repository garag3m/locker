# Generated by Django 2.0.7 on 2018-08-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0006_auto_20180811_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projector',
            name='type',
            field=models.CharField(choices=[('Datashow', 'Datashow'), ('Interativo', 'Interativo')], default='Datashow', max_length=10, verbose_name='Tipo'),
        ),
    ]
