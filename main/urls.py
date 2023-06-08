from django.urls import path
from .views import IndexView, AddProductView, ProductView, CategoryView, LogoutUserView, SignUpUserView, SignInUserView, UserProfileView, UserEditProfileView


urlpatterns = [
    path('', IndexView),
    path('add/', AddProductView),
    path('product/', ProductView),
    path('category/', CategoryView),
    path('signup', SignUpUserView),
    path('logout/', LogoutUserView),
    path('signin/', SignInUserView),
    path('profile/', UserProfileView),
    path('profile/edit/', UserEditProfileView),
]