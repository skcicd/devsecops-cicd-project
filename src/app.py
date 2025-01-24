from flask import Flask, render_template, request, send_from_directory
import os, requests 

app = Flask(__name__)

# The code below lets the Flask server respond to browser requests for a favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')


API_KEY = 'put_your_key_here' 

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'City not found'}

    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    # get host and port from environment variables
    host = os.getenv("FLASK_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_PORT", 5000))
    app.run(host=host, port=port)
