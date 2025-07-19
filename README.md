

# 🌱 AI-Powered MRV System for Carbon Offsets

This project implements an AI-powered Monitoring, Reporting, and Verification (MRV) system designed to estimate carbon offsets and biodiversity scores for forest areas based on their geographical location and size. It leverages geospatial data, machine learning, and a Streamlit interface for easy interaction.

## ✨ Features

* **Geospatial Forest Type Identification:** Pinpoints the forest type at a given latitude and longitude using a GeoJSON dataset.
* **Carbon Stock Estimation:** Predicts carbon stock per hectare for identified forest types using a trained Random Forest Regressor model.
* **CO₂ Equivalent Calculation:** Converts estimated carbon stock into CO₂ equivalent.
* **Biodiversity Scoring:** Provides a simple rule-based biodiversity score based on the identified forest type.
* **User-Friendly Interface:** Built with Streamlit for intuitive input and display of results.
* **Data Preprocessing:** Includes steps for merging TIFF files (for land cover data), converting raster data to GeoJSON, and preparing carbon stock lookup data.

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need Python 3.7+ installed. The project also relies on several Python libraries.

```bash
pip install streamlit geopandas pandas shapely scikit-learn rasterio
```

### Data Files

This project requires the following data files:

* `forest_types.geojson`: A GeoJSON file containing polygons of different forest types with a `class_name` attribute. This file is generated from `.tif` land cover data within the Colab notebook.
* `forest_carbon_stock_lookup.csv`: A CSV file containing a lookup table of `forest_type` and `carbon_stock_t_ha` values.




## 💻 Project Structure

* `app.py`: The main Streamlit application script. This script contains the UI, the logic for spatial lookup, carbon estimation, and biodiversity scoring.
* `forest_types.geojson`: (Generated) Geospatial data representing different forest types.
* `forest_carbon_stock_lookup.csv`: (Provided/Uploaded) Lookup table for carbon stock values per forest type.

## 🧠 Model Details

The carbon stock estimation uses a `RandomForestRegressor` from `scikit-learn`.
* **Features (X):** `type_encoded` (numerical representation of forest type).
* **Labels (y):** `carbon_stock_t_ha` (carbon stock in tonnes per hectare).
* **Hyperparameters:** `n_estimators=100`, `random_state=42`.

The model learns the relationship between encoded forest types and their carbon stock, allowing for predictions even if a direct, exact match isn't found in the lookup table, enhancing flexibility and generalization.

## 📊 Biodiversity Scoring(optional)
A simple rule-based system is implemented to provide a biodiversity score:
* "Evergreen" forests: Score 9/10
* "Moist Deciduous" forests: Score 7/10
* "Thorn" forests: Score 4/10
* Other types: Default score 5/10

## 🤝 Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## 📄 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

## 🙏 Acknowledgments

* Built for Hackathon — AI for Climate MRV.
* Thanks to the developers of Streamlit, GeoPandas, Pandas, Shapely, scikit-learn, and Rasterio.
"""


### Google Colab Notebook (for clean code and data preprocessing)
https://colab.research.google.com/drive/1fL5QnGYbDmBq2hhbfCn9XjgfyJgM6NlZ?usp=sharing
