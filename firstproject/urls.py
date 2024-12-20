"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path, include
from Home.views import *
from Cooking.views import *
from ToDo.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        
    # These are used for Home app
    path("", home ,name = "home"),       
    path("contact/", contact, name = "contact"),
    path("about/", about, name="about"),

    # Used for sendig Email
    path("send_email/", testingmail ,name = "testingmail"),

    # These are used for Cooking app
    path("recipe/", Recipe_view, name = "recipe"),
    path("delete_recipe/<id>/", delete_item, name = "delete_item"),
    path("update_recipe/<id>/", update_item, name = "update_item"),
    path("login/", login_page, name = "login"),
    path("logout/", logout_page, name = "logout"),
    path("register/", register, name = "register"),

    # These are used for Student model in Cooking app and pracicing working with admin panal
    path("students/", get_students, name = "get_students"),
    path("getmarks/<student_id>/", get_marks, name = "get_marks"),

    # TODO urls
    path('todo/', todoadd, name = 'todo'),
    path('edit_task/<id>/', edit_task, name = 'edit_task'),
    path('delete_task/<id>/', delete_task, name = 'delete_task'),
    

    # These are for API congfiguration
    path("", include("Cooking.urls")),
    
    
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
