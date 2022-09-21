from pprint import pprint
from urllib import response
from venv import create
from numpy import place
from geopy.geocoders import GoogleV3
import googlemaps
from google_images_search import GoogleImagesSearch
from asyncore import read
from notion_upload import createPage
import tokenFile 


token = tokenFile.token1
databaseId = tokenFile.dbID
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

API = tokenFile.API

map_client = googlemaps.Client(API)

def get_place_details(location_name):
    response = map_client.places(query=location_name)
    results = response.get('results')[0]
    my_place_id = results['place_id']

    # define the fields you would liked return. Formatted as a list.
    my_fields = ['name','formatted_address','url','type']

    # make a request for the details.
    places_details  = map_client.place(place_id= my_place_id , fields= my_fields)
    name = places_details['result']['name']
    formatted_address = places_details['result']['formatted_address']
    url = places_details['result']['url']
    type = str(places_details['result']['types'][0]).title().replace('_',' ')
    try :
        createPage(databaseId,headers, name, formatted_address, type, url)
        print(str(name) + " has been added to your database.")
    except Exception as e:
        print(e)

def main():
    location_entered = input("Please enter the name of the place you want to add: ")
    get_place_details(location_entered)

if __name__ == "__main__":
    main()