from django.conf.urls import url
from django.http import HttpResponse

from . import views
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from courses.models import Post
urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset=Post.objects.all().order_by("-date")[:25],
        template_name="courses/courses.html")),
    url('r^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name="courses/post.html"))
]