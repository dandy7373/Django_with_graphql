# Generated by Django 3.0.5 on 2020-10-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20201011_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('members', models.ManyToManyField(to='userprofile.Peer')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
