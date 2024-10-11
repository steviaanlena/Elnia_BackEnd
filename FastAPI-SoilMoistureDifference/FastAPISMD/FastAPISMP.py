# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Predefined today's soil moisture values for each province
soil_moisture_today = {
    "Aceh": 1.14,
    "Bali": 0.45,
    "Banten": 0.13,
    "Bengkulu": 1.06,
    "D.I. Yogyakarta": 0.34,
    "D.K.I. Jakarta": 0.65,
    "Gorontalo": 0.88,
    "Jambi": 1.35,
    "Jawa Barat": 0.83,
    "Jawa Tengah": 0.02,
    "Jawa Timur": 0.09,
    "Kalimantan Barat": 1.43,
    "Kalimantan Selatan": 0.99,
    "Kalimantan Tengah": 1.44,
    "Kalimantan Timur": 1.12,
    "Kalimantan Utara": 1.22,
    "Kepulauan Bangka Belitung": 1.17,
    "Kepulauan Riau": 1.07,
    "Lampung": 0.85,
    "Maluku": 1.10,
    "Maluku Utara": 1.21,
    "Nusa Tenggara Barat": 0.00,
    "Nusa Tenggara Timur": 0.00,
    "Papua": 1.17,
    "Papua Barat": 1.13,
    "Riau": 1.21,
    "Sulawesi Barat": 1.16,
    "Sulawesi Selatan": 0.78,
    "Sulawesi Tengah": 1.06,
    "Sulawesi Tenggara": 1.05,
    "Sumatera Barat": 1.29,
    "Sumatera Selatan": 0.86,
    "Sumatera Utara": 0.93
}

# Define the input data structure using Pydantic
class ProvinceInput(BaseModel):
    province: str

# Define the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Soil Moisture API"}

# Define the prediction endpoint
@app.post('/soil_moisture')
def get_soil_moisture(input_data: ProvinceInput):
    try:
        province = input_data.province

        # Check if the province exists in the dataset
        if province in soil_moisture_today:
            # Get the soil moisture for today
            soil_moisture_value = soil_moisture_today[province]
            return {'province': province, 'soil_moisture_today': soil_moisture_value}
        else:
            raise HTTPException(status_code=404, detail="Province not found")

    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(error_msg)
        raise HTTPException(status_code=500, detail="Internal server error during request.")
