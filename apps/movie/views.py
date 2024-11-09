from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from .models import Movie

def Create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False) 
            movie.save()  
            form.save_m2m()

            return redirect('movies') 
    else:
        form = MovieForm()
    
    return render(request, 'movie/create.html', {'form': form})

def List(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        return render(request, 'movie/list.html', {'movies': movies})



def Update(request, id):
    movie = get_object_or_404(Movie, id=id)  
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)  
        print(form.is_valid())
        if form.is_valid():
            form.save() 
            return redirect('movies')  
    else:
        form = MovieForm(instance=movie)  

    return render(request, 'movie/update.html', {'form': form, 'movie': movie})