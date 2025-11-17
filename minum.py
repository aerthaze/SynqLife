import requests

def hidrasi_harian(kota):
    api_key = "b9bb9ccbd6eb591071cfe196f1b8c18a"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': kota,
        'appid': [api_key],
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