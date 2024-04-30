import streamlit as st

st.set_page_config(
    page_title="streamlit-folium documentation: Draw Support",
    page_icon=":pencil:",
    layout="wide",
)

"""
# streamlit-folium: Draw Support

Folium supports some of the [most popular leaflet
plugins](https://python-visualization.github.io/folium/plugins.html). In this example,
we can add the
[`Draw`](https://python-visualization.github.io/folium/plugins.html#folium.plugins.Draw)
plugin to our map, which allows for drawing geometric shapes on the map.

When a shape is drawn on the map, the coordinates that represent that shape are passed
back as a geojson feature via the `all_drawings` and `last_active_drawing` data fields.

Draw something below to see the return value back to Streamlit!
"""
import ee
from google.oauth2 import service_account
from google.cloud import bigquery

from streamlit_folium import st_folium
 # Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
 )
client = bigquery.Client(credentials=credentials)

rectangle = ee.Geometry.Rectangle(-122.09, 37.42, -122.08, 37.43)

# Add the rectangle geometry to a FeatureCollection
rectangle_fc = ee.FeatureCollection(rectangle)

task = ee.batch.Export.table.toBigQuery(
        collection=rectangle_fc,
        table='pareus.earth_engine.mytable',
        description='put_my_data_in_bigquery',
        append=True)
task.start()

with st.echo(code_location="below"):
    import folium
    import streamlit as st
    from folium.plugins import Draw


    m = folium.Map(location=[64, 10], zoom_start=5)
    Draw(
        export=False,
        position="topleft",
        draw_options={
            "polyline": False,
            "poly": False,
            "circle": False,
            "polygon": False,
            "marker": False,
            "circlemarker": False,
            "rectangle": True,
        },
    ).add_to(m)

    #c1, c2 = st.columns(2)
    c1 = st.columns(1)
    c1 = st_folium(m, width=900, height=500)

