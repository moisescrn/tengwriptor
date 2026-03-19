#!/usr/bin/env python3
#
# ESPAÑOL
#
# This file contains functions that convert the clusters into other (unique) characters to make the final conversion better

from .letters import clusters, cluster_dict

def cluster_converter(word):
    """
    Apply the map defined by the dictionary
    """
    for cluster in clusters:
        word = word.replace(cluster, cluster_dict[cluster])
    return word
