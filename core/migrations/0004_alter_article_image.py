# Generated by Django 4.0.6 on 2022-08-09 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_article_options_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='photos/<django.db.models.fields.CharField>'),
        ),
    ]