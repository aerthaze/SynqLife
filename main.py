import json
import os
from modules import food,kalori,kesimpulan,minum,motivasi,tidur 
from utility import clear_screen, pause
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
    print("[3] 💪  Catat Aktivitas (Kalori Terbakar)")
    print("[4] 🍎  Catat Makanan (Kalori Masuk)")
    print("------------------------------------------")
    print("[5] 📊  Tampilkan Ringkasan Harian")
    print("[0] 🚪  Keluar")
    print("==========================================")
    while True: 
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            clear_screen()
            print("\nMentracking Durasi Tidur🌙 ...")
            start = input("Waktu mulai tidur (HH:MM): ")
            end = input("Waktu bangun (HH:MM): ")
            hasil = tidur.durasi_tidur(start_time=start, end_time=end)

            print(f"\n✅ Durasi tidur: {hasil}")
            daily_data["durasi_tidur"] = hasil  
            storage.save_data(daily_data)          
            print("Data tidur berhasil disimpan.")
            pause()

        elif choice == "2":
            clear_screen()
            print("\nMengkalkulasi Asupan Air💧...")
            kota=input("Masukkan nama kota untuk cek cuaca: ")
            hidrasi=minum.hidrasi_harian(kota)  

            print(f"\n✅ Rekomendasi asupan air harian: {hidrasi}")
            daily_data["rekomendasi_hidrasi"] = hidrasi
            storage.save_data(daily_data)   
            print("Data hidrasi berhasil disimpan.")
            pause()

        elif choice == "3":
            clear_screen()
            print("\nMengestimasi Kalori yang Terbakar💪 ...")
            aktivitas=input("Masukkan jenis aktivitas (misal: lari, bersepeda): ")
            durasi=int(input("Masukkan durasi aktivitas (menit): "))
            kalori= kalori.kalori_terbakar(aktivitas, durasi)
            print(f"\n✅ Kalori terbakar tercatat: {kalori} kkal")

            daily_data["kalori_keluar"] += kalori
            storage.save_data(daily_data)
            print("Data kalori terbakar berhasil disimpan.")
            pause()

        elif choice == "4":
            clear_screen()
            print("\nMenganalisis Nutrisi dari Makanan...")
            makanan=input("Masukkan nama makanan: ")
            analisis= food.analisis_makanan(makanan)  
            print(f"\n✅ Nutrisi tercatat: {makanan['kalori']} kkal")
            
            daily_data["kalori_masuk"] += makanan['kalori']
            daily_data["protein"] += makanan['protein']
            daily_data["karbohidrat"] += makanan['karbohidrat']
            daily_data["lemak"] += makanan['lemak']
            storage.save_data(daily_data)
            print("Data nutrisi berhasil disimpan.")
            pause()

        elif choice == "5":
            print("\n Menulis Daily Motivation Quote Kesehatan...")
            clear_screen()
            print("==========================================")
            print("\n📊 Ringkasan Data Kesehatan Harian Anda:")
            print("==========================================")
            kalori_data = [daily_data["calories_in"], daily_data["calories_out"]]
            makro_data = [daily_data["protein"], daily_data["carbs"], daily_data["fat"]]
            kesimpulan.show_summary(kalori_data, makro_data)
            pause()

        elif choice == "0":
            print("Terima kasih sudah menggunakan SynqLife! Stay healthy! 👋")
            break
        else:
            print("Pilihan invalid. Silahkan pilih 1-6.\n")
# Run the menu
if __name__ == "__main__":
    main_menu()