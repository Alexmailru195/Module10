class Employer:
    def Print(self):
        print("Это класс Работодатель.")

class President(Employer):
    def Print(self):
        print("Это класс Президент. Ответственен за общее руководство и стратегическое направление.")

class Manager(Employer):
    def Print(self):
        print("Это класс Менеджер. Ответственен за управление командами и повседневными операциями.")

class Worker(Employer):
    def Print(self):
        print("Это класс Рабочий. Ответственен за выполнение задач и проектов.")

employees  = [
    President(),
    Manager(),
    Worker()
]

for employee in employees:
    employee.Print()