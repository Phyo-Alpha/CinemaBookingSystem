from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils import timezone
from django.shortcuts import render, redirect
from django.db.models import Q
from manager.forms import *
from main.models import *

# Logout
def my_logout(request):
    logout(request)
    return redirect('/login')

# Functions for Main Page
def manager_home(request):
    return render(request, 'manager_home.html')

# Functions for User Preferences
@login_required(login_url='/login/')
def user_preferences(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateCustomerForm(request.POST, request.FILES, instance=request.user.customer)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile & preferences is updated successfully')
            return redirect(to='user_preferences')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateCustomerForm(instance=request.user.customer)
        # customer = Customer.objects.get(user=request.user)
        context = {'user_form': user_form, 'profile_form': profile_form}

    return render(request, 'user_preferences.html', context)

# Functions for Cinema Room
def create_cinema_room(request):
    if request.method == 'POST':
        form = CinemaRoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cinema Room created successfully')
            return redirect('cinema_room_list')
    else:
        form = CinemaRoomForm()
    return render(request, 'cinema_room_create.html', {'form': form})

def cinema_room_list(request):
    query = request.GET.get('q')
    if query:
        cinema_rooms = CinemaRoom.objects.filter(room_name__icontains=query)
    else:
        cinema_rooms = CinemaRoom.objects.all()
    return render(request, 'cinema_room_list.html', {'cinema_rooms': cinema_rooms})

def update_cinema_room(request, pk):
    cinema_room = CinemaRoom.objects.get(room_id=pk)
    if request.method == 'POST':
        form = CinemaRoomForm(request.POST, instance=cinema_room)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cinema Room updated successfully')
            return redirect('cinema_room_list')
    else:
        form = CinemaRoomForm(instance=cinema_room)
    return render(request, 'cinema_room_update.html', {'form': form})

# Functions for Food and Drinks
def food_and_drinks_create(request):
    if request.method == 'POST':
        form = FoodAndDrinksForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food and Drinks created successfully')
            return redirect('food_and_drinks_list')
    else:
        form = FoodAndDrinksForm()
    return render(request, 'food_and_drinks_create.html', {'form': form})

def food_and_drinks_list(request):
    food_and_drinks = FoodAndDrinks.objects.all()
    return render(request, 'food_and_drinks_list.html', {'food_and_drinks': food_and_drinks})

def food_and_drinks_update(request, pk):
    food_and_drinks = FoodAndDrinks.objects.get(combo_id=pk)
    if request.method == 'POST':
        form = FoodAndDrinksForm(request.POST, instance=food_and_drinks)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food and Drinks updated successfully')
            return redirect('food_and_drinks_list')
    else:
        form = FoodAndDrinksForm(instance=food_and_drinks)
    return render(request, 'food_and_drinks_update.html', {'form': form})

def food_and_drinks_delete(request, pk):
    food_and_drinks = FoodAndDrinks.objects.get(combo_id=pk)
    try:
        food_and_drinks.delete()
        messages.success(request, 'Food and Drink deleted successfully')
    except:
        pass
    return redirect('food_and_drinks_list')

# Functions for Movie
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie created successfully')
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie_create.html', {'form': form})

def movie_list(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(movie_title__icontains=query)
    else:
        movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies, 'query': query})
    

def movie_update(request, pk):
    movie = Movie.objects.get(movie_id=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie updated successfully')
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie_update.html', {'form': form})

# Functions for Movie Session
def movie_session_create(request):
    if request.method == 'POST':
        form = MovieSessionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie Session created successfully')
            return redirect('movie_session_list')
    else:
        form = MovieSessionForm()
    return render(request, 'movie_session_create.html', {'form': form})

def movie_session_list(request):
    query = request.GET.get('q')
    now = timezone.now()
    if query:
        movie_sessions = MovieSession.objects.filter(
            Q(movie_id__movie_title__icontains=query) |
            Q(room_id__room_name__icontains=query))
    else:
        movie_sessions = MovieSession.objects.all()
    return render(request, 'movie_session_list.html', {'movie_sessions': movie_sessions, 'query': query, 'now': now})

def movie_session_update(request, pk):
    movie_session = MovieSession.objects.get(session_id=pk)
    if request.method == 'POST':
        form = MovieSessionForm(request.POST, instance=movie_session)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie Session updated successfully')
            return redirect('movie_session_list')
    else:
        form = MovieSessionForm(instance=movie_session)
    return render(request, 'movie_session_update.html', {'form': form})

def movie_session_delete(request, pk):
    movie_session = MovieSession.objects.get(session_id=pk)
    try:
        movie_session.delete()
        messages.success(request, 'Movie Session deleted successfully')
    except:
        pass
    return redirect('movie_session_list')

# Functions for Seat
def seat_create(request):
    if request.method == 'POST':
        form = SeatForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seat created successfully')
            return redirect('seat_list')
    else:
        form = SeatForm()
    return render(request, 'seat_create.html', {'form': form})

def seat_list(request):
    seats = Seat.objects.all()
    return render(request, 'seat_list.html', {'seats': seats})

def seat_update(request, pk):
    seat = Seat.objects.get(seat_id=pk)
    if request.method == 'POST':
        form = SeatForm(request.POST, instance=seat)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seat updated successfully')
            return redirect('seat_list')
    else:
        form = SeatForm(instance=seat)
    return render(request, 'seat_update.html', {'form': form})

def seat_delete(request, pk):
    seat = Seat.objects.get(seat_id=pk)
    try:
        seat.delete()
        messages.success(request, 'Seat deleted successfully')
    except:
        pass
    return redirect('seat_list')

# Functions for Report
def report_page(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            tickets = Ticket.objects.filter(purchased_date__range=[start_date, end_date])
            sales = Ticket.objects.filter(purchased_date__range=[start_date, end_date]).count()
            revenue = sum(ticket.cost for ticket in tickets)
            template = get_template('report.html')
            context = {'tickets': tickets, 'revenue': revenue, 'sales': sales, 'start_date': start_date, 'end_date': end_date}
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa.CreatePDF(html, dest=response)
            return response
    else:
        form = ReportForm()
    return render(request, 'report_page.html', {'form': form})
    
