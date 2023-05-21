from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import *
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from main.extendedEncoder import ExtendedEncoder
from django.contrib import messages
import json


# Create your views here.
def mainPage(response):
    
    if response.session.get('redirect') is None:
        response.session['redirect'] = False
    
    if not response.user.is_authenticated:
        return redirect ("/login")
    
    if response.user.user_type_id == 2 and response.session['redirect'] == False:
        response.session['redirect'] = True
        return redirect ("/ticket_list")
    
    if response.user.user_type_id == 3 and response.session['redirect'] == False:
        response.session['redirect'] = True
        return redirect ("/manager_home")
    
    if response.user.user_type_id == 4 and response.session['redirect'] == False:
        response.session['redirect'] = True
        return redirect ("/admin")
    
    if response.method == 'POST' and response.POST.get('addMovie'):
        m = Movie()
        m.save()

        return redirect(reverse('home'))

    if CinemaRoom.objects.count() == 0:
        cr = CinemaRoom.objects.create(room_name="Room 1")
        cr.save()
         
    movies = Movie.objects.all()
    
    for movie in movies:    
        if MovieSession.objects.filter(movie_id = movie).count() == 0 and movie.is_active == True:
            movie_session = MovieSession (movie_id= movie, room_id = CinemaRoom.objects.get(room_id = 1), start_time = datetime.now())
            movie_session.save()
    
    sessions = MovieSession.objects.select_related('movie_id').all().values('session_id','movie_id__movie_id', 'movie_id__movie_title', 'movie_id__movie_duration', 'movie_id__movie_genre','movie_id__movie_img', 'movie_id__movie_description' ,'movie_id__is_active', 'room_id__room_id', 'room_id__room_name', 'start_time')
    sessions_list = list(sessions)
    
    for session in sessions_list:
        session['start_time'] = session['start_time'].strftime("%Y-%m-%d %H:%M:%S")
        
    sessions_json = json.dumps(sessions_list)
    return render(response, 'CinemaCustomerPages/home.html', {'movies': movies,'sessions' : sessions , 'sessions_json': sessions_json})


def movie_details(response, session_id):
    
    session = MovieSession.objects.select_related('movie_id','room_id').get(session_id=session_id)
    movie = session.movie_id
    room = session.room_id
    session_dict = model_to_dict(session)
    session_dict['start_time'] = session_dict['start_time'].strftime("%Y-%m-%d %H:%M:%S")
    session_dict['movie'] = model_to_dict(movie)
    session_dict['room'] = model_to_dict(room)
    
    customer = Customer.objects.get(user = response.user)
    customer_json = json.dumps(model_to_dict(customer), cls=ExtendedEncoder)

    if Seat.objects.filter(room_id = room).count() == 0:
        room.create_seats()
    
    
    seats = list (Seat.objects.filter(room_id = room).values('seat_id', 'seat_row', 'seat_number', 'is_available'))
    
    for seat in seats:
        seat['session_id'] = session_id
    
    session_dict['seats'] = seats
    
    session_json = json.dumps(session_dict)
    
    user_reviews = list(RatingAndReview.objects.filter(movie_id = movie).select_related('user_id').values('user_id__username', 'review', 'rating'))
    
    # intecept the review sent by the user
    if response.method == 'POST':
        print(response.POST)
        
        UserReview = RatingAndReview(movie_id = movie, user_id = response.user, review = response.POST.get('review'), rating = int(response.POST.get('rating')))
        UserReview.save()
        
        user_reviews.append({
            'user_id__username': response.user.username,
            'review': UserReview.review,
            'rating': UserReview.rating
        })
        print(user_reviews)
        userReviews_json = json.dumps(user_reviews)
        
        # save the data in session to be used in the reviewSuccess function 
        response.session["session"] = session_json
        response.session["user_review"] = userReviews_json
        response.session["customer"] = customer_json
        
        return redirect('movie_details', session_id=session_id)
        
    userReviews_json = json.dumps(user_reviews)
    return render(response, 'CinemaCustomerPages/movie_detail.html', {'movie': movie,'session_json': session_json, 'user_review' : userReviews_json, 'customer' : customer_json})

def reviewSuccess (response):
    
    session_json = response.session.get("session")
    movie = json.loads(session_json).get("movie")
    userReviews_json = response.session.get("user_review")
    customer_json = response.session.get("customer")
    
    return render(response, 'CinemaCustomerPages/movie_detail.html', {'movie': movie,'session_json': session_json, 'user_review' : userReviews_json, 'customer' : customer_json})


