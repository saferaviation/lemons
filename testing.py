from geopy.distance import geodesic
import xml.etree.ElementTree as ET


target_coords = (40.7128, -74.0060)

other_coords = [
    (41.8781, -87.6298),  # Chicago
    (34.0522, -118.2437),  # Los Angeles
    (51.5074, -0.1278),    # London
    # ... add more coordinates
]

closest_distance = float('inf')
closest_coords = None

for lat, lon in other_coords:
    distance = geodesic(target_coords, (lat, lon)).kilometers
    if distance < closest_distance:
        closest_distance = distance
        closest_coords = (lat, lon)

print("Closest Coordinates:", closest_coords)
print("Distance:", closest_distance, "km")


kml_file = "NHMS.kml"
tree = ET.parse(kml_file)
root = tree.getroot()

kml_namespace = "{http://www.opengis.net/kml/2.2}"

coordinates = root.find(".//{0}LineString/{0}coordinates".format(kml_namespace))

coordinate_strings = coordinates.text.strip().split()

points = []
for coord_str in coordinate_strings:
    lon, lat, _ = coord_str.split(',')
    points.append((float(lat), float(lon)))

print(points)

import folium

# Choose a center point for your map
center_lat, center_lon = 40.7128, -74.0060

# Create a folium map centered on the chosen point
m = folium.Map(location=[center_lat, center_lon], zoom_start=10)

# Latitude and longitude pairs for pins
pin_coords = [
    (40.7128, -74.0060),  # New York
    (34.0522, -118.2437),  # Los Angeles
    (51.5074, -0.1278),    # London
    # ... add more coordinates
]

# Add pins to the map
for lat, lon in pin_coords:
    folium.Marker([lat, lon], popup=f"Lat: {lat}, Lon: {lon}").add_to(m)

# Save the map as an HTML file
m.save("map_with_pins.html")

from PyQt5.QtWidgets import QApplication, QMainWindow, QWebEngineView
import sys

app = QApplication(sys.argv)
window = QMainWindow()
webview = QWebEngineView()

webview.setHtml(open("map_with_pins.html").read())
window.setCentralWidget(webview)
window.show()

sys.exit(app.exec_())

