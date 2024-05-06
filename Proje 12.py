import tkinter as tk
from tkinter import ttk

class Kullanici:
    def __init__(self, ad, yas, cinsiyet, hastalik):
        self.ad = ad
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.hastalik = hastalik
        self.saglik_kayitlari = []

class SaglikKaydi:
    def __init__(self, olcum_tarihi, olcum):
        self.olcum_tarihi = olcum_tarihi
        self.olcum = olcum

class Egzersiz:
    def __init__(self, ad, sure, tekrar):
        self.ad = ad
        self.sure = sure
        self.tekrar = tekrar

class Arayuz:
    def __init__(self, root):
        self.root = root
        self.root.title("Sağlık ve Egzersiz Takip Uygulaması")
        self.root.configure(background="blue")  # Arka plan rengini ayarla

        # Hastalıklara özel egzersizlerin bulunduğu sözlük
        self.egzersizler = {
            "Diyabet": ["Aerobik egzersizler: Yürüyüş, koşu, yüzme gibi kardiyovasküler egzersizler kan şekerini düzenlemeye yardımcı olur.", 
                        "Direnç egzersizleri: Dumbell çalışmaları, direnç bandı egzersizleri kas gücünü artırır ve insülin duyarlılığını iyileştirir."],

            "Hipertansiyon": ["Aerobik egzersizler: Yavaş tempolu yürüyüş, bisiklet sürme gibi düşük yoğunluklu kardiyovasküler egzersizler kan basıncını düşürmeye yardımcı olur.", 
                              "Yoga ve tai chi gibi gevşeme egzersizleri stresi azaltarak kan basıncını düşürebilir."],

            "Kanser": ["Yürüyüş ve hafif aerobik egzersizler: Kanserle mücadelede stresi azaltır, bağışıklık sistemini güçlendirir ve genel sağlık durumunu iyileştirir.", 
                       "Denge ve esneklik egzersizleri: Hastalık veya tedaviye bağlı fiziksel kısıtlamaları azaltabilir."],

            "Alzheimer Hastalığı": ["Basit yürüyüşler: Düzenli yürüyüşler beyin fonksiyonlarını iyileştirebilir ve bilişsel gerilemeyi yavaşlatabilir.", 
                                     "Hafıza oyunları ve aktiviteleri: Zihinsel egzersizler, Alzheimer hastalığının ilerlemesini yavaşlatabilir."],

            "Parkinson Hastalığı": ["Yürüyüş: Dengeyi ve koordinasyonu geliştirir.", 
                                    "Tai Chi ve yoga: Dengeyi artırır, kas esnekliğini korur ve stresi azaltır."],

            "Astım": ["Yüzme: Solunum kapasitesini artırır ve astım semptomlarını azaltabilir.", 
                      "Kardiyo egzersizler: Düşük yoğunluklu aerobik egzersizler, solunum kontrolünü geliştirebilir."],

            "KOAH": ["Solunum egzersizleri: Solunum teknikleri ve nefes alma egzersizleri solunum kapasitesini artırır.", 
                     "Yürüyüş ve hafif aerobik egzersizler: KOAH semptomlarını azaltır ve dayanıklılığı artırır."],

            "Romatoid Artrit": ["Su aerobiği: Eklem ağrılarını azaltır ve kas gücünü artırır.", 
                                "Esneme egzersizleri: Eklem hareket açıklığını artırır ve esnekliği korur."],

            "Osteoporoz": ["Direnç egzersizleri: Ağırlık kaldırma ve direnç bandı egzersizleri kemik yoğunluğunu artırır.", 
                            "Yürüyüş ve dans gibi kardiyovasküler egzersizler kemikleri güçlendirir."],

            "Kalp Hastalıkları": ["Kardiyo egzersizleri: Yürüyüş, bisiklet sürme gibi aerobik egzersizler kalp sağlığını artırır."],

            "Felç": ["Fizyoterapist tarafından belirlenen özel rehabilitasyon egzersizleri: Felçli tarafın güçlenmesi, denge ve koordinasyonun geliştirilmesi için özel egzersizler yapılabilir."],

            "Depresyon": ["Aerobik egzersizler: Yürüyüş, koşu gibi egzersizler endorfin salgısını artırarak depresyon semptomlarını azaltabilir.", 
                          "Yoga ve meditasyon: Stresi azaltır ve zihinsel iyilik hali sağlar."]
        }

        # Arayüz bileşenlerinin oluşturulması
        ttk.Label(root, text="Ad:", background="blue", foreground="white").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.ad_entry = ttk.Entry(root)
        self.ad_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        ttk.Label(root, text="Yaş:", background="blue", foreground="white").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.yas_entry = ttk.Entry(root)
        self.yas_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        ttk.Label(root, text="Cinsiyet:", background="blue", foreground="white").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.cinsiyet_entry = ttk.Entry(root)
        self.cinsiyet_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")

        ttk.Label(root, text="Hastalık:", background="blue", foreground="white").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.hastalik_secim = ttk.Combobox(root, values=list(self.egzersizler.keys()))
        self.hastalik_secim.grid(row=3, column=1, padx=5, pady=5, sticky="we")

        # Kayıt ekle butonu
        self.kayit_ekle_btn = tk.Button(root, text="Kayıt Ekle", command=self.kayit_ekle, background="white", foreground="blue")
        self.kayit_ekle_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        # Sağlık kayıtlarını göstermek için bir liste kutusu
        ttk.Label(root, text="Sağlık Kayıtları:", background="blue", foreground="white").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.saglik_liste = tk.Listbox(root, background="white", foreground="blue")
        self.saglik_liste.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        # Egzersiz listesi
        ttk.Label(root, text="Egzersizler:", background="blue", foreground="white").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.egzersiz_liste = tk.Listbox(root, background="white", foreground="blue")
        self.egzersiz_liste.grid(row=1, column=2, rowspan=6, padx=5, pady=5, sticky="we")

        # Rapor düğmesi
        self.rapor_btn = tk.Button(root, text="Rapor Ver", command=self.rapor_ver, background="white", foreground="blue")
        self.rapor_btn.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.kullanicilar = []

    def kayit_ekle(self):
        ad = self.ad_entry.get()
        yas = self.yas_entry.get()
        cinsiyet = self.cinsiyet_entry.get()
        hastalik = self.hastalik_secim.get()
        yeni_kullanici = Kullanici(ad, yas, cinsiyet, hastalik)
        self.kullanicilar.append(yeni_kullanici)
        self.saglik_liste.insert(tk.END, f"{ad}, {yas}, {cinsiyet}, {hastalik}")

        # Seçilen hastalığa özel egzersizleri ekle
        egzersizler = self.egzersizler.get(hastalik, [])
        for egzersiz in egzersizler:
            self.egzersiz_liste.insert(tk.END, egzersiz)

    def rapor_ver(self):
        rapor = ""
        for kullanici in self.kullanicilar:
            rapor += f"Ad: {kullanici.ad}, Yaş: {kullanici.yas}, Cinsiyet: {kullanici.cinsiyet}, Hastalık: {kullanici.hastalik}\n"
            rapor += "Egzersizler:\n"
            for egzersiz in self.egzersizler.get(kullanici.hastalik, []):
                rapor += f"- {egzersiz}\n"
            rapor += "\n"
        rapor_ekrani = tk.Toplevel(self.root)
        rapor_ekrani.title("Rapor")
        rapor_etiket = tk.Label(rapor_ekrani, text=rapor, background="white", foreground="blue", justify="left")
        rapor_etiket.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = Arayuz(root)
    root.mainloop()
