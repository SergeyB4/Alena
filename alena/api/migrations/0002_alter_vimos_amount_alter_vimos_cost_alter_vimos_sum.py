# Generated by Django 4.2.4 on 2023-08-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vimos',
            name='amount',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vimos',
            name='cost',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vimos',
            name='sum',
            field=models.TextField(),
        ),
    ]