# Generated by Django 3.2.9 on 2022-01-02 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='admin_email',
            new_name='customer_email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='admin_id',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='admin_name',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='admin_phone',
            new_name='customer_phone',
        ),
        migrations.AddField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]