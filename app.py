
import streamlit as st
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import difflib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

@st.cache_data
def load_data():
    forest_gdf = gpd.read_file("forest_types.geojson")
    carbon_df = pd.read_csv("forest_carbon_stock_lookup.csv")
    return forest_gdf, carbon_df

forest_gdf, carbon_df = load_data()

le = LabelEncoder()
carbon_df['type_encoded'] = le.fit_transform(carbon_df['forest_type'])
X = carbon_df[['type_encoded']]
y = carbon_df['carbon_stock_t_ha']
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

st.title("🌱 AI-Powered MRV System for Carbon Offsets")

lat = st.number_input("Enter Latitude", value=21.1458)
lon = st.number_input("Enter Longitude", value=79.0882)
area_ha = st.number_input("Area (in hectares)", value=10.0)

if st.button("Estimate Carbon Offset"):
    point = Point(lon, lat)
    match = forest_gdf[forest_gdf.contains(point)]

    if not match.empty:
        forest_type_geo = match.iloc[0]['class_name']
        st.success(f"🌳 Forest Type: {forest_type_geo}")

        all_types = carbon_df['forest_type'].tolist()
        best_match = difflib.get_close_matches(forest_type_geo, all_types, n=1)

        if best_match:
            matched_type = best_match[0]
            type_encoded = le.transform([matched_type])[0]
            carbon_per_ha = model.predict([[type_encoded]])[0]

            total_carbon = area_ha * carbon_per_ha
            co2_equivalent = total_carbon * 3.67

            st.metric("Carbon Stock (tC/ha)", f"{carbon_per_ha:.2f}")
            st.metric("Total Carbon Stock (tC)", f"{total_carbon:.2f}")
            st.metric("CO₂ Equivalent (tCO₂)", f"{co2_equivalent:.2f}")

            score = 5
            if "Evergreen" in forest_type_geo:
                score = 9
            elif "Moist Deciduous" in forest_type_geo:
                score = 7
            elif "Thorn" in forest_type_geo:
                score = 4
            st.metric("Biodiversity Score (/10)", score)

        else:
            st.error("No close match found in carbon stock table.")
    else:
        st.error("No forest found at this location.")

st.caption("Built for Hackathon — AI for Climate MRV")
