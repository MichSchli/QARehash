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
parser.add_argument('--name_dictionary', type=str, help='The location of the name dictionary')
parser.add_argument('--type_dictionary', type=str, help='The location of the name dictionary')
parser.add_argument('--vertex_dictionary', type=str, help='The location of the name dictionary')
args = parser.parse_args()

vertex_index = ElementIndex(args.vertex_dictionary)
name_cache = ElementCache(args.name_dictionary)
type_cache = ElementCache(args.type_dictionary)

name_cache.index_keys(vertex_index)
type_cache.index_keys(vertex_index)