# Generated by Django 5.0.2 on 2024-03-05 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_appoinment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deptregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptno', models.CharField(max_length=200)),
                ('deptname', models.CharField(max_length=200, null=True)),
                ('drid', models.CharField(max_length=200, null=True)),
                ('drname', models.CharField(max_length=200)),
            ],
        ),
    ]
