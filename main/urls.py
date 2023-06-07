from django.urls import path
<<<<<<< HEAD
from .views import IndexView, AddProductView, ProductView, CategoryView
=======
from .views import IndexView, AddProductView, ProductView, CategoryView, LogoutUserView, SignUpUserView, SignInUserView, UserProfileView
>>>>>>> 0faa800 (Auth-User)

urlpatterns = [
    path('', IndexView),
    path('add/', AddProductView),
    path('product/', ProductView),
    path('category/', CategoryView),
<<<<<<< HEAD
=======
    path('signup', SignUpUserView),
    path('logout/', LogoutUserView),
    path('signin', SignInUserView),
    path('profile', UserProfileView),

>>>>>>> 0faa800 (Auth-User)
]