# Generated by Django 2.1.2 on 2022-01-15 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('userId', models.IntegerField(default=0)),
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=200)),
            ],
        ),
    ]
