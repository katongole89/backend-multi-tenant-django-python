from django.urls import path, re_path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    re_path(r'^simple-data/?$', views.SimpleTenancyApiView.as_view()),
    path('simple-data/<slug:company_url>/', views.SimpleTenancyApiView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)