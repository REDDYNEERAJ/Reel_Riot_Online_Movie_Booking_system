from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from .models import Movie
import string
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




@login_required
def home_view(request):
    from .models import Location, Movie

    locations = Location.objects.all()
    selected_location_id = request.GET.get('location', None)
    movies = None
    selected_location = None   # ✅ add this

    if selected_location_id:
        selected_location = Location.objects.get(id=selected_location_id)   # ✅ fetch object
        movies = Movie.objects.filter(locations__id=selected_location_id)

    # Precompute a selected flag
    locations_with_flag = []
    for loc in locations:
        locations_with_flag.append({
            'id': loc.id,
            'name': loc.name,
            'selected': str(loc.id) == str(selected_location_id)  # True if this location is selected
        })

    return render(request, 'home.html', {
        'locations': locations_with_flag,
        'movies': movies,
        'selected_location': selected_location   # ✅ pass object
    })



from django.shortcuts import render, get_object_or_404
from .models import Movie, Theatre, Show, Location

def movie_detail_view(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    location_id = request.GET.get('location', None)

    shows = Show.objects.filter(movie=movie)
    if location_id:
        shows = shows.filter(theatre__locations__id=location_id)

    # Group shows by theatre
    theatre_shows = {}
    for show in shows:
        if show.theatre not in theatre_shows:
            theatre_shows[show.theatre] = []
        theatre_shows[show.theatre].append(show)

    return render(request, 'movie_detail.html', {
        'movie': movie,
        'theatre_shows': theatre_shows,
        'location_id': location_id
    })

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # redirect to login page after logout



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Show, Theatre, Booking

@login_required
def seat_selection_view(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    theatre = show.theatre

    # Generate seat layout from theatre settings
    seat_layout = []
    for row in range(theatre.total_rows):
        row_label = chr(65 + row)  # A, B, C ...
        row_seats = [f"{row_label}{col+1}" for col in range(theatre.seats_per_row)]
        seat_layout.append(row_seats)

    # Already booked seats
    booked_seats = Booking.objects.filter(show=show).values_list("seat_number", flat=True)
    booked_seats = list(booked_seats)

    if request.method == "POST":
        selected_seats = request.POST.getlist("seats")
        if not selected_seats:
            return render(request, "seat_selection.html", {
                "theatre": theatre,
                "show": show,
                "seat_layout": seat_layout,
                "booked_seats": booked_seats,
                "error": "Please select at least one seat."
            })

        # Save each booking
        for seat in selected_seats:
            Booking.objects.create(
                user=request.user,
                show=show,
                seat_number=seat
            )

        # 👉 Store only the seats just booked in session
        request.session['just_booked_seats'] = selected_seats  

        # Redirect to confirmation page
        return redirect("booking_confirmation", show_id=show.id)

    return render(request, "seat_selection.html", {
        "theatre": theatre,
        "show": show,
        "seat_layout": seat_layout,
        "booked_seats": booked_seats
    })


@login_required
def booking_confirmation_view(request, show_id):
    show = get_object_or_404(Show, id=show_id)

    # 👉 Only show seats from the last booking
    seats = request.session.pop('just_booked_seats', [])

    seat_count = len(seats)
    price_per_seat = 250
    subtotal = seat_count * price_per_seat
    tax = round(subtotal * 0.05, 2)
    total = subtotal + tax

    return render(request, "booking_confirmation.html", {
        "show": show,
        "seats": seats,
        "subtotal": subtotal,
        "tax": tax,
        "total": total,
    })





@login_required
def profile_view(request):
    bookings = Booking.objects.filter(user=request.user).select_related("show", "show__movie", "show__theatre")
    return render(request, "profile.html", {"bookings": bookings})