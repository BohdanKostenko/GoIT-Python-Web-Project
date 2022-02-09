# Generated by Django 4.0.2 on 2022-02-09 16:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(verbose_name='note')),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='noteapp.category')),
            ],
        ),
    ]
