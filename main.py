import customtkinter as ctk


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.title("Sistema Teste")
app.geometry("500x300")

mensagem = ctk.CTkLabel(
	app,
	text="Bem-vindo ao sistema teste!",
	font=ctk.CTkFont(size=24, weight="bold"),
)
mensagem.pack(expand=True)

app.mainloop()
