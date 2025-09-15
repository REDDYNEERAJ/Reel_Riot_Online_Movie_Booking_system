from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('movie/<int:movie_id>/', views.movie_detail_view, name='movie_detail'),
    path('theatre/<int:show_id>/seats/', views.seat_selection_view, name='seat_selection'),
    path("booking/<int:show_id>/confirmation/", views.booking_confirmation_view, name="booking_confirmation"),
    path("profile/", views.profile_view, name="profile"),

]

