import customtkinter as ctk

# Configuração da janela principal
ctk.set_appearance_mode("System")  # Segue o tema do sistema (Dark/Light)
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x420")
app.title("Calculadora Python")
app.resizable(False, False)

# Variável para armazenar a expressão
expressao = ""

def clicar(valor):
    global expressao
    expressao += str(valor)
    visor.configure(state="normal")
    visor.delete("0", "end")
    visor.insert("0", expressao)
    visor.configure(state="disabled")

def limpar():
    global expressao
    expressao = ""
    visor.configure(state="normal")
    visor.delete("0", "end")
    visor.insert("0", "0")
    visor.configure(state="disabled")

def calcular():
    global expressao
    try:
        # Avalia a expressão matemática de forma segura ou usando eval básico
        resultado = str(eval(expressao))
        expressao = resultado
        visor.configure(state="normal")
        visor.delete("0", "end")
        visor.insert("0", resultado)
        visor.configure(state="disabled")
    except Exception:
        visor.configure(state="normal")
        visor.delete("0", "end")
        visor.insert("0", "Erro")
        visor.configure(state="disabled")
        expressao = ""

# Visor da Calculadora
visor = ctk.CTkEntry(app, font=("Arial", 28), justify="right", height=60)
visor.pack(padx=15, pady=15, fill="x")
visor.insert("0", "0")
visor.configure(state="disabled")

# Frame para os botões
botoes_frame = ctk.CTkFrame(app, fg_color="transparent")
botoes_frame.pack(padx=15, pady=5, fill="both", expand=True)

# Configuração do Grid de Botões (4 colunas)
botoes_frame.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
botoes_frame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

botoes = [
    ('C', 0, 0), ('/', 0, 1), ('*', 0, 2), ('-', 0, 3),
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), 
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), 
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2)
]

for (texto, linha, coluna) in botoes:
    if texto == 'C':
        cmd = limpar
        cor = "#d9534f"
    elif texto == '=':
        cmd = calcular
        cor = "#5cb85c"
    else:
        cmd = lambda t=texto: clicar(t)
        cor = None
    
    # Se for o botão '=', faz ele ocupar 2 colunas
    if texto == '=':
        btn = ctk.CTkButton(botoes_frame, text=texto, font=("Arial", 18), fg_color=cor, command=cmd)
        btn.grid(row=linha, column=coluna, columnspan=2, sticky="nsew", padx=3, pady=3)
    else:
        btn = ctk.CTkButton(botoes_frame, text=texto, font=("Arial", 18), fg_color=cor, command=cmd)
        btn.grid(row=linha, column=coluna, sticky="nsew", padx=3, pady=3)

app.mainloop()