from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

def menu_view(request):
    return render(request,'testapp/menu.html')

def location_view(request):
    return render(request,'testapp/location.html')

def feedback_view(request):
    return render(request,'testapp/feedback.html')

def table_view(request):
    return render(request,'testapp/table.html')

def submit_view(request):
    return render(request,'testapp/submit.html')

def download_view(request):
    return render(request,'testapp/download.html')

def register_view(request):
    return render(request,'testapp/register.html')

def list_view(request):
    return render(request,'testapp/list.html')

def scoups_view(request):
    return render(request,'testapp/scoups.html')

def salads_view(request):
    return render(request,'testapp/salads.html')

def deserts_view(request):
    return render(request,'testapp/deserts.html')

def smooth_view(request):
    return render(request,'testapp/smooth.html')
