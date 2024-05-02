import ee
import streamlit as st
import folium
import random


# Function to display an EE Image on a folium map
def display_ee_image(image, region, vis_params={}):
    map_id_dict = image.getMapId(vis_params)
    folium.Map(location=[0, 0], zoom_start=2).add_ee_layer(
        ee.Image(image), vis_params, 'image', True, 0.6).add_child(
            folium.LayerControl()).add_to(region)

# Streamlit app
def main():
    st.title('dummy data to bq')

    # Create a geometry representing the rectangle
    rectangle = ee.Geometry.Rectangle(-120.09, 37.42, -122.08, 37.43)

    # Add the rectangle geometry to a FeatureCollection
    rectangle_fc = ee.FeatureCollection(rectangle)
    task = ee.batch.Export.table.toBigQuery(
      collection=rectangle_fc,
      table='pareus.earth_engine.mytable',
      description='put_my_data_in_bigquery',
      append=True)
    task.start()

    # Load an Earth Engine image
    image = ee.Image('MODIS/006/MOD09GA/2021_01_01')

    # Display the image on a map
    st.subheader('Map Display')
    folium_figure = folium.Figure(width=1000, height=500)
    display_ee_image(image, folium_figure)
    st.write(folium_figure._repr_html_(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
