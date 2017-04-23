from django.shortcuts import render
from django import views


class HomeView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {})
