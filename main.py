import json
import os
from modules import food,kesimpulan,minum,tidur 
import storage

daily_data = storage.load_data()

def main_menu():
    print("==========================================")
    print("       🩺   SynqLife V1.0   🩺")
    print("==========================================")
    print("Analisis Kesehatan Harian Otomatis Anda")
    print("------------------------------------------")
    print("[1] 🌙  Catat Durasi Tidur")
    print("[2] 💧  Cek Kebutuhan Hidrasi (Cuaca)")
    print("[3] 🍎  Catat Makanan (Kalori Masuk)")
    print("------------------------------------------")
    print("[4] 📊  Tampilkan Ringkasan Harian")
    print("[0] 🚪  Keluar")
    print("==========================================")
    while True: 
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\nMentracking Durasi Tidur🌙 ...")
            start = input("Waktu mulai tidur (HH:MM): ")
            end = input("Waktu bangun (HH:MM): ")
            hasil = tidur.durasi_tidur(start_time=start, end_time=end)

            print(f"\n✅ Durasi tidur: {hasil}")
            daily_data["durasi_tidur"] = hasil  
            storage.save_data(daily_data)          
            print("Data tidur berhasil disimpan.")
            input("\nTekan Enter untuk kembali ke menu utama...")

        elif choice == "2":
            print("\nMengkalkulasi Asupan Air💧...")
            kota=input("Masukkan nama kota untuk cek cuaca: ")
            hidrasi=minum.hidrasi_harian(kota)  

            print(f"\n✅ Rekomendasi asupan air harian: {hidrasi}")
            daily_data["rekomendasi_hidrasi"] = hidrasi
            storage.save_data(daily_data)   
            print("Data hidrasi berhasil disimpan.")
            input("\nTekan Enter untuk kembali ke menu utama...")

        elif choice == "3":
            print("\nMenganalisis Nutrisi dari Makanan...")
            makanan=input("Masukkan nama makanan: ")
            analisis= food.get_nutrition(makanan)  
            print(f"\n✅ Nutrisi tercatat: {analisis['kalori']} kkal")
            
            daily_data["kalori_masuk"] +=analisis['kalori']
            daily_data["protein"] += analisis['protein']
            daily_data["karbohidrat"] += analisis['karbohidrat']
            daily_data["lemak"] += analisis['lemak']
            storage.save_data(daily_data)
            print("Data nutrisi berhasil disimpan.")
            input("\nTekan Enter untuk kembali ke menu utama...")

        elif choice == "4":
            print("==========================================")
            print("\n📊 Ringkasan Data Kesehatan Harian Anda:")
            print("==========================================")
            kesimpulan.show_summary()
            input("\nTekan Enter untuk kembali ke menu utama...")

        elif choice == "0":
            print("Terima kasih sudah menggunakan SynqLife! Stay healthy! 👋")
            break
        else:
            print("Pilihan invalid. Silahkan pilih 1-4.\n")

if __name__ == "__main__":
    main_menu()