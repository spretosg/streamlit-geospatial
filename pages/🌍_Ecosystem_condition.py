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
    min_x, max_x = -180, 180
    min_y, max_y = -90, 90

    # Randomly generate coordinates for the rectangle
    x1 = random.uniform(min_x, max_x)
    x2 = random.uniform(min_x, max_x)
    y1 = random.uniform(min_y, max_y)
    y2 = random.uniform(min_y, max_y)

    # Create a geometry representing the rectangle
    rectangle = ee.Geometry.Rectangle([x1, y1, x2, y2])

    # Add the rectangle geometry to a FeatureCollection
    rectangle_fc = ee.FeatureCollection(rectangle)
      task = ee.batch.Export.table.toBigQuery(
      collection=rectangle_fc,
      table='pareus.earth_engine.mytable',
      description='put_my_data_in_bigquery',
      append=False)
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
