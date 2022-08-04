from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def __str__(self):
        return self.nome + (f' ({len(self.pendentes())} tarefa(s) pendente(s)) ')

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [task for task in self if not task.feito]

    def procurar(self, descricao):
        gen = (task for task in self if task.descricao == descricao)
        return next(gen, '** Não encontrado **')

    def get_tarefas(self):
        return '\n'.join(f'- {task}' for task in self)


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return f'{self.descricao}{" (Concluída) " if self.feito else ""}'


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa')
    casa.add('Lavar prato')
    print(casa)

    casa.procurar('Lavar prato').concluir()
    print(casa.get_tarefas())
    print(casa)


if __name__ == '__main__':
    main()
