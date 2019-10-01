"""name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
Символ/выражение 	Совпадающая строка
. (Точка) 	         Любой символ
^ (Каретка)          Начало строки
$ 	                 Конец строки
* 	                 0 или более повторений
+ 	                 1 или более повторений
? 	                 0 или 1 повторение
| 	                 A | B означает A или B
[a-z] 	             Любая буква в нижнем регистре
\w 	                 Любой цифробуквенный символ или _ _
\d 	                 Любая цифра

    http://127.0.0.1:8000/user/<username>
"""
from django.contrib import admin
from django.urls import path
from posts import views
from posts.views import Profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('^user/(\w+)/$', Profile.as_view())
]
