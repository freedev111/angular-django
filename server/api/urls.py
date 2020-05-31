from django.conf.urls import url
from .views import (
  JobPostView,
  JobListView,
  PositionListView,
)

urlpatterns = [
  url(r'^job/$', JobPostView.as_view()),
  url(r'^jobs/$', JobListView.as_view()),
  url(r'^jobs/(?P<id>(.+))/positions/$', PositionListView.as_view()),
]
