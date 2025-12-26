import customtkinter as ctk
from ui.ventana_ejercicios import ventana_ejercicios

def selector_nivel():
    app = ctk.CTk()
    app.title("Selecciona Nivel")
    app.geometry("600x450")

    ctk.CTkLabel(app, text="🎄 Selecciona un nivel", font=("Arial", 22)).pack(pady=30)

    def abrir(nivel):
        app.destroy()
        ventana_ejercicios(nivel)

    niveles = {
        1: "🎁 Básico",
        2: "🎄 Intermedio",
        3: "⭐ Avanzado",
        4: "❄️ Retos"
    }

    for n, texto in niveles.items():
        ctk.CTkButton(
            app,
            text=texto,
            command=lambda n=n: abrir(n),
            width=250
        ).pack(pady=10)

    app.mainloop()
