# Generated by Django 4.1.3 on 2022-12-27 15:00

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_kindergarten'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='kindergarten',
            managers=[
                ('object_kg', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='kindergarten',
            name='section',
            field=models.CharField(max_length=2),
        ),
    ]