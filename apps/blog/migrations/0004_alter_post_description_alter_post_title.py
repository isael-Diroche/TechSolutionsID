# Generated by Django 4.0.4 on 2023-08-09 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_autor_post_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]