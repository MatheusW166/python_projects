from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def __str__(self):
        return self.nome + (f' ({len(self.pendentes())} tarefa(s) pendente(s)) ')

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [task for task in self if not task.feito]

    def procurar(self, descricao):
        gen = (task for task in self if task.descricao == descricao)
        return next(gen, '** Não encontrado **')

    def get_tarefas(self):
        return '\n'.join(f'- {task}' for task in self)


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        if self.feito:
            status = '(Concluída)'
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status = '(Vencida)'
            else:
                dias = (self.vencimento - datetime.now()).days
                status = f'(Vence em {dias} dias)'
        return f'{self.descricao} {status}'


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato', datetime.now() + timedelta(days=3, minutes=12))
    casa.tarefas.append(TarefaRecorrente('Trocar lençóis', datetime.now(), 7))
    casa.tarefas.append(casa.procurar('Trocar lençóis').concluir())
    print(casa)

    print(casa.get_tarefas())
    print(casa)
    casa.procurar('Lavar prato').concluir()


if __name__ == '__main__':
    main()
