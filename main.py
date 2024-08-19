import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("MMMU")
        self.geometry("400x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)

        self.profile_selector_frame = customtkinter.CTkFrame(self, height=60)
        self.profile_selector_frame.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
        self.profile_selector_frame.grid_columnconfigure(4, weight=1)
        self.profile_selector_frame.grid_rowconfigure(0, weight=1)

        self.profile_selector = customtkinter.CTkOptionMenu(self.profile_selector_frame)
        self.profile_selector.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)


app = App()
app.mainloop()
