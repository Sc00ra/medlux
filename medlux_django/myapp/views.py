from django.shortcuts import render

# Create your views here.
def strona1(request):
    return render(request, 'strona1.html')

def strona2(request):
    return render(request, 'strona2.html')

