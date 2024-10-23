from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib import messages
from random import shuffle
import random
from PIL import Image

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Category, Package,PackageImage,Booking,Contactus
from .forms import PackageForm,CategoryForm,ContactusForm



def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.success(request, ("There Was An Error Loging In, Try Again..."))
            return redirect('user_login')
    return render(request, 'authenticate/login.html')


@login_required(login_url='user_login')
def admin_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'admin_dashboard.html')
    else:
        return redirect('user_login')

def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('index')




def index(request):
    all_categories = list(Category.objects.all())
    categories = random.sample(all_categories, min(len(all_categories), 4))

    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Your message has been successfully submitted!"
            return render(request, 'index.html', {'form': ContactusForm(),'success_message': success_message})
    else:
        form = ContactusForm()

    return render(request, 'index.html', {'form': form, 'categories': categories})


def packages_view(request):
    packages = Package.objects.all()
    return render(request, 'package_view.html', {'packages': packages})


def category_selection(request):
    categories = Category.objects.all()
    return render(request, 'category_selection.html', {'categories': categories})




def reservation(request):

    categories = Category.objects.all()
    return render(request,'reservation.html',{'categories': categories})

from django.http import JsonResponse

def get_packages(request, category_id):
    category = Category.objects.get(pk=category_id)
    packages = category.packages.all()
    
    # Convert packages to a list of dictionaries
    package_list = [{'id': package.id, 'name': package.name} for package in packages]
    
    return JsonResponse({'packages': package_list})


@require_POST
def submit_booking(request):
    # Retrieve form data
    full_name = request.POST.get('booking-form-name')
    phone = request.POST.get('booking-form-phone')
    time = request.POST.get('booking-form-time')
    date = request.POST.get('booking-form-date')
    num_people = request.POST.get('booking-form-number')
    category_id = request.POST.get('booking-form-category')
    package_id = request.POST.get('booking-form-package')
    message = request.POST.get('booking-form-message')

    # Create or get the Category and Package objects
    category = Category.objects.get(pk=category_id)
    package = Package.objects.get(pk=package_id)

    booking = Booking.objects.create(
        full_name=full_name,
        phone=phone,
        time=time,
        date=date,
        num_people=num_people,
        category=category,
        package=package,
        message=message
    )

    
    messages.success(request, "Reservation submitted successfully!")
    return redirect('reservation')

# Packages

@login_required(login_url='user_login')
def admin_add_packages(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            package = form.save()
            images = request.FILES.getlist('image')
            for image in images:
                PackageImage.objects.create(package=package, image=image)
            return redirect('admin_packages_view')  # Replace 'success_url' with your desired redirect URL after successful submission
    else:
        form = PackageForm()
    return render(request, 'admin_add_packages.html', {'form': form,'categories':categories})

@login_required(login_url='user_login')
def admin_packages_view(request):
    packages = Package.objects.all().order_by('-id')
    return render(request,'admin_packages_view.html',{'packages':packages})


@login_required(login_url='user_login')
def admin_update_packages(request, package_id):
    categories = Category.objects.all()
    package = get_object_or_404(Package, pk=package_id)
    
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES, instance=package)
        
        if form.is_valid():
            form.save()

            # Handle image removal
            if 'remove_image' in request.POST:
                remove_image_ids = request.POST.getlist('remove_image')
                for image_id in remove_image_ids:
                    try:
                        image_to_remove = PackageImage.objects.get(id=image_id)
                        image_to_remove.delete()
                    except PackageImage.DoesNotExist:
                        pass

            # Save new images
            images = request.FILES.getlist('image')
            for image in images:
                PackageImage.objects.create(package=package, image=image)

            return redirect('admin_packages_view')
    else:
        form = PackageForm(instance=package)

    return render(request, 'admin_update_packages.html', {'form': form, 'categories': categories, 'package': package})


@login_required(login_url='user_login')
def admin_delete_packages(request,id):
    packages = Package.objects.get(id=id)
    packages.delete()
    return redirect('admin_packages_view')





#Bookings 

@login_required(login_url='user_login')
def admin_booking_view(request):
    bookings = Booking.objects.all().order_by('-id')
    return render(request, 'admin_booking_view.html', {'bookings': bookings})

@login_required(login_url='user_login')
def admin_delete_bookings(request,id):
    bookings= Booking.objects.get(id=id)
    bookings.delete()
    return redirect('admin_booking_view')




# Contact Us

@login_required(login_url='user_login')
def admin_contact_view(request):
    contact = Contactus.objects.all().order_by('-id')
    return render(request,'admin_contact_view.html',{'contact':contact})

@login_required(login_url='user_login')
def admin_delete_contact(request,id):
    contact = Contactus.objects.get(id=id)
    contact.delete()
    return redirect('admin_contact_view')



# Categories
def admin_add_categories(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_category_view')  # Redirect to admin dashboard or any other page
    else:
        form = CategoryForm()
    return render(request, 'admin_add_categories.html', {'form': form})

@login_required(login_url='user_login')
def admin_category_view(request):
    categories = Category.objects.all().order_by('-id')
    return render(request,'admin_category_view.html',{'categories':categories})

@login_required(login_url='user_login')
def admin_update_categories(request, id):
    categories = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=categories)
        if form.is_valid():
            if 'remove_image' in request.POST:
                categories.image.delete()  # Delete the current image
                categories.image = None    # Remove the image field value
            form.save()
            return redirect('admin_category_view')
    else:
        form = CategoryForm(instance=categories)
    return render(request, 'admin_update_categories.html', {'form': form, 'categories': categories})
    




@login_required(login_url='user_login')
def admin_delete_categories(request,id):
    categoriess = Category.objects.get(id=id)
    categoriess.delete()
    return redirect('admin_category_view')



def package_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    packages = category.packages.all()
    return render(request, 'package_view.html', {'category': category, 'packages': packages})


def gallery_view(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    images = package.images.all()
    return render(request, 'gallery.html', {'package': package, 'images': images})
