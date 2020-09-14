from rest_framework.parsers import FileUploadParser, MultiPartParser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import get_user_model, authenticate, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.forms import UserRegistrationForm, UserForm, ProfileForm
from account.permission import UserPermissionOnAPIView
from account.serializers import UserSerializers, ProfileSerializers

User = get_user_model()

# Create your views here.


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = "account/user_form.html"
    success_url = reverse_lazy('account:login')


def profile_request(request, pk):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'account/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


class ProfileAPIView(APIView):
    parser_class = (MultiPartParser,)

    permission_classes = (UserPermissionOnAPIView,)

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        return Response(ProfileSerializers(user).data)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = ProfileSerializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(viewsets.ModelViewSet):
    base_name = 'users'
    serializer_class = UserSerializers
    queryset = User.objects.all()

    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/account/home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "account/login_form.html",
                    context={"form":form})


@login_required
def logout_request(request):
    logout(request)
    return HttpResponseRedirect('/')
