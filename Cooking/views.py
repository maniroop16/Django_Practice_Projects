from django.shortcuts import render, redirect
from Cooking.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from Cooking.seed import *

# These are used for setting CustomUser model
#from django.contrib.auth import get_user_model
#User = get_user_model()

# Create your views here.

@login_required(login_url = "/login/")
def Recipe_view(request):
    if request.method == "POST":
        data = request.POST
        Recipe_name = data.get('Recipe_Name')
        Recipe_description = data.get('Recipe_Description')
        Recipe_image = request.FILES.get('Recipe_Image')

        ''' print(Recipe_name)
        print(Recipe_description)
        print(Recipe_image)'''

        Recipeform.objects.create(
            Recipe_Name = Recipe_name,
            Recipe_Description = Recipe_description,
            Recipe_Image = Recipe_image)
        
        return redirect("/recipe/")
    
    query_set = Recipeform.objects.all()

    if request.GET.get("search"):
        query_set = query_set.filter(Recipe_Name__icontains = request.GET.get("search"))



    context = {"Recipieslist":query_set}      

    return render(request, "cookingpage.html", context)

@login_required(login_url = "/login/")
def update_item(request, id):   

    item = Recipeform.objects.get(id = id)   

    if request.method == "POST":
        data = request.POST
        Recipe_name = data.get('Recipe_Name')
        Recipe_description = data.get('Recipe_Description')
        Recipe_image = request.FILES.get('Recipe_Image')

        item.Recipe_Name = Recipe_name
        item.Recipe_Description = Recipe_description

        if Recipe_image:
            item.Recipe_Image = Recipe_image

        item.save()  
        return redirect("/recipe/")  

    context = {"Recipe":item} 

    return render(request, "updaterecipe.html", context)


@login_required(login_url = "/login/")
def delete_item(request, id):   
    item = Recipeform.objects.get(id = id)
    item.delete()

    return redirect("/recipe/")

def login_page(request):

    if request.method == "POST":
        user_name = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username = user_name).exists():
            messages.warning(request, "Invalid User / User does not exist")
            return redirect("/login/")
        
        user = authenticate(username = user_name, password = password)

        if user is None:
            messages.warning(request, "Invalid password")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/recipe/")


    return render(request, "login.html")

@login_required(login_url = "/login/")
def logout_page(request):
    logout(request)
    return redirect("/login/")

def register(request):
    
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        user_name = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username = user_name)
        if user.exists():
            messages.warning(request, "Username already exists")
            return redirect("/register/")


        user = User.objects.create(
            first_name= first_name,
            last_name= last_name,
            username= user_name
            )
        
        user.set_password(password)
        user.save()

        messages.success(request, "Account created successfully")

        return redirect ("/register/")    
    return render(request, "register.html")


def get_students(request):
    queryset = Student.objects.all()

    if request.GET.get("search"):
        search = request.GET.get("search")
        queryset = Student.objects.filter(Q(student_name__icontains = search) |
                                          Q(student_id__student_id__icontains = search) |
                                          Q(student_email__icontains = search)
                                          )

    paginator = Paginator(queryset, 5)  # Show 5 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "students.html", {"students":page_obj} )


def get_marks(request, student_id):
    #generate_studentranks()

    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    studentname = Student.objects.filter(student_id__student_id = student_id)[0].student_name
    total = queryset.aggregate(total_marks = Sum("subjectmarks"))


    return render(request, "getmarks.html",{"queryset": queryset, "studentname":studentname, "student_id":student_id,"total":total})