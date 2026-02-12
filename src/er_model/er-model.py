import networkx as nx
import matplotlib.pyplot as plt

for i in range(10):
    G = nx.erdos_renyi_graph(10, 0.08)

    plt.figure(figsize=(4, 4))   
    nx.draw(G, with_labels=True)

    plt.savefig(f"graph{i}.png", dpi=300, bbox_inches="tight")
    plt.close()                  
