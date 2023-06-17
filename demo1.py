import numpy as np
from util.camera_pose_visualizer import CameraPoseVisualizer

if __name__ == '__main__':
    # argument : the minimum/maximum value of x, y, z
    visualizer = CameraPoseVisualizer([-50, 50], [-50, 50], [0, 50])

    # argument : extrinsic matrix, color, scaled focal length(z-axis length of frame body of camera
    # visualizer.extrinsic2pyramid(np.eye(4), 'c', 10)

    RT = np.eye(4)

    visualizer.extrinsic2pyramid(RT, 'r', 5)

    R = np.eye(3)

    alpha = 1
    beta = 1
    gama = 1

    

    R = np.array([[3,4,2],
                  [2,1,2],
                  [3,4,2]]).T
    T = np.array([10,20,30])

    RT[:3,:3] = R
    RT[:3,-1] = T

    visualizer.extrinsic2pyramid(RT, 'c', 10)
    

    visualizer.show()
