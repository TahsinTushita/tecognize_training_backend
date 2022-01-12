from django.conf.urls import url
from backend import views

urlpatterns = [
    url(r"^api/users$", views.user_list),
    url(r"^api/instructors$", views.instructor_list),
    url(r"^api/customers$", views.customer_list),
    url(r"^api/categories$", views.category_list),
    url(r"^api/courses$", views.course_list),
]
