# Generated by Django 2.2.11 on 2020-05-25 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunitySetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_id', models.CharField(max_length=128, unique=True)),
                ('notify_to', models.EmailField(default='nobody@example.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='JobSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_id', models.CharField(max_length=128)),
                ('cluster_id', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'unique_together': {('community_id', 'cluster_id', 'type')},
            },
        ),
    ]