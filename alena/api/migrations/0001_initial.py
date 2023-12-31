# Generated by Django 4.2.4 on 2023-08-10 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vimos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.TextField()),
                ('docid', models.TextField()),
                ('docdate', models.TextField()),
                ('doctype', models.TextField()),
                ('docstatus', models.TextField()),
                ('docmean', models.TextField()),
                ('wcode', models.TextField()),
                ('wname', models.TextField()),
                ('dcode', models.TextField()),
                ('dname', models.TextField()),
                ('comment', models.TextField()),
                ('pos', models.TextField()),
                ('gcode', models.TextField()),
                ('gdcode', models.TextField()),
                ('gname', models.TextField()),
                ('amount', models.FloatField()),
                ('cost', models.FloatField()),
                ('sum', models.FloatField()),
            ],
        ),
    ]
