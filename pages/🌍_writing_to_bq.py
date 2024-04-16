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

    # Draw a rectangle on the map
    st.subheader('Draw a Rectangle on the Map')
    drawn_shape = st.map()
    drawn_json = drawn_shape.json_data

    # Additional form fields
    additional_info = st.text_input('Additional Information')

    # Button to submit
    if st.button('Submit'):
        # Extract rectangle coordinates
        coordinates = drawn_json['features'][0]['geometry']['coordinates'][0]
        # Convert coordinates to a format usable by Earth Engine
        rect = ee.Geometry.Rectangle(coordinates)
        # Load an Earth Engine image
        image = ee.Image('MODIS/006/MOD09GA/2021_01_01')
        # Clip the image to the drawn rectangle
        clipped_image = image.clip(rect)
        # Display the clipped image
        st.subheader('Clipped Image')
        folium_figure = folium.Figure(width=1000, height=500)
        display_ee_image(clipped_image, folium_figure)
        st.write(folium_figure._repr_html_(), unsafe_allow_html=True)

        # Save data to BigQuery
        # Assuming you have a BigQuery table called 'drawn_rectangles'
        task = ee.batch.Export.table.toBigQuery(
            collection=rect,
            table='pareus.earth_engine.mytable',
            description='put_my_data_in_bigquery',
            append=False)
        task.start()


        if errors == []:
            st.success('Data inserted successfully into BigQuery')
        else:
            st.error(f'Error inserting data into BigQuery: {errors}')

if __name__ == "__main__":
    main()
