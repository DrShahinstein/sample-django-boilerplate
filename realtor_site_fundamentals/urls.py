from django.contrib import admin
from django.urls import path
from my_realtor_site.views import IndexView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index page"),
]
