# Generated by Django 2.2.1 on 2019-05-31 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
