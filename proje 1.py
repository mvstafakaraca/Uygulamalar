import tkinter as tk
from tkinter import ttk

class Arac:
    def __init__(self, arac_id, model, kiralama_durumu):
        self.arac_id = arac_id
        self.model = model
        self.kiralama_durumu = kiralama_durumu
    
    def arac_durumu_guncelle(self, durum):
        self.kiralama_durumu = durum

class Musteri:
    def __init__(self, ad, soyad, telefon):
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon
        self.kiralamalar = []
        self.kiralanabilir = True

    def kiralama_yap(self, arac):
        self.kiralamalar.append(arac)

    def kiralama_iptal(self, arac):
        if arac in self.kiralamalar:
            self.kiralamalar.remove(arac)
            return True
        return False

    def bilgileri_goster(self):
        return f"Ad: {self.ad}\nSoyad: {self.soyad}\nTelefon: {self.telefon}"

    def bilgileri_guncelle(self, ad=None, soyad=None, telefon=None):
        if ad:
            self.ad = ad
        if soyad:
            self.soyad = soyad
        if telefon:
            self.telefon = telefon

class Kiralama:
    def __init__(self):
        self.kiralamalar = []

    def kiralama_yap(self, musteri, arac):
        self.kiralamalar.append((musteri, arac))

    def kiralama_iptal_et(self, musteri, arac):
        for kiralama in self.kiralamalar:
            if kiralama[0] == musteri and kiralama[1] == arac:
                self.kiralamalar.remove(kiralama)
                arac.arac_durumu_guncelle(True)  
                return True
        return False

    def kiralama_bilgisi(self):
        bilgi = ""
        for index, (musteri, arac) in enumerate(self.kiralamalar):
            bilgi += f"Kiralama {index+1}:\nMüşteri: {musteri.ad} {musteri.soyad}\nTelefon: {musteri.telefon}\nAraba: {arac.model}\nKiralama Durumu: {'Kirada' if arac.kiralama_durumu else 'Kiralık Değil'}\n\n"
        return bilgi

araclar = [
    Arac(1, "Toyota Corolla", False),
    Arac(2, "Honda Civic", True),
    Arac(3, "Ford Focus", False),
    Arac(4, "Renault Taliant", True),
    Arac(5, "Wolkswagen Golf", True),
    Arac(6, "Bmw M5", True)
]

musteriler = {
    "5331459323": Musteri("Dimitri", "Adımcılar", "0533 145 9323"),
    "5427813498": Musteri("Ayşe", "Cansız", "0542 781 3498"),
    "5523756261": Musteri("Yiğit Kaan", "Cansız", "0552 375 6261"),
    "5368461124": Musteri("Ali", "Akıncı", "5368461124"),
    "5377495523": Musteri("Okan", "Karaca", "5377495523")
}

kiralama = Kiralama()

def arac_sec_arac(musteri, notebook):
    arac_sec_ekrani = tk.Toplevel()
    arac_sec_ekrani.title("Araç Kiralama - Araç Seçimi")
    arac_sec_ekrani.configure(bg="#f0f0f0")

    label = tk.Label(arac_sec_ekrani, text="Lütfen kiralamak istediğiniz aracı seçiniz:", font=("Arial", 14), bg="#f0f0f0")
    label.pack()

    for arac in araclar:
        arac_button = tk.Button(arac_sec_ekrani, text=arac.model, font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda a=arac: arac_secildi(a, musteri, notebook))
        arac_button.pack(pady=5)

def arac_secildi(arac, musteri, notebook):
    if arac.kiralama_durumu:
        if musteri.kiralanabilir:
            kiralama_yap(musteri, arac)
            arac.arac_durumu_guncelle(False)
            mesaj_ekrani = tk.Toplevel()
            mesaj_ekrani.title("Araç Kiralandı")
            mesaj_ekrani.configure(bg="#f0f0f0")

            mesaj_label = tk.Label(mesaj_ekrani, text=f"{arac.model} aracı kiralandı.", font=("Arial", 12), bg="#f0f0f0")
            mesaj_label.pack(pady=10)
            musteri.kiralanabilir = False
        else:
            mesaj_ekrani = tk.Toplevel()
            mesaj_ekrani.title("Araç Kiralanamıyor")
            mesaj_ekrani.configure(bg="#f0f0f0")

            mesaj_label = tk.Label(mesaj_ekrani, text="Bu müşteriye zaten araç kiralanmış.", font=("Arial", 12), bg="#f0f0f0")
            mesaj_label.pack(pady=10)
    else:
        mesaj_ekrani = tk.Toplevel()
        mesaj_ekrani.title("Araç Kiralanamıyor")
        mesaj_ekrani.configure(bg="#f0f0f0")

        mesaj_label = tk.Label(mesaj_ekrani, text=f"{arac.model} aracı kiralanamıyor. Kiralama durumu: Kiralık Değil", font=("Arial", 12), bg="#f0f0f0")
        mesaj_label.pack(pady=10)

    notebook.select(0)

def kiralama_yap(musteri, arac):
    kiralama.kiralama_yap(musteri, arac)
    musteri.kiralama_yap(arac)

def kiralama_iptal(musteri, arac):
    kiralama.kiralama_iptal_et(musteri, arac)
    musteri.kiralama_iptal(arac)

