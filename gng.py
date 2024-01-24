# Roya Elisa Eskandani
# 24. Januar 2024

# gng.py

"""Growing Neural Gas Algorithm."""

import numpy as np
import networkx as nx
import random

import helpers

# Configuration
import json
with open('config.json', 'r') as file:
  config = json.load(file)

image_path: str = config['image_path']
image_prefix: str = config['image_prefix']
num_images: int = config['num_images']
frames: int = config['frames']
color: np.array = np.array(config['clustercolor'])
delta_color: int = config['tolerance']
delta_weight_s1: float = config['eps_b']
delta_weight: float = config['eps_N']
delta_weight_error_q1: float = config['alpha']
delta_weight_error_q2: float = config['beta']
lifetime_generation: int = config['lambda']
max_edge_age: int = config['A_max']
fac_memory: int = config['k']


n_nodes: int = 2
i_gng: int = 0
def gng(G: nx.Graph, img: np.array, utility: bool=True) -> None:
  global i_gng, n_nodes
  # 0. Preprocessing
  # 0.1. Image
  img = helpers.convertDtypeImage(img)
  height, width, _ = img.shape

  # 0.2 Get Cluster Information
  color: np.array = np.array(config['clustercolor'])
  color_tolerance: float = config['tolerance']

  # 1. Algorithm
  # 1.1. Random Element from Cluster (Color)
  new_node: np.array = np.random.randint([0, 0], [width, height], size=(2,))
  new_node_color: np.array = img[new_node[1], new_node[0]]
  if len(new_node_color) != 3: 
    print(f'Interruption: The image does not have 3 color channels.')
    sys.exit(1)
  if color_tolerance < 0.1:
    print(f'Interruption: Color Tolerance too small.')
    sys.exit(1)
  while np.linalg.norm(new_node_color - color) > color_tolerance: 
    new_node = np.random.randint([0, 0], [width, height], size=(2,))
    new_node_color: np.array = img[new_node[1], new_node[0]]
  
  # 1.2. Find nearest neighbors s1, s2
  distances = []
  indicies = []
  for node in G.nodes():
    distances += [np.linalg.norm(new_node - G.nodes[node]['pos'])]
    indicies += [node]
  indicies = [x for _, x in sorted(zip(distances, indicies))]  
  s1, s2 = indicies[:2]

  G.nodes[s1]['utility'] += np.linalg.norm(new_node - G.nodes[s2]['pos'])**2 + np.linalg.norm(new_node - G.nodes[s1]['pos'])**2
  
  # 1.2. Add new Edge
  G.add_edge(s1, s2, weight=0.0)

  # 1.3. Update Error of s1
  G.nodes[s1]['error'] += np.linalg.norm(new_node - G.nodes[s1]['pos'])

  # 1.4. Update Positions
  G.nodes[s1]['pos'] = ((1-delta_weight_s1) * G.nodes[s1]['pos'] + delta_weight_s1*new_node).astype(np.int64)

  for neighbour in G.neighbors(s1):
    weight = np.array(np.round(delta_weight * (new_node - G.nodes[neighbour]['pos'])), dtype=np.int64)
    G.nodes[neighbour]['pos'] += weight

  # 1.8. Update Egde Ages
  for neighbour in G[s1]:
    G[s1][neighbour]['weight'] += 1
  if utility:
    for u,v in G.edges():
      G[u][v]['weight'] += 1

  # 1.9. Delete aged Egdes and isolated Nodes
  edges_copy = list(G.edges())
  for edge in edges_copy:
    u, v = edge
    if G[u][v]['weight'] > max_edge_age and G.number_of_edges() > 2:
      if G.has_edge(u, v):
        G.remove_edge(u, v)

  if G.number_of_nodes() > 2:
    isolated_nodes = list(nx.isolates(G))
    G.remove_nodes_from(isolated_nodes)

  # 1.10. Add new Node
  if not (i_gng+1) % lifetime_generation:
    n_nodes += 1
    q1 = max(G.nodes, key=lambda node: G.nodes[node]['error'])
    q2 = max(G.neighbors(q1), key=lambda node: G.nodes[node]['error'])
    pos = (G.nodes[q1]['pos'] + G.nodes[q2]['pos']) // 2
    G.add_node(n_nodes, pos=pos, error=random.random() * np.finfo(float).eps, utility=100)
    # print(f'add node: {n_nodes}, {G.nodes[n_nodes]}')
  
  # 1.11. Utility
  for node in G.nodes():
    G.nodes[node]['utility'] *= (1 - delta_weight_error_q2)

  if G.number_of_nodes() > 2:
    q_E = max(G.nodes, key=lambda node: G.nodes[node]['error'])
    q_u = max(G.nodes, key=lambda node: G.nodes[node]['utility'])
    # print(q_u, G.nodes[q_u])
    if G.nodes[q_u]['utility'] < q_E / fac_memory:
      # print(f"remove node: {q_u}, {G.nodes[q_u]}")
      G.remove_node(q_u)
      G.remove_edges_from(G.edges(q_u))

  i_gng += 1