# Generated by Django 4.0.1 on 2022-02-02 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0003_alter_notes_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='notes',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='noteapp.category'),
        ),
    ]
