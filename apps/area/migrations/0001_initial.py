# Generated by Django 3.0.3 on 2020-03-02 16:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=20, verbose_name='省份')),
            ],
            options={
                'verbose_name': '省份',
                'verbose_name_plural': '省份',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=20, verbose_name='城市')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area.Province', verbose_name='所在省份')),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
            },
        ),
    ]