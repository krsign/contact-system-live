# Generated by Django 2.2 on 2020-06-08 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, upload_to='contact/'),
        ),
    ]
