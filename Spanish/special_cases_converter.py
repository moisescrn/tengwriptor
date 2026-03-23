#!/usr/bin/env python3
#
# ESPAÑOL
#
# This file contains functions that convert the clusters into other (unique) characters to make the final conversion better

from .letters import consonant_clusters, clusters, cluster_dict

def cluster_converter(word):
    """
    Apply the map defined by the dictionary
    """
    # Make firstly the consonants to avoid problems with que and qui
    for cluster in consonant_clusters:
        word = word.replace(cluster, cluster_dict[cluster])
    for cluster in clusters:
        word = word.replace(cluster, cluster_dict[cluster])
    return word
