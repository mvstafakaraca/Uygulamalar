import tkinter as tk
from tkinter import ttk, messagebox

class Proje:
    def __init__(self, ad, baslangic_tarihi, bitis_tarihi):
        self.ad = ad
        self.baslangic_tarihi = baslangic_tarihi
        self.bitis_tarihi = bitis_tarihi
        self.gorevler = []

    def gorev_ekle(self, gorev):
        self.gorevler.append(gorev)

    def gorev_sil(self, gorev):
        self.gorevler.remove(gorev)

class Gorev:
    def __init__(self, ad, calisan):
        self.ad = ad
        self.calisan = calisan

class Calisan:
    def __init__(self, ad):
        self.ad = ad

class Uygulama:
    def __init__(self, root):
        self.root = root
        self.root.title("Proje Yönetim Sistemi")

        self.stil = ttk.Style()
        self.stil.theme_use("clam")  # Arayüz teması

        self.proje_listesi = []
        self.calisan_listesi = [Calisan("Cem"), Calisan("Kemal"), Calisan("Beliz"), Calisan("Eda")]

        self.proje_label = ttk.Label(root, text="Proje Adı:", font=("Helvetica", 12))
        self.proje_label.grid(row=0, column=0, sticky="w")
        self.proje_entry = ttk.Entry(root, font=("Helvetica", 12))
        self.proje_entry.grid(row=0, column=1)

        self.baslangic_label = ttk.Label(root, text="Başlangıç Tarihi:", font=("Helvetica", 12))
        self.baslangic_label.grid(row=1, column=0, sticky="w")
        self.baslangic_entry = ttk.Entry(root, font=("Helvetica", 12))
        self.baslangic_entry.grid(row=1, column=1)

        self.bitis_label = ttk.Label(root, text="Bitiş Tarihi:", font=("Helvetica", 12))
        self.bitis_label.grid(row=2, column=0, sticky="w")
        self.bitis_entry = ttk.Entry(root, font=("Helvetica", 12))
        self.bitis_entry.grid(row=2, column=1)

        self.proje_ekle_button = ttk.Button(root, text="Proje Ekle", command=self.proje_ekle, style="Gozde.TButton")
        self.proje_ekle_button.grid(row=3, columnspan=2)

        self.proje_listbox = tk.Listbox(root, font=("Helvetica", 12))
        self.proje_listbox.grid(row=4, columnspan=2, sticky="nsew")
        self.proje_listbox.bind("<Double-Button-1>", self.proje_secildi)

        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(4, weight=1)

        self.stil.configure("Gozde.TButton", font=("Helvetica", 12))

    def proje_ekle(self):
        proje_adi = self.proje_entry.get()
        baslangic_tarihi = self.baslangic_entry.get()
        bitis_tarihi = self.bitis_entry.get()

        if proje_adi and baslangic_tarihi and bitis_tarihi:
            yeni_proje = Proje(proje_adi, baslangic_tarihi, bitis_tarihi)
            self.proje_listesi.append(yeni_proje)
            self.proje_listbox.insert(tk.END, yeni_proje.ad)
            messagebox.showinfo("Başarılı", "Proje başarıyla eklendi.")
        else:
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")

    def proje_secildi(self, event):
        if self.proje_listbox.curselection():
            secili_proje_index = self.proje_listbox.curselection()[0]
            secili_proje = self.proje_listesi[secili_proje_index]
            self.proje_detaylari_goster(secili_proje)

    def proje_detaylari_goster(self, proje):
        pencere = tk.Toplevel(self.root)
        pencere.title("Proje Detayları")

        ttk.Label(pencere, text="Proje Adı:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w")
        ttk.Label(pencere, text=proje.ad, font=("Helvetica", 12)).grid(row=0, column=1, sticky="w")

        ttk.Label(pencere, text="Başlangıç Tarihi:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w")
        ttk.Label(pencere, text=proje.baslangic_tarihi, font=("Helvetica", 12)).grid(row=1, column=1, sticky="w")

        ttk.Label(pencere, text="Bitiş Tarihi:", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w")
        ttk.Label(pencere, text=proje.bitis_tarihi, font=("Helvetica", 12)).grid(row=2, column=1, sticky="w")

        ttk.Label(pencere, text="Görevler:", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w")
        for i, gorev in enumerate(proje.gorevler):
            ttk.Label(pencere, text=f"{i + 1}. Görev: {gorev.ad}, Çalışan: {gorev.calisan.ad}", font=("Helvetica", 12)).grid(row=i + 4, columnspan=2, sticky="w")

        ttk.Button(pencere, text="Görev Ekle", command=lambda: self.gorev_ekle_penceresi(proje), style="Gozde.TButton").grid(row=len(proje.gorevler) + 4, columnspan=2)

    def gorev_ekle_penceresi(self, proje):
        pencere = tk.Toplevel(self.root)
        pencere.title("Görev Ekle")

        ttk.Label(pencere, text="Görev Adı:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w")
        gorev_entry = ttk.Entry(pencere, font=("Helvetica", 12))
        gorev_entry.grid(row=0, column=1)

        ttk.Label(pencere, text="Çalışan:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w")
        calisan_secim = ttk.Combobox(pencere, values=[calisan.ad for calisan in self.calisan_listesi], font=("Helvetica", 12))
        calisan_secim.grid(row=1, column=1)

        def gorev_ekle():
            gorev_adi = gorev_entry.get()
            secili_calisan_index = calisan_secim.current()

            if gorev_adi and secili_calisan_index != -1:
                secili_calisan = self.calisan_listesi[secili_calisan_index]
                proje.gorev_ekle(Gorev(gorev_adi, secili_calisan))
                pencere.destroy()
                self.proje_detaylari_goster(proje)
            else:
                messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")

        ttk.Button(pencere, text="Ekle", command=gorev_ekle, style="Gozde.TButton").grid(row=2, columnspan=2)

root = tk.Tk()
uygulama = Uygulama(root)
root.mainloop()
