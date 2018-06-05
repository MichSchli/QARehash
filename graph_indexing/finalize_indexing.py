import argparse

from auxilliaries.settings_reader import SettingsReader
from indexes.element_cache import ElementCache
from indexes.element_index import ElementIndex
import sys

"""
Future-proof graph indexing system
"""

parser = argparse.ArgumentParser(description='Indexes a graph')
parser.add_argument('--preprocessor_settings', type=str, help='Settings file for preprocessor')
args = parser.parse_args()

settings_reader = SettingsReader()
settings = settings_reader.read(args.preprocessor_settings)

name_cache = settings["cache_locations"]["name_cache"]
vertex_index_location = settings["cache_locations"]["vertex_index"]
vertex_type_cache = settings["cache_locations"]["vertex_type_cache"]

vertex_index = ElementIndex(vertex_index_location)
name_cache = ElementCache(name_cache)
type_cache = ElementCache(vertex_type_cache)

print("Distributing vertex indices", file=sys.stderr)
name_cache.index_keys(vertex_index)
type_cache.index_keys(vertex_index)