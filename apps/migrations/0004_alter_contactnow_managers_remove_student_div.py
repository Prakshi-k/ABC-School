# Generated by Django 4.1.3 on 2022-12-27 07:10

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_contactnow_alter_student_mobno'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='contactnow',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='div',
        ),
    ]