#!/usr/bin/env bash

GRAPH_FILE=$1
PREPROCESSOR_CONFIGURATION=$2

PYTHON='python3'

cp graph_building/build_graph_dicts.py build_graph_dicts.py

$PYTHON -u build_graph_dicts.py --graph $INDEXED_GRAPH_FILE --preprocessor_settings $PREPROCESSOR_CONFIGURATION

rm build_graph_dicts.py