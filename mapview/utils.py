import folium

def make_markers_and_add_to_map(m, house):
    folium.Marker(
        location= house.geography_location,
        popup= house.nepaliname,
        tooltip= house.englishname,
        icon= folium.Icon(icon='fa-home', prefix='fa')
    ).add_to(m)