from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# La Niña probabilities for each province (multiplied by 100)
la_nina_probabilities = {
    "Aceh": 0.01,
    "Bali": 0.06,
    "Banten": 0.24,
    "Bengkulu": 0.41,
    "D.I. Yogyakarta": 1.23,
    "D.K.I. Jakarta": 0.17,
    "Gorontalo": 0.92,
    "Jambi": 0.19,
    "Jawa Barat": 1.33,
    "Jawa Tengah": 0.10,
    "Jawa Timur": 0.09,
    "Kalimantan Barat": 0.90,
    "Kalimantan Selatan": 0.01,
    "Kalimantan Tengah": 0.03,
    "Kalimantan Timur": 0.05,
    "Kalimantan Utara": 0.46,
    "Kepulauan Bangka Belitung": 0.01,
    "Kepulauan Riau": 0.01,
    "Lampung": 0.03,
    "Maluku": 0.01,
    "Maluku Utara": 0.02,
    "Nusa Tenggara Barat": 1.19,
    "Nusa Tenggara Timur": 6.31,
    "Papua": 0.25,
    "Papua Barat": 0.26,
    "Riau": 0.01,
    "Sulawesi Barat": 0.17,
    "Sulawesi Selatan": 0.18,
    "Sulawesi Tengah": 0.14,
    "Sulawesi Tenggara": 0.94,
    "Sulawesi Utara": 0.31,
    "Sumatera Barat": 0.44,
    "Sumatera Selatan": 0.26,
    "Sumatera Utara": 0.01
}

# Define the input data structure using Pydantic
class ProvinceInput(BaseModel):
    province: str

# Define the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the La Niña Probability API"}

# Define the prediction endpoint
@app.post('/la_nina_probability')
def get_la_nina_probability(input_data: ProvinceInput):
    try:
        province = input_data.province

        # Check if the province exists in the dataset
        if province in la_nina_probabilities:
            # Get the La Niña probability
            la_nina_prob_value = round(la_nina_probabilities[province], 1)  # Round to one decimal place
            return {'province': province, 'la_nina_probability': la_nina_prob_value}
        else:
            raise HTTPException(status_code=404, detail="Province not found")

    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(error_msg)
        raise HTTPException(status_code=500, detail="Internal server error during request.")
