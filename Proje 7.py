import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sporcu Takip Uygulaması")
        self.geometry("300x200")  # Pencere boyutunu ayarla
        self.current_frame = None  # Şu anki pencereyi tutmak için
        self.completed_trainings = []  # İşaretlenen antrenmanları tutmak için liste
        self.user_info = {  # Kullanıcı bilgilerini tutmak için bir sözlük
            "Ad": "",
            "Soyad": "",
            "Yaş": "",
            "Boy": "",
            "Kilo": "",
            "Cinsiyet": "",
            "Spor Dalı": ""
        }
        self.configure(bg="white")  # Pencere arka plan rengini ayarla
        self.create_intro()

    def create_intro(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self, bg="white")
        self.current_frame.pack(pady=20)
        tk.Label(self.current_frame, text="Sporcu Takip Uygulaması", font=("Arial", 18, "bold"), fg="#1565C0", bg="white").pack(pady=10)
        tk.Button(self.current_frame, text="Devam", command=self.create_player_record, bg="#1565C0", fg="white", padx=15, pady=7).pack()

    def create_player_record(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        # Kayıt Ekranı
        self.current_frame = tk.Frame(self, bg="white")
        self.current_frame.pack(pady=20)
        
        tk.Label(self.current_frame, text="Kayıt Ekranı", font=("Arial", 14, "bold"), fg="#1565C0", bg="white").pack(pady=5)
        
        # Entry widgets
        tk.Label(self.current_frame, text="Ad:", font=("Arial", 10), fg="black", bg="white").pack()
        self.entry_name = tk.Entry(self.current_frame, font=("Arial", 10))
        self.entry_name.pack()
        
        tk.Label(self.current_frame, text="Soyad:", font=("Arial", 10), fg="black", bg="white").pack()
        self.entry_surname = tk.Entry(self.current_frame, font=("Arial", 10))
        self.entry_surname.pack()
        
        tk.Label(self.current_frame, text="Yaş:", font=("Arial", 10), fg="black", bg="white").pack()
        self.entry_age = tk.Entry(self.current_frame, font=("Arial", 10))
        self.entry_age.pack()
        
        tk.Label(self.current_frame, text="Boy:", font=("Arial", 10), fg="black", bg="white").pack()
        self.entry_height = tk.Entry(self.current_frame, font=("Arial", 10))
        self.entry_height.pack()
        
        tk.Label(self.current_frame, text="Kilo:", font=("Arial", 10), fg="black", bg="white").pack()
        self.entry_weight = tk.Entry(self.current_frame, font=("Arial", 10))
        self.entry_weight.pack()
        
        tk.Label(self.current_frame, text="Cinsiyet:", font=("Arial", 10), fg="black", bg="white").pack()
        self.gender_var = tk.StringVar(self.current_frame)
        self.gender_var.set("Erkek")  # Default value
        genders = ["Erkek", "Kadın"]
        gender_menu = tk.OptionMenu(self.current_frame, self.gender_var, *genders)
        gender_menu.config(font=("Arial", 8))
        gender_menu.pack()
        
        tk.Label(self.current_frame, text="Spor Dalı Seçimi:", font=("Arial", 10), fg="black", bg="white").pack()
        self.sport_var = tk.StringVar(self.current_frame)
        self.sport_var.set("Futbol")  # Default value
        sports = ["Futbol", "Basketbol", "Voleybol"]
        sport_menu = tk.OptionMenu(self.current_frame, self.sport_var, *sports)
        sport_menu.config(font=("Arial", 8))
        sport_menu.pack()
        
        # İlerle butonu
        tk.Button(self.current_frame, text="İlerle", command=self.update_user_info_and_create_menu, bg="#1565C0", fg="white", padx=15, pady=7).pack(pady=15)

    def update_user_info_and_create_menu(self):
        # Kullanıcı bilgilerini güncelle
        self.user_info["Ad"] = self.entry_name.get()
        self.user_info["Soyad"] = self.entry_surname.get()
        self.user_info["Yaş"] = self.entry_age.get()
        self.user_info["Boy"] = self.entry_height.get()
        self.user_info["Kilo"] = self.entry_weight.get()
        self.user_info["Cinsiyet"] = self.gender_var.get()
        self.user_info["Spor Dalı"] = self.sport_var.get()
        
        # Ana menüye ilerle
        self.create_menu()

    def create_menu(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self, bg="white")
        self.current_frame.pack(pady=20)
        tk.Label(self.current_frame, text="Ana Menü", font=("Arial", 14, "bold"), fg="#1565C0", bg="white").pack(pady=5)
        tk.Button(self.current_frame, text="Antrenman Programı", command=self.create_training, bg="#1565C0", fg="white", padx=15, pady=7).pack()
        tk.Button(self.current_frame, text="İlerlemeler", command=self.create_progress_record, bg="#1565C0", fg="white", padx=15, pady=7).pack()
        tk.Button(self.current_frame, text="Raporlarım", command=self.create_progress_report, bg="#1565C0", fg="white", padx=15, pady=7).pack()
        tk.Button(self.current_frame, text="Çıkış", command=self.quit_app, bg="#d32f2f", fg="white", padx=15, pady=7).pack()

    def create_training(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self, bg="white")
        self.current_frame.pack(pady=20)
        sport = self.sport_var.get()
        training_plan = self.get_training_plan(sport)
        tk.Label(self.current_frame, text="Antrenman Programı", font=("Arial", 14, "bold"), fg="#1565C0", bg="white").pack(pady=5)
        for training in training_plan:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.current_frame, text=training, variable=var, font=("Arial", 10), fg="black", bg="white")
            chk.pack(anchor=tk.W)
            self.completed_trainings.append((training, var))
        tk.Button(self.current_frame, text="Ana Menü", command=self.create_menu, bg="#1565C0", fg="white", padx=15, pady=7).pack()

    def create_progress_record(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self, bg="white")
        self.current_frame.pack(pady=20)
        tk.Label(self.current_frame, text="İlerlemeler", font=("Arial", 14, "bold"), fg="#1565C0", bg="white").pack(pady=5)
        selected_trainings = [training[0] for training in self.completed_trainings if training[1].get()]
        for training in selected_trainings:
            tk.Label(self.current_frame, text=training, font=("Arial", 10), fg="black", bg="white").pack(anchor=tk.W)
        tk.Button(self.current_frame, text="Ana Menü", command=self.create_menu, bg="#1565C0", fg="white", padx=15, pady=7).pack()

    def create_progress_report(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self, bg="white")
        self.current_frame.pack(pady=20)
        tk.Label(self.current_frame, text="Raporlarım", font=("Arial", 14, "bold"), fg="#1565C0", bg="white").pack(pady=5)
        for key, value in self.user_info.items():
            tk.Label(self.current_frame, text=f"{key}: {value}", font=("Arial", 10), fg="black", bg="white").pack(anchor=tk.W)
        tk.Button(self.current_frame, text="Ana Menü", command=self.create_menu, bg="#1565C0", fg="white", padx=15, pady=7).pack()

    def quit_app(self):
        self.destroy()

    def get_training_plan(self, sport):
        if sport == "Futbol":
            return [
                "Isınma (10 dk):\n5 dk hafif koşu veya yerinde koşu\n5 dk kol ve bacak esnetme",
                "Dribbling ve Pas Çalışması (15 dk):\n5 dk top sürme ve dribbling\n5 dk pas çalışması\n5 dk pas-dribbling kombinasyonları",
                "Hücum ve Savunma (20 dk):\n10 dk hücum pozisyonları\n10 dk savunma pozisyonları",
                "Koşu ve Dayanıklılık (15 dk):\n10 dk hızlı koşu\n5 dk dinlenme veya hafif koşu",
                "Bitirme ve Şut Çalışması (10 dk):\n5 dk şut çalışması\n5 dk bitirme çalışması",
                "Soğuma ve Esneme (10 dk):\n5 dk hafif tempolu yürüyüş veya koşu\n5 dk tam vücut esneme"
            ]
        elif sport == "Basketbol":
            return [
                "Isınma (10 dk):\n5 dk hafif koşu veya yerinde koşu\n5 dk kol ve bacak esnetme",
                "Temel Beceri Çalışması (20 dk):\n5 dk şut çalışması\n5 dk top sürme ve drible\n5 dk pas ve alıştırma\n5 dk savunma ve hücum pozisyonları",
                "Koşu ve Dayanıklılık (15 dk):\n10 dk hızlı koşu\n5 dk dinlenme veya hafif koşu",
                "Serbest Atış ve Bitirme (10 dk):\n5 dk serbest atış çalışması\n5 dk hücum ve bitirme çalışması",
                "Soğuma ve Esneme (10 dk):\n5 dk hafif tempolu yürüyüş veya koşu\n5 dk tam vücut esneme"
            ]
        elif sport == "Voleybol":
            return [
                "Isınma (10 dk):\n5 dk hafif koşu veya yerinde koşu\n5 dk kol ve bacak esnetme",
                "Pas ve Dribbling (15 dk):\n5 dk temel pas teknikleri\n5 dk top sürme ve dribbling\n5 dk pas-dribbling kombinasyonları",
                "Hücum ve Savunma (20 dk):\n10 dk hücum pozisyonları\n10 dk savunma pozisyonları",
                "Koşu ve Dayanıklılık (15 dk):\n10 dk hızlı koşu\n5 dk dinlenme veya hafif koşu",
                "Servis ve Karşılama (10 dk):\n5 dk servis teknikleri\n5 dk servis karşılama ve kontrol",
                "Soğuma ve Esneme (10 dk):\n5 dk hafif tempolu yürüyüş veya koşu\n5 dk tam vücut esneme"
            ]
        else:
            return []

app = Application()
app.mainloop()
