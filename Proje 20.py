import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Örnek oyuncu koleksiyonu verisi
oyuncu_koleksiyonu = [
    {"oyuncu_adi": "Ahmet", "favori_oyun": "The Legend of Zelda", "koleksiyonu": ["The Witcher 3: Wild Hunt", "Red Dead Redemption 2"]},
    {"oyuncu_adi": "Mehmet", "favori_oyun": "Red Dead Redemption 2", "koleksiyonu": ["The Legend of Zelda", "The Witcher 3: Wild Hunt"]},
    {"oyuncu_adi": "Ayşe", "favori_oyun": "The Witcher 3: Wild Hunt", "koleksiyonu": ["The Legend of Zelda", "Red Dead Redemption 2"]}
]

# Örnek oyuncu değerlendirmeleri verisi
oyuncu_değerlendirmeleri = {
    "Ahmet": ["Harika bir oyuncu!", "Favori oyunu da benim favorim."],
    "Mehmet": ["Yardımsever ve deneyimli.", "Oyun koleksiyonu mükemmel!"],
    "Ayşe": ["İyi bir takas ortağı.", "Oyun zevki benimkine benziyor."]
}

def close_all_tabs():
    # Tüm sekmeleri kapat
    tabs = tab_control.tabs()
    for tab in tabs:
        tab_control.forget(tab)

def open_collection_tab():
    close_all_tabs()
    
    # Koleksiyon sekmesini aç
    collection_tab = ttk.Frame(tab_control)
    tab_control.add(collection_tab, text="Koleksiyon")
    tab_control.pack(expand=1, fill="both")

    # Sekmenin içeriği
    collection_tree = ttk.Treeview(collection_tab, columns=("Oyuncu Adı", "Favori Oyun", "Koleksiyon"), show="headings", style="Treeview")
    collection_tree.heading("Oyuncu Adı", text="Oyuncu Adı")
    collection_tree.heading("Favori Oyun", text="Favori Oyun")
    collection_tree.heading("Koleksiyon", text="Koleksiyon")
    collection_tree.pack(expand=1, fill="both")
    
    # Stil tanımlama
    style = ttk.Style()
    style.configure("Treeview", background="#FFFF00", foreground="black", fieldbackground="#FFFF00")

    # Oyuncu koleksiyonundaki her oyunu tabloya ekle
    for oyun in oyuncu_koleksiyonu:
        collection_tree.insert("", "end", values=(oyun["oyuncu_adi"], oyun["favori_oyun"], ", ".join(oyun["koleksiyonu"])))
    
    # Yönetim metotları
    delete_button = ttk.Button(collection_tab, text="Seçilen Oyuncuyu Sil", command=lambda: delete_item(collection_tree))
    delete_button.pack(side="left", padx=10, pady=10)

