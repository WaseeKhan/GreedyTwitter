# Generated by Django 3.2 on 2021-04-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilesApp', '0007_alter_profile_bio'),
        ('postsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='likes', to='profilesApp.Profile'),
        ),
    ]
