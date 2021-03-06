# Generated by Django 2.2.11 on 2020-07-13 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128, unique=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'communities',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('available_from', models.DateTimeField(blank=True, null=True)),
                ('available_to', models.DateTimeField(blank=True, null=True)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='community.Cluster')),
            ],
        ),
    ]
