# Copyright (c) 2022, Ora Lassila & So Many Aircraft
# All rights reserved.
#
# See LICENSE for licensing information
#
# This module implements some useful stuff when programming with RDFLib.

from rdfhelpers.rdfhelpers import graphFrom, expandQName, URI, getvalue, setvalue
from rdfhelpers.rdfhelpers import isContainerItemPredicate, makeContainerItemPredicate, diff
from rdfhelpers.rdfhelpers import cbd, cbdAnalysis
from rdfhelpers.rdfhelpers import getContainerStatements, getContainerItems, setContainerItems
from rdfhelpers.rdfhelpers import SPARQLRepository, JournaledGraph, FocusedGraph, CBDGraph
from rdfhelpers.templated import identity, mapDict, Templated, TemplatedQueryMixin
from rdfhelpers.constructor import Constructor
from rdfhelpers.labels import LabelCache, SKOSLabelCache
from rdfhelpers.gsp import GraphStoreClient

__all__ = [
    'graphFrom', 'expandQName', 'URI', 'getvalue', 'setvalue',
    'isContainerItemPredicate', 'makeContainerItemPredicate', 'diff',
    'cbd', 'cbdAnalysis',
    'getContainerStatements', 'getContainerItems', 'setContainerItems',
    'SPARQLRepository', 'JournaledGraph', 'FocusedGraph', 'CBDGraph',
    'identity', 'mapDict', 'Templated', 'TemplatedQueryMixin',
    'Constructor',
    'LabelCache', 'SKOSLabelCache',
    'GraphStoreClient'
]
