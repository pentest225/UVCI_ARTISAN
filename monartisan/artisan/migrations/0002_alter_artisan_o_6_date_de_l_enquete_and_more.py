# Generated by Django 5.0.6 on 2024-05-18 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artisan',
            name='O_6_DATE_DE_L_ENQUETE',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='artisan',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='artisan',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
