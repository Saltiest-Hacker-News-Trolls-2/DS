# Generated by Django 2.2.7 on 2019-11-20 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191120_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='saltyuser',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='saltyuser',
            name='rank',
            field=models.IntegerField(),
        ),
    ]
