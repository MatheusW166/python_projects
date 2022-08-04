from datetime import datetime, timedelta


class TarefaNaoEncontrada(Exception):
    pass


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
        try:
            return [task for task in self if task.descricao == descricao][0]
        except IndexError as e:
            raise TarefaNaoEncontrada(str(e))  # Relançando exceção

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
    try:
        casa.procurar('Trocar lençóis').concluir()
    except TarefaNaoEncontrada as e:
        print(f'A causa foi: "{str(e)}"')
    finally:
        print('Sempre executado após try ou catch')


if __name__ == '__main__':
    main()
