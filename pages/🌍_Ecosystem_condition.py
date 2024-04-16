import ee
import streamlit as st
import folium


# Function to display an EE Image on a folium map
def display_ee_image(image, region, vis_params={}):
    map_id_dict = image.getMapId(vis_params)
    folium.Map(location=[0, 0], zoom_start=2).add_ee_layer(
        ee.Image(image), vis_params, 'image', True, 0.6).add_child(
            folium.LayerControl()).add_to(region)

# Streamlit app
def main():
    st.title('Google Earth Engine App with Streamlit')

    # Define a region of interest (for demonstration, using a bounding box)
    bbox = ee.Geometry.BBox(-180, -90, 180, 90)

    # Load an Earth Engine image
    image = ee.Image('MODIS/006/MOD09GA/2021_01_01')

    # Display the image on a map
    st.subheader('Map Display')
    folium_figure = folium.Figure(width=1000, height=500)
    display_ee_image(image, folium_figure)
    st.write(folium_figure._repr_html_(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
