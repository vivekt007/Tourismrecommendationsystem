from django.conf.urls import url, include
from . import views
from .views import home2
from django.urls import path

urlpatterns = [
    url(r'^accounts/profile/$', views.UserProfileView.as_view(), name="profile"),
    url(r'^accounts/status/$', views.UserStatusView.as_view(), name="status"),
    path('home2/', home2, name='home2'),
    path('mcq/', views.multiple_choice_question, name='mcq'),
    path('travel_questions/', views.travel_questions, name='travel_questions'),
    path('gtq/', views.get_travel_questions, name='gtq'),
    path('tq/', views.travel_questions, name='tq'),
    path('mcq2/', views.mcq2, name='mcq2'),
    path('dd/', views.main, name='dd'),
    path('travel_input/',views.travel_input, name='travel_input'),
    path('state_detail/', views.state_detail, name='state_detail'),
    path('display_places/',views.display_places, name='display_places'),
    path('add_place/', views.add_place, name='add_place'),
    path('save_review/', views.save_review, name='save_review'),
    
    


]
