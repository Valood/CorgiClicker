from django.shortcuts import render, redirect
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Corgi, Boost
from django.contrib.auth.models import User
# Create your views here.


class RegisterAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration.html", context=context)

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=name, password=password)
            login(request, user)
            Corgi.objects.create(user=user)
            return redirect("/")
        else:
            messages.success(request, ("Проблема с данными, введите другие"))
            form = UserCreationForm()
        return render(request, "registration.html", context={"form": form})


class LogoutAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        logout(request)
        return redirect("/")


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        if request.POST:
            username = request.POST.get("username", False)
            password = request.POST.get("password", False)
        else:
            request_data = dict(request.data)
            username = request_data["username"]
            password = request_data["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            print(123)
            if request.POST:
                return redirect("/game")
            return Response("OK", status=status.HTTP_200_OK)
        print(12321312312)
        messages.success(request, ("Некорректно введены данные"))
        return  render(request, "login.html")

def register_user_render(request):
    return render(request, "registration.html")


class BoostAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        username = request.query_params.get("username")
        print(username)
        user = User.objects.get(username=username)
        response_data = {}
        user = Corgi.objects.get(user=user)
        response_data["corgies"] = user.corgies
        response_data["corgies_per_click"] = user.corgies_per_click
        response_data["corgies_per_second"] = user.corgies_per_second
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        request_data = dict(request.data)
        username = request_data["username"]
        user = User.objects.get(username=username)
        user = Corgi.objects.get(user=user)
        corgies = request_data["corgies"]
        corgies_per_click = request_data["corgies_per_click"]
        user.corgies = int(request_data["corgies"])
        user.corgies_per_click = int(request_data["corgies_per_click"])
        user.corgies_per_second = int(request_data["corgies_per_second"])
        user.save()
        return Response("OK", status=status.HTTP_200_OK)

class GameAPIView(APIView):
    permission_classes = (AllowAny,)

    @csrf_exempt
    def get(self, request):
        print("fdagffdfgdsfgdsfgdsfgdsfgsdf", request.user)
        return render(request, "game.html")


