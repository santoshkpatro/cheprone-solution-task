from django.shortcuts import redirect, render
from .models import User

# Create your views here.
def home_view(request):
    users = User.objects.all()
    if users is not None:
        context = {'users': users}
    else:
        context = {}
    return render(request, 'home_view.html', context)


def add_view(request):
    if request.method == 'POST':
        # Extracting details from POST dict
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        comments = request.POST.get('comments')
        number = request.POST.get('number')
        try:
            image = request.FILES['image']
        except:
            image = None
        
        # Checking validation
        if len(username) > 3 and len(email) > 3 and len(password) > 3:
            # Creating user object
            user = User(username=username, email=email, password=password, name=name, comments=comments, number=number, image=image)
            user.save()
        else:
            # Printing error message
            print("Validation Error")
        return redirect('home_view')
    return render(request, 'add_view.html')


def delete_view(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('home_view')


def edit_view(request, user_id):
    user = User.objects.get(id=user_id)
    context = {'user': user}
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        number = request.POST.get('number')
        comments = request.POST.get('comments')
        if len(username) > 3 and len(email) > 3:
            user.name = name
            user.username = username
            user.email = email
            user.comments = comments
            user.number = number

            # Saving to database
            user.save()
            return redirect('home_view')
    return render(request, 'edit_view.html', context)

def detail_view(request, user_id):
    user = User.objects.get(id=user_id)
    context = {'user': user}
    return render(request, 'detail_view.html', context)