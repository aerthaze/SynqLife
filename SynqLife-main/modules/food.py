import requests

API_URL = "https://id.openfoodfacts.org/cgi/search.pl"

def get_nutrition(query):
    """
    Mencari data nutrisi dari endpoint OpenFoodFacts Indonesia.
    Memprioritaskan nama produk Bahasa Indonesia ('product_name_id').
    """
    
    params = {
        'search_terms': query,
        'search_simple': 1,
        'action': 'process',
        'json': 1,
        'page_size': 1,
        'fields': 'product_name,product_name_id,nutriments' 
    }
    
    try:
        response = requests.get(API_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('products') and len(data['products']) > 0:
                product = data['products'][0]
                nutriments = product.get('nutriments', {})
                
                product_name = product.get('product_name_id', product.get('product_name', query))
                
                kalori = nutriments.get('energy-kcal_100g', 0)
                protein = nutriments.get('proteins_100g', 0)
                karbohidrat = nutriments.get('carbohydrates_100g', 0)
                lemak = nutriments.get('fat_100g', 0)
                
                print(f"Info nutrisi ditemukan untuk: {product_name}")
                print("(Catatan: Data berikut adalah perkiraan per 100g)")

                return {
                    "kalori": float(calories),
                    "protein": float(protein),
                    "karbohidrat": float(carbs),
                    "lemak": float(fat)
                }
            else:
                print(f"Tidak ada produk yang ditemukan untuk '{query}' di database Indonesia.")
                return {"kalori": 0, "protein": 0, "karbohidrat": 0, "lemak": 0}
                
    except requests.exceptions.RequestException as e:
        print(f"Error saat menghubungi API: {e}")
        return {"kalori": 0, "protein": 0, "karbohidrat": 0, "lemak": 0}
    
    return {"kalori": 0, "protein": 0, "karbohidrat": 0, "lemak": 0}