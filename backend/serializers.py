from django.db.models import fields
from rest_framework import serializers
from backend.models import (
    User,
    Customer,
    Instructor,
    Category,
    Course,
    Gallery,
    Blog,
    Reviews,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_id", "user_name", "user_phone", "user_email", "admin")


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("customer_id", "customer_name", "customer_phone", "customer_email")


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = (
            "inst_id",
            "inst_name",
            "inst_designation",
            "inst_description",
            "inst_quote",
            "inst_img",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("cat_id", "category", "cat_img")


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "course_id",
            "cat_id",
            "inst_id",
            "course_title",
            "course_desc",
            "course_content",
            "course_classes",
            "course_credit",
            "course_fee",
            "course_img",
        )


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ("img_id", "img_desc", "image")


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            "blog_id",
            "blog_title",
            "blog",
            "blog_author",
            "blog_img",
            "publish_date",
        )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = (
            "id",
            "reviewer_name",
            "reviewer_designation",
            "review",
            "reviewer_img",
        )
