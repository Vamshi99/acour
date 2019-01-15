from django.urls import path

from . import views

app_name = 'track'
urlpatterns = [
    path('<int:package_id>/', views.detail, name = 'detail'),#package details page
    path('submit/', views.submit, name = 'submit'),#Submit entry
    path('entry/', views.entry, name = 'entry'),#Add entry
    path('sclick/', views.sclick, name = 'sclick'),#Search click
    path('validate/', views.validate, name = 'validate'),#Validate OTP
    path('search/', views.search, name = 'search'),#Search page
    path('scan/', views.scan, name = 'scan'),#Scan page
    path('<int:package_id>/deliver/', views.deliver, name = 'deliver'),#Deliver page
    path('', views.index, name = 'index'),
]
