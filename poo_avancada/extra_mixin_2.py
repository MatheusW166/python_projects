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

    def __str__(self) -> str:
        return super().__str__() + ' (MIXIN) '


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name + ' <enviado de Person> '


class Employee(DictMixin, Person):
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
print(e)
