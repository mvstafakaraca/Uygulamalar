import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

class Event:
    def __init__(self, event_id, name, date, location):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.location = location

class Participant:
    def __init__(self, participant_id, name, email):
        self.participant_id = participant_id
        self.name = name
        self.email = email

class Ticket:
    def __init__(self, ticket_id, event, participant, price):
        self.ticket_id = ticket_id
        self.event = event
        self.participant = participant
        self.price = price

class EventManagementApp:
    def __init__(self, master):
        self.master = master
        master.title("Etkinlik Yönetim Sistemi")
        master.configure(bg="#f0f0f0")

        self.ticket_prices = {
            "Hadise Konseri - Küçükçiftlik Park": {"Vip": 150, "Normal": 100, "Öğrenci": 80},
            "Teoman Konseri - Adana": {"Vip": 130, "Normal": 80, "Öğrenci": 60},
            "Hayko Cepkin Konseri - Beşiktaş Park": {"Vip": 180, "Normal": 120, "Öğrenci": 100},
            "Galatasaray-Sivasspor Maçı": {"Vip": 100, "Normal": 50, "Öğrenci": 40},
            "Konyaspor-Fenerbahçe Maçı": {"Vip": 120, "Normal": 60, "Öğrenci": 50},
            "Beşiktaş-Rizespor Maçı": {"Vip": 130, "Normal": 55, "Öğrenci": 45}
        }

        self.label_welcome = tk.Label(master, text="Etkinlik Yönetim Sistemine Hoşgeldiniz!", font=("Arial", 16), bg="#f0f0f0")
        self.label_welcome.pack(pady=20)
        self.button_continue = tk.Button(master, text="Devam", command=self.show_events, bg="#3c9d9b", fg="white", font=("Arial", 12))
        self.button_continue.pack()

    def show_events(self):
        self.clear_previous_widgets()

        self.label_events = tk.Label(self.master, text="Etkinlikler", font=("Arial", 14), bg="#f0f0f0")
        self.label_events.pack(pady=10)

        self.button_music = tk.Button(self.master, text="Müzik", command=self.show_music_events, bg="#3c9d9b", fg="white", font=("Arial", 12))
        self.button_music.pack()

        self.button_football = tk.Button(self.master, text="Futbol", command=self.show_football_events, bg="#3c9d9b", fg="white", font=("Arial", 12))
        self.button_football.pack()

    def show_music_events(self):
        self.clear_previous_widgets()

        self.label_music_events = tk.Label(self.master, text="Müzik Etkinlikleri", font=("Arial", 14), bg="#f0f0f0")
        self.label_music_events.pack(pady=10)

        for event_name, categories in self.ticket_prices.items():
            if "Konseri" in event_name:
                self.create_event_buttons(event_name, categories)

        self.create_back_button(self.show_events)

    def show_football_events(self):
        self.clear_previous_widgets()

        self.label_football_events = tk.Label(self.master, text="Futbol Etkinlikleri", font=("Arial", 14), bg="#f0f0f0")
        self.label_football_events.pack(pady=10)

        for event_name, categories in self.ticket_prices.items():
            if "Maçı" in event_name:
                self.create_event_buttons(event_name, categories)

        self.create_back_button(self.show_events)

    def clear_previous_widgets(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def create_back_button(self, command):
        self.button_back = tk.Button(self.master, text="Menüye Dön", command=command, bg="#3c9d9b", fg="white", font=("Arial", 12))
        self.button_back.pack()

    def create_event_buttons(self, event_name, categories):
        self.label_event = tk.Label(self.master, text=event_name, font=("Arial", 12), bg="#f0f0f0")
        self.label_event.pack(pady=5)
        for category, price in categories.items():
            button_text = f"{category} - {price} TL"
            tk.Button(self.master, text=button_text, command=lambda ev=event_name, cat=category, price=price: self.choose_ticket_count(ev, cat, price), bg="#3c9d9b", fg="white", font=("Arial", 10)).pack()

    def choose_ticket_count(self, event_name, category, price):
        while True:
            ticket_count = simpledialog.askinteger("Bilet Sayısı Seç", f"Lütfen {event_name} için {category} bilet sayısını seçin (0-4):", minvalue=0, maxvalue=4)
            if ticket_count is None:
                return  # Kullanıcı iptal etti, çıkış yap

            total_price = ticket_count * price
            messagebox.showinfo("Bilet Bilgileri", f"Toplam Fiyat: {total_price} TL")
            self.show_user_info()
            break

    def show_user_info(self):
        name = simpledialog.askstring("Kullanıcı Bilgileri", "Adınız:")
        surname = simpledialog.askstring("Kullanıcı Bilgileri", "Soyadınız:")
        while True:
            tc = simpledialog.askstring("Kullanıcı Bilgileri", "TC Kimlik Numaranız:")
            if tc is None:
                return  # Kullanıcı iptal etti, çıkış yap
            if len(tc) == 11:
                break
            else:
                messagebox.showerror("Hata", "Geçersiz TC Kimlik Numarası. Lütfen 11 haneli bir numara girin.")

        age = simpledialog.askinteger("Kullanıcı Bilgileri", "Yaşınız:")
        messagebox.showinfo("Bilgi", "Etkinlik sepetinize eklenmiştir!\nİyi Eğlenceler!")
        self.show_exit_options()

    def show_exit_options(self):
        self.exit_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.exit_frame.pack(pady=20)

        self.button_menu = tk.Button(self.exit_frame, text="Menüye Dön", command=self.show_events, bg="#3c9d9b", fg="white", font=("Arial", 12))
        self.button_menu.pack(side=tk.LEFT, padx=10)

        self.button_exit = tk.Button(self.exit_frame, text="Çıkış", command=self.master.destroy, bg="#3c9d9b", fg="white", font=("Arial", 12))
        self.button_exit.pack(side=tk.RIGHT, padx=10)

def main():
    conn = sqlite3.connect('etkinlik_yonetim.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Events (
                    event_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    date DATE NOT NULL,
                    location TEXT NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Participants (
                    participant_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Tickets (
                    ticket_id INTEGER PRIMARY KEY,
                    event_id INTEGER,
                    participant_id INTEGER,
                    price REAL,
                    FOREIGN KEY(event_id) REFERENCES Events(event_id),
                    FOREIGN KEY(participant_id) REFERENCES Participants(participant_id)
                    )''')

    conn.commit()

    root = tk.Tk()
    app = EventManagementApp(root)
    root.mainloop()

    conn.close()

if __name__ == "__main__":
    main()
