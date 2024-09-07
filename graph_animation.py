import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def create_graph_animation():
    # Create a graph with 20 nodes
    G = nx.Graph()
    G.add_nodes_from(range(20))

    # Set up the fixed subgraph with 10 nodes
    fixed_subgraph = nx.erdos_renyi_graph(10, 0.5)
    fixed_edges = list((i, j) for (i, j) in fixed_subgraph.edges())
    G.add_edges_from(fixed_edges)

    # Custom layout function
    def custom_layout(G):
        pos = {}
        # Position fixed nodes on the left half
        for i in range(10):
            pos[i] = (random.uniform(0, 0.5), random.uniform(0, 1))
        # Position non-fixed nodes on the right half
        for i in range(10, 20):
            pos[i] = (random.uniform(0.5, 1), random.uniform(0, 1))
        return pos

    # Generate fixed positions for all nodes
    pos = custom_layout(G)

    # Function to update the graph
    def update(frame):
        # Keep the fixed edges
        edges = fixed_edges.copy()
        
        # Calculate the current edge probability
        # Start with high probability and decrease over time
        edge_prob = max(0.8 - (frame / 100) * 0.6, 0.2)
        
        # Add edges based on current probability
        for i in range(10, 20):  # Non-fixed nodes
            for j in range(20):  # Can connect to any node
                if i != j and (i, j) not in edges and (j, i) not in edges:
                    if random.random() < edge_prob:
                        edges.append((i, j))
        
        G.clear_edges()
        G.add_edges_from(edges)
        
        # Clear the current figure and draw the new graph
        plt.clf()
        nx.draw(G, pos, with_labels=True, node_color=['red']*10 + ['lightblue']*10, node_size=500, font_size=10)
        plt.title(f"Frame {frame}: Edge Probability {edge_prob:.2f}")
        
    # Create the animation
    fig, ax = plt.subplots(figsize=(12, 10))
    ani = animation.FuncAnimation(fig, update, frames=100, interval=200, repeat=True)
    
    # Save the animation
    ani.save('graph_animation.gif', writer='pillow')

create_graph_animation()