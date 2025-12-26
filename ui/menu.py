import customtkinter as ctk
from ui.selector_nivel import selector_nivel

def menu_principal():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.title("🎄 Python Navideño")
    app.geometry("600x400")

    titulo = ctk.CTkLabel(app, text="🎄 Python Navideño", font=("Arial", 28))
    titulo.pack(pady=40)

    subtitulo = ctk.CTkLabel(
        app,
        text="Aprende programación con ejercicios festivos",
        font=("Arial", 14)
    )
    subtitulo.pack(pady=10)

    def abrir_niveles():
        app.destroy()
        selector_nivel()

    ctk.CTkButton(app, text="🎁 Empezar", command=abrir_niveles).pack(pady=20)
    ctk.CTkButton(app, text="❌ Salir", command=app.destroy).pack(pady=10)

    app.mainloop()
