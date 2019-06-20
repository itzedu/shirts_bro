from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def register(request):
    # validations
    errors = False
    if(len(request.POST['first_name']) < 1):
        messages.error(request, 'First name is required')
        errors = True
    if(len(request.POST['last_name']) < 1):
        messages.error(request, 'Last name is required')
        errors = True
    if(len(request.POST['email']) < 1):
        messages.error(request, 'Email is required')
        errors = True
    if(len(request.POST['password']) < 1):
        messages.error(request, 'Password is required')
        errors = True
    if(request.POST['password'] != request.POST['confirm_password']):
        messages.error(request, 'Passwords do not match')
        errors = True

    if(errors):
        return redirect('/')
    
    # user creation
    hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'], 
        email = request.POST['email'], 
        password = hashed, 
    )

    request.session['user_id'] = user.id
    return redirect('/main')

def login(request):
    try:
        user = User.objects.get(email = request.POST['email'])
        if(bcrypt.checkpw(request.POST['password'].encode(), user.password.encode())):
            request.session['user_id'] = user.id
            return redirect('/main')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/')
    except User.DoesNotExist:
        messages.error(request, 'Invalid Credentials')
        return redirect('/')

def main(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You fool')
        return redirect('/')
    else:
        user = User.objects.get(id = request.session['user_id'])
        context = {
            'current_user': user
        }
        return render(request, 'store/main.html', context)

def new_shirt(request):
    return render(request, 'store/new_shirt.html')


def create_shirt(request):
    user = User.objects.get(id = request.session['user_id'])
    Shirt.objects.create(
        color = request.POST['color'],
        size = request.POST['size'],
        fabric = request.POST['fabric'],
        fabricator = user
    )
    return redirect('/main')

def show_shirt(request, shirt_id):
    shirt = Shirt.objects.get(id = shirt_id)
    context = {
        'shirt': shirt
    }
    return render(request, 'store/show_shirt.html', context)

def delete_shirt(request, shirt_id):
    Shirt.objects.get(id = shirt_id).delete()
    return redirect('/main')

def logout(request):
    request.session.clear()
    return redirect('/')