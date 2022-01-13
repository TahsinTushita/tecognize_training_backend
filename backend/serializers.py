from django.db.models import fields
from rest_framework import serializers
from backend.models import User, Customer, Instructor, Category, Course, Gallery


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
            "inst_img",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("cat_id", "category")


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "course_id",
            "cat_id",
            "course_title",
            "course_desc",
            "course_fee",
            "course_img",
        )


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ("img_id", "img_desc", "image")
