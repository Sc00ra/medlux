from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        lista_grup = list(user.groups.all())[0].name
        print(lista_grup)
        print(user)
        if user is not None:
            login(request, user)
            if lista_grup == 'admin':
                return redirect('/admin')
            elif lista_grup == 'CEO':  
                return redirect('CEO')  
            elif lista_grup == 'Dyrektor':  
                return redirect('Dyrektor/')  
            elif lista_grup == 'HR':  
                return redirect('HR/')  
            elif lista_grup == 'Ksiegowa':  
                return redirect('Ksiegowa/')  
            elif lista_grup == 'Pracownik':  
                return redirect('Pracownik/')  
            elif lista_grup == 'Recepcja':  
                return redirect('Recepcja/')
            elif lista_grup == 'Zaopatrzenie':  
                return redirect('Zaopatrzenie/')    

    return render(request, 'login.html')


def dyr_view(request):
    return render(request, 'dyrektor.html')
def CEO_view(request):
    return render(request, 'ceo.html')
def HR_view(request):
    return render(request, 'hr.html')
def Ksiegowa_view(request):
    return render(request, 'Ksiegowa.html')
def Pracownik_view(request):
    return render(request, 'pracownik_os.html')
def Recepcja_view(request):
    return render(request, 'recepcja_os1.html')
def Zaopatrzenie_view(request):
    return render(request, 'zaopatrzenie.html')
def Harmonogram_sal_dyr_view(request):
    return redirect(request,'harmonogram_sal.html')