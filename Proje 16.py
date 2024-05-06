import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Kullanıcıları saklamak için bir sözlük oluştur
users = {}

# Film ve içerik örnekleri
films = {
    "Avatar": {"Yönetmen": "James Cameron", "Tür": "Bilim Kurgu"},
    "The Matrix": {"Yönetmen": "Wachowski Kardeşler", "Tür": "Aksiyon, Bilim Kurgu"},
    "Inception": {"Yönetmen": "Christopher Nolan", "Tür": "Bilim Kurgu, Gerilim"},
    "Interstellar": {"Yönetmen": "Christopher Nolan", "Tür": "Bilim Kurgu, Drama"},
    "The Dark Knight": {"Yönetmen": "Christopher Nolan", "Tür": "Aksiyon, Suç, Drama"},
    "Pulp Fiction": {"Yönetmen": "Quentin Tarantino", "Tür": "Suç, Drama"},
}

contents = {
    "The Crown": {"Süre": "60 dakika", "Tür": "Drama"},
    "Breaking Bad": {"Süre": "45-55 dakika", "Tür": "Suç, Drama"},
    "Friends": {"Süre": "20-25 dakika", "Tür": "Komedi"},
    "Stranger Things": {"Süre": "42-62 dakika", "Tür": "Bilim Kurgu, Korku"},
    "Game of Thrones": {"Süre": "50-82 dakika", "Tür": "Drama, Fantezi"},
}

# Örnek izleme geçmişi verisi
history_data = [
    "Avatar izlendi",
    "The Crown izlendi",
    "Friends izlendi"
]

def register():
    username = entry_username_register.get()
    password = entry_password_register.get()
    
    # Kullanıcı adının zaten kullanılmadığından emin ol
    if username in users:
        messagebox.showerror("Hata", "Bu kullanıcı adı zaten alınmış.")
    elif len(password) < 6:
        messagebox.showerror("Hata", "Şifre en az 6 karakter içermelidir.")
    else:
        users[username] = password
        messagebox.showinfo("Başarılı", "Kayıt başarılı.")
        # Giriş kutularını temizle
        entry_username_register.delete(0, tk.END)
        entry_password_register.delete(0, tk.END)

def login():
    username = entry_username_login.get()
    password = entry_password_login.get()
    
    # Kullanıcı adı ve şifre doğru mu kontrol et
    if username in users and users[username] == password:
        messagebox.showinfo("Başarılı", "Giriş başarılı. Hoş geldiniz, {}".format(username))
        # Giriş kutularını temizle
        entry_username_login.delete(0, tk.END)
        entry_password_login.delete(0, tk.END)
        # Giriş penceresini gizle
        root.withdraw()
        # Yeni pencere oluştur ve Film ve Dizi İzleme Servisi adını ver
        open_movie_service()
    else:
        messagebox.showerror("Hata", "Hatalı kullanıcı adı veya şifre.")

def open_movie_service():
    # Yeni pencere oluştur
    movie_window = tk.Toplevel(root)
    movie_window.title("Film ve Dizi İzleme Servisi")
    movie_window.geometry("600x400")  # Pencere boyutunu ayarla

    # Butonları ekleyelim
    button1 = tk.Button(movie_window, text="Filmler", command=lambda: show_content(movie_window, films, "Filmler"), bg="skyblue", fg="white", font=("Arial", 12, "bold"))
    button1.pack(pady=5)
    
    button2 = tk.Button(movie_window, text="İçerikler", command=lambda: show_content(movie_window, contents, "İçerikler"), bg="orange", fg="white", font=("Arial", 12, "bold"))
    button2.pack(pady=5)

    button3 = tk.Button(movie_window, text="İzleme Geçmişi", command=view_history, bg="green", fg="white", font=("Arial", 12, "bold"))
    button3.pack(pady=5)

    button4 = tk.Button(movie_window, text="Film Ekle", command=add_movie, bg="purple", fg="white", font=("Arial", 12, "bold"))
    button4.pack(pady=5)

    button_exit = tk.Button(movie_window, text="Çıkış", command=root.destroy, bg="red", fg="white", font=("Arial", 12, "bold"))
    button_exit.pack(pady=5)

def show_content(window, content_dict, content_type):
    # Yeni pencere oluştur
    content_window = tk.Toplevel(window)
    content_window.title(content_type)  # Sekme başlığını içerik türü olarak ayarla

    for title, info in content_dict.items():
        # İçeriği tanımla
        if content_type == "Filmler":
            label_title = ttk.Label(content_window, text="Film Adı: {}".format(title), font=("Arial", 10, "bold"))
        else:
            label_title = ttk.Label(content_window, text="İçerik Adı: {}".format(title), font=("Arial", 10, "bold"))
        label_title.pack(padx=20, pady=5)

        for key, value in info.items():
            label_info = ttk.Label(content_window, text="{}: {}".format(key, value), font=("Arial", 10))
            label_info.pack(padx=20, pady=5)

        # İçeriği izle butonu
        if content_type == "İçerikler":  # Sadece İçerikler sekmesinde göster
            button_watch = tk.Button(content_window, text="İçerik İzle", command=lambda t=title: watch_content(content_window, content_type[:-1], t), bg="blue", fg="white", font=("Arial", 10, "bold"))
            button_watch.pack(pady=5)

