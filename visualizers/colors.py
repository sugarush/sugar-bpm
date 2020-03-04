from glumpy import gl

from visualizer import Visualizer


class Colors(Visualizer):

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs, count=4)
        self.quad['position'] = (-1,+1), (+1,+1), (-1,-1), (+1,-1)
        self.quad['color'] = (1,1,0,1), (1,0,0,1), (0,0,1,1), (0,1,0,1)
        self.quad['distance'] = 0.5
        self.quad['theta'] = 0
        self.method = gl.GL_TRIANGLE_STRIP

    def input(self, data, bands):
        lows = bands[0]
        self.quad['theta'] += lows * 0.0025
