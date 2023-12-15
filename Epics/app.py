from flask import Flask, render_template, request
import folium
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map', methods=['POST'])
def map():
    location = request.form['location']

   
    geolocator = Nominatim(user_agent="geo_locator")
    location_data = geolocator.geocode(location, exactly_one=True)

    if location_data:
        latitude = location_data.latitude
        longitude = location_data.longitude
        state_code = location_data.raw.get('address', {}).get('state', '')
        country_code = location_data.raw.get('address', {}).get('country_code', '')

       
        my_map = folium.Map(location=[latitude, longitude], zoom_start=12)
        folium.Marker([latitude, longitude], popup=f"Latitude: {latitude}, Longitude: {longitude}, State Code: {state_code}, Country Code: {country_code}").add_to(my_map)

        
        my_map.save('templates/map.html')

        return render_template('map.html')
    else:
        return "Location not found."

if __name__ == '__main__':
    app.run(debug=True)
