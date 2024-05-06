import tkinter as tk

class Event:
    def __init__(self, name, description, main_characters, period):
        self.name = name
        self.description = description
        self.main_characters = main_characters
        self.period = period

    def __str__(self):
        return f"{self.name}: {self.description}\nBaş Kahramanlar: {', '.join(self.main_characters)}\nDönem: {self.period}"

class Period:
    def __init__(self, name, description, info):
        self.name = name
        self.description = description
        self.info = info

    def __str__(self):
        return f"{self.name}: {self.description}"

class Person:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class HistoryDatabaseApp:
    def __init__(self, master):
        self.master = master
        master.title("Tarihçi - Tarihi Olaylar Veritabanı")
        self.events = self.load_events()
        self.periods = self.load_periods()
        self.persons = self.load_persons()

    def load_events(self):
        events = [
            Event("I. Dünya Savaşı", "Büyük Güçler arasındaki çatışma sonucu milyonlarca insanın ölümüne yol açan ve dünya haritasını değiştiren bir savaş.", ["Çeşitli ülkelerin liderleri", "Askeri komutanlar"], "1914-1918"),
            Event("Berlin Duvarı'nın Yıkılması", "Almanya'nın yeniden birleşmesini sağlayan ve Doğu ve Batı Almanya arasındaki sınırları kaldıran olay.", ["Almanya liderleri", "Soğuk Savaş döneminin liderleri"], "1989"),
            Event("Lale Devri", "Osmanlı İmparatorluğu'nda lüks ve refahın doruk noktasına ulaştığı dönemdir. Sanat, edebiyat ve mimari alanlarında büyük ilerlemeler kaydedilmiştir.", ["Saray ve devlet görevlileri", "Lüks yaşam sürmekte olan vatandaşlar"], "1718-1730"),
            Event("Fransız Devrimi'nin Başlaması", "Fransa'da mutlakiyetçi monarşinin sona erdiği ve demokrasinin, eşitliğin ve özgürlüğün temellerinin atıldığı devrim.", ["Fransız devrimcileri", "Louis XVI"], "1789"),
            Event("İstanbul'un Fethi", "Fatih Sultan Mehmet'in Konstantinopolis'i fethetmesi, Bizans İmparatorluğu'nun sonunu getirerek Osmanlı İmparatorluğu'nun gücünü artırdı.", ["Fatih Sultan Mehmet"], "1453"),
            Event("Karlofça Antlaşması", "Osmanlı İmparatorluğu'nun Avrupa'daki toprak kayıplarını kabul ettiği antlaşma.", ["Osmanlı İmparatorluğu yetkilileri"], "1699"),
            Event("Mustafa Kemal Paşa'nın Samsun'a Çıkışı", "Mustafa Kemal Paşa'nın, Mondros Mütarekesi sonrası Türk Kurtuluş Savaşı'nı başlatmak üzere 19 Mayıs 1919'da Samsun'a çıkması.", ["Mustafa Kemal Paşa"], "1919"),
            Event("Türkiye Cumhuriyeti'nin İlanı ve Mustafa Kemal Atatürk'ün İlk Cumhurbaşkanı Seçilmesi", "Osmanlı İmparatorluğu'nun sona ermesinin ardından Türkiye Cumhuriyeti'nin ilan edilmesi ve Mustafa Kemal Atatürk'ün Türkiye Cumhuriyeti'nin ilk Cumhurbaşkanı olarak seçilmesi.", ["Mustafa Kemal Atatürk"], "1923")
        ]
        return events

    def load_persons(self):
        persons = [
            Person("Çeşitli ülkelerin liderleri", "Bu dönemde savaşan ülkelerin liderleri ve önemli politikacıları."),
            Person("Askeri komutanlar", "Bu dönemde savaşan ülkelerin askeri liderleri ve komutanları."),
            Person("Almanya liderleri", "Almanya'nın önemli politikacıları ve liderleri."),
            Person("Soğuk Savaş döneminin liderleri", "Soğuk Savaş döneminin etkili liderleri."),
            Person("Saray ve devlet görevlileri", "Osmanlı İmparatorluğu'nda saray ve devletin önemli görevlileri."),
            Person("Lüks yaşam sürmekte olan vatandaşlar", "Osmanlı İmparatorluğu'nda lüks yaşam süren vatandaşlar."),
            Person("Fransız devrimcileri", "Fransız Devrimi'nde etkili olan figürler."),
            Person("Louis XVI", "Fransız Kralı."),
            Person("Fatih Sultan Mehmet", "Osmanlı Padişahı ve İstanbul'un Fethi'nin lideri."),
            Person("Osmanlı İmparatorluğu yetkilileri", "Osmanlı İmparatorluğu'nun önemli yöneticileri."),
            Person("Mustafa Kemal Paşa", "Türk Kurtuluş Savaşı'nın lideri."),
            Person("Mustafa Kemal Atatürk", "Türkiye Cumhuriyeti'nin kurucusu ve ilk Cumhurbaşkanı.")
        ]
        return persons

    def load_periods(self):
        periods = [
            Period("1914-1918", "Birinci Dünya Savaşı dönemi", "Birinci Dünya Savaşı, 1914-1918 yılları arasında çeşitli ülkeler arasında gerçekleşen bir savaştır."),
            Period("1989", "Soğuk Savaş'ın sonu ve Berlin Duvarı'nın yıkılması dönemi", "Soğuk Savaş'ın sona erdiği ve Almanya'nın birleştiği dönem."),
            Period("1718-1730", "Osmanlı İmparatorluğu'nda Lale Devri", "Osmanlı İmparatorluğu'nda sanat ve lüksün yaygın olduğu bir dönem."),
            Period("1789", "Fransız Devrimi dönemi", "Fransa'da mutlakiyetçi monarşinin sona erdiği ve demokrasinin başladığı dönem."),
            Period("1453", "İstanbul'un Fethi dönemi", "İstanbul'un Fatih Sultan Mehmet tarafından fethedildiği dönem."),
            Period("1699", "Karlofça Antlaşması dönemi", "Osmanlı İmparatorluğu'nun Avrupa'daki toprak kayıplarının olduğu dönem."),
            Period("1919", "Mustafa Kemal Paşa'nın Samsun'a Çıkışı dönemi", "Türk Kurtuluş Savaşı'nın başladığı dönem."),
            Period("1923", "Türkiye Cumhuriyeti'nin İlanı ve Mustafa Kemal Atatürk'ün İlk Cumhurbaşkanı Seçilmesi dönemi", "Türkiye'nin cumhuriyetle yönetilmeye başlandığı ve Mustafa Kemal Atatürk'ün ilk cumhurbaşkanı seçildiği dönem.")
        ]
        return periods

    def show_main_window(self):
        main_window = tk.Toplevel(self.master)
        main_window.title("Tarihi Olaylar")

        event_label = tk.Label(main_window, text="Tarihi Olaylar", font=("Arial", 16, "bold"), fg="blue")
        event_label.pack(padx=10, pady=10)

        description_label = tk.Label(main_window, text="Bu uygulamada çeşitli tarihi olaylara ve bu olaylarla ilişkilendirilmiş kişilere ve dönemlere erişebilirsiniz.", fg="green")
        description_label.pack(padx=10, pady=10)

        continue_button = tk.Button(main_window, text="Devam", command=lambda: [main_window.destroy(), self.show_add_search_window()])
        continue_button.pack(pady=10)

    def show_add_search_window(self):
        add_search_window = tk.Toplevel(self.master)
        add_search_window.title("Olay Ekle veya Sorgula")

        back_button = tk.Button(add_search_window, text="Geri", command=lambda: [add_search_window.destroy(), self.show_main_window()])
        back_button.grid(row=0, column=0)

        add_event_button = tk.Button(add_search_window, text="Olay Ekle", command=self.add_event_window, bg="yellow")
        add_event_button.grid(row=0, column=1)

        search_event_button = tk.Button(add_search_window, text="Olay Sorgula", command=self.search_event, bg="orange")
        search_event_button.grid(row=0, column=2)

    def add_event_window(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Olay Ekle")

        event_label = tk.Label(add_window, text="Olay Adı:")
        event_label.grid(row=0, column=0)

        self.event_name_entry = tk.Entry(add_window)
        self.event_name_entry.grid(row=0, column=1)

        description_label = tk.Label(add_window, text="Açıklama:")
        description_label.grid(row=1, column=0)

        self.description_entry = tk.Entry(add_window)
        self.description_entry.grid(row=1, column=1)

        characters_label = tk.Label(add_window, text="Baş Kahramanlar (virgülle ayırın):")
        characters_label.grid(row=2, column=0)

        self.characters_entry = tk.Entry(add_window)
        self.characters_entry.grid(row=2, column=1)

        period_label = tk.Label(add_window, text="Dönem:")
        period_label.grid(row=3, column=0)

        self.period_entry = tk.Entry(add_window)
        self.period_entry.grid(row=3, column=1)

        add_button = tk.Button(add_window, text="Olayı Ekle", command=self.add_event)
        add_button.grid(row=4, column=0, columnspan=2)

    def add_event(self):
        name = self.event_name_entry.get()
        description = self.description_entry.get()
        characters = [char.strip() for char in self.characters_entry.get().split(",")]
        period = self.period_entry.get()
        new_event = Event(name, description, characters, period)
        self.events.append(new_event)
        self.event_name_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.characters_entry.delete(0, tk.END)
        self.period_entry.delete(0, tk.END)

    def search_event(self):
        search_window = tk.Toplevel(self.master)
        search_window.title("Olay Sorgula")

        back_button = tk.Button(search_window, text="Geri", command=lambda: [search_window.destroy(), self.show_add_search_window()])
        back_button.grid(row=0, column=0)

        event_options = [event.name for event in self.events]

        event_label = tk.Label(search_window, text="Tarihi Olay Seçiniz:")
        event_label.grid(row=1, column=0)

        event_var = tk.StringVar(search_window)
        event_var.set(event_options[0])

        event_menu = tk.OptionMenu(search_window, event_var, *event_options)
        event_menu.grid(row=1, column=1)

        query_label = tk.Label(search_window, text="Araştırmak istediğiniz konuyu seçiniz:")
        query_label.grid(row=2, column=0)

        query_var = tk.StringVar(search_window)
        query_var.set("Olay")

        query_menu = tk.OptionMenu(search_window, query_var, "Olay", "Şahsiyet", "Dönem")
        query_menu.grid(row=2, column=1)

        search_button = tk.Button(search_window, text="Sorgula", command=lambda: self.show_result(event_var.get(), query_var.get()))
        search_button.grid(row=3, column=0, columnspan=2)

    def show_result(self, event_title, query_type):
        result_window = tk.Toplevel(self.master)
        result_window.title("Sonuç")

        selected_event = next((event for event in self.events if event.name == event_title), None)

        if selected_event is None:
            result_label = tk.Label(result_window, text="Seçilen olay bulunamadı.")
            result_label.pack(padx=10, pady=10)
            return

        if query_type == "Olay":
            result_label = tk.Label(result_window, text=str(selected_event), wraplength=400)
            result_label.pack(padx=10, pady=10)
        elif query_type == "Şahsiyet":
            result_label = tk.Label(result_window, text="Olayın Baş Kahramanları:", font=("Arial", 12, "bold"))
            result_label.pack(padx=10, pady=5)
            for character in selected_event.main_characters:
                person_info = next((person.description for person in self.persons if person.name == character), "")
                person_label = tk.Label(result_window, text=f"{character}: {person_info}")
                person_label.pack(padx=10, pady=2)
        elif query_type == "Dönem":
            period_info = next((period.description for period in self.periods if period.name == selected_event.period), "")
            result_label = tk.Label(result_window, text=f"Olayın Dönemi: {period_info}")
            result_label.pack(padx=10, pady=10)

root = tk.Tk()
app = HistoryDatabaseApp(root)
app.show_main_window() 
root.mainloop()
