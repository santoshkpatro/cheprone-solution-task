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
        # print(request.POST)
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        comments = request.POST.get('comments')
        image = request.FILES['image']
        # print("Details: " + name + username + email + password + comments)
        user = User(name=name, username=username, email=email, password=password, comments=comments, image=image)
        user.save()
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
        user.name = request.POST.get('name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.comments = request.POST.get('comments')
        user.save()
        return redirect('home_view')
    return render(request, 'edit_view.html', context)