# Generated by Django 3.2.9 on 2022-02-28 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('blog_title', models.CharField(max_length=255)),
                ('blog', models.TextField()),
                ('blog_author', models.CharField(max_length=100)),
                ('blog_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('publish_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('cat_img', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_phone', models.CharField(max_length=22)),
                ('customer_email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('img_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('img_desc', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('inst_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('inst_name', models.CharField(max_length=100)),
                ('inst_designation', models.CharField(max_length=150)),
                ('inst_description', models.TextField()),
                ('inst_quote', models.TextField(null=True)),
                ('inst_img', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=100)),
                ('reviewer_designation', models.CharField(max_length=150)),
                ('review', models.TextField()),
                ('reviewer_img', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_phone', models.CharField(max_length=22)),
                ('user_email', models.CharField(max_length=255)),
                ('admin', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('course_title', models.CharField(max_length=200)),
                ('course_desc', models.TextField()),
                ('course_content', models.TextField(null=True)),
                ('course_classes', models.IntegerField(null=True)),
                ('course_credit', models.FloatField(null=True)),
                ('course_fee', models.IntegerField()),
                ('course_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('cat_id', models.ForeignKey(db_column='cat_id', on_delete=django.db.models.deletion.CASCADE, to='backend.category')),
                ('inst_id', models.ForeignKey(db_column='inst_id', on_delete=django.db.models.deletion.CASCADE, to='backend.instructor')),
            ],
        ),
    ]
