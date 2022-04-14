class Project:
    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.webpage = 'https://raspsgri.com/' + name + '/'

    def full_info(self):
        return '{} {} {}'.format(self.index, self.name, self.webpage)


project_1 = Project(0, 'tiwa')
project_2 = Project(1, 'fdsi')

print(project_1.full_info())
print(project_2.full_info())
