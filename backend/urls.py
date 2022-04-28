from django.conf.urls import url
from backend import views

urlpatterns = [
    url(r"^backend/api/users$", views.user_list),
    url(r"^backend/api/instructors$", views.instructor_list),
    url(r"^backend/api/customers$", views.customer_list),
    url(r"^backend/api/categories$", views.category_list),
    url(r"^backend/api/courses$", views.course_list),
    url(r"^backend/api/popular-courses$", views.popular_courses),
    url(r"^backend/api/single-course/([a-zA-Z0-9_]+)$", views.single_course),
    url(r"^backend/api/gallery$", views.gallery_list),
    url(r"^backend/api/blogs$", views.blog_list),
    url(r"^backend/api/single-blog/([a-zA-Z0-9_]+)$", views.single_blog),
    url(r"^backend/api/reviews$", views.review_list),
    url(r"^backend/api/contact$", views.contact, name="contact"),
    url(r"^backend/api/image/([a-zA-Z0-9_]+\.(?:jpg|gif|png|jpeg))$", views.getImage),
]
