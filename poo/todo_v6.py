from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def __str__(self):
        return self.nome + (f' ({len(self.pendentes())} tarefa(s) pendente(s)) ')

    # Sobrecarga do operador +=
    # projeto += tarefa
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa

        args = {**kwargs, 'vencimento': vencimento}
        funcao_escolhida(tarefa, **args)

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
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(
            self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato', datetime.now() + timedelta(days=3, minutes=12))
    casa += TarefaRecorrente('Trocar lençóis', datetime.now(), 7)
    casa.procurar('Trocar lençóis').concluir()
    print(casa.get_tarefas())


if __name__ == '__main__':
    main()
