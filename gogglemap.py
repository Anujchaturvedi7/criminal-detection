from flask import Flask
import googlemaps

gmaps = googlemaps.Client(key='YOUR_API_KEY')

def get_location(address):
    geocode_result = gmaps.geocode(address)
    return geocode_result