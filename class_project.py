class Project:
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.webpage = 'https://raspsgri.com/' + name + '/'

a1 = Project('fdsi',0)
print (a1.webpage)