def open_players_tab():
    close_all_tabs()
    
    # Oyuncular sekmesini aç
    players_tab = ttk.Frame(tab_control)
    tab_control.add(players_tab, text="Oyuncular")
    tab_control.pack(expand=1, fill="both")
    
    # Font ayarı
    label_font = ("Arial", 10)

    # Oyuncuların bilgilerini gösteren etiketler
    for oyuncu in oyuncu_koleksiyonu:
        oyuncu_adi_label = ttk.Label(players_tab, text=f"Oyuncu Adı: {oyuncu['oyuncu_adi']}", font=label_font)
        oyuncu_adi_label.pack(pady=2)
        
        favori_oyun_label = ttk.Label(players_tab, text=f"Favori Oyunu: {oyuncu['favori_oyun']}", font=label_font)
        favori_oyun_label.pack(pady=2)
        
        koleksiyon_label = ttk.Label(players_tab, text="Koleksiyonu:", font=label_font)
        koleksiyon_label.pack(pady=2)
        
        for oyun in oyuncu['koleksiyonu']:
            koleksiyon_oyun_label = ttk.Label(players_tab, text=f"- {oyun}", font=label_font)
            koleksiyon_oyun_label.pack(pady=2)
        
        separator = ttk.Separator(players_tab, orient='horizontal')
        separator.pack(fill='x', pady=5)
    
    # Oyuncu ekleme butonu
    add_player_frame = ttk.Frame(players_tab)
    add_player_frame.pack(side="bottom", pady=10)

    # Etiketler ve giriş alanları oluşturma
    name_label = ttk.Label(add_player_frame, text="Oyuncu Adı:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = ttk.Entry(add_player_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    game_label = ttk.Label(add_player_frame, text="Favori Oyun:")
    game_label.grid(row=1, column=0, padx=5, pady=5)
    game_entry = ttk.Entry(add_player_frame)
    game_entry.grid(row=1, column=1, padx=5, pady=5)

    collection_label = ttk.Label(add_player_frame, text="Koleksiyonu (virgülle ayırarak girin):")
    collection_label.grid(row=2, column=0, padx=5, pady=5)
    collection_entry = ttk.Entry(add_player_frame)
    collection_entry.grid(row=2, column=1, padx=5, pady=5)

    # Oyuncu ekleme butonu
    add_button = ttk.Button(add_player_frame, text="Oyuncu Ekle", command=lambda: add_player(
        name_entry.get(), 
        game_entry.get(), 
        collection_entry.get(),
        players_tab
    ))
    add_button.grid(row=3, columnspan=2, padx=5, pady=5)

def open_games_tab():
    close_all_tabs()
    
    # Oyunlar sekmesini aç
    games_tab = ttk.Frame(tab_control)
    tab_control.add(games_tab, text="Oyunlar")
    tab_control.pack(expand=1, fill="both")
    
    # Sekmenin içeriği
    games_tree = ttk.Treeview(games_tab, columns=("Name", "Genre", "Platform"), show="headings", style="Treeview")
    games_tree.heading("Name", text="Oyun Adı")
    games_tree.heading("Genre", text="Türü")
    games_tree.heading("Platform", text="Platformu")
    games_tree.pack(expand=1, fill="both")
    
    # Stil tanımlama
    style = ttk.Style()
    style.configure("Treeview", background="#FFFF00", foreground="black", fieldbackground="#FFFF00")
    
    # Örnek oyunları eklemek
    games_tree.insert("", "end", values=("The Legend of Zelda: Breath of the Wild", "Aksiyon-Macera", "Nintendo Switch"))
    games_tree.insert("", "end", values=("Red Dead Redemption 2", "Açık Dünya", "PlayStation 4"))
    games_tree.insert("", "end", values=("The Witcher 3: Wild Hunt", "RPG", "PC"))
    games_tree.insert("", "end", values=("God of War", "Aksiyon-Macera", "PlayStation 4"))
    games_tree.insert("", "end", values=("Animal Crossing: New Horizons", "Simülasyon", "Nintendo Switch"))
    games_tree.insert("", "end", values=("Cyberpunk 2077", "RPG", "PC"))
    
    # Yeni oyun eklemek için giriş alanları ve buton
    name_label = ttk.Label(games_tab, text="Oyun Adı:")
    name_label.pack()
    name_entry = ttk.Entry(games_tab)
    name_entry.pack()
    
    genre_label = ttk.Label(games_tab, text="Türü:")
    genre_label.pack()
    genre_entry = ttk.Entry(games_tab)
    genre_entry.pack()
    
    platform_label = ttk.Label(games_tab, text="Platformu:")
    platform_label.pack()
    platform_entry = ttk.Entry(games_tab)
    platform_entry.pack()
    
    # Eklenen oyunun bilgilerini göstermek için etiket
    game_info_label = ttk.Label(games_tab, text="")
    game_info_label.pack()
    
    add_button = ttk.Button(games_tab, text="Oyun Ekle", command=lambda: add_item(games_tree, name_entry, genre_entry, platform_entry, game_info_label))
    add_button.pack()
    
    # Oyun silme butonu
    delete_button = ttk.Button(games_tab, text="Seçilen Oyunu Sil", command=lambda: delete_item(games_tree))
    delete_button.pack()

def open_reviews_tab():
    close_all_tabs()
    
    # Değerlendirmeler sekmesini aç
    reviews_tab = ttk.Frame(tab_control)
    tab_control.add(reviews_tab, text="Değerlendirmeler")
    tab_control.pack(expand=1, fill="both")
    
    # Font ayarı
    label_font = ("Arial", 10)
    
    # Seçim menüsü için isim listesi
    names = [oyuncu['oyuncu_adi'] for oyuncu in oyuncu_koleksiyonu]
    selected_name = tk.StringVar()
    name_label = ttk.Label(reviews_tab, text="İsim:")
    name_label.pack(pady=5)
    name_menu = ttk.Combobox(reviews_tab, textvariable=selected_name, values=names)
    name_menu.pack(pady=5)
    
    # Değerlendirme girişi için giriş kutusu
    review_label = ttk.Label(reviews_tab, text="Değerlendirme:")
    review_label.pack(pady=5)
    review_entry = ttk.Entry(reviews_tab, width=50)
    review_entry.pack(pady=5)
    
    # Değerlendirme kaydetme butonu
    save_button = ttk.Button(reviews_tab, text="Değerlendirmeyi Kaydet", command=lambda: save_review(selected_name.get(), review_entry.get(), review_text))
    save_button.pack(pady=5)
    
    # Değerlendirme metni gösteren alan
    review_text = tk.Text(reviews_tab, height=10, width=50)
    review_text.pack(pady=5)

def save_review(item_name, review, review_text):
    # Burada yapılacak olan, kullanıcının girdiği değerlendirmeyi bir veri yapısında saklamak olacak.
    # Bu örnekte basitçe print ile ekrana yazdırıyoruz.
    review_text.insert(tk.END, f"{item_name} değerlendirmesi: {review}\n")

def add_item(tree, name_entry, genre_entry, platform_entry, game_info_label):
    # Kullanıcının girdiği verileri al
    item_name = name_entry.get()
    item_genre = genre_entry.get()
    item_platform = platform_entry.get()
    
    # Eğer herhangi bir alan boşsa, kullanıcıya uyarı ver
    if not (item_name and item_genre and item_platform):
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun.")
        return
    
    # Verileri tabloya ekle
    tree.insert("", "end", values=(item_name, item_genre, item_platform))
    
    # Eklenen öğenin bilgilerini etiketler altında göster
    game_info_label.config(text=f"Eklenen Öğe: {item_name} ({item_genre}, {item_platform})")
    
    # Girdi alanlarını temizle
    name_entry.delete(0, tk.END)
    genre_entry.delete(0, tk.END)
    platform_entry.delete(0, tk.END)

def delete_item(tree):
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)

