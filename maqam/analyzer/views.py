from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "analyzer/index.html", {
        
    })

def result(request):
    if request.method == 'POST': 
        audio_file = request.POST.get("audio-file")
        
        print(request)
        return render(request, 'analyzer/result.html', {'audio_file' : audio_file})
    return render(request, "analyzer/index.html")
