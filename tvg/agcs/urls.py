from django.conf.urls import url
from . import views

app_name = "agcs"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^companies/$', views.CompaniesListView.as_view(), name="companies_list"),
    url(r'^companies/(?P<pk>\d+)$', views.CompaniesDetailView.as_view(), name="companies_detail"),
    url(r'^logout/', views.logout, name="logout"),

]
