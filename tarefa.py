class Tarefa:
    def __init__(self, titulo):
        self.titulo = titulo
        self.concluida = False

    def status(self):
        return "Concluída" if self.concluida else "Pendente"
