import argparse

from graph_building.graphlet import Graphlet
from graph_indexing.graph_indexing_components.graph_name_handler import GraphNameHandler
from graph_indexing.graph_indexing_components.graph_printer import GraphPrinter
from graph_indexing.graph_indexing_components.graph_relation_counter import GraphRelationCounter
from graph_indexing.graph_indexing_components.graph_relation_filter import GraphRelationFilter
from graph_indexing.graph_indexing_components.graph_relation_indexer import GraphRelationIndexer
from graph_indexing.graph_indexing_components.graph_type_handler import GraphTypeHandler
from graph_indexing.graph_indexing_components.graph_vertex_indexer import GraphVertexIndexer
from graph_indexing.graph_iterators.graph_file_iterator import GraphFileIterator
from indexes.element_cache import ElementCache
from indexes.element_index import ElementIndex

"""
Future-proof graph indexing system
"""

parser = argparse.ArgumentParser(description='Indexes a graph')
parser.add_argument('--graph', type=str, help='The location of the graph')
parser.add_argument('--type_dictionary', type=str, help='The location of the name dictionary')
parser.add_argument('--graph_dictionary', type=str, help='The location of the name dictionary')
args = parser.parse_args()

graph_iterator = GraphFileIterator(args.graph)
type_cache = ElementCache(args.type_dictionary)

vertex_graphs = ElementCache(args.graph_dictionary + ".entities")
event_graphs = ElementCache(args.graph_dictionary + ".events")

for graph in graph_iterator.iterate():
    graph = [int(graph[0]), int(graph[1]), int(graph[2])]

    subject_type = type_cache.get(int(graph[0]))
    object_type = type_cache.get(int(graph[2]))

    if subject_type == 0:
        if object_type == 0 or object_type == 2:
            if not vertex_graphs.contains(graph[0]):
                vertex_graphs.add(graph[0], Graphlet(graph[0]))

            if not vertex_graphs.contains(graph[2]):
                vertex_graphs.add(graph[2], Graphlet(graph[2]))

            graph_0 = vertex_graphs.get(graph[0])
            graph_0.add_entity(graph[1], graph[2])
            graph_2 = vertex_graphs.get(graph[2])
            graph_2.add_entity_inverse(graph[1], graph[0])

            vertex_graphs.update(graph[0], graph_0)
            vertex_graphs.update(graph[2], graph_2)
        else:
            if not vertex_graphs.contains(graph[0]):
                vertex_graphs.add(graph[0], Graphlet(graph[0]))

            if not event_graphs.contains(graph[2]):
                event_graphs.add(graph[2], Graphlet(graph[2]))

            graph_0 = vertex_graphs.get(graph[0])
            graph_0.add_event(graph[1], graph[2])
            graph_2 = event_graphs.get(graph[2])
            graph_2.add_entity_inverse(graph[1], graph[0])

            vertex_graphs.update(graph[0], graph_0)
            event_graphs.update(graph[2], graph_2)
    elif subject_type == 1:
            if not event_graphs.contains(graph[0]):
                event_graphs.add(graph[0], Graphlet(graph[0]))

            if not vertex_graphs.contains(graph[2]):
                vertex_graphs.add(graph[2], Graphlet(graph[2]))

            graph_0 = event_graphs.get(graph[0])
            graph_0.add_entity(graph[1], graph[2])
            graph_2 = vertex_graphs.get(graph[2])
            graph_2.add_event_inverse(graph[1], graph[0])

            event_graphs.update(graph[0], graph_0)
            vertex_graphs.update(graph[2], graph_2)