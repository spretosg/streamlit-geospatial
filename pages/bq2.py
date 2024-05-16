import streamlit as st
import folium
import streamlit as st
from folium.plugins import Draw
import ee
from google.oauth2 import service_account
from google.cloud import bigquery
from streamlit_folium import st_folium
import geemap.foliumap as geemap

    # Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
    )
geemap.ee_initialize()
""" @st.cache_data
def ee_authenticate(token_name="EARTHENGINE_TOKEN"):
    geemap.ee_initialize(token_name=token_name) """

    



def main():
    st.title('dummy data to bq')

    rectangle = ee.Geometry.Rectangle(-109.09, 66.42, -122.08, 37.43)

    # Add the rectangle geometry to a FeatureCollection
    rectangle_fc = ee.FeatureCollection(rectangle)
    task = ee.batch.Export.table.toBigQuery(
      collection=rectangle_fc,
      table='pareus.earth_engine.mytable',
      description='streamlit_gee_bq_task',
      append=True)
    task.start()


if __name__ == "__main__":
    main()