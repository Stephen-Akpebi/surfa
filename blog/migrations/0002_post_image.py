# Generated by Django 4.0.3 on 2022-04-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='provide value for each post', upload_to='featured_image/%y/%m/%d'),
            preserve_default=False,
        ),
    ]