def add_player(name, favorite_game, collection, players_tab):
    # Boş kutu bırakılıp bırakılmadığını kontrol et
    if not (name and favorite_game and collection):
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun.")
        return

    oyuncu_koleksiyonu.append({"oyuncu_adi": name, "favori_oyun": favorite_game, "koleksiyonu": collection})
    messagebox.showinfo("Başarılı", f"{name} adlı oyuncu başarıyla eklendi.")
    
    # Yeni eklenen oyuncunun bilgilerini oyuncular sekmesine ekleyin
    # Font ayarı
    label_font = ("Arial", 10)

    # Yeni eklenen oyuncunun bilgilerini gösteren etiketler
    oyuncu_adi_label = ttk.Label(players_tab, text=f"Oyuncu Adı: {name}", font=label_font)
    oyuncu_adi_label.pack(pady=2)

    favori_oyun_label = ttk.Label(players_tab, text=f"Favori Oyunu: {favorite_game}", font=label_font)
    favori_oyun_label.pack(pady=2)

    koleksiyon_label = ttk.Label(players_tab, text="Koleksiyonu:", font=label_font)
    koleksiyon_label.pack(pady=2)

    for oyun in collection:
        koleksiyon_oyun_label = ttk.Label(players_tab, text=f"- {oyun}", font=label_font)
        koleksiyon_oyun_label.pack(pady=2)

    separator = ttk.Separator(players_tab, orient='horizontal')
    separator.pack(fill='x', pady=5)

# Ana pencere oluşturma
root = tk.Tk()
root.title("Video Oyun Koleksiyonu Yönetimi")
root.attributes('-fullscreen', True)  # Tam ekran modu

# Stil tanımlama
style = ttk.Style()
style.theme_use('clam')  # Stil olarak 'clam' kullanılacak
style.configure('.', background='#FFD700')  # Tüm widget'lar için arka plan rengi

# Sekme kontrolü oluşturma
tab_control = ttk.Notebook(root)

# Oyunlar sekmesi butonu
games_button = ttk.Button(root, text="Oyunlar", command=open_games_tab, style='C.TButton')
games_button.pack(side="left", padx=10, pady=10)

# Oyuncular sekmesi butonu
players_button = ttk.Button(root, text="Oyuncular", command=open_players_tab, style='C.TButton')
players_button.pack(side="left", padx=10, pady=10)

# Koleksiyon sekmesi butonu
collection_button = ttk.Button(root, text="Koleksiyon", command=open_collection_tab, style='C.TButton')
collection_button.pack(side="left", padx=10, pady=10)

# Değerlendirme sekmesi butonu
reviews_button = ttk.Button(root, text="Değerlendirmeler", command=open_reviews_tab, style='C.TButton')
reviews_button.pack(side="left", padx=10, pady=10)

# Çıkış butonu
exit_button = ttk.Button(root, text="Çıkış", command=root.destroy, style='C.TButton')
exit_button.pack(side="right", padx=10, pady=10)

root.mainloop()
