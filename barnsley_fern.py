#!/usr/bin/env python
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as ani

class Fractal:

    # Constructor Arguments
    # tforms : array<Transform>
    # probs  : array<Float [0, 1]> 
    
    def __init__(self, tforms, probs):

        self.transforms = {}
        self.current_pt = np.array([0.0, 0.0])
        
        it = 0
        for tr, pr in zip(tforms, probs):
            key = tuple([it, pr + it])
            self.transforms[key] = tr
            it += pr

    def calc_next(self):
        r_num = random.random()
        for pr, tr in self.transforms.items():
            if pr[0] <= r_num and pr[1] > r_num:
                self.current_pt = tr.apply(self.current_pt)
                break
        
        return self.current_pt

# Affine Transformation
class Transform:

    # Constructor Arguments
    # A_ : Numpy array <Float>
    # b_ : Numpy array <Float>
    # len(A_) must equal len(b_)

    def __init__(self, A_, b_):
        
        self.A = A_
        self.b = b_

    def apply(self, vect):
        return self.A.dot(vect) + self.b

class Plotter:

    def __init__(self, func_, interval=1):
        self.x_data = []
        self.y_data = []
        self.func = func_
        self.fig, self.ax = plt.subplots()
        self.ani = ani.FuncAnimation(self.fig, self.update, 
                                     init_func=self.setup, 
                                     interval=interval, 
                                     blit=True)
    
    def update(self, frame):
        new_value = self.func()
        self.x_data.append(new_value[0])
        self.y_data.append(new_value[1])
        self.plot.set_offsets(list(zip(self.x_data, self.y_data)))
        return self.plot,

    def setup(self):
        self.plot = self.ax.scatter(self.x_data, self.y_data, 
                                    marker='o', s=0.1, c='green',
                                    animated=True)
        self.ax.axis([-2.5, 3.5, -1, 11])
        self.ax.axis('off')
        return self.plot,

    def show(self):
        plt.show()

def main():
    
    # Stem
    f1 = Transform(np.array([[0.00, 0.00], 
                             [0.00, 0.16]]),
                   np.array([0.00, 0.00]))

    # Decreasing leaflet size
    f2 = Transform(np.array([[ 0.85, 0.04],
                             [-0.04, 0.85]]),
                   np.array([0.00, 1.60]))

    # Left Leaflet
    f3 = Transform(np.array([[0.20, -0.26],
                             [0.23,  0.22]]),
                   np.array([0.00, 1.60]))

    # Right Leaflet
    f4 = Transform(np.array([[-0.15, 0.28],
                            [  0.26, 0.24]]),
                   np.array([0.00, 0.44]))
    
    transforms    = [f1,   f2,   f3,   f4  ]
    probabilities = [0.01, 0.85, 0.07, 0.07]
    
    fern = Fractal(transforms, probabilities)

    plotter = Plotter(fern.calc_next)
    plotter.show()    

if __name__ == "__main__":
    main()
