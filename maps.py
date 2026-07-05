import requests

def get_nearby_shelters(latitude, longitude):
    """
    Placeholder function for nearby shelters.

    In a production version, this function would call the
    Google Maps Places API and return nearby shelters.
    """

    shelters = [
        {
            "name": "City Community Shelter",
            "address": "Main Road",
            "distance": "1.2 km"
        },
        {
            "name": "Government Relief Center",
            "address": "Station Road",
            "distance": "2.5 km"
        },
        {
            "name": "District Emergency Shelter",
            "address": "Central Park",
            "distance": "3.1 km"
        }
    ]

    return shelters