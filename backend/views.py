from django.db.models import query
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import base64
from django.db import connection

from backend.models import Course, User, Customer, Instructor, Category

from backend.serializers import (
    UserSerializer,
    CustomerSerializer,
    InstructorSerializer,
    CategorySerializer,
    CourseSerializer,
)

from rest_framework.decorators import api_view

# Create your views here.


# User


@api_view(["GET", "POST"])
def user_list(request):
    if request.method == "GET":
        users = User.objects.all()

        user_name = request.GET.get("user_name", None)
        if user_name is not None:
            users = users.filter(user_name_icontains=user_name)

        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method == "POST":
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Instructor


@api_view(["GET", "POST"])
def instructor_list(request):
    if request.method == "GET":
        instructors = Instructor.objects.all()

        inst_name = request.GET.get("inst_name", None)
        if inst_name is not None:
            instructors = instructors.filter(user_name_icontains=inst_name)

        inst_serializer = InstructorSerializer(instructors, many=True)
        return JsonResponse(inst_serializer.data, safe=False)

    elif request.method == "POST":
        # inst_data = JSONParser().parse(request)
        # data = base64.b64decode(request)
        # inst_serializer = InstructorSerializer(data=inst_data)
        # if inst_serializer.is_valid():
        #     inst_serializer.save()
        #     return JsonResponse(inst_serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(inst_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        cursor = connection.cursor()
        prod = Instructor()
        prod.inst_id = request.POST.get("inst_id")
        prod.inst_name = request.POST.get("inst_name")
        prod.inst_designation = request.POST.get("inst_designation")
        prod.inst_description = request.POST.get("inst_description")
        prod.inst_img = request.FILES["inst_img"]
        prod.save()
        # customer_data = JSONParser().parse(request)
        # print(customer_data)
        query = "INSERT INTO backend_instructor VALUES(%s,%s,%s,%s,%s)"

        cursor.execute(
            query,
            params=(
                prod.inst_id,
                prod.inst_name,
                prod.inst_designation,
                prod.inst_description,
                prod.inst_img,
            ),
        )
        r = cursor.fetchone()
        return JsonResponse(r, safe=False)


# @api_view(["PUT"])
# def customer_fee_update(request):
# cursor = connection.cursor()
# customer_data = JSONParser().parse(request)
# # customer_data = json.load(request)
# print(customer_data)
# query = "UPDATE training_backend_customer SET cust_total_fee=%s,cust_paid_fee=%s,cust_due_fee=%s,cust_units=%s WHERE cust_id=%s"

# cursor.execute(
#     query,
#     params=(
#         customer_data["cust_total_fee"],
#         customer_data["cust_paid_fee"],
#         customer_data["cust_due_fee"],
#         customer_data["cust_units"],
#         customer_data["cust_id"],
#     ),
# )
# r = cursor.fetchone()
# return JsonResponse(r, safe=False)


# Customer


@api_view(["GET", "POST"])
def customer_list(request):
    if request.method == "GET":
        customers = Customer.objects.all()

        customer_name = request.GET.get("customer_name", None)
        if customer_name is not None:
            customers = customers.filter(user_name_icontains=customer_name)

        cust_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(cust_serializer.data, safe=False)

    elif request.method == "POST":
        cust_data = JSONParser().parse(request)
        cust_serializer = CustomerSerializer(data=cust_data)
        if cust_serializer.is_valid():
            cust_serializer.save()
            return JsonResponse(cust_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(cust_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Category


@api_view(["GET", "POST"])
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()

        category = request.GET.get("category", None)
        if category is not None:
            categories = categories.filter(user_name_icontains=category)

        cat_serializer = CategorySerializer(categories, many=True)
        return JsonResponse(cat_serializer.data, safe=False)

    elif request.method == "POST":
        cat_data = JSONParser().parse(request)
        cat_serializer = CategorySerializer(data=cat_data)
        if cat_serializer.is_valid():
            cat_serializer.save()
            return JsonResponse(cat_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(cat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Course


@api_view(["GET", "POST"])
def course_list(request):
    if request.method == "GET":
        courses = Course.objects.all()

        course_title = request.GET.get("course_title", None)
        if course_title is not None:
            courses = courses.filter(user_name_icontains=course_title)

        course_serializer = CourseSerializer(courses, many=True)
        return JsonResponse(course_serializer.data, safe=False)

    elif request.method == "POST":
        course_data = JSONParser().parse(request)
        course_serializer = CourseSerializer(data=course_data)
        if course_serializer.is_valid():
            course_serializer.save()
            return JsonResponse(course_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(
            course_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
