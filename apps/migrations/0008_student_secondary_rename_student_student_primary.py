# Generated by Django 4.1.3 on 2022-12-27 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_alter_kindergarten_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_secondary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('rollno', models.IntegerField()),
                ('fname', models.CharField(max_length=200)),
                ('mname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=250)),
                ('dob', models.CharField(max_length=20)),
                ('mobno', models.CharField(max_length=10)),
                ('add', models.CharField(max_length=500)),
                ('std', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='student',
            new_name='student_primary',
        ),
    ]