# import argparse
# import load_data
# import graph_generator
# import graph_viewer_tk as gvt
# import matplotlib.pyplot as plt
# import mlflow
# import torch
# import torch_geometric
# import numpy as np

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--data_dir", type=str)
#     args = parser.parse_args()
#     latlon = load_data.main(args.data_dir)
#     nodes,edges = graph_generator.generate_ico_sphere(res=10.0)
#     bipartite_graph = graph_generator.generate_bipartite_graph(source=latlon, target=nodes)
#     inverse = graph_generator.invert_bipartite_graph(bipartite_graph=bipartite_graph)
#     print(bipartite_graph)
#     print(inverse)

import torch
from torch_geometric.data import Data

import mlflow

edge_index = torch.tensor([[0, 1, 1, 2],
                           [1, 0, 2, 1]], dtype=torch.long)
x = torch.tensor([[-1], [0], [1]], dtype=torch.float)

data = Data(x=x, edge_index=edge_index) 

mlflow.log_text(data.keys,'keys.txt')


mlflow.log_metric('num_nodes',data.num_nodes)
mlflow.log_metric('num_edges',data.num_edges)
mlflow.log_metric('num_node_features',data.num_node_features)

with open('outputs/my_custom_log_file.txt', 'a') as f:
    f.write(f"Data has isolated nodes {data.has_isolated_nodes()}")