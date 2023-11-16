import tkinter as tk
from tkinter import ttk

class SistemaCadastro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro FIFA")


        self.times = []
        self.jogadores = []
        self.tecnicos = []

        self.progress = ttk.Progressbar(self, mode="indeterminate")
        self.progress.pack(padx=40, pady=40)

        self.label = tk.Label(self, text="Carregando Cadastro FIFA", font=("Helvetica", 12))
        self.label.pack(padx=30, pady=10)

        self.protocol("WM_DELETE_WINDOW", self.fechar_tela)

        self.iniciar_carregamento()

    def fechar_tela(self):
        self.destroy()

    def iniciar_carregamento(self):
        self.progress.start(70)
        self.label.config(text="Carregando Cadastro FIFA...")
        self.after(3000, self.carregar_interface)

    def carregar_interface(self):
        self.progress.stop()
        self.progress.destroy()
        self.label.destroy()

        self.title("Cadastro de Campeonato FIFA")
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(padx=10, pady=10)


        self.tab_times = tk.Frame(self.notebook)
        self.notebook.add(self.tab_times, text="Times")
        self.criar_formulario_time()


        self.tab_jogadores = tk.Frame(self.notebook)
        self.notebook.add(self.tab_jogadores, text="Jogadores")
        self.criar_formulario_jogador()

        
        self.tab_comissao = tk.Frame(self.notebook)
        self.notebook.add(self.tab_comissao, text="Comissão Técnica")
        self.criar_formulario_comissao()

        self.notebook.pack(padx=10, pady=10)

    def criar_formulario_time(self):
        tk.Label(self.tab_times, text="Nome do Time:").grid(row=0, column=0, padx=10, pady=5)
        self.nome_time_entry = tk.Entry(self.tab_times)
        self.nome_time_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.tab_times, text="Cidade:").grid(row=1, column=0, padx=10, pady=5)
        self.cidade_entry = tk.Entry(self.tab_times)
        self.cidade_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.tab_times, text="Mascote:").grid(row=2, column=0, padx=10, pady=5)
        self.mascote_entry = tk.Entry(self.tab_times)
        self.mascote_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.tab_times, text="Cadastrar Time", command=self.cadastrar_time).grid(row=3, column=0, columnspan=2, pady=10)

    def criar_formulario_jogador(self):
        tk.Label(self.tab_jogadores, text="Nome do Jogador:").grid(row=0, column=0, padx=10, pady=5)
        self.nome_jogador_entry = tk.Entry(self.tab_jogadores)
        self.nome_jogador_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.tab_jogadores, text="Time:").grid(row=1, column=0, padx=10, pady=5)
        self.time_jogador_entry = tk.Entry(self.tab_jogadores)
        self.time_jogador_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.tab_jogadores, text="Número da Camisa:").grid(row=2, column=0, padx=10, pady=5)
        self.numero_camisa_entry = tk.Entry(self.tab_jogadores)
        self.numero_camisa_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.tab_jogadores, text="Cadastrar Jogador", command=self.cadastrar_jogador).grid(row=3, column=0, columnspan=2, pady=10)

    def criar_formulario_comissao(self):
        tk.Label(self.tab_comissao, text="Nome do Técnico:").grid(row=0, column=0, padx=10, pady=5)
        self.nome_tecnico_entry = tk.Entry(self.tab_comissao)
        self.nome_tecnico_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.tab_comissao, text="Time do Técnico:").grid(row=1, column=0, padx=10, pady=5)
        self.time_tecnico_entry = tk.Entry(self.tab_comissao)
        self.time_tecnico_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.tab_comissao, text="Esquema Tático:").grid(row=2, column=0, padx=10, pady=5)
        self.esquema_tatico_entry = tk.Entry(self.tab_comissao)
        self.esquema_tatico_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.tab_comissao, text="Cadastrar Técnico", command=self.cadastrar_tecnico).grid(row=3, column=0, columnspan=2, pady=10)

    def cadastrar_time(self):
        nome_time = self.nome_time_entry.get()
        cidade = self.cidade_entry.get()
        mascote = self.mascote_entry.get()

        if nome_time and cidade and mascote:
            time = {"Nome": nome_time, "Cidade": cidade, "Mascote": mascote}
            self.times.append(time)
            print(f"Time {nome_time} cadastrado com sucesso!")
        else:
            print("Por favor, preencha todos os campos.")

    def cadastrar_jogador(self):
        nome_jogador = self.nome_jogador_entry.get()
        time_jogador = self.time_jogador_entry.get()
        numero_camisa = self.numero_camisa_entry.get()

        if nome_jogador and time_jogador and numero_camisa:
            jogador = {"Nome": nome_jogador, "Time": time_jogador, "Número da Camisa": numero_camisa}
            self.jogadores.append(jogador)
            print(f"Jogador {nome_jogador} cadastrado com sucesso!")
        else:
            print("Por favor, preencha todos os campos.")

    def cadastrar_tecnico(self):
        nome_tecnico = self.nome_tecnico_entry.get()
        time_tecnico = self.time_tecnico_entry.get()
        esquema_tatico = self.esquema_tatico_entry.get()

        if nome_tecnico and time_tecnico and esquema_tatico:
            tecnico = {"Nome": nome_tecnico, "Time": time_tecnico, "Esquema Tático": esquema_tatico}
            self.tecnicos.append(tecnico)
            print(f"Técnico {nome_tecnico} cadastrado com sucesso!")
        else:
            print("Por favor, preencha todos os campos.")

if __name__ == "__main__":
    app = SistemaCadastro()
    app.mainloop()
