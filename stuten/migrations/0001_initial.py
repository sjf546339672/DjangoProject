# Generated by Django 3.0.5 on 2020-09-08 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clazz',
            fields=[
                ('cno', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=20, verbose_name='班级:')),
            ],
        ),
        migrations.CreateModel(
            name='Stu',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=30, verbose_name='姓名:')),
                ('clazz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuten.Clazz')),
            ],
        ),
    ]
