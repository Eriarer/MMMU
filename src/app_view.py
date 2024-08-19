# src/views/app_view.py
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class AppView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MMMU")
        self.geometry("400x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)

        # Configurar la interfaz gráfica aquí
        self.profile_selector_frame = ctk.CTkFrame(self, height=60)
        self.profile_selector_frame.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
        self.profile_selector_frame.grid_columnconfigure(0, weight=1)
        self.profile_selector_frame.grid_rowconfigure(0, weight=1)

        self.profile_selector = ctk.CTkOptionMenu(self.profile_selector_frame)
        self.profile_selector.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)

        # Otros elementos de la interfaz gráfica aquí

    def run(self):
        self.mainloop()
