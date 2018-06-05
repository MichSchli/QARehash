#!/usr/bin/env bash

GRAPH_FILE=$1
PREPROCESSOR_CONFIGURATION=$2

PYTHON='python3'

cp graph_indexing/index_names.py index_names.py
cp graph_indexing/index_graph.py index_graph.py
cp graph_indexing/finalize_indexing.py finalize_indexing.py

$PYTHON -u index_names.py --graph $GRAPH_FILE --preprocessor_settings $PREPROCESSOR_CONFIGURATION
$PYTHON -u index_graph.py --graph $GRAPH_FILE --preprocessor_settings $PREPROCESSOR_CONFIGURATION
$PYTHON -u finalize_indexing.py --preprocessor_settings $PREPROCESSOR_CONFIGURATION

rm index_names.py
rm index_graph.py
rm finalize_indexing.py