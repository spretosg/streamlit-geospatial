def ee_st_authenticate():
    """Add Earth Engine token to Streamlit app.
    With Geemap/Stremlit never use ee.Authenticate() as it will not work.
    """
    import streamlit as st
    import geemap
    import os
    EARTHENGINE_TOKEN = st.secrets["EARTHENGINE_TOKEN"]
    print(st.secrets["EARTHENGINE_TOKEN"])

    
    geemap.ee_initialize(token_name=EARTHENGINE_TOKEN)
    print(f"Earth Engine authenticated successfully: {EARTHENGINE_TOKEN}")

ee_st_authenticate()