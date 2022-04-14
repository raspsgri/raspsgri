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


Project.num_changer(1)
Project.c_progress_changer(3)

project_1 = Project(0, 'tiwa')
project_2 = Project(1, 'fdsi')

project_1.o_progress_changer(43)
project_2.o_progress_changer(23)
project_1.show_availability()
project_2.show_availability()

print(project_1.full_info())
print(project_2.full_info())
print('number of projects: ', Project.num_of_projects)
