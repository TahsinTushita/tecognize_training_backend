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
    inst_description = models.TextField()
    inst_img = models.ImageField(null=True, blank=True, upload_to="images/")


class Category(models.Model):
    cat_id = models.BigAutoField(auto_created=True, primary_key=True)
    category = models.CharField(max_length=100, blank=False)


class Course(models.Model):
    course_id = models.BigAutoField(auto_created=True, primary_key=True)
    cat_id = models.ForeignKey(Category, db_column="cat_id", on_delete=models.CASCADE)
    course_title = models.CharField(max_length=200, blank=False)
    course_desc = models.TextField()
    course_fee = models.IntegerField()
    course_img = models.ImageField(null=True, blank=True, upload_to="course_images/")


class Gallery(models.Model):
    img_id = models.BigAutoField(auto_created=True, primary_key=True)
    img_desc = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="gallery/")


class Blog(models.Model):
    blog_id = models.BigAutoField(auto_created=True, primary_key=True)
    blog_title = models.CharField(max_length=255, blank=False)
    blog = models.TextField()
    blog_author = models.CharField(max_length=100, blank=False)
    blog_img = models.ImageField(null=True, blank=True, upload_to="blog_images/")
    publish_date = models.DateField()


class Reviews(models.Model):
    reviewer_name = models.CharField(max_length=100, blank=False)
    reviewer_designation = models.CharField(max_length=150, blank=False)
    review = models.TextField()
    reviewer_img = models.ImageField(
        null=True, blank=True, upload_to="reviewer_images/"
    )
