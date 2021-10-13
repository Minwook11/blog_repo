# Generated by Django 3.2.7 on 2021-10-05 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('level', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Complex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_1', models.IntegerField()),
                ('key_2', models.IntegerField()),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.case')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.level')),
            ],
        ),
    ]