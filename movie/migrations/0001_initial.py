# Generated by Django 3.0.5 on 2020-09-07 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('mname', models.CharField(max_length=100, unique=True)),
                ('mdesc', models.TextField(blank=True, null=True)),
                ('mimg', models.CharField(max_length=120)),
                ('mlink', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'movie',
                'managed': False,
            },
        ),
    ]
