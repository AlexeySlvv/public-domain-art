# Generated by Django 3.2 on 2023-01-09 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnythingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directory', models.CharField(max_length=256)),
                ('prompt', models.CharField(max_length=1000)),
                ('season', models.CharField(max_length=10)),
            ],
        ),
    ]