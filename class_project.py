class Project:
    progress = 1

    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.availability = 0
        self.webpage = 'https://raspsgri.com/' + name + '/'

    def full_info(self):
        return '{} {} {} {}'.format(self.index, self.name, self.availability, self.webpage)

    def show_availability(self):
        self.availability = int(self.availability * self.progress)


project_1 = Project(0, 'tiwa')
project_2 = Project(1, 'fdsi')

project_1.progress = 43
project_2.progress = 23
project_1.show_availability()
project_2.show_availability()

print(project_1.full_info())
print(project_2.full_info())
