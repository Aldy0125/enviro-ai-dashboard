from fastapi import FastAPI, HTTPException
import uvicorn
import requests
import xml.etree.ElementTree as ET

# Inisialisasi Server Utama (Ini yang tadi terhapus)
app = FastAPI(
    title="Enviro AI Dashboard API", 
    description="Backend Service untuk agregasi data lingkungan dan peringatan dini BMKG.", 
    version="1.1"
)

# Endpoint 1: Health Check
@app.get("/")
def health_check():
    return {
        "status": "Online", 
        "system": "Enviro AI Backend",
        "message": "Engine is running perfectly."
    }

# Endpoint 2: Integrasi Data Real-time BMKG dengan Defensive Programming
@app.get("/api/v1/gempa-realtime")
def get_gempa_realtime():
    try:
        url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.xml"
        response = requests.get(url)
        response.raise_for_status() 
        
        root = ET.fromstring(response.content)
        gempa = root.find('gempa')
        
        # Helper function agar server tidak crash jika BMKG mengubah struktur XML-nya
        def safe_get(tag_path):
            element = gempa.find(tag_path)
            return element.text if element is not None and element.text else "Data tidak tersedia"
        
        # Merombak XML menjadi arsitektur JSON yang bersih
        return {
            "status": "success",
            "source": "BMKG Indonesia",
            "data": {
                "tanggal": safe_get('Tanggal'),
                "jam": safe_get('Jam'),
                "koordinat": safe_get('point/coordinates'), # Membaca hierarki nested XML dengan benar
                "magnitude": safe_get('Magnitude'),
                "kedalaman": safe_get('Kedalaman'),
                "wilayah": safe_get('Wilayah'),
                "potensi_tsunami": safe_get('Potensi'),
                "dirasakan": safe_get('Dirasakan')
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sistem gagal mengekstrak data BMKG: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)