from django.urls import path
from base.views import user_views as views




urlpatterns = [
    
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile',views.getUserProfile, name="user-profile"),
    path('profile/update',views.updateUserProfile, name="user-profile-update"),
   
    path('update/<str:pk>', views.updateUserProfileByAdmin, name="update-user-profile"),
    path('delete/<str:pk>', views.deleteUser, name="delete-user"),
    path('register', views.registerUser, name="register"),
    path('<str:pk>', views.getUserById, name='user'),
    path('', views.getUsers, name="all-users"),
   
]