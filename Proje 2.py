import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class Doktor:
    def __init__(self, isim, uzmanlik_alani):
        self.isim = isim
        self.uzmanlik_alani = uzmanlik_alani
        self.musaitlik_durumu = True  # Doktorlar başlangıçta müsait durumda

class RandevuSistemi:
    def __init__(self, root):
        self.root = root
        self.root.title("Randevu Sistemi")
        self.root.geometry("550x550")
        self.root.configure(background="#FFD700")  # Sarı arka plan

        # Doktorlar oluşturuluyor
        self.doktorlar = [
            Doktor("Dr. Hüseyin Ahmet Can", "Dahiliye"),
            Doktor("Dr. Ayşe Taşçı", "Nöroloji"),
            Doktor("Dr. Dağhan Yıldız", "Kardiyoloji")
        ]

        # Başlık etiketi
        self.baslik_label = ttk.Label(root, text="Randevu Sistemi", background="#FFD700", font=("Helvetica", 20), foreground="#000080")  # Lacivert yazı
        self.baslik_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        # Doktor seçimi için Combobox oluşturuluyor
        self.doktor_label = ttk.Label(root, text="Doktor Seçin:", background="#FFD700", font=("Helvetica", 12), foreground="#000080")  # Lacivert yazı
        self.doktor_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.doktor_combobox = ttk.Combobox(root, values=[f"{doktor.isim} - {doktor.uzmanlik_alani}" for doktor in self.doktorlar], width=50)
        self.doktor_combobox.grid(row=1, column=1, padx=10, pady=10)

        # Doktorların müsaitlik durumunu göstermek için etiketler oluşturuluyor
        self.musaitlik_label = ttk.Label(root, text="Doktorların Müsaitlik Durumu:", background="#FFD700", font=("Helvetica", 12), foreground="#000080")  # Lacivert yazı
        self.musaitlik_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.musaitlik_etiketler = []
        for i, doktor in enumerate(self.doktorlar):
            musaitlik_etiket = ttk.Label(root, text=f"{doktor.isim}: {'Müsait' if doktor.musaitlik_durumu else 'Müsait Değil'}", background="#FFD700", font=("Helvetica", 10), foreground="#000080")  # Lacivert yazı
            musaitlik_etiket.grid(row=i+3, column=0, columnspan=2, padx=10, pady=5, sticky="w")
            self.musaitlik_etiketler.append(musaitlik_etiket)

        # Hasta Bilgileri
        self.isim_label = ttk.Label(root, text="İsim:", background="#FFD700", font=("Helvetica", 12), foreground="#000080")  # Lacivert yazı
        self.isim_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        self.isim_entry = ttk.Entry(root, width=40)
        self.isim_entry.grid(row=6, column=1, padx=10, pady=10)

        self.tc_label = ttk.Label(root, text="TC Kimlik No:", background="#FFD700", font=("Helvetica", 12), foreground="#000080")  # Lacivert yazı
        self.tc_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")

        self.tc_entry = ttk.Entry(root, width=40)
        self.tc_entry.grid(row=7, column=1, padx=10, pady=10)

        # Randevu Tarihi
        self.tarih_label = ttk.Label(root, text="Randevu Tarihi (GG.AA.YYYY):", background="#FFD700", font=("Helvetica", 12), foreground="#000080")  # Lacivert yazı
        self.tarih_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

        self.tarih_entry = ttk.Entry(root, width=40)
        self.tarih_entry.grid(row=8, column=1, padx=10, pady=10)

        # Başarıyla oluşturulan randevuları göstermek için bir alan oluşturuluyor
        self.randevu_bilgisi_label = ttk.Label(root, text="Başarıyla Oluşturulan Randevular:", background="#FFD700", font=("Helvetica", 12), foreground="#000080")  # Lacivert yazı
        self.randevu_bilgisi_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.randevu_bilgisi_listbox = tk.Listbox(root, width=60, height=10)
        self.randevu_bilgisi_listbox.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

        # Butonlar
        self.randevu_al_button = ttk.Button(root, text="Randevu Al", command=self.randevu_al)
        self.randevu_al_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

        self.randevu_iptal_button = ttk.Button(root, text="Randevu İptal", command=self.randevu_iptal)
        self.randevu_iptal_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

        self.cikis_button = ttk.Button(root, text="Çıkış", command=root.quit)
        self.cikis_button.grid(row=13, column=0, columnspan=2, padx=10, pady=10)

    def tarih_gecerli_mi(self, tarih_str):
        try:
            tarih = datetime.strptime(tarih_str, "%d.%m.%Y")
            return tarih >= datetime.now()
        except ValueError:
            return False

    def randevu_al(self):
        secili_doktor_secimi = self.doktor_combobox.get()
        secili_isim = self.isim_entry.get()
        secili_tc = self.tc_entry.get()
        secili_tarih = self.tarih_entry.get()

        # TC kimlik numarası doğrulaması
        if len(secili_tc) != 11 or secili_tc.startswith('0'):
            messagebox.showerror("Hata", "Geçersiz TC Kimlik No!")
            return

        # Tarih geçerlilik kontrolü
        if not self.tarih_gecerli_mi(secili_tarih):
            messagebox.showerror("Hata", "Geçersiz tarih!")
            return

        # Seçilen doktoru bul
        secili_doktor_adi, secili_uzmanlik_alani = secili_doktor_secimi.split(" - ")
        secili_doktor = None
        for doktor in self.doktorlar:
            if doktor.isim == secili_doktor_adi and doktor.uzmanlik_alani == secili_uzmanlik_alani:
                secili_doktor = doktor
                break

        if secili_doktor is None:
            messagebox.showerror("Hata", "Geçersiz doktor seçimi!")
            return

        # Müsaitlik kontrolü
        if not secili_doktor.musaitlik_durumu:
            messagebox.showerror("Hata", "Seçilen doktor şu anda müsait değil.")
            return

        # Randevu alındığında doktorun müsaitlik durumunu güncelle
        secili_doktor.musaitlik_durumu = False

        # Randevu bilgilerini listbox'a ekle
        randevu_bilgisi = f"Doktor: {secili_doktor_adi} - {secili_uzmanlik_alani}, İsim: {secili_isim}, TC: {secili_tc}, Tarih: {secili_tarih}"
        self.randevu_bilgisi_listbox.insert(tk.END, randevu_bilgisi)

        # Doktorun müsaitlik durumunu güncelle
        self.guncelle_musaitlik_etiketi(secili_doktor_adi, False)

        # Bildirim göster
        messagebox.showinfo("Bilgi", "Randevu başarıyla oluşturuldu.\n" + randevu_bilgisi)

    def randevu_iptal(self):
        secili_index = self.randevu_bilgisi_listbox.curselection()
        if not secili_index:
            messagebox.showerror("Hata", "Lütfen iptal etmek istediğiniz randevuyu seçin.")
            return

        secili_index = secili_index[0]
        secili_randevu = self.randevu_bilgisi_listbox.get(secili_index)
        self.randevu_bilgisi_listbox.delete(secili_index)
        self.randevu_bilgisi_listbox.insert(secili_index, secili_randevu + " - İptal Edildi")
        messagebox.showinfo("Bilgi", "Randevu başarıyla iptal edildi.")

        # Doktorun müsaitlik durumunu güncelle
        secili_doktor_adi = secili_randevu.split(",")[0].split(":")[1].strip().split(" - ")[0]
        self.guncelle_musaitlik_etiketi(secili_doktor_adi, True)

    def guncelle_musaitlik_etiketi(self, doktor_adi, durum):
        for etiket in self.musaitlik_etiketler:
            if doktor_adi in etiket.cget("text"):
                etiket.config(text=f"{doktor_adi}: {'Müsait' if durum else 'Müsait Değil'}")
                break

def main():
    root = tk.Tk()
    randevu_sistemi = RandevuSistemi(root)
    root.mainloop()

if __name__ == "__main__":
    main()
