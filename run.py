import math
import matplotlib.pyplot as plt
import networkx as nx
import random
import sys


GAMMA = 0.5
NUMBER_OF_NODES = 1000


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
            number_of_edges = graph.number_of_edges()
            sorted_node_degrees = sorted(
                [(node_id, graph.in_degree(node_id) / number_of_edges) for node_id in graph.nodes()],
                key=lambda x: -x[1]
            )
            sum = 0
            index = 0
            random_number = random.random()
            while sum < random_number:
                sum += sorted_node_degrees[index][1]
                index += 1
            selected_node_id = sorted_node_degrees[index][0]
            graph.add_edge(i, selected_node_id)
    print()  # newline

    degree_count = {}
    for node_id in graph.nodes():
        node_degree = graph.in_degree(node_id)
        if node_degree in degree_count:
            degree_count[node_degree] += 1
        else:
            degree_count[node_degree] = 1
    sorted_degree_count = sorted(degree_count.items(), key=lambda item: -item[0])
    x = [math.log2(max(1, item[0])) for item in sorted_degree_count]
    y = [math.log2(max(1, item[1])) for item in sorted_degree_count]
    plt.plot(x, y)
    plt.xlabel('log of degree')
    plt.ylabel('log of count')
    plt.show()


if __name__ == '__main__':
    run()
