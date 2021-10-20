from django.urls import path
from base.views import user_views as views


urlpatterns = [
    path('', views.getUsers, name="users"),
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('register/', views.registerUser, name='register'),
    path('profile/', views.getUserProfile, name="users-profile"),
    path('update/', views.updateUser, name="update-user"),

    path('profile/update/', views.updateUserProfile, name="users-profile-update"),
    path('delete/<str:pk>/', views.delteUsers, name="users-profile-update"),
    path('detail/<str:pk>/', views.getUserById, name="user"),

]
