from django.db.models import query
from django.shortcuts import render, redirect

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import base64
from django.db import connection
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

from backend.models import (
    Course,
    User,
    Customer,
    Instructor,
    Category,
    Gallery,
    Blog,
    Reviews,
)

from backend.serializers import (
    UserSerializer,
    CustomerSerializer,
    InstructorSerializer,
    CategorySerializer,
    CourseSerializer,
    GallerySerializer,
    BlogSerializer,
    ReviewSerializer,
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
        # data = base64.b64decode(request)
        inst_name = request.POST.get("inst_name")
        inst_designation = request.POST.get("inst_designation")
        inst_description = request.POST.get("inst_description")
        inst_quote = request.POST.get("inst_quote")
        inst_img = request.FILES["inst_img"]
        inst_serializer = InstructorSerializer(
            data={
                "inst_name": inst_name,
                "inst_designation": inst_designation,
                "inst_description": inst_description,
                "inst_quote": inst_quote,
                "inst_img": inst_img,
            }
        )
        if inst_serializer.is_valid():
            inst_serializer.save()
            return JsonResponse(inst_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(inst_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # cursor = connection.cursor()
        # prod = Instructor()
        # prod.inst_name = request.POST.get("inst_name")
        # prod.inst_designation = request.POST.get("inst_designation")
        # prod.inst_description = request.POST.get("inst_description")
        # prod.inst_img = request.FILES["inst_img"]
        # prod.save()
        # query = "INSERT INTO backend_instructor VALUES(%s,%s,%s,%s)"

        # cursor.execute(
        #     query,
        #     params=(
        #         prod.inst_name,
        #         prod.inst_designation,
        #         prod.inst_description,
        #         prod.inst_img,
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
        # cat_data = JSONParser().parse(request)
        # cat_serializer = CategorySerializer(data=cat_data)
        # if cat_serializer.is_valid():
        #     cat_serializer.save()
        #     return JsonResponse(cat_serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(cat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        category = request.POST.get("category")
        cat_img = request.FILES["cat_img"]
        cat_serializer = CategorySerializer(
            data={
                "category": category,
                "cat_img": cat_img,
            }
        )
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
        cat_id = request.POST.get("cat_id")
        inst_id = request.POST.get("inst_id")
        course_title = request.POST.get("course_title")
        course_desc = request.POST.get("course_desc")
        course_content = request.POST.get("course_content")
        course_classes = request.POST.get("course_classes")
        course_credit = request.POST.get("course_credit")
        course_fee = request.POST.get("course_fee")
        course_img = request.FILES["course_img"]
        course_serializer = CourseSerializer(
            data={
                "cat_id": cat_id,
                "inst_id": inst_id,
                "course_title": course_title,
                "course_desc": course_desc,
                "course_content": course_content,
                "course_classes": course_classes,
                "course_credit": course_credit,
                "course_fee": course_fee,
                "course_img": course_img,
            }
        )

        if course_serializer.is_valid():
            course_serializer.save()
            return JsonResponse(course_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(
            course_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def popular_courses(request):
    cursor = connection.cursor()
    query = "SELECT course_title,course_id,course_img,course_credit,course_classes,inst_name FROM backend_course INNER JOIN backend_instructor ON backend_course.inst_id=backend_instructor.inst_id"
    cursor.execute(query)

    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["GET"])
def single_course(request, course_id):
    cursor = connection.cursor()
    query = "SELECT course_id,course_title,course_desc,course_content,course_classes,course_credit,course_fee,course_img,inst_name,category FROM backend_course INNER JOIN backend_instructor ON backend_course.inst_id=backend_instructor.inst_id INNER JOIN backend_category ON backend_course.cat_id=backend_category.cat_id WHERE course_id=%s"

    cursor.execute(query, params=(course_id))
    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["GET", "POST"])
def gallery_list(request):
    if request.method == "GET":
        gallery = Gallery.objects.all()

        gallery_serializer = GallerySerializer(gallery, many=True)
        return JsonResponse(gallery_serializer.data, safe=False)

    elif request.method == "POST":
        img_desc = request.POST.get("img_desc")
        image = request.FILES["image"]
        gallery_serializer = GallerySerializer(
            data={
                "img_desc": img_desc,
                "image": image,
            }
        )

        if gallery_serializer.is_valid():
            gallery_serializer.save()
            return JsonResponse(gallery_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(
            gallery_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "POST"])
def blog_list(request):
    if request.method == "GET":
        blogs = Blog.objects.all()

        blog_serializer = BlogSerializer(blogs, many=True)
        return JsonResponse(blog_serializer.data, safe=False)

    elif request.method == "POST":
        blog_title = request.POST.get("blog_title")
        blog = request.POST.get("blog")
        blog_author = request.POST.get("blog_author")
        blog_img = request.FILES["blog_img"]
        publish_date = request.POST.get("publish_date")
        blog_serializer = BlogSerializer(
            data={
                "blog_title": blog_title,
                "blog": blog,
                "blog_author": blog_author,
                "blog_img": blog_img,
                "publish_date": publish_date,
            }
        )

        if blog_serializer.is_valid():
            blog_serializer.save()
            return JsonResponse(blog_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(blog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def single_blog(request, blog_id):
    cursor = connection.cursor()
    query = "SELECT * from backend_blog WHERE blog_id=%s"

    cursor.execute(query, params=(blog_id))
    columns = [col[0] for col in cursor.description]
    return JsonResponse(
        [dict(zip(columns, row)) for row in cursor.fetchall()], safe=False
    )


@api_view(["GET", "POST"])
def review_list(request):
    if request.method == "GET":
        reviews = Reviews.objects.all()

        review_serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(review_serializer.data, safe=False)

    elif request.method == "POST":
        reviewer_name = request.POST.get("reviewer_name")
        reviewer_designation = request.POST.get("reviewer_designation")
        review = request.POST.get("review")
        reviewer_img = request.FILES["reviewer_img"]
        review_serializer = ReviewSerializer(
            data={
                "reviewer_name": reviewer_name,
                "reviewer_designation": reviewer_designation,
                "review": review,
                "reviewer_img": reviewer_img,
            }
        )

        if review_serializer.is_valid():
            review_serializer.save()
            return JsonResponse(review_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(
            review_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def getImage(request, imgName):
    image_data = open("media/images/" + imgName, "rb").read()
    return HttpResponse(image_data, content_type="image/png")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email_address"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())

            try:
                send_mail(
                    subject,
                    message,
                    "training@tecognize.com",  # office email
                    ["training@tecognize.com"],  # office email
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("contact")

    form = ContactForm()
    return render(request, "index.html", {"form": form})  # course outline form page
