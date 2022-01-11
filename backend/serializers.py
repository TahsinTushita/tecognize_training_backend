from django.db.models import fields
from rest_framework import serializers
from backend.models import User
from backend.models import Customer
from backend.models import Instructor


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
            "instructor_id",
            "instructor_name",
            "instructor_designation",
            "instructor_description",
        )
