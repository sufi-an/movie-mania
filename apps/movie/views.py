from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Movie
from django.core.exceptions import PermissionDenied


class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie/create.html'
    success_url = reverse_lazy('movies')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        
        return super().form_valid(form)

class MovieListView(ListView):
    model = Movie
    template_name = 'movie/list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = super().get_queryset()  # Get the default queryset
        
        user = self.request.user
        queryset = queryset.filter(created_by=user)
        
        # Add any other queryset modifications here
        return queryset

class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie/update.html'
    success_url = reverse_lazy('movies')

    def get_object(self, queryset=None):
       
        movie = super().get_object(queryset)
        
        # Check if the current user is the creator
        if movie.created_by != self.request.user:
            raise PermissionDenied 
        
        return movie


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie/detail.html"

    def get_object(self, queryset=None):
       
        movie = super().get_object(queryset)
        
        # Check if the current user is the creator
        if movie.created_by != self.request.user:
            raise PermissionDenied 
        
        return movie

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movie/delete.html'
    success_url = reverse_lazy('movies')

    def get_object(self, queryset=None):
       
        movie = super().get_object(queryset)
        
        # Check if the current user is the creator
        if movie.created_by != self.request.user:
            raise PermissionDenied 
        
        return movie


