from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from movie_tracker.forms import *
from django.views import View

class SignUp(View):
    template_name = "signup.html"

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('movies_index')

        return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})