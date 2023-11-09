
# -*- coding: utf-8 -*-
""" a module for a dark channel based algorithm which remove haze from pictures """

__author__ = 'Ray'

import math
import numpy as np
import cv2

class Node(object):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def print_info(self):
        print(f'{self.x}:{self.y}:{self.value}')

def get_min_channel(img):
    if len(img.shape) == 3 and img.shape[2] == 3:
        pass
    else:
        print("Bad image shape, input must be color image")
        return None

    img_gray = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
    local_min = 255

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            local_min = min(img[i, j, :])
            img_gray[i, j] = local_min

    return img_gray

def get_dark_channel(img, block_size=3):
    if len(img.shape) == 2:
        pass
    else:
        print("Bad image shape, input image must be two dimensions")
        return None

    if block_size % 2 == 0 or block_size < 3:
        print('BlockSize is not odd or too small')
        return None

    add_size = block_size // 2

    new_height = img.shape[0] + block_size - 1
    new_width = img.shape[1] + block_size - 1

    img_middle = np.pad(img, ((add_size, add_size), (add_size, add_size)), 'edge')
    img_dark = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            local_min = np.min(img_middle[i:i + block_size, j:j + block_size])
            img_dark[i, j] = local_min

    return img_dark

def get_atomspheric_light(dark_channel, img, mean_mode=False, percent=0.001):
    size = dark_channel.size
    height, width = dark_channel.shape

    nodes = [Node(i, j, dark_channel[i, j]) for i in range(height) for j in range(width)]
    nodes.sort(key=lambda node: node.value, reverse=True)

    atomspheric_light = 0

    if int(percent * size) == 0:
        atomspheric_light = np.max(img[nodes[0].x, nodes[0].y])
        return atomspheric_light

    if mean_mode:
        atomspheric_light = np.mean([img[node.x, node.y] for node in nodes[:int(percent * size)]])
        return int(atomspheric_light)

    atomspheric_light = np.max([img[node.x, node.y] for node in nodes[:int(percent * size)]])
    return atomspheric_light

def get_recover_scene(img, omega=0.95, t0=0.1, block_size=15, mean_mode=False, percent=0.001):
    img_gray = get_min_channel(img)
    img_dark = get_dark_channel(img_gray, block_size=block_size)
    atomspheric_light = get_atomspheric_light(img_dark, img, mean_mode=mean_mode, percent=percent)

    transmission = 1 - omega * img_dark / atomspheric_light
    transmission[transmission < t0] = t0

    scene_radiance = np.zeros(img.shape)
    img = img.astype('float64')
    for i in range(3):
        scene_radiance[:, :, i] = (img[:, :, i] - atomspheric_light) / transmission + atomspheric_light
        scene_radiance[:, :, i] = np.clip(scene_radiance[:, :, i], 0, 255)

    scene_radiance = scene_radiance.astype('uint8')
    return scene_radiance

def sample():
    inp = input("Please input the name of the image:")
    img = cv2.imread(f'{inp}', cv2.IMREAD_COLOR)
    scene_radiance = get_recover_scene(img)
    cv2.imshow('original', img)
    cv2.imshow('test', scene_radiance)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    sample()
