# Generated by Django 4.1.1 on 2022-10-03 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='meet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='pics')),
                ('descr', models.CharField(max_length=500)),
            ],
        ),
    ]
