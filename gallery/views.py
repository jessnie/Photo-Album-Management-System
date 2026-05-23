from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator
import cloudinary.uploader
from .models import RecipePhoto
from .forms import RecipePhotoForm


# Mixin to check if user owns the photo or is admin
class OwnerOrAdminMixin(UserPassesTestMixin):
    def test_func(self):
        photo = self.get_object()
        return self.request.user.id == photo.owner_id or self.request.user.is_staff


class GalleryListView(LoginRequiredMixin, FormMixin, ListView):
    """Display list of all photos with search functionality"""
    model = RecipePhoto
    template_name = 'gallery/home.html'
    context_object_name = 'photos'
    paginate_by = 2
    form_class = RecipePhotoForm
    login_url = 'login'

    def get_queryset(self):
        queryset = RecipePhoto.objects.all().order_by('-uploaded_at')
        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['query'] = query
        context['form'] = self.get_form()
        context['photo_count'] = RecipePhoto.objects.count()
        # Add is_owner for each photo
        for photo in context.get('photos', []):
            photo.is_owner = self.request.user.id == photo.owner_id
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            photo = form.save(commit=False)
            photo.owner = request.user
            photo.save()
            messages.success(request, 'Photo uploaded successfully!')
            return redirect('gallery_home')
        return self.get(request, *args, **kwargs)


class PhotoDetailView(LoginRequiredMixin, DetailView):
    """Display single photo details"""
    model = RecipePhoto
    template_name = 'gallery/detail.html'
    context_object_name = 'photo'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user.id == self.object.owner_id
        return context


class PhotoCreateView(LoginRequiredMixin, CreateView):
    """Create a new photo - handled by GalleryListView POST"""
    model = RecipePhoto
    form_class = RecipePhotoForm
    template_name = 'gallery/create.html'
    success_url = reverse_lazy('gallery_home')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Photo created successfully!')
        return super().form_valid(form)


class PhotoUpdateView(LoginRequiredMixin, OwnerOrAdminMixin, UpdateView):
    """Update a photo - only owner or admin can update"""
    model = RecipePhoto
    form_class = RecipePhotoForm
    template_name = 'gallery/edit.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('gallery_home')
    login_url = 'login'

    def get_queryset(self):
        """Only return photos owned by the user or accessible by admins"""
        if self.request.user.is_staff:
            return RecipePhoto.objects.all()
        return RecipePhoto.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user.id == self.object.owner_id
        return context

    def form_valid(self, form):
        messages.success(self.request, f"'{form.instance.title}' updated successfully!")
        return super().form_valid(form)


class PhotoDeleteView(LoginRequiredMixin, OwnerOrAdminMixin, DeleteView):
    """Delete a photo - only owner or admin can delete"""
    model = RecipePhoto
    template_name = 'gallery/delete.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('gallery_home')
    login_url = 'login'

    def get_queryset(self):
        """Only return photos owned by the user or accessible by admins"""
        if self.request.user.is_staff:
            return RecipePhoto.objects.all()
        return RecipePhoto.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user.id == self.object.owner_id
        return context

    def delete(self, request, *args, **kwargs):
        photo = self.get_object()
        title = photo.title

        # Delete from Cloudinary
        if photo.image:
            try:
                cloudinary.uploader.destroy(photo.image.public_id)
            except Exception as e:
                print(f"Cloudinary deletion failed: {e}")

        messages.success(request, f"'{title}' was completely deleted.")
        return super().delete(request, *args, **kwargs)


class UserPhotosView(LoginRequiredMixin, ListView):
    """Display photos owned by the current user"""
    model = RecipePhoto
    template_name = 'gallery/user_photos.html'
    context_object_name = 'photos'
    paginate_by = 6
    login_url = 'login'

    def get_queryset(self):
        return RecipePhoto.objects.filter(owner=self.request.user).order_by('-uploaded_at')


# Legacy view functions for backwards compatibility
def gallery_view(request):
    return GalleryListView.as_view()(request)


def edit_recipe(request, pk):
    return PhotoUpdateView.as_view()(request, pk=pk)


def delete_recipe(request, pk):
    return PhotoDeleteView.as_view()(request, pk=pk)


# ===== AUTHENTICATION VIEWS =====

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


class RegisterView(CreateView):
    """Register a new user"""
    model = User
    template_name = 'gallery/register.html'
    fields = ['username', 'email', 'password']
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Validate input
        if not username or not email or not password:
            messages.error(request, 'All fields are required!')
            return render(request, self.template_name)

        if password != password_confirm:
            messages.error(request, 'Passwords do not match!')
            return render(request, self.template_name)

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, self.template_name)

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return render(request, self.template_name)

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request, 'Account created successfully! Please log in.')
        return redirect(self.success_url)


class LoginView(View):
    """Login view for existing users"""
    template_name = 'gallery/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('gallery_home')
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('gallery_home')
        else:
            messages.error(request, 'Invalid username or password!')
            return render(request, self.template_name)


class LogoutView(LoginRequiredMixin, View):
    """Logout the current user"""
    login_url = 'login'

    def get(self, request):
        auth_logout(request)
        messages.success(request, 'Logged out successfully!')
        return redirect('login')


class ProfileView(LoginRequiredMixin, View):
    """Display user profile"""
    template_name = 'gallery/profile.html'
    login_url = 'login'

    def get(self, request):
        user = request.user
        photo_count = RecipePhoto.objects.filter(owner=user).count()
        context = {
            'user': user,
            'photo_count': photo_count,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user = request.user
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')