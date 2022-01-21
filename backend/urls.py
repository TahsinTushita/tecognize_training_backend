from django.conf.urls import url
from backend import views

urlpatterns = [
    url(r"^backend/api/users$", views.user_list),
    url(r"^backend/api/instructors$", views.instructor_list),
    url(r"^backend/api/customers$", views.customer_list),
    url(r"^backend/api/categories$", views.category_list),
    url(r"^backend/api/courses$", views.course_list),
    url(r"^backend/api/gallery$", views.gallery_list),
    url(r"^backend/api/blogs$", views.blog_list),
    url(r"^backend/api/reviews$", views.review_list),
    url(r"^backend/api/image/([a-zA-Z0-9_]+\.(?:jpg|gif|png|jpeg))$", views.getImage),
]