def kiralama_bilgisi_ekrani():
    bilgi_ekrani = tk.Toplevel()
    bilgi_ekrani.title("Kiralama Bilgisi")
    bilgi_ekrani.configure(bg="#f0f0f0")

    bilgi_label = tk.Label(bilgi_ekrani, text=kiralama.kiralama_bilgisi(), font=("Arial", 12), bg="#f0f0f0")
    bilgi_label.pack(pady=10)

def kapat(root):
    root.destroy()

def kiralama_ekrani():
    root = tk.Tk()
    root.title("Araç Kiralama Sistemi")
    root.attributes('-fullscreen', True)  
    root.configure(bg="#f0f0f0")

    notebook = ttk.Notebook(root)

    ana_sekme = tk.Frame(notebook, bg="#f0f0f0")
    label = tk.Label(ana_sekme, text="Hoş Geldiniz!", fg="#3E50B4", font=("Arial", 24), bg="#f0f0f0")
    label.pack(pady=10)

    button_kiralama = tk.Button(ana_sekme, text="Araç Kirala", bg="#4CAF50", fg="white", font=("Arial", 18), command=lambda: notebook.select(1))
    button_kiralama.pack(pady=10)

    button_iptal = tk.Button(ana_sekme, text="Kiralama İptal Et", bg="#FF5733", fg="white", font=("Arial", 18), command=lambda: kiralama_iptal_ekrani())
    button_iptal.pack(pady=5)

    button_bilgi = tk.Button(ana_sekme, text="Kiralama Bilgisi", bg="#FFA500", fg="white", font=("Arial", 18), command=kiralama_bilgisi_ekrani)
    button_bilgi.pack(pady=5)

    button_kapat = tk.Button(ana_sekme, text="Kapat", bg="#606060", fg="white", font=("Arial", 18), command=lambda: kapat(root))
    button_kapat.pack(pady=5)

    notebook.add(ana_sekme, text="Ana")

    kiralama_sekme = tk.Frame(notebook, bg="#f0f0f0")

    label_kiralama = tk.Label(kiralama_sekme, text="Müşteri Seçimi", font=("Arial", 24), bg="#f0f0f0")
    label_kiralama.pack(pady=10)

    for musteri in musteriler.values():
        musteri_button = tk.Button(kiralama_sekme, text=f"{musteri.ad} {musteri.soyad}", font=("Arial", 18), bg="#3E50B4", fg="white", command=lambda m=musteri: arac_sec_arac(m, notebook))
        musteri_button.pack()

    notebook.add(kiralama_sekme, text="Kiralama")

    notebook.pack(fill="both", expand=True)

    root.mainloop()

def kiralama_iptal_ekrani():
    iptal_ekrani = tk.Toplevel()
    iptal_ekrani.title("Kiralama İptali")
    iptal_ekrani.configure(bg="#f0f0f0")

    label = tk.Label(iptal_ekrani, text="Lütfen iptal etmek istediğiniz müşteriyi seçiniz:", font=("Arial", 14), bg="#f0f0f0")
    label.pack()

    for musteri in musteriler.values():
        musteri_button = tk.Button(iptal_ekrani, text=f"{musteri.ad} {musteri.soyad}", font=("Arial", 12), bg="#3E50B4", fg="white", command=lambda m=musteri: musteri_secildi(m, iptal_ekrani))
        musteri_button.pack()

def musteri_secildi(musteri, iptal_ekrani):
    iptal_ekrani.destroy()
    iptal_ekrani = tk.Toplevel()
    iptal_ekrani.title("Kiralama İptali")
    iptal_ekrani.configure(bg="#f0f0f0")

    label = tk.Label(iptal_ekrani, text="Lütfen iptal etmek istediğiniz aracı seçiniz:", font=("Arial", 14), bg="#f0f0f0")
    label.pack()

    arac_listesi = tk.Listbox(iptal_ekrani, width=30, height=5)
    arac_listesi.pack(padx=10, pady=5)

    for arac in araclar:
        if arac in musteri.kiralamalar:
            arac_listesi.insert(tk.END, arac.model)

    def iptal_et():
        secili_index = arac_listesi.curselection()
        if secili_index:
            secili_arac = musteri.kiralamalar[secili_index[0]]
            kiralama_iptal(musteri, secili_arac)
            mesaj_ekrani = tk.Toplevel()
            mesaj_ekrani.title("Kiralama İptali")
            mesaj_ekrani.configure(bg="#f0f0f0")
            mesaj_label = tk.Label(mesaj_ekrani, text=f"{secili_arac.model} aracının kiralama işlemi iptal edildi.", font=("Arial", 12), bg="#f0f0f0")
            mesaj_label.pack()
            iptal_ekrani.destroy()
        else:
            mesaj_ekrani = tk.Toplevel()
            mesaj_ekrani.title("Hata")
            mesaj_ekrani.configure(bg="#f0f0f0")
            mesaj_label = tk.Label(mesaj_ekrani, text="Lütfen bir araç seçin.", font=("Arial", 12), bg="#f0f0f0")
            mesaj_label.pack()

    button_iptal = tk.Button(iptal_ekrani, text="İptal Et", font=("Arial", 14), bg="#FF5733", fg="white", command=iptal_et)
    button_iptal.pack(pady=10)

def musteri_ekle(ad, soyad, telefon):
    musteri = Musteri(ad, soyad, telefon)
    musteriler[telefon] = musteri

musteri_ekle("Ahmet", "Yılmaz", "5551234567")
musteri_ekle("Zeynep", "Kara", "5339876543")

kiralama_ekrani()
