import argparse

from graph_indexing.graph_indexing_components.graph_name_handler import GraphNameHandler
from graph_indexing.graph_indexing_components.graph_printer import GraphPrinter
from graph_indexing.graph_indexing_components.graph_relation_counter import GraphRelationCounter
from graph_indexing.graph_indexing_components.graph_relation_filter import GraphRelationFilter
from graph_indexing.graph_indexing_components.graph_relation_indexer import GraphRelationIndexer
from graph_indexing.graph_indexing_components.graph_vertex_indexer import GraphVertexIndexer
from graph_indexing.graph_iterators.graph_file_iterator import GraphFileIterator

"""
Future-proof graph indexing system
"""

parser = argparse.ArgumentParser(description='Indexes a graph')
parser.add_argument('--graph', type=str, help='The location of the graph')
args = parser.parse_args()

graph_processor = GraphPrinter()
graph_processor = GraphRelationIndexer(graph_processor)
graph_processor = GraphVertexIndexer(graph_processor)
graph_processor = GraphRelationCounter(graph_processor)
graph_processor = GraphRelationFilter(graph_processor)
graph_processor = GraphNameHandler(graph_processor)

graph_iterator = GraphFileIterator(args.graph)

non_events = []

for graph in graph_iterator.iterate():
    processed = graph_processor.process(graph)
    if processed:
        print("\t".join(processed))