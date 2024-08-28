from django.shortcuts import render
from firstApp.models import Movie
from firstApp.forms import MovieInfoForm


#def studentDetailsView(request):
#    form = forms.StudentInfoForm()
#    studentInfo = {'form':form}
#    return render(request,'firstApp/index.html',context=studentInfo)

def home_page_view(request):
    return render(request, 'firstApp/index.html')

def add_movie_view(request):
    form = MovieInfoForm()
    if request.method == 'POST':
        form = MovieInfoForm(request.POST)
        if form.is_valid():
            form.save()
        return home_page_view
    return render(request,'firstApp/add_movie.html',{'form':form})

def list_movie_view(request):
    movies_list = Movie.objects.all()
    return render(request,'firstApp/list_movie.html',{'movies_list':movies_list})
       





