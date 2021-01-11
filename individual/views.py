import math
from django.http import Http404
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Individual,Rating
from .forms import IndividualCreateForm,RatingCreateForm,SearchForm

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def browse_view(request):
    individuals = Individual.objects.all()

    search_form = SearchForm(request.POST or None)
    if request.method == 'POST' and request.POST['search'] !='':
        search_form = SearchForm(request.POST)
        individuals = Individual.objects.filter(name=request.POST['search'])
        print(request.POST)

    context = {"individuals":individuals,'search_form':search_form}
    return render(request,"individual/browse.html",context)

def create_individual_view(request):
    form = IndividualCreateForm()
    if request.method == 'POST':
        form = IndividualCreateForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('/individual/browse')
    else:
        return render(request, 'individual/post.html', {"form": form})

def read_individual_view(request,individual_id):
    try:
        individual = Individual.objects.get(id = individual_id)
    except Individual.DoesNotExist:
        raise Http404

    ratingQuery = Rating.objects.filter(individual__pk = individual.id)

    sum = 0
    floor = 0
    minusceil = 0
    odd = False
    avg = 0
    alreadyRate = False
    if len(ratingQuery)!= 0:
        for r in ratingQuery:
            sum += r.rating
            if request.user == r.author:
                alreadyRate = True
        avg = sum / len(ratingQuery)
        floor = math.floor(avg)
        minusceil = 5 - math.ceil(avg)
        if avg %1 != 0:
            odd = True

    rating_form = RatingCreateForm(request.POST or None)

    context = {
        'individual': individual,
        'rating':ratingQuery,
        'floor':floor,
        'minusceil':minusceil,
        'odd':odd,
        'avg':avg,
        'alreadyRate':alreadyRate,
        'rating_form':rating_form,
    }
    
    if request.method == 'POST':
        print(request.POST)
        rating_form = RatingCreateForm(request.POST)
        if rating_form.is_valid():
            obj = rating_form.save(commit=False)
            obj.individual = individual
            obj.author = request.user
            obj.save()
            return render(request,"individual/detail.html",context)
    
    return render(request,"individual/detail.html",context)

def update_individual_view(request,individual_id):
    try:
        individual = Individual.objects.get(id = individual_id)
    except Individual.DoesNotExist:
        raise Http404
    form = IndividualCreateForm(request.POST or None, instance = individual)
    if request.method == 'POST':
        form = IndividualCreateForm(request.POST, request.FILES, instance = individual)
        if form.is_valid():
            form.save()
            return redirect(f"/individual/{individual_id}")
    context = {
        'individual': individual,
        'form':form
    }
    return render(request,"individual/edit.html",context)

def delete_individual_view(request,individual_id):
    try:
        individual = Individual.objects.get(id = individual_id)
    except Individual.DoesNotExist:
        return redirect('/individual')
    individual.delete()
    return redirect('/individual')

def update_rate_view(request,individual_id,rate_id):
    try:
        rate = Rating.objects.get(id = rate_id)
        individual = Individual.objects.get(id = individual_id)
    except:
        return redirect(f"/individual/{individual_id}")
    form = RatingCreateForm(request.POST or None, instance = rate)
    if request.method == 'POST':
        form = RatingCreateForm(request.POST, instance = rate)
        if form.is_valid():
            form.save()
            return redirect(f"/individual/{individual_id}")
    context = {
        'individual': individual,
        'form_edit_rate':form
    }
    return render(request,"individual/edit.html",context)

def delete_rate_view(request,individual_id,rate_id):
    try:
        rate = Rating.objects.get(id = rate_id)
    except Rating.DoesNotExist:
        return redirect(f"/individual/{individual_id}")
    rate.delete()
    return redirect(f"/individual/{individual_id}")