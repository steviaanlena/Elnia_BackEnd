from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# El Nino probabilities for each province (multiplied by 100)
el_nino_probabilities = {
    "Aceh": 99.99,
    "Bali": 99.94,
    "Banten": 99.76,
    "Bengkulu": 99.59,
    "D.I. Yogyakarta": 98.77,
    "D.K.I. Jakarta": 99.83,
    "Gorontalo": 99.08,
    "Jambi": 99.81,
    "Jawa Barat": 98.67,
    "Jawa Tengah": 99.90,
    "Jawa Timur": 99.91,
    "Kalimantan Barat": 99.10,
    "Kalimantan Selatan": 99.99,
    "Kalimantan Tengah": 99.97,
    "Kalimantan Timur": 99.95,
    "Kalimantan Utara": 99.54,
    "Kepulauan Bangka Belitung": 99.99,
    "Kepulauan Riau": 99.99,
    "Lampung": 99.97,
    "Maluku": 99.99,
    "Maluku Utara": 99.98,
    "Nusa Tenggara Barat": 98.81,
    "Nusa Tenggara Timur": 93.69,
    "Papua": 99.75,
    "Papua Barat": 99.74,
    "Riau": 99.99,
    "Sulawesi Barat": 99.83,
    "Sulawesi Selatan": 99.82,
    "Sulawesi Tengah": 99.86,
    "Sulawesi Tenggara": 99.06,
    "Sulawesi Utara": 99.69,
    "Sumatera Barat": 99.56,
    "Sumatera Selatan": 99.74,
    "Sumatera Utara": 99.99
}

# Define the input data structure using Pydantic
class ProvinceInput(BaseModel):
    province: str

# Define the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the El Nino Probability API"}

# Define the prediction endpoint
@app.post('/el_nino_probability')
def get_el_nino_probability(input_data: ProvinceInput):
    try:
        province = input_data.province

        # Check if the province exists in the dataset
        if province in el_nino_probabilities:
            # Get the El Nino probability
            el_nino_prob_value = round(el_nino_probabilities[province], 2)  # Round to one decimal place
            return {'province': province, 'el_nino_probability': el_nino_prob_value}
        else:
            raise HTTPException(status_code=404, detail="Province not found")

    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(error_msg)
        raise HTTPException(status_code=500, detail="Internal server error during request.")
