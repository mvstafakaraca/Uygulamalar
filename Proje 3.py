import tkinter as tk
from tkinter import messagebox

# Kullanıcı veritabanı (örneğin: kullanıcı adları ve şifreleri)
user_database = {}

# Kitap veritabanı
book_database = []

# Kullanıcının ödünç aldığı kitaplar
borrowed_books = {}

# Giriş fonksiyonu
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in user_database and user_database[username] == password:
        messagebox.showinfo("Başarılı", "Giriş Başarılı!")
        open_library(username)
    else:
        messagebox.showerror("Hata", "Geçersiz Kullanıcı Adı veya Şifre")

# Kayıt fonksiyonu
def register():
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()

    if new_username and new_password:
        if new_username not in user_database:
            user_database[new_username] = new_password
            messagebox.showinfo("Başarılı", "Kayıt Başarılı!")
        else:
            messagebox.showerror("Hata", "Bu Kullanıcı Adı Zaten Var!")
    else:
        messagebox.showerror("Hata", "Lütfen Kullanıcı Adı ve Şifre Girin")

# Kütüphane penceresini açan fonksiyon
def open_library(current_user):
    # Giriş penceresini kapat
    root.withdraw()

    # Kütüphane penceresini oluştur
    library_window = tk.Toplevel()
    library_window.title("Kütüphane Sistemi")

    # Kitapları görüntüleme düğmesi
    view_books_button = tk.Button(library_window, text="Kitapları Görüntüle", command=lambda: view_books(library_window))
    view_books_button.pack(pady=10)

    # Kitap ekleme düğmesi
    add_book_button = tk.Button(library_window, text="Kitap Ekle", command=add_book)
    add_book_button.pack(pady=10)

# Kitapları görüntüleme fonksiyonu
def view_books(library_window):
    # Kitapları görüntüleme penceresini oluştur
    view_books_window = tk.Toplevel()
    view_books_window.title("Kitaplar")

    # Kitapları listeleyen liste kutusu
    books_listbox = tk.Listbox(view_books_window)
    books_listbox.pack()

    for book in book_database:
        books_listbox.insert(tk.END, book)

    # Kitaba tıklama işlevini bağlama
    books_listbox.bind("<Double-Button-1>", lambda event: borrow_book(event, books_listbox))

    # Kütüphane penceresini kapat
    library_window.withdraw()

# Kitap ödünç alma fonksiyonu
def borrow_book(event, books_listbox):
    selected_book_index = books_listbox.curselection()
    if selected_book_index:
        selected_book = books_listbox.get(selected_book_index)
        if selected_book not in borrowed_books.values():
            borrow_window = tk.Toplevel()
            borrow_window.title("Kitap Ödünç Alma")
            
            # Kitap bilgisi etiketi
            book_info_label = tk.Label(borrow_window, text=f"Kitap Adı: {selected_book}")
            book_info_label.pack()

            # Kullanıcı adı etiketi ve giriş kutusu
            username_label = tk.Label(borrow_window, text="Kullanıcı Adı:")
            username_label.pack()
            username_entry = tk.Entry(borrow_window)
            username_entry.pack()

            # Ödünç al düğmesi
            borrow_button = tk.Button(borrow_window, text="Ödünç Al", command=lambda: borrow(selected_book, username_entry.get(), borrow_window))
            borrow_button.pack(pady=10)
        else:
            messagebox.showerror("Hata", "Bu kitap zaten ödünç alınmış.")
    else:
        messagebox.showerror("Hata", "Lütfen bir kitap seçin.")

# Kitap ödünç alma işlemi
def borrow(book_name, username, borrow_window):
    if username in user_database:
        borrowed_books[username] = book_name
        messagebox.showinfo("Başarılı", f"{book_name} adlı kitap {username} tarafından ödünç alındı.")
        borrow_window.destroy()
    else:
        messagebox.showerror("Hata", "Geçersiz kullanıcı adı.")

# Kitap ekleme fonksiyonu
def add_book():
    # Yeni kitap ekranını oluştur
    add_book_window = tk.Toplevel()
    add_book_window.title("Yeni Kitap Ekle")

    # Yeni kitap adı etiketi ve giriş kutusu
    new_book_label = tk.Label(add_book_window, text="Yeni Kitap Adı:")
    new_book_label.pack()
    new_book_entry = tk.Entry(add_book_window)
    new_book_entry.pack()

    # Kitap ekleme düğmesi
    add_button = tk.Button(add_book_window, text="Ekle", command=lambda: save_book(add_book_window, new_book_entry.get()))
    add_button.pack(pady=10)

# Kitapı veritabanına kaydetme fonksiyonu
def save_book(add_book_window, book_name):
    if book_name:
        book_database.append(book_name)
        messagebox.showinfo("Başarılı", f"{book_name} adlı kitap eklendi.")
        add_book_window.destroy()
    else:
        messagebox.showerror("Hata", "Lütfen bir kitap adı girin.")

# Tkinter penceresi oluşturma
root = tk.Tk()
root.title("Kütüphane Giriş Sistemi")

# Kullanıcı adı etiketi ve giriş kutusu
username_label = tk.Label(root, text="Kullanıcı Adı:")
username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Şifre etiketi ve giriş kutusu
password_label = tk.Label(root, text="Şifre:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Giriş düğmesi
login_button = tk.Button(root, text="Giriş Yap", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Yeni kullanıcı adı etiketi ve giriş kutusu
new_username_label = tk.Label(root, text="Yeni Kullanıcı Adı:")
new_username_label.grid(row=3, column=0, padx=10, pady=5)
new_username_entry = tk.Entry(root)
new_username_entry.grid(row=3, column=1, padx=10, pady=5)

# Yeni şifre etiketi ve giriş kutusu
new_password_label = tk.Label(root, text="Yeni Şifre:")
new_password_label.grid(row=4, column=0, padx=10, pady=5)
new_password_entry = tk.Entry(root, show="*")
new_password_entry.grid(row=4, column=1, padx=10, pady=5)

# Kayıt ol düğmesi
register_button = tk.Button(root, text="Kayıt Ol", command=register)
register_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

root.mainloop()