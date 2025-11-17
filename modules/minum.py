import requests
import modules.config as config

def hidrasi_harian(kota):
    api_key = config.OPENWEATHER_API_KEY    
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': kota,
        'appid': config.OPENWEATHER_API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            if temp > 28:
                return f"Suhu: {temp}°C. Rekomendasi hidrasi: 3.0 Liter per hari."
            else:
                return f"Suhu: {temp}°C. Rekomendasi hidrasi: 2.5 Liter per hari."
        else:
            error_msg = data.get('message', 'Unknown error')
            return f"Error {response.status_code}: {error_msg}"
            
    except requests.exceptions.RequestException as e:
        return f"Terjadi kesalahan koneksi: {e}"
    except KeyError:
        return "Data cuaca tidak lengkap dari API."
    except Exception as e:
        return f"Terjadi kesalahan tak terduga: {e}"