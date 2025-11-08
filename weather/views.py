import requests
from django.shortcuts import render, redirect
from .forms import CityForm
from .models import city


def index(request):
    """
    Render the weather index page.
    """

    API_KEY = ""

    new_city = None
    err_msg = ''
    message = ''
    message_class = ''
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            
            # ✅ Correctly formatted URL with f-string and quotes
            url = f"http://api.openweathermap.org/data/2.5/weather?q={new_city}&units=metric&appid={API_KEY}"

            existing_city_count = city.objects.filter(name=new_city).count()
            
            if existing_city_count == 0:
                r = requests.get(url).json()
                if r.get('cod') == 200:
                    form.save()
                else:
                    err_msg = "City doesn’t exist or invalid API key."
            else:
                err_msg = "City already exists in the database!"
        
        if err_msg:
            message = err_msg
            message_class = 'alert-danger'
        else:
            message = 'City added successfully!'
            message_class = 'alert-success'
    
    form = CityForm()
    cities = city.objects.all()
    weather_data = []

    # ✅ Loop to fetch weather data for saved cities
    for citi in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={citi.name}&units=metric&appid={API_KEY}"
        r = requests.get(url).json()

        # Protect against missing keys if the API fails
        if r.get('cod') == 200:
            city_weather = {
                'city': citi.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
            weather_data.append(city_weather)
        else:
            print(f"⚠️ Failed to get data for {citi.name}: {r}")

    context = {
        'weather_data': weather_data,
        'form': form,
        'message': message,
        'message_class': message_class
    }

    return render(request, 'weather/weather.html', context)


def about(request):
    return render(request, 'weather/about.html')


def delete_city(request, city_name):
    city.objects.get(name=city_name).delete()
    return redirect('home')


def help(request):
    return render(request, 'weather/help.html')
