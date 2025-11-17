import os
import json
daily_data = {
    "durasi_tidur": "Belum dicatat",
    "rekomendasi_hidrasi": "Belum dicek",
    "quote_motivasi": "Belum dilihat",
    "kalori_masuk": 0,
    "kalori_keluar": 0,
    "protein": 0,
    "karbohidrat": 0,
    "lemak": 0
}
FILE_NAME = 'health_data.json'
def load_data():
    """
    Memuat data harian dari file JSON.
    Jika file tidak ada atau korup, kembalikan data default.
    """
    if not os.path.exists(FILE_NAME):
        print("File data tidak ditemukan, membuat file baru...")
        save_data(daily_data)
        return daily_data
    
    try:
        with open(FILE_NAME, 'r') as f:
            data = json.load(f)

            for key in daily_data:
                if key not in data:
                    data[key] = daily_data[key]
            return data
    except (json.JSONDecodeError, IOError):
        print("File data korup atau error. Menggunakan data default.")
        return daily_data

def save_data(data):
    """
    Menyimpan dictionary data ke file JSON.
    """
    try:
        with open(FILE_NAME, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Gagal menyimpan data ke file: {e}")