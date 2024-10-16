from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Monthly average temperatures for each province
province_temperatures = {
    "Aceh": [17.56, 17.63, 17.93, 17.48, 17.31, 17.52, 17.98],
    "Bali": [24.21, 24.69, 25.05, 24.65, 24.35, 24.61, 25.21],
    "Banten": [25.18, 25.01, 25.78, 25.23, 25.34, 25.65, 26.3],
    "Bengkulu": [23.47, 24.4, 24.38, 24.26, 24.24, 24.67, 24.83],
    "D.I. Yogyakarta": [26.09, 25.63, 25.68, 25.5, 25.33, 25.66, 25.95],
    "D.K.I. Jakarta": [25.78, 25.74, 26.23, 25.75, 25.81, 26.02, 26.55],
    "Gorontalo": [26.96, 27.35, 27.84, 27.08, 26.65, 26.97, 27.47],
    "Jambi": [24.22, 24.26, 24.37, 23.64, 23.9, 24.34, 24.79],
    "Jawa Barat": [20.96, 19.99, 19.7, 19.58, 19.54, 19.54, 19.81],
    "Jawa Tengah": [25.92, 24.85, 24.74, 24.65, 24.52, 24.57, 25.14],
    "Jawa Timur": [27.24, 26.07, 26.48, 25.31, 25.33, 25.37, 25.98],
    "Kalimantan Barat": [24.65, 24.8, 24.91, 24.59, 24.4, 24.63, 24.85],
    "Kalimantan Selatan": [25.12, 23.94, 24.58, 24.03, 23.72, 23.95, 24.6],
    "Kalimantan Tengah": [24.84, 24.77, 25.2, 24.73, 24.46, 24.72, 24.92],
    "Kalimantan Timur": [25.27, 25.02, 25.65, 24.87, 24.58, 25.03, 25.59],
    "Kalimantan Utara": [23.19, 22.91, 22.79, 22.25, 22.01, 22.33, 22.73],
    "Kepulauan Bangka Belitung": [26.14, 25.98, 26.63, 25.87, 26.03, 26.61, 27.19],
    "Kepulauan Riau": [26.06, 26.41, 26.73, 25.77, 25.93, 26.78, 27.69],
    "Lampung": [25.03, 24.57, 24.97, 24.42, 24.67, 25.01, 25.3],
    "Maluku": [23.18, 23.42, 23.79, 23.55, 23.33, 23.27, 23.62],
    "Maluku Utara": [26.42, 26.18, 26.54, 26.03, 25.78, 26.16, 26.3],
    "Nusa Tenggara Barat": [25.94, 25.56, 25.15, 24.68, 24.44, 24.79, 25.33],
    "Nusa Tenggara Timur": [28.23, 26.77, 26.45, 25.83, 25.58, 25.65, 26.27],
    "Papua": [21.56, 22.15, 21.91, 21.11, 21.14, 21.3, 21.18],
    "Papua Barat": [23.32, 23.57, 23.65, 22.78, 22.5, 22.64, 22.73],
    "Riau": [24.12, 24.12, 24.01, 23.22, 23.35, 24.1, 24.53],
    "Sulawesi Barat": [18.49, 17.06, 17.2, 16.81, 16.53, 16.95, 17.36],
    "Sulawesi Selatan": [27.03, 26.4, 26.57, 26.0, 25.98, 25.84, 26.23],
    "Sulawesi Tengah": [18.48, 16.59, 16.87, 16.32, 15.98, 16.21, 16.48],
    "Sulawesi Tenggara": [27.24, 27.25, 27.82, 27.13, 26.98, 26.6, 27.21],
    "Sulawesi Utara": [24.66, 24.48, 25.06, 24.25, 23.76, 24.25, 24.42],
    "Sumatera Barat": [22.12, 22.76, 22.54, 22.21, 22.32, 22.79, 23.04],
    "Sumatera Selatan": [24.46, 24.22, 24.33, 23.72, 23.92, 24.3, 24.73],
    "Sumatera Utara": [15.12, 15.54, 16.14, 15.7, 15.67, 15.95, 16.33]
}

# Define the input data structure using Pydantic
class ProvinceInput(BaseModel):
    province: str

# Define the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Province Monthly Average Temperatures API"}

# Define the endpoint to fetch temperature data
@app.post('/province_temperatures')
def get_province_temperatures(input_data: ProvinceInput):
    try:
        province = input_data.province

        # Check if the province exists in the dataset
        if province in province_temperatures:
            # Get the monthly average temperatures
            temperatures = province_temperatures[province]
            return {'province': province, 'monthly_avg_temperatures': temperatures}
        else:
            raise HTTPException(status_code=404, detail="Province not found")

    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(error_msg)
        raise HTTPException(status_code=500, detail="Internal server error during request.")