def watch_content(window, content_type, title):
    # İzleme geçmişine içeriği ekle
    history_data.append("{} izlendi".format(title))

    # Kullanıcıya izlendiğini bildir
    messagebox.showinfo("İçerik İzle", "{} adlı {} izleniyor...".format(title, content_type))

def view_history():
    # İzleme geçmişi penceresini oluştur
    history_window = tk.Toplevel(root)
    history_window.title("İzleme Geçmişi")
    history_window.geometry("400x300")  # Pencere boyutunu ayarla
    history_window.protocol("WM_DELETE_WINDOW", lambda: show_root(history_window))

    # İzleme geçmişi verisini göster
    for i, data in enumerate(history_data, start=1):
        label = tk.Label(history_window, text="{}. {}".format(i, data), font=("Arial", 10))
        label.pack(padx=20, pady=5)

def show_root(window):
    # İzleme geçmişi penceresi yerine ana pencereyi göster
    window.destroy()

def add_movie():
    # Yeni pencere oluştur
    add_movie_window = tk.Toplevel(root)
    add_movie_window.title("Film Ekle")

    # Film adı giriş kutusu
    label_movie_name = tk.Label(add_movie_window, text="Film Adı:", font=("Arial", 10))
    label_movie_name.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_movie_name = tk.Entry(add_movie_window)
    entry_movie_name.grid(row=0, column=1, padx=5, pady=5)

    # Yönetmen giriş kutusu
    label_director = tk.Label(add_movie_window, text="Yönetmen:", font=("Arial", 10))
    label_director.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_director = tk.Entry(add_movie_window)
    entry_director.grid(row=1, column=1, padx=5, pady=5)

    # Tür giriş kutusu
    label_genre = tk.Label(add_movie_window, text="Tür:", font=("Arial", 10))
    label_genre.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_genre = tk.Entry(add_movie_window)
    entry_genre.grid(row=2, column=1, padx=5, pady=5)

    # Kaydet butonu
    button_save = tk.Button(add_movie_window, text="Film Ekle", command=lambda: save_movie(add_movie_window, entry_movie_name.get(), entry_director.get(), entry_genre.get()), bg="green", fg="white", font=("Arial", 10, "bold"))
    button_save.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

def save_movie(window, name, director, genre):
    if name.strip() == "" or director.strip() == "" or genre.strip() == "":
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")
    else:
        films[name] = {"Yönetmen": director, "Tür": genre}
        messagebox.showinfo("Başarılı", "{} filmi başarıyla eklendi.".format(name))
        window.destroy()
        update_movie_tab()

def update_movie_tab():
    # Önce var olan içeriği temizleyelim
    for widget in frame_films.winfo_children():
        widget.destroy()

    # Şimdi güncel filmleri gösterelim
    for title, info in films.items():
        label_title = ttk.Label(frame_films, text="Film Adı: {}".format(title), font=("Arial", 10, "bold"))
        label_title.pack(padx=20, pady=5)

        label_director = ttk.Label(frame_films, text="Yönetmen: {}".format(info["Yönetmen"]), font=("Arial", 10))
        label_director.pack(padx=20, pady=5)

        label_genre = ttk.Label(frame_films, text="Tür: {}".format(info["Tür"]), font=("Arial", 10))
        label_genre.pack(padx=20, pady=5)

# Ana pencere oluştur
root = tk.Tk()
root.title("Kullanıcı Girişi")
root.configure(bg="white")

# film çerçevesi
frame_films = tk.LabelFrame(root, text="Filmler", bg="white")

# Kayıt ol etiket ve giriş kutusu
frame_register = tk.LabelFrame(root, text="Kayıt Ol", padx=10, pady=10, bg="white")
frame_register.grid(row=0, column=0, padx=10, pady=10)

label_username_register = tk.Label(frame_register, text="Kullanıcı Adı:", bg="white", font=("Arial", 10))
label_username_register.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_username_register = tk.Entry(frame_register)
entry_username_register.grid(row=0, column=1, padx=5, pady=5)

label_password_register = tk.Label(frame_register, text="Şifre:", bg="white", font=("Arial", 10))
label_password_register.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_password_register = tk.Entry(frame_register, show="*")
entry_password_register.grid(row=1, column=1, padx=5, pady=5)

button_register = tk.Button(frame_register, text="Kayıt Ol", command=register, bg="green", fg="white", font=("Arial", 10, "bold"))
button_register.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Giriş yap etiket ve giriş kutusu
frame_login = tk.LabelFrame(root, text="Giriş Yap", padx=10, pady=10, bg="white")
frame_login.grid(row=0, column=1, padx=10, pady=10)

label_username_login = tk.Label(frame_login, text="Kullanıcı Adı:", bg="white", font=("Arial", 10))
label_username_login.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_username_login = tk.Entry(frame_login)
entry_username_login.grid(row=0, column=1, padx=5, pady=5)

label_password_login = tk.Label(frame_login, text="Şifre:", bg="white", font=("Arial", 10))
label_password_login.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_password_login = tk.Entry(frame_login, show="*")
entry_password_login.grid(row=1, column=1, padx=5, pady=5)

button_login = tk.Button(frame_login, text="Giriş Yap", command=login, bg="blue", fg="white", font=("Arial", 10, "bold"))
button_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Ana döngüyü başlat
root.mainloop()
