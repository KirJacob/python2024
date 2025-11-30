# list methods
from typing import Type

lst = [1, 2, 15, -10]
print(lst)
lst.append(100)
print(lst)
lst.pop(0)
print(lst)
lst.remove(15)
print(lst)

# dunder methods
# str, repr, eq


class JobVacancy:

    def __init__(self, salary, company_name, language_and_stack, schedule):
        self.salary = salary
        self.company_name = company_name
        self.language_and_stack = language_and_stack
        self.schedule = schedule

    def __repr__(self):
        return f"JobVacancy({self.salary}, {self.company_name}, {self.language_and_stack}, {self.schedule})"

    def __eq__(self, other):
        if isinstance(other, JobVacancy):
            return self.salary == other.salary and self.company_name == other.company_name \
                   and self.language_and_stack == other.language_and_stack and self.schedule == other.schedule
        return False

    def __str__(self):
        return f"QA Automation engineer, company={self.company_name}, with tech={self.language_and_stack} " \
               f"and salary={self.salary}"


dela_sport = JobVacancy(4000, 'Delasport', 'Java', 'hybrid')
dela_sport2 = JobVacancy(4000, 'Delasport', 'Java', 'hybrid')
print(str(dela_sport))
print(dela_sport)
print(dela_sport2.__eq__(dela_sport))



















