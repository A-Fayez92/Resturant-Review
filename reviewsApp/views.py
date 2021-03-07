from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, reviewForm
from django.contrib.auth.decorators import login_required
from .models import resturants, review
from textblob import TextBlob


# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'signup.html', context)


@login_required(login_url='login')
def home(request):
    res = resturants.objects.all()
    context = {
        'res': res
        # 'all_blogs':all_blogs
    }

    return render(request, 'home.html', context)


@login_required(login_url='login')
def add_review(request, pk):
    resturant = resturants.objects.get(pk=pk)
    form = reviewForm()
    form.fields["author"].initial = request.user.id
    form.fields["resturant"].initial = resturant.id
    if request.method == "POST":
        form = reviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'resturant': resturant, 'form': form}
    return render(request, 'add_review.html', context)


@login_required(login_url='login')
def view_review(request, pk):
    all_reviews = review.objects.filter(resturant=pk)
    resturant = resturants.objects.get(pk=pk)

    neg = 0.0
    pos = 0.0
    neg_count = 0
    neutral_count = 0
    pos_count = 0
    for revieww in all_reviews:
        # print tweet.text
        blob = TextBlob(revieww.content)
        if blob.sentiment.polarity < 0:  #Negative
            neg += blob.sentiment.polarity
            neg_count += 1
        elif blob.sentiment.polarity == 0:  #Neutral
            neutral_count += 1
        else:  #Positive
            pos += blob.sentiment.polarity
            pos_count += 1

    context = {
        'resturant': resturant,
        'all_reviews': all_reviews,
        'pos': pos_count,
        'neg': neg_count,
        'neu': neutral_count
    }
    return render(request, 'view_review.html', context)


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')