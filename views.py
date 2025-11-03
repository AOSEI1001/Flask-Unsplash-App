from flask import Blueprint, render_template
from flask import request
import requests
import os
#from dotenv import load_dotenv
#load_dotenv()

# Create a blueprint
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/', methods=['GET', 'POST'])
def index():

    print(os.environ.get("WEATHER_KEY"))
    api_key = os.environ.get('WEATHER_KEY')
    api_response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=14.32&lon=10.98&appid='+ api_key)

    if api_response.status_code == 200:
        data = api_response.json()
        
        icon_code = data['weather'][0]['icon']
        description = data['weather'][0]['description']
        main = data['weather'][0]['main']
        
        image_url = f"http://openweathermap.org/img/wn/" + icon_code + "@2x.png"
        
        
    else:
        icon_code = None
        image_url = None
        main = None
        description = None

    return render_template('index.html', image_url=image_url, main=main, description=description)



@main_blueprint.route('/conditional')
def conditional():
    user = 'admin'
    return render_template('conditional.html', user=user)


@main_blueprint.route('/loop')
def loop():
    users = ['admin', 'user', 'guest']
    return render_template('loop.html', items=users)


@main_blueprint.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f'Logged in as {username}'
    
    return render_template('form.html')