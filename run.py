import math
import matplotlib.pyplot as plt
import networkx as nx
import os
import random
import sys


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
OUTPUT_PATH = os.path.join(BASE_DIR, 'out.png')
GAMMA = 0.5
NUMBER_OF_NODES = 20000


def run():
    graph = nx.DiGraph()
    graph.add_nodes_from([0, 1, 2, 3])
    graph.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])

    for i in range(4, NUMBER_OF_NODES):
        if i % 100 == 0:
            sys.stdout.write('\r[%d]' % i)
            sys.stdout.flush()

        graph.add_node(i)
        if random.random() < GAMMA:
            graph.add_edge(
                i,
                random.choice(list(range(i)))
            )
        else:
            number_of_edges = i
            random_number = random.random()
            sum = 0
            node_id = 0
            while sum / number_of_edges < random_number:
                sum += graph.in_degree(node_id)
                node_id += 1
            graph.add_edge(i, node_id)
    print()  # newline

    degree_count = {}
    for node_id in graph.nodes():
        node_degree = graph.in_degree(node_id)
        if node_degree in degree_count:
            degree_count[node_degree] += 1
        else:
            degree_count[node_degree] = 1
    sorted_degree_count = sorted(degree_count.items(), key=lambda item: -item[0])
    x = [math.log10(max(1, item[0])) for item in sorted_degree_count]
    y = [math.log10(max(1, item[1])) for item in sorted_degree_count]
    plt.plot(x, y)
    plt.xlabel('log10 of degree')
    plt.ylabel('log10 of count')
    plt.savefig(OUTPUT_PATH)


if __name__ == '__main__':
    run()
