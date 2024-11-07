# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import  Student, Course, Department, Topic
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from webapp.storage import SupabaseStorage





def home(request):
    return render(request, "cool/index.html")



def register_student(request):
    departments = Department.objects.all()
    error_message = ""

    if request.method == 'POST':
        first_name = request.POST.get('first_name').lower()
        last_name = request.POST.get('last_name').lower()
        department_name = request.POST.get('department')
        email = request.POST.get('email').lower()
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        school = request.POST.get('institution').lower()  # Assuming this is passed as an ID or string
        profile_pic = request.FILES.get('profilepic')  # Retrieve the uploaded image
        print("profile_pic.name")


        # Initialize storage
        storage = SupabaseStorage()

        # Handle image upload
        image_url = None
        if profile_pic:
            post = 'media/' + profile_pic.name
            print(profile_pic.name)
            try:
                filename = storage.save(post, profile_pic)
                image_url = storage.url(filename)
            except Exception as e:
                error_message = "Failed to upload image to Supabase storage. Please try again."
                print(f"Error uploading image: {e}")

        # Basic validation
        if username and password and school and first_name and last_name and department_name and email:
            # Fetch the Department instance
            department = get_object_or_404(Department, name=department_name)

            # Create the user and student records
            user = User(username=username, password=make_password(password), first_name=first_name, last_name=last_name, email=email)
            user.save()

            # Create Student instance, including the profile picture if uploaded
            student = Student(
                user=user,
                department=department,
                school=school,
                image=image_url  # Store the image URL instead of the file
            )
            student.save()
            login(request, user)

            return redirect('home')
        else:
            error_message = "All fields are required."

    return render(request, 'register_student.html', {'error_message': error_message, 'alldepartments': departments})

def loginview(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"],
                            password=request.POST["password"])
        if user:
            login(request, user)
            return redirect('myprofile')
    return render(request, 'login.html')


@login_required
def list_departments(request):
    departments = Department.objects.all()
    print(departments)
    return render(request, "cool/departments.html", {"departments": departments})


@login_required
def list_all_courses(request):
    all_courses = Course.objects.all()
    return render(request, 'list_courses.html', {'courses': all_courses})


@login_required
def list_courses(request, department_id=None):
    if department_id:
        department = get_object_or_404(Department, id=department_id)
        print("here")
        courses = department.courses.all()  # Access courses through the related_name
    return render(request, 'list_courses.html', {'courses': courses, "department": department})


@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    topics = course.topics.all()
    return render(request, 'course_detail.html', {'course': course, 'topics': topics})


@login_required
def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    return render(request, 'topic_detail.html', {'topic': topic})



@login_required
def myprofile(request):
    user = request.user.username
    courses = Course.objects.all()
    return render(request, 'myprofile.html',{'user': user,'courses': courses} )

