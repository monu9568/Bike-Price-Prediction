

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("bike_data_cleaned.csv")

data = df[['model_year', 'kms_driven_num', 'owner_clean', 'location_clean',
           'mileage_num', 'power_num', 'brand', 'price_num']].copy()
data = data.dropna()
data_filtered = data[(data['price_num'] >= 10000) & (data['price_num'] <= 800000)]


le_owner = LabelEncoder()
le_brand = LabelEncoder()
data_filtered['owner_encoded'] = le_owner.fit_transform(data_filtered['owner_clean'])
data_filtered['brand_encoded'] = le_brand.fit_transform(data_filtered['brand'])


X = data_filtered[['model_year', 'kms_driven_num', 'power_num', 'mileage_num', 'owner_encoded', 'brand_encoded']]
y = np.log1p(data_filtered['price_num'])  


model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X, y)


st.title("Bike Price Prediction Dashboard 🏍️")


model_year = st.number_input("Model Year", min_value=int(data['model_year'].min()), max_value=int(data['model_year'].max()), value=2018)
kms_driven = st.number_input("Kilometers Driven", min_value=0, max_value=int(data['kms_driven_num'].max()), value=10000)
power = st.number_input("Power (bhp)", min_value=float(data['power_num'].min()), max_value=float(data['power_num'].max()), value=20.0)
mileage = st.number_input("Mileage (kmpl)", min_value=float(data['mileage_num'].min()), max_value=float(data['mileage_num'].max()), value=40.0)
owner = st.selectbox("Owner Type", options=data['owner_clean'].unique())
brand = st.selectbox("Brand", options=data['brand'].unique())


owner_encoded = le_owner.transform([owner])[0]
brand_encoded = le_brand.transform([brand])[0]


input_data = np.array([[model_year, kms_driven, power, mileage, owner_encoded, brand_encoded]])


pred_log = model.predict(input_data)
pred_price = np.expm1(pred_log)[0]

st.success(f"💰 Predicted Bike Price: ₹{pred_price:,.0f}")
