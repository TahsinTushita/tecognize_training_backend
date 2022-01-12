from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.BigAutoField(auto_created=True, primary_key=True)
    user_name = models.CharField(max_length=100, blank=False)
    user_phone = models.CharField(max_length=22, blank=False)
    user_email = models.CharField(max_length=255, blank=False)
    admin = models.BooleanField()


class Customer(models.Model):
    customer_id = models.BigAutoField(auto_created=True, primary_key=True)
    customer_name = models.CharField(max_length=100, blank=False)
    customer_phone = models.CharField(max_length=22, blank=False)
    customer_email = models.CharField(max_length=255, blank=False)


class Instructor(models.Model):
    inst_id = models.BigAutoField(auto_created=True, primary_key=True)
    inst_name = models.CharField(max_length=100, blank=False)
    inst_designation = models.CharField(max_length=150, blank=False)
    inst_description = models.CharField(max_length=255, blank=False)


class Category(models.Model):
    cat_id = models.BigAutoField(auto_created=True, primary_key=True)
    category = models.CharField(max_length=100, blank=False)


class Course(models.Model):
    course_id = models.BigAutoField(auto_created=True, primary_key=True)
    cat_id = models.ForeignKey(Category, db_column="cat_id", on_delete=models.CASCADE)
    course_title = models.CharField(max_length=200, blank=False)
    course_desc = models.CharField(max_length=255, blank=False)
    course_fee = models.IntegerField()
