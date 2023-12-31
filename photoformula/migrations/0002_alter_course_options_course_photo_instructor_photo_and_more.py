# Generated by Django 5.0 on 2023-12-28 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoformula', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('name', 'price'), 'verbose_name_plural': 'Course'},
        ),
        migrations.AddField(
            model_name='course',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo'),
        ),
        migrations.AddField(
            model_name='material',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo'),
        ),
    ]
