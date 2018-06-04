import argparse

from graph_indexing.graph_indexing_components.graph_name_handler import GraphNameHandler
from graph_indexing.graph_iterators.graph_file_iterator import GraphFileIterator
from indexes.element_cache import ElementCache

"""
Future-proof graph indexing system
"""

parser = argparse.ArgumentParser(description='Indexes the names in a graph')
parser.add_argument('--graph', type=str, help='The location of the graph')
parser.add_argument('--name_dictionary', type=str, help='The location of the name dictionary')
args = parser.parse_args()

name_index = ElementCache(args.name_dictionary)
graph_processor = GraphNameHandler(None, "name", name_index, index=True)

graph_iterator = GraphFileIterator(args.graph)

non_events = []

for graph in graph_iterator.iterate():
    processed = graph_processor.process(graph)
    if processed:
        print("\t".join(processed))