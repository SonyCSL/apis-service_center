# Generated by Django 2.2.11 on 2020-05-18 04:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Failure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=128)),
                ('community_id', models.CharField(blank=True, max_length=128, null=True)),
                ('cluster_id', models.CharField(blank=True, max_length=128, null=True)),
                ('program_id', models.CharField(blank=True, max_length=128, null=True)),
                ('unit_id', models.CharField(blank=True, max_length=128, null=True)),
                ('detected', models.DateTimeField(default=django.utils.timezone.now)),
                ('closed', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
