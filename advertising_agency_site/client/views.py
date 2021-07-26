from django.shortcuts import render, redirect
from .models import Clients
from .forms import ClientForm


def get_client_profile(request):
    client_profile = Clients.objects.get(user=request.user.id)
    return render(request, 'client/client_profile.html', {'client_profile': client_profile})


def create_client_profile(request):
    if request.method == 'POST':
        form_client = ClientForm(request.POST)
        if form_client.is_valid():
            client_form = form_client.save(commit=False)
            client_form.user = request.user  # The logged-in user
            client_form.save()
            return redirect('home')
    else:
        form_client = ClientForm()
        return render(request, 'client/create_client_profile.html', {'form_client': form_client})
