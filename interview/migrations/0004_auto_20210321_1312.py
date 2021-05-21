# Generated by Django 3.1.7 on 2021-03-21 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0003_auto_20210204_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='interviewer',
            field=models.CharField(default='', max_length=128, verbose_name='인터뷰어'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interview',
            name='photographer',
            field=models.CharField(default='', max_length=128, verbose_name='포토그래퍼'),
            preserve_default=False,
        ),
    ]
