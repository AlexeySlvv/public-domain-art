# Generated by Django 3.2.16 on 2023-01-10 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_anything', '0002_auto_20230110_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anythingmodel',
            name='prompt',
        ),
        migrations.RemoveField(
            model_name='anythingmodel',
            name='season',
        ),
        migrations.AddField(
            model_name='anythingmodel',
            name='image_name',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DirectoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('prompt', models.CharField(max_length=1000)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_anything.seasonmodel')),
            ],
        ),
        migrations.AlterField(
            model_name='anythingmodel',
            name='directory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_anything.directorymodel'),
        ),
    ]
