# Generated by Django 2.2.7 on 2019-11-18 19:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=15)),
                ('text', models.TextField(max_length=500)),
                ('by', models.CharField(max_length=50)),
                ('time', models.DateField(default=django.utils.timezone.now)),
                ('parent', models.CharField(max_length=50)),
                ('url', models.URLField(max_length=75)),
                ('score', models.IntegerField()),
                ('title', models.TextField(max_length=100)),
                ('descendants', models.IntegerField()),
            ],
        ),
    ]
