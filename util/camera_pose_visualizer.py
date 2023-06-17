import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class CameraPoseVisualizer:
    def __init__(self, xlim, ylim, zlim):
        # self.fig = plt.figure(figsize=(18, 7))
        # self.ax = self.fig.gca(projection='3d')
        self.fig,self.ax = plt.subplots(1,1,
                                        subplot_kw={'projection':'3d'},
                                        figsize=(18,7))
        
        self.ax.set_aspect("auto")
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)
        self.ax.set_zlim(zlim)
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_zlabel('z')
        print('initialize camera pose visualizer')

    def extrinsic2pyramid(self, P, color='r',
                          focal_len_scaled=5, aspect_ratio=0.3):

        a = aspect_ratio
        f = focal_len_scaled
        
        vertex_std = np.array([[  0,    0,0,1],
                               [f*a, -f*a,f,1],
                               [f*a,  f*a,f,1],
                               [-f*a, f*a,f,1],
                               [-f*a,-f*a,f,1]])
        
        V = vertex_std @ P.T # vertex transformed
        meshes = [[V[0,:-1], V[1][:-1], V[2,:-1]],
                  [V[0,:-1], V[2,:-1], V[3,:-1]],
                  [V[0,:-1], V[3,:-1], V[4,:-1]],
                  [V[0,:-1], V[4,:-1], V[1,:-1]],
                  [V[1,:-1], V[2,:-1], V[3,:-1], V[4,:-1]]]
        
        self.ax.add_collection3d( Poly3DCollection(meshes,
                                                   facecolors=color,
                                                   linewidths=0.3,
                                                   edgecolors=color,
                                                   alpha=0.35))

    def customize_legend(self, list_label):
        list_handle = []
        for idx, label in enumerate(list_label):
            color = plt.cm.rainbow(idx / len(list_label))
            patch = Patch(color=color, label=label)
            list_handle.append(patch)
        plt.legend(loc='right', bbox_to_anchor=(1.8, 0.5), handles=list_handle)

    def colorbar(self, max_frame_length):
        cmap = mpl.cm.rainbow
        norm = mpl.colors.Normalize(vmin=0, vmax=max_frame_length)
        self.fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
                          orientation='vertical', label='Frame Number')

    def show(self):
        plt.title('Extrinsic Parameters')
        plt.show()