def addtoCart(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        data = json_data.get("data")
        request.session["cart"] = data
        return HttpResponse("OK")
    
def ticketcart(request):
    data = request.session.get("cart")
    tickets = json.loads(json.dumps(data)) if data else [] 
    
    customer = Customer.objects.get(user = request.user)
    customer_points = customer.loyalty_points
    
    if not tickets:
        messages.error(request, "Your cart is empty")
        return redirect("/")
    
    for seat in tickets['seats']:
        seat['foodcomboes'] = {}
    
    foodcombo = FoodAndDrinks.objects.all().values()
    foodcombo_json = json.dumps(list(foodcombo))
    context = {"tickets": json.dumps(tickets), "foodcombo": foodcombo_json, "loyalty_points": customer_points}
    return render(request, "CinemaCustomerPages/ticketcart.html", context)

@csrf_exempt
def updateCart(request):
    if request.method == "POST":
        data = request.POST.get("data")
        request.session["cart"] = data
        request.session.save()
        return redirect("/ticketcart")
    
def checkout(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        data = json_data.get("data")
        request.session["checkout"] = data
        return HttpResponse("OK")
        
def checkOutCart(request):
    
    data = request.session.get("checkout")
    data_json = json.loads(json.dumps(data)) if data else []
    
    room_id = data_json["tickets"]["session"]["room"]["room_id"]
    
    customer = Customer.objects.get(user = request.user)
    customer.set_points(data_json["loyalty_points"])
      
    for seat in data_json["tickets"]["seats"]:
        print(int(seat["seat"])+1)
        seat_obj = Seat.objects.get(seat_number=  int(seat["seat"])+1, room_id = room_id)
       
        foodcombo_details = seat.get("foodcomboes").values()
        ticketType = seat.get("ticketType")
        ticket_price = seat.get("price")
        
        combo = None
        for value in foodcombo_details:
            combo = FoodAndDrinks.objects.get(combo_name = value.get("combo_name"),
                                          combo_price = value.get("combo_price"))
        
        
        if seat_obj.is_available == False:
            messages.error(request, "Seat " + str(seat_obj.seat_row) + str(seat_obj.seat_number) + " is not available")
            return redirect("/ticketcart")
        else :
            seat_obj.is_available = False
            seat_obj.save()
            
            if not Ticket.objects.filter(seat_id = seat_obj).count() > 0:
                movie_session = MovieSession.objects.get(session_id = data_json["tickets"]["session"]["session_id"])
                ticket = Ticket.objects.create(movie_session = movie_session, seat_id = seat_obj, 
                                               combo_id = combo, user_id = request.user, ticket_type = ticketType, 
                                               cost = float(ticket_price), is_paid = True)
                ticket.save()
                
                
                customer.add_points(5)
    
    del request.session["cart"]
    request.session.modified = True
    
    return redirect("/TicketsPurse")



def TicketsPurse(request):
    
    user_tickets = Ticket.objects.filter(user_id = request.user).select_related("movie_session", "seat_id")
    
    tickets_dict = {}
    for index , ticket in enumerate(user_tickets):
        ticket.purchased_date = ticket.purchased_date.strftime("%Y-%m-%d %H:%M:%S")
        tickets_dict[str(index)] = model_to_dict(ticket)
        tickets_dict[str(index)]["movie_session"] = model_to_dict(ticket.movie_session)
        tickets_dict[str(index)]["movie_session"]["start_time"] = tickets_dict[str(index)]["movie_session"]["start_time"].strftime("%Y-%m-%d %H:%M:%S")
        tickets_dict[str(index)]["movie_session"]["movie_id"] = model_to_dict(ticket.movie_session.movie_id)
        tickets_dict[str(index)]["seat_id"] = model_to_dict(ticket.seat_id)
        
        if ticket.combo_id:
            tickets_dict[str(index)]["combo_id"] = model_to_dict(ticket.combo_id)
        
    
    context = {"tickets": json.dumps(tickets_dict)}
    
    return render(request, "CinemaCustomerPages/myPurchasedTickets.html", context=context)

def test(request):
    return render(request, 'CinemaCustomerPages/test.html')

def mainPageAlter(request):
    return render (request, 'CinemaCustomerPages/homealternative.html')


