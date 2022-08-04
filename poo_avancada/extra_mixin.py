'''
    Mixins são classes herdadas para acrescentar funcionalidades,
    sem necessariamente haver uma relação de herança entre elas.
'''

import json


class JSONMixin:
    def to_json(self):
        return json.dumps(self.to_dict())


class DictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, attributes: dict) -> dict:
        result = {}
        for key, value in attributes.items():
            result[key] = self._traverse(key, value)

        return result

    def _traverse(self, key, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        if isinstance(value, dict):
            return self._traverse_dict(value)
        if isinstance(value, list):
            return [self._traverse(key, v) for v in value]
        if hasattr(value, '__dict__'):  # hasattr serve pra métodos tbm.
            return self._traverse_dict(value.__dict__)
        return value


class Person:
    def __init__(self, name):
        self.name = name


'''
    Mixin antes.
'''


class Employee(DictMixin, JSONMixin, Person):
    def __init__(self, name, skills, dependents):
        super().__init__(name)
        self.skills = skills
        self.dependents = dependents


e = Employee(
    name='John',
    skills=['Python Programming', 'Project Management'],
    dependents={'wife': 'Jane', 'children': ['Alice', 'Bob']},
)

print(e.to_dict())
print(e.to_json())
