import storage
import matplotlib.pyplot as plt

def show_summary():
    data = storage.load_data()

    kalori = data.get('kalori_masuk', 0)
    tidur = data.get('durasi_tidur', 'Belum dicatat')
    hidrasi = data.get('rekomendasi_hidrasi', 'Belum dicek')

    protein = data.get('protein', 0)
    karbo = data.get('karbohidrat', 0)
    lemak = data.get('lemak', 0)

    print("\n📊 RINGKASAN KESEHATAN HARI INI\n")
    print(f"🔥 Kalori: {kalori} kkal")
    print(f"😴 Tidur : {tidur}")
    print(f"💧 Hidrasi: {hidrasi}")
    print(f"🥩 Protein: {protein} g")
    print(f"🍚 Karbo : {karbo} g")
    print(f"🧈 Lemak : {lemak} g\n")

    labels = ['Protein', 'Karbohidrat', 'Lemak']
    values = [protein, karbo, lemak]
    colors = ['#4CAF50', '#FFC107', '#FF5722']

    plt.figure(figsize=(6,4))
    bars = plt.bar(labels, values, color=colors)

    plt.title('Distribusi Makronutrien (gram)')
    plt.xlabel('Makronutrien')
    plt.ylabel('Jumlah (g)')
    plt.grid(axis='y', linestyle='--', alpha=0.3)

    # tampilkan angka
    for bar in bars:
        yval = bar.get_height()
        pos = yval + 0.5 if yval > 0 else 0.3
        plt.text(bar.get_x() + bar.get_width()/2, pos, f"{yval}g", ha='center', fontsize=9)

    plt.tight_layout()
    plt.show()
