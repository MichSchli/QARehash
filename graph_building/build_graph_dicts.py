import argparse

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
args = parser.parse_args()

graph_iterator = GraphFileIterator(args.graph)
type_cache = ElementCache(args.type_dictionary)

vertex_to_vertex_dicts = {}
vertex_to_event_dicts = {}
event_to_vertex_dicts = {}

for graph in graph_iterator.iterate():
    subject_type = type_cache.get(int(graph[0]))
    object_type = type_cache.get(int(graph[2]))

    if subject_type == 0:
        if object_type == 0 or object_type == 2:
            if graph[0] not in vertex_to_vertex_dicts:
                vertex_to_vertex_dicts[graph[0]] = []

            vertex_to_vertex_dicts[graph[0]].append((graph[1], graph[2]))
        else:
            if graph[0] not in vertex_to_event_dicts:
                vertex_to_event_dicts[graph[0]] = []

                vertex_to_event_dicts[graph[0]].append((graph[1], graph[2]))
    elif subject_type == 1:
            if graph[0] not in event_to_vertex_dicts:
                event_to_vertex_dicts[graph[0]] = []

                event_to_vertex_dicts[graph[0]].append((graph[1], graph[2]))

print(vertex_to_vertex_dicts)
print(vertex_to_event_dicts)
print(event_to_vertex_dicts)