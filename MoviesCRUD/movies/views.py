from django.shortcuts import render, redirect
from movies.models import Movie
from movies.forms import MovieForm

# Create your views here.
def show(request):
    movies = Movie.objects.all()
    return render(request, "show.html", {'movies': movies})

def edit(request, m_ID):
    movie = Movie.objects.get(id = m_ID)
    return render(request, "edit.html", {'movie': movie})

def update(request, m_ID):
    movie = Movie.objects.get(id = m_ID)
    form = MovieForm(request.POST, instance = movie)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, "edit.html", {'movie': movie})

def destroy(request, m_ID):
    movie = Movie.objects.get(id = m_ID)
    movie.delete()
    return redirect("/show")

def movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                print("Error in saving form!")
    else:
        form = MovieForm()
        return render(request, "index.html", {'form': form})
