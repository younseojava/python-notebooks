"""
1. given a list of 3-D point coordinates
2. find the volume of the minimum enclosing surface
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull

def main():
    # generate random points
    points = np.random.rand(30, 3)
    # find the convex hull
    hull = ConvexHull(points)
    # plot the points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:,0], points[:,1], points[:,2])
    # plot the convex hull
    for simplex in hull.simplices:
        ax.plot(points[simplex, 0], points[simplex, 1], points[simplex, 2], 'k-')
    plt.show()

if __name__ == '__main__':
    main()