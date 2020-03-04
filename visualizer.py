from glumpy import gloo


class Visualizer(object):

    def __init__(self, count):
        self.fragment = f'./library/fragment/{self.__class__.__name__.lower()}.frag'
        self.vertex = f'./library/vertex/{self.__class__.__name__.lower()}.frag'
        self.quad = gloo.Program(self.vertex, self.fragment, count=count)
