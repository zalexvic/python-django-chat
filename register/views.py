from django.shortcuts import render, redirect
from .forms import RegisterForm
from chat.models import Profile


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            profile = Profile()

            profile.user = user
            profile.handle = form.cleaned_data['handle']
            if form.cleaned_data['profile_pic']:
                profile.profile_pic = form.cleaned_data['profile_pic']

            profile.save()
        return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register/signup.html', {'form': form})