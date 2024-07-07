from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .utils import make_markers_and_add_to_map
from .models import HhSurvey
from folium.plugins import TagFilterButton
from folium.plugins import Search

import folium
import geopandas
import os 
import numpy as np
import random






class MapView(TemplateView):
    template_name = 'map.html'
    
    def get_context_data(self, **kwargs):
        figure = folium.Figure()
        
        # generate base data
        data = (np.random.normal(size=(100,2)) * np.array([[1, 1]]) + 
                np.array([[48, 5]]))
        
        # make a map
        m = folium.Map(
            location= [27.0149456, 87.1688135],
            zoom_start= 11,
            tiles= 'OpenStreetMap',
            control_scale=True,
            height='90%',
            max_bounds=True 
        )
        
        url = 'mapview/media/mapview/hh_survey_4 July_2024.json'
        gdf = geopandas.read_file("mapview/media/mapview/hh_survey_4 July_2024.json")
        gdf.head()
        
        folium.GeoJson(gdf, 
                       name="Household Heads",
                       zoom_on_click=True,
                       marker=folium.Marker(icon=folium.Icon(icon='star')),
                       tooltip=folium.GeoJsonTooltip(fields=["Name:","House Number","Ward Number"]),
                       popup=folium.GeoJsonPopup(fields=["Name:", "House Number", "Tole", "Ward Number", "Phone Number"]),   
                       smooth_factor=10,          
                       ).add_to(m)
        
        m.add_to(figure)
        
        household = folium.GeoJson(gdf, 
                       name="Household Heads",
                       zoom_on_click=True,
                       marker=folium.Marker(icon=folium.Icon(icon='star')),
                       tooltip=folium.GeoJsonTooltip(fields=["Name:","House Number","Ward Number"]),
                       popup=folium.GeoJsonPopup(fields=["Name:", "House Number", "Tole", "Ward Number", "Phone Number"]),   
                       smooth_factor=10,          
                       ).add_to(m)
        
        m.add_to(figure)
        
        householdsearch= Search(
            layer= household,
            geom_type="Point",
            placeholder="Serach for a household name",
            collapsed=True,
            search_label="Name in Block Letter",            
        ).add_to(m)
        
        # generat the data to segment by (levels of another pandas column in practical usage)
        categories = ['category{}'.format(i+1) for i in range(30)]
        category_column = [random.choice(categories) for i in range(len(data))]
        
        #create map and add the data with additional parameter tags as the segmentation
        for i, latlng in enumerate(data):
            category = category_column[i]
            folium.Marker(
                tuple(latlng),
                tags=[category]
            ).add_to(m)
        
        TagFilterButton(categories).add_to(m)
         
        
        # fetch the objects from database and make markers for them
        # for house in HhSurvey.objects.all():
        #     make_markers_and_add_to_map(m, house)
                    
        # render and send to template
        figure.render()
        return {"map": figure}
    
        folium.LayerControl().add_to(m)


