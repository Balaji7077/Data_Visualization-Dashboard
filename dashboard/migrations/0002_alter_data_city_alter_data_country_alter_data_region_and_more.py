# Generated by Django 4.2.6 on 2024-07-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='region',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='topic',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='year',
            field=models.IntegerField(default=None, null=True),
        ),
    ]