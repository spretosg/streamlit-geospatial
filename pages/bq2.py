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
#ee.Initialize()
geemap.ee_initialize()
    

rectangle = ee.Geometry.Rectangle(-88.09, 37.42, -122.08, 37.43)

def main():
    st.title('dummy data to bq')

    rectangle = ee.Geometry.Rectangle(-88.09, 37.42, -122.08, 37.43)

    # Add the rectangle geometry to a FeatureCollection
    rectangle_fc = ee.FeatureCollection(rectangle)
    task = ee.batch.Export.table.toBigQuery(
      collection=rectangle_fc,
      table='pareus.earth_engine.mytable',
      description='test_task1',
      append=True)
    task.start()


if __name__ == "__main__":
    main()