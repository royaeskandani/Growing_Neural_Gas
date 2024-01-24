# Roya Elisa Eskandani
# 24. Januar 2024

# main.py

"""Programm"""
'! Only for uint8 or float32 '

''' Checklist
  - Static and Dynamic
  1. Configuration
  2. Graph (networkx)
  3. Animation
'''
'''TODO
  - Variability of the initial graph
    - n nodes
    - max n*(n-1)/2 edges
'''

import os
from typing import List
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

import helpers
from gng import gng

# Configuration
import json
with open('config.json', 'r') as file:
  config = json.load(file)

eps_b: float = config['eps_b']
eps_N: float = config['eps_N']
alpha: float = config['alpha']
beta: float = config['beta']
lambd: int = config['lambda']
A_max: int = config['A_max']


i_img: int = 0
def update(frame):
  global i_img
  if (frame) % 100 == frame-1: print(f'frame: {frame}')
  img: np.ndarray = plt.imread(f'{images[i_img]}')
  i_img = (i_img+1) % n if frame % steps_per_image_load == 0 else i_img # animation repeatable

  ax.clear()
  ax.imshow(img)
  
  gng(G, img, utility)
  options = {
    'node_color': 'black',
    'node_size': 10,
    'width': 1, 
    'with_labels': False }
  pos = nx.get_node_attributes(G, 'pos')
  nx.draw(G, pos, **options)

  plt.xlim(0, width)
  plt.ylim(0, height)
  if utility:
    plt.title('Growing Neural Gas with Utility')
  else:
    plt.title('Growing Neural Gas')
  additional_info = f"eps_b: {eps_b} eps_N: {eps_N}, alpha: {alpha}, beta: {beta}, lambda: {lambd}, A_max: {A_max}"
  plt.text(0.5, -0.1, additional_info, ha='center', va='center', transform=ax.transAxes)
  ax.invert_yaxis()

  return ()


if __name__ == '__main__':
  # 0. Preprocessing
  # 0.1. Get Animation Information
  frames: int = config['frames']
  frames_per_ms: int = config['frames_per_ms']
  steps_per_image_load: int = config['steps_per_image_load']

  # 0.2. Load Images
  dic: str = config['image_path']
  prefix: str = config['image_prefix']
  n: int = config['num_images']
  utility: bool = True

  images: List[str] = helpers.loadImages(dic, prefix)
  height, width, _ = plt.imread(images[0]).shape


  # 1. Initialization Graph: 2 Nodes, 1 Edge
  n_nodes: int = 2
  G: nx.Graph = nx.Graph()
  for i in range(n_nodes):
    pos: np.array = np.random.randint([0, 0], [width-1, height-1], size=(2,))
    G.add_node(i, pos=pos, error=random.random(), utility=100)

  G.add_edge(0, 1, weight=0.0)


  # 2. Animation
  fig, ax = plt.subplots()
  ani = FuncAnimation(fig, update, frames=frames, interval=frames_per_ms, repeat=True)

  if prefix.endswith('_'):
    ani.save(f'{prefix[:-1]}.mp4', writer='ffmpeg', fps=100, dpi=300)
    print(G)
  else:
    ani.save(f'{prefix}.mp4', writer='ffmpeg', fps=200, dpi=300)
    plt.show()
    print(G), print(f'Number of connected components: {nx.number_connected_components(G)}')