#!/usr/bin/env bash

INDEXED_GRAPH_FILE='/home/michael/Projects/QuestionAnswering/GCNQA3/data/toy-125/toy.preprocessed.graph'
PREPROCESSOR_CONFIGURATION='/home/michael/Projects/QuestionAnswering/GCNQA3/configurations/preprocessor/toy_local.cfg'

PYTHON='python3'

cp graph_building/build_graph_dicts.py build_graph_dicts.py

$PYTHON -u build_graph_dicts.py --graph $INDEXED_GRAPH_FILE --preprocessor_settings $PREPROCESSOR_CONFIGURATION

rm build_graph_dicts.py