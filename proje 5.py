import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

class Kurs:
    def __init__(self, kurs_adi, egitmen, icerik):
        self.kurs_adi = kurs_adi
        self.egitmen = egitmen
        self.icerik = icerik

class Egitmen:
    def __init__(self, isim, uzmanlik):
        self.isim = isim
        self.uzmanlik = uzmanlik

class Ogrenci:
    def __init__(self, isim, email, sifre, secilen_ogretmen):
        self.isim = isim
        self.email = email
        self.sifre = sifre
        self.secilen_ogretmen = secilen_ogretmen

class Uygulama:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Online Eğitim Platformu")

        self.kayitli_ogrenciler = []  
        self.kurslar = {
            "Ümit Özdağ - Milli Güvenlik": Kurs("Ümit Özdağ - Milli Güvenlik", "Ümit Özdağ", 
                                                 "Milli güvenlik, ulus milletin, vatan topraklarının, deniz kıta sahanlığının, millî kurumlar, değerler ve çıkarların tüm askeri, siyasi, diplomatik ve ekonomik imkânlar kullanılarak iç ve dış tehditlerden korunumunu ifade eden genel bir topyekûn savunma ve tehdit önleme kavramıdır. Kararlı ve istikrarlı bir anayurt güvenliği sağlanabilmesi için birçok ülke tarafından uygulanan genel stratejiler arasında."),
            "Efloud - Price Action": Kurs("Efloud - Price Action", "Efloud", 
                                           "Price Action Stratejisi Nedir, Nasıl Uygulanır?\n\n"
                                           "Price Action stratejisi, karmaşık göstergeler veya osilatörler kullanmadan sadece fiyat grafiğini inceleyerek uygulanır. "
                                           "Price Action stratejisinin uygulanmasında şu adımlar takip edilir:\n\n"
                                           "- Destek ve Direnç Seviyelerini Belirleme: Bu seviyeler, fiyatın tarihsel olarak zorlandığı veya geri çekildiği bölgelerdir. Yatırımcılar, bu seviyelere yaklaştığında fiyatın tepki vereceğini beklerler.\n"
                                           "- Trendin Belirlenmesi: Price Action yatırımcıları genellikle ‘trend dostunuzdur’ ilkesini benimserler. Fiyat hareketinin genel yönü belirlenir ve ticaret bu yöne doğru yapılır.\n"
                                           "- Fiyat Formasyonlarını ve Modellerini Tanıma: Fiyat hareketleri içinde belirginleşen bazı formasyonlar (örneğin, çift tepe, çift dip, bayrak ve flama formasyonları) gelecekteki hareketleri tahmin etmek için kullanılır.\n"
                                           "- Giriş ve Çıkış Noktalarını Belirleme: Destek, direnç ve fiyat formasyonlarına dayanarak, ticarete ne zaman girilip çıkılacağına karar verilir.\n"
                                           "- Risk Yönetimi ve Pozisyon Boyutlandırma: Her ticarette, ne kadar risk alınacağını ve pozisyon boyutunun ne olacağını belirlemek kritiktir. "
                                           "Price Action stratejisi uygularken, potansiyel zararın sınırlanması için durdurma emirleri (stop-loss) sıklıkla kullanılır.\n\n"
                                           "Price Action stratejisi, tecrübe ve pratik gerektiren bir yaklaşımdır. Başarılı olabilmek için, yatırımcının piyasa hareketlerini dikkatlice gözlemleyerek ve analiz ederek sürekli olarak öğrenmesi ve kendini geliştirmesi gerekir."),
            "Marcus Aurelius - Felsefe": Kurs("Marcus Aurelius - Felsefe", "Marcus Aurelius", 
                                              "Genellikle “Filozof Kral” olarak anılan Marcus Aurelius, M.S. 2. yüzyılda Roma İmparatorluğu’nu yönetiyordu. "
                                              "Ancak mirası siyasi başarılarının çok ötesine uzanıyor. Marcus Aurelius’u gerçekten istisnai kılan şey, insan deneyimine dair derin anlayışı ve yazıları aracılığıyla ebedi bilgeliği aktarma yeteneğidir. "
                                              "Şimdi işimize bakalım. Neden Marcus Aurelius konusunda bu kadar heyecanlıyım?\n\n"
                                              "Her şey onun “Meditasyonlar” olarak bilinen hayranlık uyandıran düşünce ve yansıma koleksiyonuna indirgeniyor. Bilge bir imparatorun ruhunu döktüğü ve hayata, mutluluğa ve insan varoluşumuzun özüne dair samimi düşüncelerini paylaştığı gizli bir bilgelik hazinesine rastladığınızı hayal edin.\n\n"
                                              "Bu mücevheri ilk keşfettiğimde hayatımı bu kadar derinden etkileyeceğine dair hiçbir fikrim yoktu. Ama şunu söyleyeyim, internetin uçsuz bucaksız çölünde gizli bir vahaya rastlamak gibiydi. "
                                              "Marcus Aurelius’un Stoacı felsefesi varlığımın derinliklerinde bir etki yarattı.")
        }

        self.isim_etiket = tk.Label(pencere, text="İsim:", font=("Arial", 12))
        self.isim_etiket.grid(row=0, column=0)

        self.isim_giris = tk.Entry(pencere, font=("Arial", 12))
        self.isim_giris.grid(row=0, column=1)

        self.eposta_etiket = tk.Label(pencere, text="E-posta:", font=("Arial", 12))
        self.eposta_etiket.grid(row=1, column=0)

        self.eposta_giris = tk.Entry(pencere, font=("Arial", 12))
        self.eposta_giris.grid(row=1, column=1)

        self.sifre_etiket = tk.Label(pencere, text="Şifre:", font=("Arial", 12))
        self.sifre_etiket.grid(row=2, column=0)

        self.sifre_giris = tk.Entry(pencere, show="*", font=("Arial", 12))
        self.sifre_giris.grid(row=2, column=1)

        self.ogretmenler = ["Ümit Özdağ - Milli Güvenlik", "Efloud - Price Action", "Marcus Aurelius - Felsefe"]
        self.secilen_ogretmen = tk.StringVar(pencere)
        self.secilen_ogretmen.set(self.ogretmenler[0]) 

        self.ogretmen_etiket = tk.Label(pencere, text="Öğretmen ve Ders Seçimi:", font=("Arial", 12))
        self.ogretmen_etiket.grid(row=3, column=0)

        self.ogretmen_secim = tk.OptionMenu(pencere, self.secilen_ogretmen, *self.ogretmenler)
        self.ogretmen_secim.grid(row=3, column=1)

        self.giris_buton = tk.Button(pencere, text="Giriş Yap", command=self.giris_yap, font=("Arial", 12))
        self.giris_buton.grid(row=4, column=0)

        self.kayit_ol_buton = tk.Button(pencere, text="Kayıt Ol", command=self.kayit_ol, font=("Arial", 12))
        self.kayit_ol_buton.grid(row=4, column=1)

    def giris_yap(self):
        eposta = self.eposta_giris.get()
        sifre = self.sifre_giris.get()

        for ogrenci in self.kayitli_ogrenciler:
            if ogrenci.email == eposta and ogrenci.sifre == sifre:
                self.giris_yapildi(ogrenci)
                return

        messagebox.showerror("Hata", "E-posta veya şifre hatalı!")

    def kayit_ol(self):
        isim = self.isim_giris.get()
        eposta = self.eposta_giris.get()
        sifre = self.sifre_giris.get()
        secilen_ogretmen = self.secilen_ogretmen.get()

        for ogrenci in self.kayitli_ogrenciler:
            if ogrenci.email == eposta:
                messagebox.showerror("Hata", "Bu e-posta adresiyle daha önce kayıt yapılmış!")
                return

        self.kayitli_ogrenciler.append(Ogrenci(isim, eposta, sifre, secilen_ogretmen))
        messagebox.showinfo("Başarılı", "Kayıt işlemi başarılı!")

    def giris_yapildi(self, ogrenci):
        messagebox.showinfo("Hoş Geldiniz", f"Hoş geldiniz, {ogrenci.isim}!")

        ders_icerik = self.kurslar[ogrenci.secilen_ogretmen].icerik
        self.ders_icerik_penceresi = tk.Toplevel(self.pencere)
        self.ders_icerik_penceresi.title("Ders İçeriği")

        ders_icerik_text = ScrolledText(self.ders_icerik_penceresi, width=60, height=20, font=("Arial", 12))
        ders_icerik_text.insert(tk.END, ders_icerik)
        ders_icerik_text.pack()

if __name__ == "__main__":
    pencere = tk.Tk()
    uygulama = Uygulama(pencere)
    pencere.mainloop()
