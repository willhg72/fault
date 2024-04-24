import re
import os
from  fastapi import status, HTTPException
from typing import List
from geopy.distance import geodesic
import requests
from settings import API_URL
  

def calculate_distances(coordinates):
    '''
    This function receive a specific coordinate(lat, long) and calculate the distance of 10 more close fails from this point , then return a list sorted by distancia_promedio ASC
    '''
    total_info_fails_row_data = get_fails_row_data(API_URL)
    cleaned_info_fails_row_data = clean_fails_row_data(
        total_info_fails_row_data)
   
    return calculated_and_sorted_data(cleaned_info_fails_row_data, coordinates)



def get_fails_row_data(data_url) -> list:
    '''
    This function receive the url and gets the data from the API.
    '''
    try:
        
        total_info_fails_row_data = requests.get(data_url)
        total_info_fails_row_data.raise_for_status()

    except requests.exceptions.ConnectionError:
        print("A connection error occurred. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        
    return total_info_fails_row_data


def clean_fails_row_data(total_info_fails_row_data) -> list:
    '''
    This function receive the row data and clean it.
    '''
    cleaned_info_fails_row_data: dict = {}
    info_fails = total_info_fails_row_data.json().get("features")
    for fail in info_fails:
        if "falla" in fail["attributes"]["Tipo"].lower() and fail["attributes"]["NombreFalla"] != None:
            cleaned_info_fails_row_data[(fail["attributes"]["OBJECTID"])] = {
                "Tipo": fail["attributes"]["Tipo"],
                "NombreFalla": fail["attributes"]["NombreFalla"],
                "coordenadaInicioFalla": fail["geometry"]["paths"][0][0],
                "coordenadaFinFalla": fail["geometry"]["paths"][0][-1]
            }
    return cleaned_info_fails_row_data


def calculated_and_sorted_data(cleaned_info_fails_row_data: list[dict], coordinates: List[float]) -> dict:
    '''
    This function receive the cleaned data and an specific coordinates and calculate the distance each 10 more close fails , then return a list of 10 more close fails sorted ASC by distancia_promedio.
    '''
    
    pattern = r'/^[-]?\d+[\.]?\d*, [-]?\d+[\.]?\d*$/'
    if re.match(pattern, str(coordinates[0])) and re.match(pattern, str(coordinates[1])):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid coordinates, must be in the [-90; 90] range and Longitude must be in the [-180; 180] range")
    if  coordinates[0] <= -90 or coordinates[0] >= 90:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid latitude")
    if coordinates[1] <= -180 or coordinates[1] >= 180:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid longitude")
    
    for key, value in cleaned_info_fails_row_data.items():
        cleaned_info_fails_row_data[key]["distancia_incio_falla"] = geodesic(
            (coordinates[0], coordinates[1]),
            (value["coordenadaInicioFalla"][1], value["coordenadaInicioFalla"][0]),
        ).km
        cleaned_info_fails_row_data[key]["distancia_fin_falla"] = geodesic(
            (coordinates[0], coordinates[1]),
            (value["coordenadaFinFalla"][1], value["coordenadaFinFalla"][0]),
        ).km
        cleaned_info_fails_row_data[key]["distancia_promedio"] = (
            (cleaned_info_fails_row_data[key]["distancia_incio_falla"] +
              cleaned_info_fails_row_data[key]["distancia_fin_falla"])/2
        )
    sorted_data = sorted(
        cleaned_info_fails_row_data.items(), key=lambda x: x[1]["distancia_promedio"]
    
    )
    final_data: dict = {}
    sorted_data = dict(sorted_data[:20])
    sorted_data = dict(sorted(sorted_data.items(), key=lambda x: x[1]["distancia_promedio"], reverse=True))
    for k,v in sorted_data.items():
        final_data[v["NombreFalla"]] = round(v["distancia_promedio"], 2)
    final_data = sorted(final_data.items(), key=lambda x: x[1])[:10]
    return dict(final_data)