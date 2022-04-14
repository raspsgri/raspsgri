class Project:
    num_of_projects = 0
    progress = 0

    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.availability = 1
        self.webpage = 'https://raspsgri.com/' + name + '/'
        Project.num_of_projects += 1

    def full_info(self):
        return '{} {} {} {}'.format(self.index, self.name, self.availability, self.webpage)

    def show_availability(self):
        self.availability = int(self.availability * self.progress)

    def o_progress_changer(self, amount):
        self.progress *= amount

    @classmethod
    def num_changer(cls, amount):
        cls.num_of_projects = amount

    @classmethod
    def c_progress_changer(cls, amount):
        cls.progress = amount

    @classmethod
    def creator(cls, prj_str):
        index, name = prj_str.split('_')
        return cls(index, name)

    @staticmethod
    def printer(x):
        print(x)


class Employee(Project):
    def __init__(self, first, last):
        #super().__init__(self, index, name)
        self.first = first
        self.last = last
        self.email = first + '_' + last + '@raspsgri.com'

    @classmethod
    def emp_creator(cls, emp_str):
        first, last = emp_str.split('_')
        return cls(first, last)


Project.num_changer(1)
Project.c_progress_changer(1.09)

str_one = '0_tiwa'
str_two = '1_fdsi'
str_three = 'ras_psgri'
project_1 = Project.creator(str_one)
project_2 = Project.creator(str_two)
employee_1 = Employee.emp_creator(str_three)

project_1.o_progress_changer(43)
project_2.o_progress_changer(23)
project_1.show_availability()
project_2.show_availability()

Project.printer(project_1.full_info())
Project.printer(project_2.full_info())
Project.printer(Project.num_of_projects)
print(employee_1.first)
