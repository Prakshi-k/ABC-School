# Generated by Django 4.1.3 on 2022-12-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('rollno', models.IntegerField()),
                ('fname', models.CharField(max_length=200)),
                ('mname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=250)),
                ('dob', models.IntegerField()),
                ('mobno', models.IntegerField()),
                ('add', models.CharField(max_length=500)),
                ('std', models.IntegerField()),
                ('div', models.CharField(max_length=10)),
            ],
        ),
    ]
