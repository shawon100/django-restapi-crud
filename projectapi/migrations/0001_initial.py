# Generated by Django 2.2.6 on 2019-12-26 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_code', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
            ],
        ),
    ]
