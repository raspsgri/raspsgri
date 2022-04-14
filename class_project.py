class Project:
    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.webpage = 'https://raspsgri.com/' + name + '/'


project_1 = Project(0, 'tiwa')
project_2 = Project(1, 'fdsi')

print('{} {} {}'.format(project_1.index, project_1.name, project_1.webpage))
print('{} {} {}'.format(project_2.index, project_2.name, project_2.webpage))
