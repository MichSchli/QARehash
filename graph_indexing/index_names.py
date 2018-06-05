import argparse

from auxilliaries.settings_reader import SettingsReader
from graph_indexing.graph_indexing_components.graph_name_handler import GraphNameHandler
from graph_indexing.graph_iterators.graph_file_iterator import GraphFileIterator
from indexes.element_cache import ElementCache
import sys

"""
Future-proof graph indexing system
"""

parser = argparse.ArgumentParser(description='Indexes the names in a graph')
parser.add_argument('--graph', type=str, help='The location of the graph')
parser.add_argument('--preprocessor_settings', type=str, help='Settings file for preprocessor')
args = parser.parse_args()

settings_reader = SettingsReader()
settings = settings_reader.read(args.preprocessor_settings)

name_cache = settings["cache_locations"]["name_cache"]
name_relation = settings["other"]["name_relation"]
discarded_name_file = settings["filters"]["names"]

name_index = ElementCache(name_cache)
graph_processor = GraphNameHandler(None, name_relation, name_index, discarded_name_file, index=True)

graph_iterator = GraphFileIterator(args.graph)

non_events = []

print("Indexing names", file=sys.stderr)
for i,graph in enumerate(graph_iterator.iterate()):
    if i % 10000000 == 0:
        print(str(i), file=sys.stderr)
    processed = graph_processor.process(graph)
    if processed:
        print("\t".join(processed))