# Generated by Django 3.1.7 on 2021-05-13 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
        ('Videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.subject'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
