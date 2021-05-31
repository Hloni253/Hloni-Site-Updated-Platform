# Generated by Django 3.1.7 on 2021-05-10 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Sites', '0002_sites_topic'),
        ('Videos', '0001_initial'),
        ('Notes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('copied_notes', models.ManyToManyField(blank=True, related_name='Notes', to='Notes.Notes')),
                ('saved_sites', models.ManyToManyField(blank=True, related_name='Sites', to='Sites.Sites')),
                ('saved_videos', models.ManyToManyField(blank=True, related_name='Videos', to='Videos.Videos')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
