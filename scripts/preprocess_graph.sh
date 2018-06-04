#!/usr/bin/env bash

GRAPH_FILE='data/toy-125/toy.graph'
INDEX_DIR='data/toy-125/cache'

NAME_CACHE=$INDEX_DIR'/name_cache'
TYPE_CACHE=$INDEX_DIR'/type_cache'
RELATION_INDEX=$INDEX_DIR'/relation_index'
VERTEX_INDEX=$INDEX_DIR'/vertex_index'

cp graph_indexing/index_names.py index_names.py
cp graph_indexing/index_graph.py index_graph.py
cp graph_indexing/finalize_indexing.py finalize_indexing.py

python3 -u index_names.py --graph $GRAPH_FILE --name_dictionary $NAME_CACHE
python3 -u index_graph.py --graph $GRAPH_FILE --name_dictionary $NAME_CACHE --type_dictionary $TYPE_CACHE --relation_dictionary $RELATION_INDEX --vertex_dictionary $VERTEX_INDEX
python3 -u finalize_indexing.py --name_dictionary $NAME_CACHE --type_dictionary $TYPE_CACHE --vertex_dictionary $VERTEX_INDEX

rm index_names.py
rm index_graph.py
rm finalize_indexing.py