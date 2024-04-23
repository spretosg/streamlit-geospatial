import ee
import streamlit as st
import folium
import geemap.foliumap as geemap


@st.cache_data
def ee_authenticate(token_name="EARTHENGINE_TOKEN"):
    geemap.ee_initialize(token_name=token_name)


# Function to display an EE Image on a folium map
def display_ee_image(image, region, vis_params={}):
    map_id_dict = image.getMapId(vis_params)
    folium.Map(location=[0, 0], zoom_start=2).add_ee_layer(
        ee.Image(image), vis_params, 'image', True, 0.6).add_child(
            folium.LayerControl()).add_to(region)

# Streamlit app
def main():
    st.title('Google Earth Engine - bigquery')

    # Draw a rectangle on the map
    st.subheader('Draw a Rectangle on the Map')
    Map = geemap.Map(center=[40, -100], zoom=4)
    image = ee.Image("USGS/SRTMGL1_003")
    # Set visualization parameters.
    vis_params = {
        "min": 0,
        "max": 4000,
        "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
    }

    width = 950
    height = 600

    # Add Earth Engine DEM to map
    Map.addLayer(image, vis_params, "SRTM DEM")

    Map.draw_features

    roi = ee.FeatureCollection(Map.draw_features)
    Map.to_streamlit(width=width, height=height)

if __name__ == "__main__":
    main()
