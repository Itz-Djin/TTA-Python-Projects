# Generated by Django 4.1 on 2022-08-10 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(blank=True, default='', max_length=30)),
                ('lName', models.CharField(blank=True, default='', max_length=30)),
                ('Email', models.CharField(default='', max_length=60)),
                ('Username', models.CharField(blank=True, default='', max_length=30)),
            ],
        ),
    ]
