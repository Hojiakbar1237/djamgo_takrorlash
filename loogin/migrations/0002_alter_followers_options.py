# Generated by Django 4.2.1 on 2023-05-20 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loogin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='followers',
            options={'verbose_name': 'Follower', 'verbose_name_plural': 'Followers'},
        ),
    ]
