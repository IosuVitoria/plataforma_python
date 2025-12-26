import customtkinter as ctk
from utils.evaluador import evaluar
from ejercicios import nivel1, nivel2, nivel3, nivel4

niveles = {
    1: nivel1.ejercicios,
    2: nivel2.ejercicios,
    3: nivel3.ejercicios,
    4: nivel4.ejercicios
}

def ventana_ejercicios(nivel):
    ejercicios = niveles[nivel]
    indice = 0

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.title(f"Editor de Código - Nivel {nivel}")
    app.geometry("1000x650")

    top = ctk.CTkFrame(app, height=50)
    top.pack(fill="x")
    titulo = ctk.CTkLabel(
        top,
        text=f"Nivel {nivel} - Editor Python",
        font=("Arial", 18)
    )
    titulo.pack(pady=10)

    main = ctk.CTkFrame(app)
    main.pack(fill="both", expand=True, padx=10, pady=10)
    main.grid_columnconfigure(0, weight=1)
    main.grid_columnconfigure(1, weight=2)

    panel_ejercicio = ctk.CTkFrame(main)
    panel_ejercicio.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
    lbl_ejercicio = ctk.CTkLabel(
        panel_ejercicio,
        text="",
        font=("Arial", 14),
        justify="left",
        wraplength=350
    )
    lbl_ejercicio.pack(padx=10, pady=10, fill="both", expand=True)

    panel_editor = ctk.CTkFrame(main)
    panel_editor.grid(row=0, column=1, sticky="nsew", padx=(5, 0))

    lbl_editor = ctk.CTkLabel(panel_editor, text="Editor de Código", font=("Arial", 14))
    lbl_editor.pack(anchor="w", padx=10, pady=(10,0))

    editor = ctk.CTkTextbox(
        panel_editor,
        height=300,
        font=("Consolas", 14),
        text_color="#ffffff",
        fg_color="#1e1e1e",
        corner_radius=8
    )
    editor.pack(fill="both", expand=True, padx=10, pady=10)

    lbl_salida = ctk.CTkLabel(panel_editor, text="Consola de salida", font=("Arial", 13))
    lbl_salida.pack(anchor="w", padx=10)

    consola = ctk.CTkTextbox(
        panel_editor,
        height=120,
        font=("Consolas", 13),
        text_color="#00ff00",
        fg_color="#000000",
        corner_radius=8
    )
    consola.pack(fill="x", padx=10, pady=(5, 10))
    consola.configure(state="disabled")

    feedback = ctk.CTkLabel(panel_editor, text="", font=("Arial", 14))
    feedback.pack(pady=5)

    botones = ctk.CTkFrame(app)
    botones.pack(pady=10)
    
    def cargar():
        lbl_ejercicio.configure(text=ejercicios[indice]["enunciado"])
        editor.delete("1.0", "end")
        editor.insert("1.0", "# Escribe tu código aquí\n")
        consola.configure(state="normal")
        consola.delete("1.0", "end")
        consola.configure(state="disabled")
        feedback.configure(text="", text_color="white")

    def ejecutar():
        codigo = editor.get("1.0", "end")
        correcto, salida = evaluar(codigo, ejercicios[indice]["salida"])
        consola.configure(state="normal")
        consola.delete("1.0", "end")
        consola.insert("1.0", salida)
        consola.configure(state="disabled")
        if correcto:
            feedback.configure(text="✅ Correcto", text_color="green")
        else:
            feedback.configure(text="❌ Incorrecto", text_color="red")

    def siguiente():
        nonlocal indice
        if indice < len(ejercicios) -1:
            indice += 1
            cargar()

    def anterior():
        nonlocal indice
        if indice > 0:
            indice -= 1
            cargar()

    ctk.CTkButton(botones, text="⬅ Anterior", command=anterior).pack(side="left", padx=10)
    ctk.CTkButton(botones, text="▶ Ejecutar", command=ejecutar).pack(side="left", padx=10)
    ctk.CTkButton(botones, text="Siguiente ➡", command=siguiente).pack(side="left", padx=10)

    cargar()
    app.mainloop()
