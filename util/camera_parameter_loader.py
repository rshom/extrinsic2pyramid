import json
import os
import numpy as np
import quaternion

class CameraParameterLoader:
    def __init__(self):
        print('initialize camera parameter lodaer')

    def get_intrinsic(self, path):
        with open(os.path.join(path, '_camera_settings.json'), 'r') as f:
            param_cam = json.load(f)
            param_intrinsic = param_cam['camera_settings'][0]['intrinsic_settings']
            cx = param_intrinsic['cx']
            cy = param_intrinsic['cy']
            fx = param_intrinsic['fx']
            fy = param_intrinsic['fy']
            s = param_intrinsic['s']
            mat_intrinsic = np.array([[fx, s, cx],
                                      [0, fy, cy],
                                      [0, 0, 1]])
        return mat_intrinsic

    def get_extrinsic(self, path):
        with open(path, 'r') as f:
            param_cam = json.load(f)['camera_data']
            T = param_cam['location_worldframe']
            R = param_cam['quaternion_xyzw_worldframe']

            print()
            print(R)
            print(T)

            mat_rotation = quaternion.as_rotation_matrix(
                np.quaternion(R[3], R[0], R[1], R[2]))
            mat_translation = np.array([[T[0]], [T[1]], [T[2]]])
            mat_extrinsic = np.concatenate(
                [np.concatenate([mat_rotation, mat_translation], axis=1), np.array([[0, 0, 0, 1]])], axis=0)
            
            return mat_extrinsic
