import customtkinter as ctk
from tkinter import font as tkFont

BUTTON_FONT_NAME = "Comfortaa"

class GuiApp:
    def __init__(self, master, authorize_callback, input_callback, send_callback):
        self.BUTTON_FONT = ctk.CTkFont(family=BUTTON_FONT_NAME, size=14, weight=tkFont.BOLD)
        self.authorize_callback = authorize_callback
        self.input_callback = input_callback
        self.send_callback = send_callback

        text_font = ctk.CTkFont(family="Lexend", size=14, weight=tkFont.NORMAL)

        self.master = master

        self.title = ctk.CTkLabel(master=self.master, text="Summit", font=("Impact", 24))
        self.title.grid(row=0, padx=20, pady=(40, 0))
        self.subtitle = ctk.CTkLabel(master=self.master, text="Todas as decisões da sua empresa para todos os colaboradores", font=text_font)
        self.subtitle.grid(row=1, pady=(0, 40))

        self.button = ctk.CTkButton(master=self.master, text="Autorizar", command=self._authorize, font=self.BUTTON_FONT)
        self.button.grid(row=2, padx=20)

        self.input_text = None
        self.instructions = None
        self.input_field = None
        self.svar = None

        self.master.grid_columnconfigure(0, weight=1)

    def send(self):
        if not self.input_text.get(): return

        self.instructions.destroy()
        self.input_field.destroy()
        self.send_button.destroy()

        self.svar = ctk.StringVar(value="Processando... Isso pode levar alguns minutos!")
        message = ctk.CTkLabel(master=self.master, textvariable=self.svar, wraplength=300, font=(None, 14))
        message.grid(row=2, padx=20, pady=(0, 20))

        res = self.send_callback(self.input_text.get().split(" "))
        if res:
            self.svar.set("Obrigado por utilizar o Summit! Em alguns minutos, confira os emails cadastrados!")
        else: 
            self.svar.set("Ops... algo deu errado. Por favor tente novamente mais tarde ou entre em contato com nosso desenvolvedor.")
            
    def _authorize(self):
        if self.authorize_callback():
            self.button.destroy()

            self.instructions = ctk.CTkLabel(master=self.master, text="Por favor, insira os emails que serão notificados (separados por espaço):")
            self.instructions.grid(row=2, padx=20, pady=(0, 20))

            self.input_text = ctk.StringVar()

            self.input_field = ctk.CTkEntry(master=self.master, width=400, height=20, textvariable=self.input_text)
            self.input_field.grid(row=3)

            self.send_button = ctk.CTkButton(master=self.master, text="Enviar", command=self.send, font=self.BUTTON_FONT)
            self.send_button.grid(row=4, pady=20)
        else:
            pass

    

