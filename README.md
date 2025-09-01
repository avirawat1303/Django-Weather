# Django Weather Forecast App
A clean and simple weather application built with Django that provides real-time weather data for cities worldwide.
It fetches live data from the OpenWeatherMap API and displays it in a user-friendly, responsive interface styled with Bootstrap.

# Features
Global City Search: Instantly find the current weather for any city worldwide.

Detailed Forecast: Get essential data points including temperature (°C), weather conditions (e.g., "Clear Sky," "Light Rain"), humidity, and wind speed.

Dynamic UI: The interface updates instantly with the weather information for the city you searched for.

Responsive Design: A clean layout that works seamlessly on both desktop and mobile devices.

# Project is created with
* [Django 4.2](https://docs.djangoproject.com/en/4.2/)
* [Bootstrap 4](https://getbootstrap.com/)
* [OpenWeatherMap](https://openweathermap.org/)

How to use or install this app on your computer?
### 1. Install the requirement.txt on your computer using pip

```python
pip install -r requirements.txt
```

### 2.  After install all the requirement.txt extract the project and open the project, type this on your terminal 
```python
python manage.py makemigrations
python manage.py migrate
```

### 3. Run the server using 
```python
python manage.py runserver
```

Your django it's live now open your browser and type 127.0.0.1:8000

# Database Configuration
Note: This project is configured to use MySQL by default. If you want to use a different database or connect to your own MySQL instance, you can easily change the database name, host, port, username, and password in the DATABASES section of the settings.py file.

