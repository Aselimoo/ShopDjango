from django.shortcuts import render, redirect
from .models import Category, Product, Profile
from .forms import CategoryForm, ProductForm, UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def IndexView(request):
    return render(request, 'main/index.html')


def ProductView(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'main/product.html', context=context)


def AddProductView(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Добавление продукта прошло успешно")
        else:
            messages.error(request, form.errors)
            # messages.debug
            # messages.warning
            # messages.info
            # messages.success
            # messages.error
    else:
        form = ProductForm()

    context = {
        "form": form
    }
    return render(request, 'main/addproduct.html', context=context)


def CategoryView(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Категория добавлена")
        else:
            messages.error(request, form.errors)
    else:
        form = CategoryForm()

    context = {
        "form": form
    }
    return render(request, 'main/category.html', context=context)



def LogoutUserView(request):
    logout(request)
    return redirect('/')


def SignUpUserView(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # не сохраняй в БД
            if user.password != request.POST.get('password2'):
                messages.error(request, "Пароли не совпадают")
                return redirect ('/signup')
            else:
                user.set_password(user.password)
                form.save()
                messages.success(request, "Регистрация прошла успешно")
                return redirect('/')
    else:
        form = UserForm()
    return render(request, "AuthenticateUser/signup.html", {"form": form})


def SignInUserView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)

        if username and password:
            try:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Вы успешно вошли!')
                    return redirect("/")
                else:
                    messages.error(request, 'Неверное имя пользователя или пароль.')
            except Exception as e:
                messages.error(request, 'Произошла ошибка при аутентификации. Пожалуйста, попробуйте снова.')
        else:
            messages.error(request, 'Пожалуйста, введите имя пользователя и пароль.')
    
    return render(request, "AuthenticateUser/signin.html")


def UserProfileView(request):
    if request.user.is_authenticated:
        profile = Profile.objects.all()
        context = {
            'profile': profile
        }
        return render(request, 'Profile/profile.html', context=context)
        # return render(request, 'Profile/profile.html', context={'profile': profile})
    else:
        return redirect('/signin')

