import argparse

from auxilliaries.settings_reader import SettingsReader
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
import sys

"""
Future-proof graph indexing system
"""

parser = argparse.ArgumentParser(description='Indexes a graph')
parser.add_argument('--graph', type=str, help='The location of the graph')
parser.add_argument('--preprocessor_settings', type=str, help='Settings file for preprocessor')
args = parser.parse_args()

settings_reader = SettingsReader()
settings = settings_reader.read(args.preprocessor_settings)

name_cache = settings["cache_locations"]["name_cache"]
name_relation = settings["other"]["name_relation"]
relation_index_location = settings["cache_locations"]["relation_index"]
vertex_index_location = settings["cache_locations"]["vertex_index"]
vertex_type_cache = settings["cache_locations"]["vertex_type_cache"]

discarded_name_file = settings["filters"]["names"]
discarded_relation_file = settings["filters"]["relations"]

graph_processor = GraphPrinter()
relation_index = ElementIndex(relation_index_location)
graph_processor = GraphRelationIndexer(graph_processor, relation_index)
graph_processor = GraphRelationCounter(graph_processor)

vertex_index = ElementIndex(vertex_index_location)
graph_processor = GraphVertexIndexer(graph_processor, vertex_index)

name_cache = ElementCache(name_cache)
type_cache = ElementCache(vertex_type_cache)
graph_processor = GraphTypeHandler(graph_processor, type_cache, name_cache)

graph_processor = GraphRelationFilter(graph_processor, discarded_relation_file, name_relation)

graph_iterator = GraphFileIterator(args.graph)

non_events = []

print("Indexing graph", file=sys.stderr)
for i,graph in enumerate(graph_iterator.iterate()):
    if i % 10000000 == 0:
        print(str(i), file=sys.stderr)
    processed = graph_processor.process(graph)
    if processed is not None:
        print("\t".join(processed))