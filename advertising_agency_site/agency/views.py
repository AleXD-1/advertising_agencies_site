from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Agencies, Services
from review.models import Reviews
from .forms import AgencyForm
from review.forms import ReviewForm


# class HomeAgencies(ListView):
#     model = AgenciesServices
#     template_name = 'agency/home.html'
#     context_object_name = 'agency'


# class ViewProfile(DetailView):
#     model = AgenciesServices
#     template_name = 'agency/profile.html'
#     context_object_name = 'agency_item'


# class CreateAgency(LoginRequiredMixin, CreateView):
#     form_class = AgencyForm
#     template_name = 'agency/create_agency.html'
#     raise_exception = True


def create_agency(request):
    if request.method == 'POST':
        form_agency = AgencyForm(request.POST)
        if form_agency.is_valid():
            agency_form = form_agency.save(commit=False)
            agency_form.user = request.user  # The logged-in user
            agency_form.save()
            return redirect('/')
    else:
        form_agency = AgencyForm()
        return render(request, 'agency/create_agency.html', {'form_agency': form_agency})


def home(request):
    agencies = Agencies.objects.all().select_related('services', 'city', 'region')
    return render(request, 'agency/home.html', {'agencies': agencies})


def get_service(request, service_id):
    agencies = Agencies.objects.filter(services_id=service_id).select_related('services', 'city', 'region')
    service = Services.objects.get(pk=service_id)
    return render(request, 'agency/service.html', {'agencies': agencies, 'service': service})


def view_agency(request, agency_id):
    agency_item = Agencies.objects.get(pk=agency_id)
    reviews = Reviews.objects.filter(agency_id=agency_id).select_related('client')
    if request.method == 'POST':
        form_review = ReviewForm(request.POST)
        if form_review.is_valid():
            review_form = form_review.save(commit=False)
            review_form.client = request.user.clients  # The logged-in user
            review_form.agency = agency_item  # The agency
            review_form.save()
            return redirect('/')
    else:
        form_review = ReviewForm()
    context = {'agency_item': agency_item, 'reviews': reviews, 'form_review': form_review}
    return render(request, 'agency/view_agency.html', context)


def get_profile(request):
    agencies_profile = Agencies.objects.filter(user=request.user.id).select_related('services', 'city', 'region')
    return render(request, 'agency/profile.html', {'agencies_profile': agencies_profile})
