import tkinter as tk
from tkinter import ttk, messagebox
import random

class Kullanici:
    def __init__(self, ad, soyad, email):
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.biletler = []

class Etkinlik:
    def __init__(self, ad, tarih, mekan):
        self.ad = ad
        self.tarih = tarih
        self.mekan = mekan

class Bilet:
    def __init__(self, numara, etkinlik):
        self.numara = numara
        self.etkinlik = etkinlik

class Arayuz:
    def __init__(self, root):
        self.root = root
        self.root.title("Etkinlik ve Bilet Yönetimi")
        self.root.configure(background="white")

        # Kullanıcı bilgileri girişi
        self.ad_label = ttk.Label(root, text="Ad:")
        self.ad_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.ad_entry = ttk.Entry(root)
        self.ad_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        self.soyad_label = ttk.Label(root, text="Soyad:")
        self.soyad_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.soyad_entry = ttk.Entry(root)
        self.soyad_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        self.email_label = ttk.Label(root, text="E-posta:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.email_entry = ttk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")

        self.giris_btn = ttk.Button(root, text="Giriş", command=self.giris)
        self.giris_btn.grid(row=3, columnspan=2, padx=5, pady=5)

        # Kullanıcı bilgi paneli
        self.kullanici_bilgi = tk.Text(root, height=2, width=30)
        self.kullanici_bilgi.grid(row=4, columnspan=2, padx=5, pady=5, sticky="we")

        # Bilet listesi
        self.bilet_listesi = tk.Listbox(root, height=5, width=50)
        self.bilet_listesi.grid(row=5, columnspan=2, padx=5, pady=5, sticky="we")
        self.bilet_listesi.bind("<Double-Button-1>", self.bilet_detay)

    def giris(self):
        ad = self.ad_entry.get()
        soyad = self.soyad_entry.get()
        email = self.email_entry.get()

        self.kullanici = Kullanici(ad, soyad, email)
        self.kullanici_bilgi.insert(tk.END, f"Giriş başarılı! Hoş geldiniz, {ad} {soyad}.\n")

        # self.ikinci_sayfa = IkinciSayfa(self.root, self.kullanici, self.bilet_listesi)

    def bilet_detay(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            bilet = self.kullanici.biletler[index]

            # bilet_detay = BiletDetay(self.root, bilet, self.kullanici)

class IkinciSayfa:
    def __init__(self, root, kullanici, bilet_listesi):
        self.root = root
        self.kullanici = kullanici
        self.bilet_listesi = bilet_listesi

        self.ikinci_sayfa = tk.Toplevel(self.root)
        self.ikinci_sayfa.title("Bilet İşlemleri")
        self.ikinci_sayfa.configure(background="white")

        self.etkinlikler = ["Konser", "Spor Etkinliği", "Tiyatro Gösterisi", "Konferans"]

        ttk.Label(self.ikinci_sayfa, text="Etkinlik Seç:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.etkinlik_combo = ttk.Combobox(self.ikinci_sayfa, values=self.etkinlikler)
        self.etkinlik_combo.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        self.bilet_al_btn = ttk.Button(self.ikinci_sayfa, text="Bilet Al", command=self.bilet_al)
        self.bilet_al_btn.grid(row=1, columnspan=2, padx=5, pady=5)

    def bilet_al(self):
        etkinlik = self.etkinlik_combo.get()
        yeni_etkinlik = Etkinlik(etkinlik, "10.10.2024", "Örnek Mekan")
        bilet_numarasi = random.randint(10000, 99999)
        yeni_bilet = Bilet(bilet_numarasi, yeni_etkinlik)

        if len([b for b in self.kullanici.biletler if b.etkinlik.ad == yeni_etkinlik.ad]) > 0:
            messagebox.showerror("Hata", "Aynı etkinlikten birden fazla bilet alınamaz!")
        else:
            self.kullanici.biletler.append(yeni_bilet)
            self.bilet_listesi.insert(tk.END, f"{yeni_etkinlik.ad} - Bilet Numarası: {bilet_numarasi}")

# class BiletDetay:
#     def __init__(self, root, bilet, kullanici):
#         self.root = root
#         self.bilet = bilet
#         self.kullanici = kullanici
#
#         self.bilet_detay = tk.Toplevel(self.root)
#         self.bilet_detay.title("Bilet Detayı")
#         self.bilet_detay.configure(background="white")
#
#         ttk.Label(self.bilet_detay, text=f"{self.bilet.etkinlik.ad} Bilet Detayı").grid(row=0, column=0, columnspan=2, padx=5, pady=5)
#
#         ttk.Label(self.bilet_detay, text=f"Bilet Numarası: {self.bilet.numara}").grid(row=1, column=0, columnspan=2, padx=5, pady=5)
#
#         ttk.Label(self.bilet_detay, text="Bilet İşlemleri").grid(row=2, column=0, columnspan=2, padx=5, pady=5)
#
#         self.satis_btn = ttk.Button(self.bilet_detay, text="Satış Yap", command=self.satis)
#         self.satis_btn.grid(row=3, column=0, padx=5, pady=5)
#
#         self.iade_btn = ttk.Button(self.bilet_detay, text="İade Yap", command=self.iade)
#         self.iade_btn.grid(row=3, column=1, padx=5, pady=5)

#     def satis(self):
#         self.kullanici.biletler.remove(self.bilet)
#         messagebox.showinfo("Bilgi", "Bilet satışı başarıyla gerçekleştirildi.")
#         self.root.destroy()
#
#     def iade(self):
#         self.kullanici.biletler.remove(self.bilet)
#         messagebox.showinfo("Bilgi", "Bilet iadesi başarıyla gerçekleştirildi.")
#         self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = Arayuz(root)
    root.mainloop()
