# Generated by Django 3.2.9 on 2022-01-12 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='inst_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]