# -*- coding: utf-8 -*-
r"""
Generic graphs (common to directed/undirected)

This module implements the base class for graphs and digraphs, and methods that
can be applied on both. Here is what it can do:

**Basic Graph operations:**

.. csv-table::
    :class: contentstable
    :widths: 30, 70
    :delim: |

    :meth:`~GenericGraph.networkx_graph` | Return a new ``NetworkX`` graph from the Sage graph
    :meth:`~GenericGraph.igraph_graph` | Return an ``igraph`` graph from the Sage graph
    :meth:`~GenericGraph.to_dictionary` | Create a dictionary encoding the graph.
    :meth:`~GenericGraph.copy` | Return a copy of the graph.
    :meth:`~GenericGraph.export_to_file` | Export the graph to a file.
    :meth:`~GenericGraph.adjacency_matrix` | Return the adjacency matrix of the (di)graph.
    :meth:`~GenericGraph.incidence_matrix` | Return an incidence matrix of the (di)graph
    :meth:`~GenericGraph.distance_matrix` | Return the distance matrix of the (strongly) connected (di)graph
    :meth:`~GenericGraph.weighted_adjacency_matrix` | Return the weighted adjacency matrix of the graph
    :meth:`~GenericGraph.kirchhoff_matrix` | Return the Kirchhoff matrix (a.k.a. the Laplacian) of the graph.
    :meth:`~GenericGraph.has_loops` | Return whether there are loops in the (di)graph
    :meth:`~GenericGraph.allows_loops` | Return whether loops are permitted in the (di)graph
    :meth:`~GenericGraph.allow_loops` | Change whether loops are permitted in the (di)graph
    :meth:`~GenericGraph.loops` | Return a list of all loops in the (di)graph
    :meth:`~GenericGraph.loop_edges` | Return a list of all loops in the (di)graph
    :meth:`~GenericGraph.number_of_loops` | Return the number of edges that are loops
    :meth:`~GenericGraph.loop_vertices` | Return a list of vertices with loops
    :meth:`~GenericGraph.remove_loops` | Remove loops on vertices in ``vertices``.
    :meth:`~GenericGraph.has_multiple_edges` | Return whether there are multiple edges in the (di)graph.
    :meth:`~GenericGraph.allows_multiple_edges` | Return whether multiple edges are permitted in the (di)graph.
    :meth:`~GenericGraph.allow_multiple_edges` | Change whether multiple edges are permitted in the (di)graph.
    :meth:`~GenericGraph.multiple_edges` | Return any multiple edges in the (di)graph.
    :meth:`~GenericGraph.name` | Return or set the graph's name.
    :meth:`~GenericGraph.is_immutable` | Return whether the graph is immutable.
    :meth:`~GenericGraph.weighted` | Whether the (di)graph is to be considered as a weighted (di)graph.
    :meth:`~GenericGraph.antisymmetric` | Test whether the graph is antisymmetric
    :meth:`~GenericGraph.density` | Return the density
    :meth:`~GenericGraph.order` | Return the number of vertices.
    :meth:`~GenericGraph.size` | Return the number of edges.
    :meth:`~GenericGraph.add_vertex` | Create an isolated vertex.
    :meth:`~GenericGraph.add_vertices` | Add vertices to the (di)graph from an iterable container of vertices
    :meth:`~GenericGraph.delete_vertex` | Delete vertex, removing all incident edges.
    :meth:`~GenericGraph.delete_vertices` | Delete vertices from the (di)graph taken from an iterable container of vertices.
    :meth:`~GenericGraph.has_vertex` | Check if ``vertex`` is one of the vertices of this graph.
    :meth:`~GenericGraph.random_vertex` | Return a random vertex of ``self``.
    :meth:`~GenericGraph.random_vertex_iterator` | Return an iterator over random vertices of ``self``.
    :meth:`~GenericGraph.random_edge` | Return a random edge of ``self``.
    :meth:`~GenericGraph.random_edge_iterator` | Return an iterator over random edges of ``self``.
    :meth:`~GenericGraph.vertex_boundary` | Return a list of all vertices in the external boundary of ``vertices1``, intersected with ``vertices2``.
    :meth:`~GenericGraph.set_vertices` | Associate arbitrary objects with each vertex
    :meth:`~GenericGraph.set_vertex` | Associate an arbitrary object with a vertex.
    :meth:`~GenericGraph.get_vertex` | Retrieve the object associated with a given vertex.
    :meth:`~GenericGraph.get_vertices` | Return a dictionary of the objects associated to each vertex.
    :meth:`~GenericGraph.vertex_iterator` | Return an iterator over the given vertices.
    :meth:`~GenericGraph.neighbor_iterator` | Return an iterator over neighbors of ``vertex``.
    :meth:`~GenericGraph.vertices` | Return a list of the vertices.
    :meth:`~GenericGraph.neighbors` | Return a list of neighbors (in and out if directed) of ``vertex``.
    :meth:`~GenericGraph.merge_vertices` | Merge vertices.
    :meth:`~GenericGraph.add_edge` | Add an edge from ``u`` to ``v``.
    :meth:`~GenericGraph.add_edges` | Add edges from an iterable container.
    :meth:`~GenericGraph.subdivide_edge` | Subdivide an edge `k` times.
    :meth:`~GenericGraph.subdivide_edges` | Subdivide `k` times edges from an iterable container.
    :meth:`~GenericGraph.delete_edge` | Delete the edge from ``u`` to ``v``
    :meth:`~GenericGraph.delete_edges` | Delete edges from an iterable container.
    :meth:`~GenericGraph.contract_edge` | Contract an edge from ``u`` to ``v``.
    :meth:`~GenericGraph.contract_edges` | Contract edges from an iterable container.
    :meth:`~GenericGraph.delete_multiedge` | Delete all edges from ``u`` to ``v``.
    :meth:`~GenericGraph.set_edge_label` | Set the edge label of a given edge.
    :meth:`~GenericGraph.has_edge` | Check whether ``(u, v)`` is an edge of the (di)graph.
    :meth:`~GenericGraph.edges` | Return a :class:`~EdgesView` of edges.
    :meth:`~GenericGraph.edge_boundary` | Return a list of edges ``(u,v,l)`` with ``u`` in ``vertices1``
    :meth:`~GenericGraph.edge_iterator` | Return an iterator over edges.
    :meth:`~GenericGraph.edges_incident` | Return incident edges to some vertices.
    :meth:`~GenericGraph.edge_label` | Return the label of an edge.
    :meth:`~GenericGraph.edge_labels` | Return a list of the labels of all edges in ``self``.
    :meth:`~GenericGraph.remove_multiple_edges` | Remove all multiple edges, retaining one edge for each.
    :meth:`~GenericGraph.clear` | Empty the graph of vertices and edges and removes name, associated objects, and position information.
    :meth:`~GenericGraph.degree` | Return the degree (in + out for digraphs) of a vertex or of vertices.
    :meth:`~GenericGraph.average_degree` | Return the average degree of the graph.
    :meth:`~GenericGraph.degree_histogram` | Return a list, whose ith entry is the frequency of degree i.
    :meth:`~GenericGraph.degree_iterator` | Return an iterator over the degrees of the (di)graph.
    :meth:`~GenericGraph.degree_sequence` | Return the degree sequence of this (di)graph.
    :meth:`~GenericGraph.random_subgraph` | Return a random subgraph containing each vertex with probability ``p``.
    :meth:`~GenericGraph.add_clique` | Add a clique to the graph with the given vertices.
    :meth:`~GenericGraph.add_cycle` | Add a cycle to the graph with the given vertices.
    :meth:`~GenericGraph.add_path` | Add a path to the graph with the given vertices.
    :meth:`~GenericGraph.complement` | Return the complement of the (di)graph.
    :meth:`~GenericGraph.line_graph` | Return the line graph of the (di)graph.
    :meth:`~GenericGraph.to_simple` | Return a simple version of itself (i.e., undirected and loops and multiple edges are removed).
    :meth:`~GenericGraph.disjoint_union` | Return the disjoint union of self and other.
    :meth:`~GenericGraph.union` | Return the union of self and other.
    :meth:`~GenericGraph.relabel` | Relabel the vertices of ``self``
    :meth:`~GenericGraph.degree_to_cell` | Return the number of edges from vertex to an edge in cell.
    :meth:`~GenericGraph.subgraph` | Return the subgraph containing the given vertices and edges.
    :meth:`~GenericGraph.is_subgraph` | Check whether ``self`` is a subgraph of ``other``.

**Graph products:**

.. csv-table::
    :class: contentstable
    :widths: 30, 70
    :delim: |

    :meth:`~GenericGraph.cartesian_product` | Return the Cartesian product of self and other.
    :meth:`~GenericGraph.tensor_product` | Return the tensor product, also called the categorical product, of self and other.
    :meth:`~GenericGraph.lexicographic_product` | Return the lexicographic product of self and other.
    :meth:`~GenericGraph.strong_product` | Return the strong product of self and other.
    :meth:`~GenericGraph.disjunctive_product` | Return the disjunctive product of self and other.

**Paths and cycles:**

.. csv-table::
    :class: contentstable
    :widths: 30, 70
    :delim: |

    :meth:`~GenericGraph.eulerian_orientation` | Return a DiGraph which is an Eulerian orientation of the current graph.
    :meth:`~GenericGraph.eulerian_circuit` | Return a list of edges forming an Eulerian circuit if one exists.
    :meth:`~GenericGraph.minimum_cycle_basis` | Return a minimum weight cycle basis of the graph.
    :meth:`~GenericGraph.cycle_basis` | Return a list of cycles which form a basis of the cycle space of ``self``.
    :meth:`~GenericGraph.all_paths` | Return a list of all paths (also lists) between a pair of vertices in the (di)graph.
    :meth:`~GenericGraph.triangles_count` | Return the number of triangles in the (di)graph.
    :meth:`~GenericGraph.shortest_simple_paths` | Return an iterator over the simple paths between a pair of vertices.

**Linear algebra:**

.. csv-table::
    :class: contentstable
    :widths: 30, 70
    :delim: |

    :meth:`~GenericGraph.spectrum` | Return a list of the eigenvalues of the adjacency matrix.
    :meth:`~GenericGraph.eigenvectors` | Return the *right* eigenvectors of the adjacency matrix of the graph.
    :meth:`~GenericGraph.eigenspaces` | Return the *right* eigenspaces of the adjacency matrix of the graph.

**Some metrics:**

.. csv-table::
    :class: contentstable
    :widths: 30, 70
    :delim: |

    :meth:`~GenericGraph.cluster_triangles` | Return the number of triangles for the set nbunch of vertices as a dictionary keyed by vertex.
    :meth:`~GenericGraph.clustering_average` | Return the average clustering coefficient.
    :meth:`~GenericGraph.clustering_coeff` | Return the clustering coefficient for each vertex in nbunch
    :meth:`~GenericGraph.cluster_transitivity` | Return the transitivity (fraction of transitive triangles) of the graph.
    :meth:`~GenericGraph.szeged_index` | Return the Szeged index of the graph.
    :meth:`~GenericGraph.katz_centrality` | Return the katz centrality of the vertex u of the graph.
    :meth:`~GenericGraph.katz_matrix` | Return the katz matrix of the graph.
    :meth:`~GenericGraph.pagerank` | Return the PageRank of the vertices of ``self``.

**Automorphism group:**

.. csv-table::
    :class: contentstable
    :widths: 30, 70
    :delim: |

    :meth:`~GenericGraph.coarsest_equitable_refinement` | Return the coarsest partition which is finer than the input partition, and equitable with respect to self.
    :meth:`~GenericGraph.automorphism_group` | Return the largest subgroup of the automorphism group of the (di)graph whose orbit partition is finer than the partition given.
    :meth:`~GenericGraph.is_vertex_transitive` | Return whether the automorphism group of self is transitive within the partition provided
    :meth:`~GenericGraph.is_isomorphic` | Test for isomorphism between self and other.
    :meth:`~GenericGraph.canonical_label` | Return the canonical graph.
    :meth:`~GenericGraph.is_cayley` | Check whether the graph is a Cayley graph.

**Graph properties:**

.. csv-table::
    :class: contentstable
    :widths: 30, 70
    :delim: |

    :meth:`~GenericGraph.is_eulerian` | Return ``True`` if the graph has a (closed) tour that visits each edge exactly once.
    :meth:`~GenericGraph.is_planar` | Check whether the graph is planar.
    :meth:`~GenericGraph.is_circular_planar` | Check whether the graph is circular planar (outerplanar)
    :meth:`~GenericGraph.is_regular` | Return ``True`` if this graph is (`k`-)regular.
    :meth:`~GenericGraph.is_chordal` | Check whether the given graph is chordal.
    :meth:`~GenericGraph.is_bipartite` | Test whether the given graph is bipartite.
    :meth:`~GenericGraph.is_circulant` | Check whether the graph is a circulant graph.
    :meth:`~GenericGraph.is_interval` | Check whether the graph is an interval graph.
    :meth:`~GenericGraph.is_gallai_tree` | Return whether the current graph is a Gallai tree.
    :meth:`~GenericGraph.is_clique` | Check whether a set of vertices is a clique
    :meth:`~GenericGraph.is_cycle` | Check whether ``self`` is a (directed) cycle graph.
    :meth:`~GenericGraph.is_independent_set` | Check whether ``vertices`` is an independent set of ``self``
    :meth:`~GenericGraph.is_transitively_reduced` | Test whether the digraph is transitively reduced.
    :meth:`~GenericGraph.is_equitable` | Check whether the given partition is equitable with respect to self.
    :meth:`~GenericGraph.is_self_complementary` | Check whether the graph is self-complementary.

**Traversals:**

.. csv-table::
    :class: contentstable
    :widths: 30, 70
    :delim: |

    :meth:`~GenericGraph.breadth_first_search` | Return an iterator over the vertices in a breadth-first ordering.
    :meth:`~GenericGraph.depth_first_search` | Return an iterator over the vertices in a depth-first ordering.
    :meth:`~GenericGraph.lex_BFS` | Perform a lexicographic breadth first search (LexBFS) on the graph.
    :meth:`~GenericGraph.lex_UP` | Perform a lexicographic UP search (LexUP) on the graph.
    :meth:`~GenericGraph.lex_DFS` | Perform a lexicographic depth first search (LexDFS) on the graph.
    :meth:`~GenericGraph.lex_DOWN` | Perform a lexicographic DOWN search (LexDOWN) on the graph.

**Distances:**

.. csv-table::
    :class: contentstable
    :widths: 30, 70
    :delim: |

    :meth:`~GenericGraph.centrality_betweenness` | Return the betweenness centrality
    :meth:`~GenericGraph.centrality_closeness` | Returns the closeness centrality (1/average distance to all vertices)
    :meth:`~GenericGraph.distance` | Return the (directed) distance from u to v in the (di)graph
    :meth:`~GenericGraph.distance_all_pairs` | Return the distances between all pairs of vertices.
    :meth:`~GenericGraph.distances_distribution` | Return the distances distribution of the (di)graph in a dictionary.
    :meth:`~GenericGraph.girth` | Return the girth of the graph.
    :meth:`~GenericGraph.odd_girth` | Return the odd girth of the graph.
    :meth:`~GenericGraph.shortest_path` | Return a list of vertices representing some shortest path from `u` to `v`
    :meth:`~GenericGraph.shortest_path_length` | Return the minimal length of paths from u to v
    :meth:`~GenericGraph.shortest_paths` | Return a dictionary associating to each vertex v a shortest path from u to v, if it exists.
    :meth:`~GenericGraph.shortest_path_lengths` | Return a dictionary of shortest path lengths keyed by targets that are connected by a path from u.
    :meth:`~GenericGraph.shortest_path_all_pairs` | Compute a shortest path between each pair of vertices.
    :meth:`~GenericGraph.wiener_index` | Return the Wiener index of the graph.
    :meth:`~GenericGraph.average_distance` | Return the average distance between vertices of the graph.

**Flows, connectivity, trees:**

.. csv-table::
    :class: contentstable
    :widths: 30, 70
    :delim: |

    :meth:`~GenericGraph.is_connected` | Test whether the (di)graph is connected.
    :meth:`~GenericGraph.connected_components` | Return the list of connected components
    :meth:`~GenericGraph.connected_components_number` | Return the number of connected components.
    :meth:`~GenericGraph.connected_components_subgraphs` | Return a list of connected components as graph objects.
    :meth:`~GenericGraph.connected_component_containing_vertex` | Return a list of the vertices connected to vertex.
    :meth:`~GenericGraph.connected_components_sizes` | Return the sizes of the connected components as a list.
    :meth:`~GenericGraph.blocks_and_cut_vertices` | Compute the blocks and cut vertices of the graph.
    :meth:`~GenericGraph.blocks_and_cuts_tree` | Compute the blocks-and-cuts tree of the graph.
    :meth:`~GenericGraph.is_cut_edge` | Return True if the input edge is a cut-edge or a bridge.
    :meth:`~GenericGraph.is_cut_vertex` | Return True if the input vertex is a cut-vertex.
    :meth:`~GenericGraph.edge_cut` | Return a minimum edge cut between vertices `s` and `t`
    :meth:`~GenericGraph.vertex_cut` | Return a minimum vertex cut between non-adjacent vertices `s` and `t`
    :meth:`~GenericGraph.flow` | Return a maximum flow in the graph from ``x`` to ``y``
    :meth:`~GenericGraph.nowhere_zero_flow` | Return a `k`-nowhere zero flow of the (di)graph.
    :meth:`~GenericGraph.edge_disjoint_paths` | Return a list of edge-disjoint paths between two vertices
    :meth:`~GenericGraph.vertex_disjoint_paths` | Return a list of vertex-disjoint paths between two vertices
    :meth:`~GenericGraph.edge_connectivity` | Return the edge connectivity of the graph.
    :meth:`~GenericGraph.vertex_connectivity` | Return the vertex connectivity of the graph.
    :meth:`~GenericGraph.transitive_closure` | Compute the transitive closure of a graph and returns it.
    :meth:`~GenericGraph.transitive_reduction` | Return a transitive reduction of a graph.
    :meth:`~GenericGraph.min_spanning_tree` | Return the edges of a minimum spanning tree.
    :meth:`~GenericGraph.spanning_trees_count` | Return the number of spanning trees in a graph.
    :meth:`~GenericGraph.dominator_tree`    | Returns a dominator tree of the graph.
    :meth:`~GenericGraph.connected_subgraph_iterator` | Iterator over the induced connected subgraphs of order at most `k`

**Plot/embedding-related methods:**

.. csv-table::
    :class: contentstable
    :widths: 30, 70
    :delim: |

    :meth:`~GenericGraph.set_embedding` | Set a combinatorial embedding dictionary to ``_embedding`` attribute.
    :meth:`~GenericGraph.get_embedding` | Return the attribute _embedding if it exists.
    :meth:`~GenericGraph.faces` | Return the faces of an embedded graph.
    :meth:`~GenericGraph.genus` | Return the number of faces of an embedded graph.
    :meth:`~GenericGraph.planar_dual` | Return the planar dual of an embedded graph.
    :meth:`~GenericGraph.get_pos` | Return the position dictionary
    :meth:`~GenericGraph.set_pos` | Set the position dictionary.
    :meth:`~GenericGraph.layout_planar` | Compute a planar layout of the graph using Schnyder's algorithm.
    :meth:`~GenericGraph.is_drawn_free_of_edge_crossings` | Check whether the position dictionary gives a planar embedding.
    :meth:`~GenericGraph.latex_options` | Return an instance of :class:`~sage.graphs.graph_latex.GraphLatex` for the graph.
    :meth:`~GenericGraph.set_latex_options` | Set multiple options for rendering a graph with LaTeX.
    :meth:`~GenericGraph.layout` | Return a layout for the vertices of this graph.
    :meth:`~GenericGraph.layout_spring` | Return a spring layout for this graph
    :meth:`~GenericGraph.layout_ranked` | Return a ranked layout for this graph
    :meth:`~GenericGraph.layout_extend_randomly` | Extend randomly a partial layout
    :meth:`~GenericGraph.layout_circular` | Return a circular layout for this graph
    :meth:`~GenericGraph.layout_tree` | Return an ordered tree layout for this graph
    :meth:`~GenericGraph.layout_forest` | Return an ordered forest layout for this graph
    :meth:`~GenericGraph.layout_graphviz` | Call ``graphviz`` to compute a layout of the vertices of this graph.
    :meth:`~GenericGraph._circle_embedding` | Set some vertices on a circle in the embedding of this graph.
    :meth:`~GenericGraph._line_embedding` | Set some vertices on a line in the embedding of this graph.
    :meth:`~GenericGraph.graphplot` | Return a :class:`~sage.graphs.graph_plot.GraphPlot` object.
    :meth:`~GenericGraph.plot` | Return a :class:`~sage.plot.graphics.Graphics` object representing the (di)graph.
    :meth:`~GenericGraph.show` | Show the (di)graph.
    :meth:`~GenericGraph.plot3d` | Plot the graph in three dimensions.
    :meth:`~GenericGraph.show3d` | Plot the graph using :class:`~sage.plot.plot3d.tachyon.Tachyon`, and shows the resulting plot.
    :meth:`~GenericGraph.graphviz_string` | Return a representation in the ``dot`` language.
    :meth:`~GenericGraph.graphviz_to_file_named` | Write a representation in the ``dot`` language in a file.

**Algorithmically hard stuff:**

.. csv-table::
    :class: contentstable
    :widths: 30, 70
    :delim: |

    :meth:`~GenericGraph.steiner_tree` | Return a tree of minimum weight connecting the given set of vertices.
    :meth:`~GenericGraph.edge_disjoint_spanning_trees` | Return the desired number of edge-disjoint spanning trees/arborescences.
    :meth:`~GenericGraph.feedback_vertex_set` | Compute the minimum feedback vertex set of a (di)graph.
    :meth:`~GenericGraph.multiway_cut` | Return a minimum edge multiway cut
    :meth:`~GenericGraph.max_cut` | Return a maximum edge cut of the graph.
    :meth:`~GenericGraph.longest_path` | Return a longest path of ``self``.
    :meth:`~GenericGraph.traveling_salesman_problem` | Solve the traveling salesman problem (TSP)
    :meth:`~GenericGraph.is_hamiltonian` | Test whether the current graph is Hamiltonian.
    :meth:`~GenericGraph.hamiltonian_cycle` | Return a Hamiltonian cycle/circuit of the current graph/digraph
    :meth:`~GenericGraph.hamiltonian_path` | Return a Hamiltonian path of the current graph/digraph
    :meth:`~GenericGraph.multicommodity_flow` | Solve a multicommodity flow problem.
    :meth:`~GenericGraph.disjoint_routed_paths` | Return a set of disjoint routed paths.
    :meth:`~GenericGraph.dominating_set` | Return a minimum dominating set of the graph
    :meth:`~GenericGraph.greedy_dominating_set` | Return a greedy distance-`k` dominating set of the graph.
    :meth:`~GenericGraph.subgraph_search` | Return a copy of ``G`` in ``self``.
    :meth:`~GenericGraph.subgraph_search_count` | Return the number of labelled occurrences of ``G`` in ``self``.
    :meth:`~GenericGraph.subgraph_search_iterator` | Return an iterator over the labelled copies of ``G`` in ``self``.
    :meth:`~GenericGraph.characteristic_polynomial` | Return the characteristic polynomial of the adjacency matrix of the (di)graph.
    :meth:`~GenericGraph.genus` | Return the minimal genus of the graph.
    :meth:`~GenericGraph.crossing_number` | Return the crossing number of the graph.

**Miscellaneous**

.. csv-table::
    :class: contentstable
    :widths: 30, 70
    :delim: |

    :meth:`~GenericGraph.edge_polytope` | Return the edge polytope of ``self``.
    :meth:`~GenericGraph.symmetric_edge_polytope` | Return the symmetric edge polytope of ``self``.

Methods
-------
"""

# ****************************************************************************
#
#       Copyright (C) 2010      Alexandre Blondin Masse <alexandre.blondin.masse at gmail.com>
#                               Ben Edwards <bedwards@cs.unm.edu>
#                               Carl Witty <cwitty@newtonlabs.com>
#                               Gregory McWhirter <gmcwhirt@uci.edu>
#                               Johan Sebastian Rosenkilde Nielsen <j.s.r.nielsen@mat.dtu.dk>
#                               Minh Van Nguyen <nguyenminh2@gmail.com>
#                               Mitesh Patel <qed777@gmail.com>
#                               Sebastian Pancratz <sage@pancratz.org>
#                               Tom Boothby <boothby@u.washington.edu>
#                     2010-2011 Robert L. Miller <rlm@rlmiller.org>
#                               Fidel Barrera-Cruz <fidel.barrera@gmail.com>
#                               Leif Leonhardy <not.really@online.de>
#                               Rob Beezer <beezer@ups.edu>
#                     2010-2012 Dmitrii Pasechnik <dimpase@gmail.com>
#                               Jason Grout <jason-sage@creativetrax.com>
#                     2010-2013 Burcin Erocal <burcin@erocal.org>
#                     2010-2014 Mike Hansen <mhansen@gmail.com>
#                     2010-2015 Nicolas M. Thiery <nthiery@users.sf.net>
#                     2010-2016 Nathann Cohen <nathann.cohen@gmail.com>
#                     2010-2017 J. H. Palmieri <palmieri@math.washington.edu>
#                     2010-2018 Christian Stump <christian.stump@univie.ac.at>
#                     2010-2022 Vincent Delecroix <20100.delecroix at gmail.com>
#                     2011      Anne Schilling <anne@math.ucdavis.edu>
#                               Diego de Estrada <destrada@dc.uba.ar>
#                               Eviatar Bach <eviatarbach@gmail.com>
#                               Geoffrey Ehrman <gehrman@gmail.com>
#                               Ivan Andrus <darthandrus@gmail.com>
#                               Michael Orlitzky <michael@orlitzky.com>
#                     2011-2012 Lukas Lansky <lansky@kam.mff.cuni.cz>
#                     2011-2013 Robert Miller <rlm@rlmiller.org>
#                     2011-2015 André Apitzsch <andre.apitzsch@st.ovgu.de>
#                               Andrey Novoseltsev <novoselt@gmail.com>
#                     2011-2018 Jeroen Demeyer <jdemeyer@cage.ugent.be>
#                     2012      Dan Drake <drake@kaist.edu>
#                               Javier López Peña <vengoroso@gmail.com>
#                               Karl-Dieter Crisman <kcrisman@gmail.com>
#                               Keshav Kini <keshav.kini@gmail.com>
#                               Lauren Keough <s-lkeough1@math.unl.edu>
#                               Nathan Carter <ncarter@bentley.edu>
#                               Punarbasu Purkayastha <ppurka@gmail.com>
#                               Stefano Leucci <leucci.stefano@gmail.com>
#                     2012-2013 Frédéric Chapoton <chapoton at math.univ-lyon1.fr>
#                     2012-2015 Jernej Azarija <jernej.azarija@gmail.com>
#                                Volker Braun <vbraun.name@gmail.com>
#                     2012-2018 Julian Rueth <julian.rueth@gmail.com>
#                     2013      Alexandre Prusch Züge <alexandrezuge@gmail.com>
#                               Austin Roberts <austinis@math.washington.edu>
#                               Birk Eisermann <eisermbi@fastmail.fm>
#                               Uros Slana <urossla@gmail.com>
#                     2013-2014 R. Andrew Ohana <andrew.ohana@gmail.com>
#                               Simon King <simon.king@uni-jena.de>
#                     2013-2018 Darij Grinberg <darijgrinberg@gmail.com>
#                               Frédéric Chapoton <chapoton@math.univ-lyon1.fr>
#                     2014      Emmanuel Charpentier <emm.charpentier@free.fr>
#                               Erick Matsen <matsen@fhcrc.org>
#                               Erik Massop <e.massop@hccnet.nl>
#                               Florian Oosterhof <f.m.oosterhof@student.tue.nl>
#                               Jean-Pierre Flori <jean-pierre.flori@ssi.gouv.fr>
#                               Ralf Stephan <ralf@ark.in-berlin.de>
#                               Robert Lipshitz <lipshitz@math.columbia.edu>
#                               Thierry Monteil <sage@lma.metelu.net>
#                     2014-2015 Wilfried Luebbe <wluebbe@gmail.com>
#                     2014-2017 Travis Scrimshaw <tscrim at ucdavis.edu>
#                     2014-2018 David Coudert <david.coudert@inria.fr>
#                               Jori Mäntysalo <jori.mantysalo@uta.fi>
#                     2015      David Einstein <deinst@gmail.com>
#                               François Bissey <francois.bissey@canterbury.ac.nz>
#                               Michele Borassi <michele.borassi@imtlucca.it>
#                               Sergios Lenis <sergioslenis@gmail.com>
#                     2015-2016 Janoš Vidali <janos.vidali@fmf.uni-lj.si>
#                     2015-2018 Dima Pasechnik <dimpase@gmail.com>
#                     2016      Jeremias Epperlein <jeremias.epperlein@gmail.com>
#                               Marco Cognetta <cognetta.marco@gmail.com>
#                               Peleg Michaeli <freepeleg@gmail.com>
#                     2016-2018 Sébastien Labbé <slabqc@gmail.com>
#                     2017      Emile Nadeau <nadeau.emile@gmail.com>
#                               John Cremona <john.cremona@gmail.com>
#                               Lokesh Jain <lokeshj1703@gmail.com>
#                               Zachary Gershkoff <zgershkoff@gmail.com>
#                     2017-2018 Moritz Firsching <moritz@math.fu-berlin.de>
#                     2018      Erik M. Bray <erik.bray@lri.fr>
#                               Meghana M Reddy <mreddymeghana@gmail.com>
#                     2019      Rajat Mittal <rajat.mttl@gmail.com>
#                     2020      Jonathan Kliem <jonathan.kliem@fu-berlin.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************

from copy import copy

from sage.graphs.views import EdgesView
from .generic_graph_pyx import GenericGraph_pyx, spring_layout_fast, layout_split
from .dot2tex_utils import assert_have_dot2tex

from sage.misc.decorators import options
from sage.misc.cachefunc import cached_method
from sage.misc.prandom import random
from sage.misc.superseded import deprecation
from sage.misc.lazy_import import LazyImport

from sage.rings.integer_ring import ZZ
from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.matrix.constructor import matrix
from sage.rings.rational_field import QQ
from sage.features.igraph import python_igraph as igraph_feature

to_hex = LazyImport('matplotlib.colors', 'to_hex')


class GenericGraph(GenericGraph_pyx):
    """
    Base class for graphs and digraphs.

    .. automethod:: __eq__
    """

    # Nice defaults for plotting arrays of graphs (see sage.misc.functional.show)
    graphics_array_defaults = {'layout': 'circular', 'vertex_size': 50,
                               'vertex_labels': False, 'graph_border': True}

    def __init__(self):
        r"""
        Every graph carries a dictionary of options, set here to ``None``.

        Some options are added to the global :data:`sage.misc.latex.latex`
        instance which will insure that if LaTeX is used to render the graph,
        then the right packages are loaded and MathJax reacts properly.

        Most other initialization is done in the directed and undirected
        subclasses.

        TESTS::

            sage: g = Graph()
            sage: g
            Graph on 0 vertices
        """
        self._latex_opts = None

    def __setstate__(self, state):
        r"""
        Set the state from a pickle dict

        TESTS::

            sage: G = graphs.PetersenGraph()
            sage: s = dumps(G)
            sage: H = loads(s)
            sage: all(k in H.__dict__ for k in G.__dict__.keys())
            True
        """
        for k, v in state.items():
            self.__dict__[k] = v

    def __add__(self, other):
        """
        Return a graph isomorphic to disjoint union of this graph with `other`.

        Labels of the resulting graph will always be consecutive integers
        starting from zero.

        .. SEEALSO:: :meth:`disjoint_union`

        EXAMPLES::

            sage: G = Graph({'a': ['b', 'c']})
            sage: H = Graph({'c': ['d', 'e', 'f']})
            sage: J = G + H; J
            Graph on 3 vertices disjoint_union Graph on 4 vertices: Graph on 7 vertices
            sage: J.vertices(sort=True)
            [0, 1, 2, 3, 4, 5, 6]

        TESTS::

            sage: G = Graph({'a': ['b', 'c']})
            sage: E = Graph()
            sage: G+E
            Graph on 3 vertices disjoint_union Graph on 0 vertices: Graph on 3 vertices
            sage: E+G
            Graph on 0 vertices disjoint_union Graph on 3 vertices: Graph on 3 vertices
            sage: E+E
            Graph on 0 vertices disjoint_union Graph on 0 vertices: Graph on 0 vertices
            sage: G+42
            Traceback (most recent call last):
            ...
            TypeError: adding <class 'sage.graphs.graph.Graph'> and <class 'sage.rings.integer.Integer'> is not defined
        """
        if isinstance(other, GenericGraph):
            return self.disjoint_union(other, labels='integers')
        raise TypeError("adding {} and {} is not defined".format(type(self), type(other)))

    def __eq__(self, other):
        """
        Compare self and other for equality.

        Do not call this method directly. That is, for ``G.__eq__(H)`` write
        ``G == H``.

        Two graphs are considered equal if the following hold:
         - they are either both directed, or both undirected;
         - they have the same settings for loops, multiedges, and weightedness;
         - they have the same set of vertices;
         - they have the same (multi)set of arrows/edges, where labels of
           arrows/edges are taken into account if *and only if* the graphs are
           considered weighted. See :meth:`~GenericGraph.weighted`.

        Note that this is *not* an isomorphism test.

        EXAMPLES::

            sage: G = graphs.EmptyGraph()
            sage: H = Graph()
            sage: G == H
            True
            sage: G.to_directed() == H.to_directed()
            True
            sage: G = graphs.RandomGNP(8, .9999)
            sage: H = graphs.CompleteGraph(8)
            sage: G == H  # random - most often true
            True
            sage: G = Graph({0: [1, 2, 3, 4, 5, 6, 7]} )
            sage: H = Graph({1: [0], 2: [0], 3: [0], 4: [0], 5: [0], 6: [0], 7: [0]} )
            sage: G == H
            True
            sage: G.allow_loops(True)
            sage: G == H
            False
            sage: G = graphs.RandomGNP(9, .3).to_directed()
            sage: H = graphs.RandomGNP(9, .3).to_directed()
            sage: G == H # most often false
            False
            sage: G = Graph(multiedges=True, sparse=True)
            sage: G.add_edge(0, 1)
            sage: H = copy(G)
            sage: H.add_edge(0, 1)
            sage: G == H
            False

        Note that graphs must be considered weighted, or Sage will not pay
        attention to edge label data in equality testing::

            sage: foo = Graph(sparse=True)
            sage: foo.add_edges([(0, 1, 1), (0, 2, 2)])
            sage: bar = Graph(sparse=True)
            sage: bar.add_edges([(0, 1, 2), (0, 2, 1)])
            sage: foo == bar
            True
            sage: foo.weighted(True)
            sage: foo == bar
            False
            sage: bar.weighted(True)
            sage: foo == bar
            False

        """
        # inputs must be (di)graphs:
        if not isinstance(other, GenericGraph):
            return False
        from sage.graphs.graph import Graph
        g1_is_graph = isinstance(self, Graph)  # otherwise, DiGraph
        g2_is_graph = isinstance(other, Graph)  # otherwise, DiGraph
        # Fast checks
        if (g1_is_graph != g2_is_graph or
                self.allows_multiple_edges() != other.allows_multiple_edges() or
                self.allows_loops() != other.allows_loops() or
                self.order() != other.order() or
                self.size() != other.size() or
                self.weighted() != other.weighted()):
            return False

        return self._backend.is_subgraph(other._backend, self, ignore_labels=not self.weighted())

    @cached_method
    def __hash__(self):
        """
        Compute a hash for ``self``, if ``self`` is immutable.

        Only immutable graphs are hashable. The resulting value is cached.

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: {G: 1}[G]
            Traceback (most recent call last):
            ...
            TypeError: This graph is mutable, and thus not hashable. Create
            an immutable copy by `g.copy(immutable=True)`
            sage: G_imm = Graph(G, data_structure="static_sparse")
            sage: G_imm == G
            True
            sage: {G_imm: 1}[G_imm]  # indirect doctest
            1
            sage: G_imm.__hash__() is G_imm.__hash__()
            True

        TESTS:

        Equality and hash do not depend on ordering of vertices. In other words,
        `G1 == G2` can be `True` even when
        `G1.vertices(sort=True) == G2.vertices(sort=True)` is
        `False`. This is parts 1 and 2 of issue :trac:`17086`. ::

            sage: import functools
            sage: @functools.total_ordering
            ....: class C:
            ....:     order = ((0, 0), (0, 1), (1, 1), (1, 0))
            ....:     # Hasse diagram:
            ....:     #   0,0 < 0,1
            ....:     #    ^     ^
            ....:     #   1,0 > 1,1
            ....:     def __init__(self, x):
            ....:         assert x in self.order
            ....:         self.x = x
            ....:     def __repr__(self):
            ....:         return 'C(%r)' % (self.x,)
            ....:     # ordering depends on full self.x
            ....:     def __lt__(self, other):
            ....:         return self.order.index(self.x) < self.order.index(other.x)
            ....:     # equality depends only on the second coordinate.
            ....:     def __eq__(self, other):
            ....:         return self.x[1] == other.x[1]
            ....:     def __hash__(self):
            ....:         return hash(self.x[1])
            sage: G1 = Graph({C((0, 0)): [], C((0, 1)): []}, immutable=True)
            sage: G2 = Graph({C((1, 0)): [], C((1, 1)): []}, immutable=True)
            sage: (G1.vertices(sort=True), G2.vertices(sort=True))
            ([C((0, 0)), C((0, 1))], [C((1, 1)), C((1, 0))])
            sage: G1 == G2
            True
            sage: G1.__hash__() == G2.__hash__()
            True

        Hash of unweighted graphs does not depend on edge labels. That is,
        part 3 of issue :trac:`17086` is fixed ::

            sage: G1 = Graph({0: {1: 'edge label A'}}, immutable=True)
            sage: G2 = Graph({0: {1: 'edge label B'}}, immutable=True)
            sage: G1 == G2
            True
            sage: G1.__hash__() == G2.__hash__()
            True

        """
        if self.is_immutable():
            edge_items = self.edge_iterator(labels=self._weighted)
            if self.allows_multiple_edges():
                from collections import Counter
                edge_items = Counter(edge_items).items()
            return hash((frozenset(self.vertex_iterator()),
                         self._weighted,
                         frozenset(edge_items)))
        raise TypeError("This graph is mutable, and thus not hashable. "
                        "Create an immutable copy by `g.copy(immutable=True)`")

    def __mul__(self, n):
        r"""
        Return the sum of a graph with itself `n` times.

        EXAMPLES::

            sage: G = graphs.CycleGraph(3)
            sage: H = G * 3; H
            Cycle graph disjoint_union Cycle graph disjoint_union Cycle graph: Graph on 9 vertices
            sage: H.vertices(sort=True)
            [0, 1, 2, 3, 4, 5, 6, 7, 8]
            sage: H = G * 1; H
            Cycle graph: Graph on 3 vertices
        """
        if isinstance(n, (int, Integer)):
            if n < 1:
                raise TypeError('multiplication of a graph and a nonpositive integer is not defined')
            if n == 1:
                return copy(self)
            return sum([self] * (n - 1), self)
        else:
            raise TypeError('multiplication of a graph and something other than an integer is not defined')

    def __ne__(self, other):
        """
        Test for inequality, complement of ``__eq__``.

        EXAMPLES::

            sage: g = Graph()
            sage: g2 = copy(g)
            sage: g == g
            True
            sage: g != g
            False
            sage: g2 == g
            True
            sage: g2 != g
            False
            sage: g is g
            True
            sage: g2 is g
            False
        """
        return (not (self == other))

    def __rmul__(self, n):
        """
        Return the sum of a graph with itself `n` times.

        EXAMPLES::

            sage: G = graphs.CycleGraph(3)
            sage: H = int(3) * G; H
            Cycle graph disjoint_union Cycle graph disjoint_union Cycle graph: Graph on 9 vertices
            sage: H.vertices(sort=True)
            [0, 1, 2, 3, 4, 5, 6, 7, 8]
        """
        return self * n

    def __str__(self):
        """
        str(G) returns the name of the graph, unless the name is the empty
        string, in which case it returns the default representation.

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: str(G)
            'Petersen graph'
        """
        if self.name():
            return self.name()
        else:
            return repr(self)

    def _bit_vector(self):
        """
        Return a string representing the edges of the (simple) graph for
        ``graph6`` and ``dig6`` strings.

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: G._bit_vector()
            '101001100110000010000001001000010110000010110'
            sage: len([a for a in G._bit_vector() if a == '1'])
            15
            sage: G.num_edges()
            15

        TESTS:

        Check that :trac:`27695` is fixed::

            sage: G = Graph([[0,1,2],[(0,1)]])
            sage: G.relabel({0:2,2:0})
            sage: G._bit_vector()
            '001'

        Check that :trac:`27695` fixes :trac:`26800`::

            sage: P = graphs.PetersenGraph()
            sage: v = P.random_vertex()
            sage: P.add_cycle(P.neighbors(v))
            sage: P.delete_vertex(v)
            sage: P.canonical_label(algorithm='sage')._bit_vector()
            '001100001111000000011010100110100011'
        """
        self._scream_if_not_simple()
        n = self.order()
        if self._directed:
            total_length = n * n

            def bit(x, y):
                return x * n + y
        else:
            total_length = (n * (n - 1)) // 2

            def n_ch_2(b):
                return int(b * (b - 1)) // 2

            def bit(x, y):
                return n_ch_2(max(x, y)) + min(x, y)

        bit_vector = set()

        try:
            V = sorted(self)
        except TypeError:
            V = self
        v_to_int = {v: i for i, v in enumerate(V)}
        for u, v in self.edge_iterator(labels=False):
            bit_vector.add(bit(v_to_int[u], v_to_int[v]))
        bit_vector = sorted(bit_vector)
        s = []
        j = 0
        for i in bit_vector:
            s.append('0' * (i - j) + '1')
            j = i + 1
        s = "".join(s)
        s += '0' * (total_length - len(s))
        return s

    def _latex_(self):
        r"""
        Return a string to render the graph using `\LaTeX`.

        To adjust the string, use the :meth:`set_latex_options` method to set
        options, or call the :meth:`latex_options` method to get a
        :class:`~sage.graphs.graph_latex.GraphLatex` object that may be used to
        also customize the output produced here.  Possible options are
        documented at :meth:`sage.graphs.graph_latex.GraphLatex.set_option`.

        EXAMPLES::

            sage: from sage.graphs.graph_latex import check_tkz_graph
            sage: check_tkz_graph()  # random - depends on TeX installation
            sage: g = graphs.CompleteGraph(2)
            sage: print(g._latex_())
            \begin{tikzpicture}
            \definecolor{cv0}{rgb}{0.0,0.0,0.0}
            \definecolor{cfv0}{rgb}{1.0,1.0,1.0}
            \definecolor{clv0}{rgb}{0.0,0.0,0.0}
            \definecolor{cv1}{rgb}{0.0,0.0,0.0}
            \definecolor{cfv1}{rgb}{1.0,1.0,1.0}
            \definecolor{clv1}{rgb}{0.0,0.0,0.0}
            \definecolor{cv0v1}{rgb}{0.0,0.0,0.0}
            %
            \Vertex[style={minimum size=1.0cm,draw=cv0,fill=cfv0,text=clv0,shape=circle},LabelOut=false,L=\hbox{$0$},x=2.5cm,y=5.0cm]{v0}
            \Vertex[style={minimum size=1.0cm,draw=cv1,fill=cfv1,text=clv1,shape=circle},LabelOut=false,L=\hbox{$1$},x=2.5cm,y=0.0cm]{v1}
            %
            \Edge[lw=0.1cm,style={color=cv0v1,},](v0)(v1)
            %
            \end{tikzpicture}
        """
        from sage.graphs.graph_latex import setup_latex_preamble
        setup_latex_preamble()

        return self.latex_options().latex()

    def _matrix_(self, R=None, vertices=None):
        """
        Return the adjacency matrix of the graph over the specified ring.

        INPUT:

        - ``R`` -- a ring

        - ``vertices`` -- list (default: ``None``); the ordering of the vertices
          defining how they should appear in the matrix. By default, the
          ordering given by :meth:`GenericGraph.vertices` is used.

        EXAMPLES::

            sage: G = graphs.CompleteBipartiteGraph(2, 3)
            sage: m = matrix(G); m.parent()
            Full MatrixSpace of 5 by 5 dense matrices over Integer Ring
            sage: m
            [0 0 1 1 1]
            [0 0 1 1 1]
            [1 1 0 0 0]
            [1 1 0 0 0]
            [1 1 0 0 0]
            sage: G._matrix_()
            [0 0 1 1 1]
            [0 0 1 1 1]
            [1 1 0 0 0]
            [1 1 0 0 0]
            [1 1 0 0 0]
            sage: factor(m.charpoly())
            x^3 * (x^2 - 6)
        """
        return self.am(vertices=vertices, base_ring=R)

    def _repr_(self):
        """
        Return a string representation of the graph.

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: G._repr_()
            'Petersen graph: Graph on 10 vertices'
        """
        name = ""
        if self.allows_loops():
            name += "looped "
        if self.allows_multiple_edges():
            name += "multi-"
        if self._directed:
            name += "di"
        name += "graph on %d vert" % self.order()
        if self.order() == 1:
            name += "ex"
        else:
            name += "ices"
        name = name.capitalize()
        if self.name() != '':
            name = self.name() + ": " + name
        return name

    def is_immutable(self):
        """
        Check whether the graph is immutable.

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: G.is_immutable()
            False
            sage: Graph(G, immutable=True).is_immutable()
            True
        """
        return getattr(self, '_immutable', False)

    # Formats

    def copy(self, weighted=None, data_structure=None, sparse=None, immutable=None):
        """
        Change the graph implementation

        INPUT:

        - ``weighted`` -- boolean (default: ``None``); weightedness for the
          copy. Might change the equality class if not ``None``.

        - ``sparse`` -- boolean (default: ``None``); ``sparse=True`` is an alias
          for ``data_structure="sparse"``, and ``sparse=False`` is an alias for
          ``data_structure="dense"``. Only used when ``data_structure=None``.

        - ``data_structure`` -- string (default: ``None``); one of ``"sparse"``,
          ``"static_sparse"``, or ``"dense"``. See the documentation of
          :class:`Graph` or :class:`DiGraph`.

        - ``immutable`` -- boolean (default: ``None``); whether to create a
          mutable/immutable copy. Only used when ``data_structure=None``.

          * ``immutable=None`` (default) means that the graph and its copy will
            behave the same way.

          * ``immutable=True`` is a shortcut for
            ``data_structure='static_sparse'``

          * ``immutable=False`` means that the created graph is mutable. When
            used to copy an immutable graph, the data structure used is
            ``"sparse"`` unless anything else is specified.

        .. NOTE::

            If the graph uses
            :class:`~sage.graphs.base.static_sparse_backend.StaticSparseBackend`
            and the ``_immutable`` flag, then ``self`` is returned rather than a
            copy (unless one of the optional arguments is used).

        OUTPUT:

        A Graph object.

        .. WARNING::

           Please use this method only if you need to copy but change the
           underlying data structure or weightedness. Otherwise simply do
           ``copy(g)`` instead of ``g.copy()``.

        .. WARNING::

           If ``weighted`` is passed and is not the weightedness of the
           original, then the copy will not equal the original.

        EXAMPLES::

            sage: g = Graph({0: [0, 1, 1, 2]}, loops=True, multiedges=True, sparse=True)
            sage: g == copy(g)
            True
            sage: g = DiGraph({0: [0, 1, 1, 2], 1: [0, 1]}, loops=True, multiedges=True, sparse=True)
            sage: g == copy(g)
            True

        Note that vertex associations are also kept::

            sage: d = {0: graphs.DodecahedralGraph(), 1: graphs.FlowerSnark(), 2: graphs.MoebiusKantorGraph(), 3: graphs.PetersenGraph()}
            sage: T = graphs.TetrahedralGraph()
            sage: T.set_vertices(d)
            sage: T2 = copy(T)
            sage: T2.get_vertex(0)
            Dodecahedron: Graph on 20 vertices

        Notice that the copy is at least as deep as the objects::

            sage: T2.get_vertex(0) is T.get_vertex(0)
            False

        Examples of the keywords in use::

            sage: G = graphs.CompleteGraph(9)
            sage: H = G.copy()
            sage: H == G; H is G
            True
            False
            sage: G1 = G.copy(sparse=True)
            sage: G1 == G
            True
            sage: G1 is G
            False
            sage: G2 = copy(G)
            sage: G2 is G
            False

        Argument ``weighted`` affects the equality class::

            sage: G = graphs.CompleteGraph(5)
            sage: H1 = G.copy(weighted=False)
            sage: H2 = G.copy(weighted=True)
            sage: [G.weighted(), H1.weighted(), H2.weighted()]
            [False, False, True]
            sage: [G == H1, G == H2, H1 == H2]
            [True, False, False]
            sage: G.weighted(True)
            sage: [G == H1, G == H2, H1 == H2]
            [False, True, False]

        TESTS:

        We make copies of the ``_pos`` attribute::

            sage: g = graphs.PathGraph(3)
            sage: h = copy(g)
            sage: h._pos is g._pos
            False

        We make sure that one can make immutable copies by providing the
        ``data_structure`` optional argument, and that copying an immutable
        graph returns the graph::

            sage: G = graphs.PetersenGraph()
            sage: hash(G)
            Traceback (most recent call last):
            ...
            TypeError: This graph is mutable, and thus not hashable. Create an
            immutable copy by `g.copy(immutable=True)`
            sage: g = G.copy(immutable=True)
            sage: hash(g)    # random
            1833517720
            sage: g==G
            True
            sage: (g is g.copy()) and (g is not copy(g))
            True

        ``immutable=True`` is a short-cut for
        ``data_structure='static_sparse'``::

            sage: g is g.copy(data_structure='static_sparse') is g.copy(immutable=True)
            True

        If a graph pretends to be immutable, but does not use the static sparse
        backend, then the copy is not identical with the graph, even though it
        is considered to be hashable::

            sage: P = Poset(([1, 2, 3, 4], [[1, 3], [1, 4], [2, 3]]), linear_extension=True, facade=False)
            sage: H = P.hasse_diagram()
            sage: H._immutable = True
            sage: hash(H)   # random
            -1843552882
            sage: copy(H) is H
            False

        Bad input::

            sage: G.copy(data_structure="sparse", sparse=False)
            Traceback (most recent call last):
            ...
            ValueError: you cannot define 'immutable' or 'sparse' when 'data_structure' has a value
            sage: G.copy(data_structure="sparse", immutable=True)
            Traceback (most recent call last):
            ...
            ValueError: you cannot define 'immutable' or 'sparse' when 'data_structure' has a value
            sage: G.copy(immutable=True, sparse=False)
            Traceback (most recent call last):
            ...
            ValueError: there is no dense immutable backend at the moment

        Which backend? ::

            sage: G.copy(data_structure="sparse")._backend
            <sage.graphs.base.sparse_graph.SparseGraphBackend object at ...>
            sage: G.copy(data_structure="dense")._backend
            <sage.graphs.base.dense_graph.DenseGraphBackend object at ...>
            sage: G.copy(data_structure="static_sparse")._backend
            <sage.graphs.base.static_sparse_backend.StaticSparseBackend object at ...>
            sage: G.copy(immutable=True)._backend
            <sage.graphs.base.static_sparse_backend.StaticSparseBackend object at ...>
            sage: G.copy(immutable=True, sparse=True)._backend
            <sage.graphs.base.static_sparse_backend.StaticSparseBackend object at ...>
            sage: G.copy(immutable=False, sparse=True)._backend
            <sage.graphs.base.sparse_graph.SparseGraphBackend object at ...>
            sage: G.copy(immutable=False, sparse=False)._backend
            <sage.graphs.base.sparse_graph.SparseGraphBackend object at ...>

        Fake immutable graphs::

            sage: G._immutable = True
            sage: G.copy()._backend
            <sage.graphs.base.sparse_graph.SparseGraphBackend object at ...>
        """
        # Which data structure should be used ?
        if data_structure is not None:
            # data_structure is already defined so there is nothing left to do
            # here ! Did the user try to define too much ?
            if immutable is not None or sparse is not None:
                raise ValueError("you cannot define 'immutable' or 'sparse' "
                                 "when 'data_structure' has a value")
        # At this point :
        # - data_structure is None.
        elif immutable is True:
            data_structure = 'static_sparse'
            if sparse is False:
                raise ValueError("there is no dense immutable backend at the moment")
        elif immutable is False:
            # If the users requests a mutable graph and input is immutable, we
            # choose the 'sparse' cgraph backend. Unless the user explicitly
            # asked for something different.
            if self.is_immutable():
                data_structure = 'dense' if sparse is False else 'sparse'
        elif sparse is True:
            data_structure = "sparse"
        elif sparse is False:
            data_structure = "dense"

        # Immutable copy of an immutable graph ? return self !
        # (if okay for weightedness)
        if (self.is_immutable() and
                (weighted is None or self._weighted == weighted)):
            from sage.graphs.base.static_sparse_backend import StaticSparseBackend
            if (isinstance(self._backend, StaticSparseBackend) and
                    (data_structure == 'static_sparse' or data_structure is None)):
                return self

        if data_structure is None:
            from sage.graphs.base.dense_graph import DenseGraphBackend
            if isinstance(self._backend, DenseGraphBackend):
                data_structure = "dense"
            else:
                data_structure = "sparse"

        G = self.__class__(self, name=self.name(), pos=copy(self._pos),
                           weighted=weighted,
                           data_structure=data_structure)

        attributes_to_copy = ('_assoc', '_embedding')
        for attr in attributes_to_copy:
            if hasattr(self, attr):
                copy_attr = {}
                old_attr = getattr(self, attr)
                if isinstance(old_attr, dict):
                    for v, value in old_attr.items():
                        try:
                            copy_attr[v] = value.copy()
                        except AttributeError:
                            copy_attr[v] = copy(value)
                    setattr(G, attr, copy_attr)
                else:
                    setattr(G, attr, copy(old_attr))

        return G

    def __copy__(self):
        """
        Copy the graph.

        OUTPUT:

        A new graph instance that is as close as possible to the original
        graph. The output is always mutable.

        EXAMPLES::

            sage: g = Graph({0: [1, 2, 3], 2: [4]}, immutable=True)
            sage: g.weighted(list(range(5)))
            Traceback (most recent call last):
            ...
            TypeError: This graph is immutable and can thus not be changed.
            Create a mutable copy, e.g., by `copy(g)`
            sage: h = copy(g)    # indirect doctest
            sage: h.add_vertex()
            5
        """
        return self.copy(immutable=False)

    def export_to_file(self, filename, format=None, **kwds):
        r"""
        Export the graph to a file.

        INPUT:

        - ``filename`` -- string; a file name

        - ``format`` -- string (default: ``None``); select the output format
          explicitly. If set to ``None`` (default), the format is set to be the
          file extension of ``filename``. Admissible formats are: ``adjlist``,
          ``dot``, ``edgelist``, ``gexf``, ``gml``, ``graphml``,
          ``multiline_adjlist``, ``pajek``, ``yaml``.

        - All other arguments are forwarded to the subfunction. For more
          information, see their respective documentation:

          .. csv-table::
              :class: contentstable
              :widths: 30, 70
              :delim: |

              ``adjlist`` | http://networkx.lanl.gov/reference/generated/networkx.readwrite.adjlist.write_adjlist.html
              ``dot`` | https://networkx.github.io/documentation/latest/reference/generated/networkx.drawing.nx_pydot.write_dot.html
              ``edgelist`` | http://networkx.lanl.gov/reference/generated/networkx.readwrite.edgelist.write_edgelist.html
              ``gexf`` | http://networkx.lanl.gov/reference/generated/networkx.readwrite.gexf.write_gexf.html
              ``gml`` | http://networkx.lanl.gov/reference/generated/networkx.readwrite.gml.write_gml.html
              ``graphml`` | http://networkx.lanl.gov/reference/generated/networkx.readwrite.graphml.write_graphml.html
              ``multiline_adjlist`` | http://networkx.lanl.gov/reference/generated/networkx.readwrite.multiline_adjlist.write_multiline_adjlist.html
              ``pajek`` | http://networkx.lanl.gov/reference/generated/networkx.readwrite.pajek.write_pajek.html
              ``yaml`` | http://networkx.lanl.gov/reference/generated/networkx.readwrite.nx_yaml.write_yaml.html

        .. SEEALSO::

            * :meth:`~sage.structure.sage_object.SageObject.save` -- save a Sage
              object to a 'sobj' file (preserves all its attributes)

        .. NOTE::

            This functions uses the ``write_*`` functions defined in NetworkX
            (see http://networkx.lanl.gov/reference/readwrite.html).

        EXAMPLES::

            sage: g = graphs.PetersenGraph()
            sage: filename = tmp_filename(ext=".pajek")
            sage: g.export_to_file(filename)
            sage: import networkx
            sage: G_networkx = networkx.read_pajek(filename)
            sage: Graph(G_networkx).is_isomorphic(g)
            True
            sage: filename = tmp_filename(ext=".edgelist")
            sage: g.export_to_file(filename, data=False)
            sage: h = Graph(networkx.read_edgelist(filename))
            sage: g.is_isomorphic(h)
            True

        TESTS::

            sage: g.export_to_file("hey", format="When I feel heavy metaaaaaallll...")
            Traceback (most recent call last):
            ...
            ValueError: format 'When I feel heavy metaaaaaallll...' unknown
            sage: g.export_to_file("my_file.Yeeeeppeeeeee")
            Traceback (most recent call last):
            ...
            RuntimeError: the file format could not be guessed from 'my_file.Yeeeeppeeeeee'
        """
        import networkx

        formats = {"adjlist"           : networkx.write_adjlist,
                   "dot"               : networkx.drawing.nx_pydot.write_dot,
                   "edgelist"          : networkx.write_edgelist,
                   "gexf"              : networkx.write_gexf,
                   "gml"               : networkx.write_gml,
                   "graphml"           : networkx.write_graphml,
                   "multiline_adjlist" : networkx.write_multiline_adjlist,
                   "pajek"             : networkx.write_pajek}

        if format is None:
            ext = filename[1 + filename.rfind("."):]
            if ext not in formats:
                raise RuntimeError("the file format could not be guessed from '{}'".format(filename))
            format = ext

        if format not in formats:
            raise ValueError("format '{}' unknown".format(format))

        formats[format](self.networkx_graph(), filename, **kwds)

    def _scream_if_not_simple(self, allow_loops=False, allow_multiple_edges=False):
        r"""
        Raise an exception if the graph is not simple.

        This function is called by some functions of the Graph library when they
        have been written for simple graphs only (i.e. neither loops nor
        multiple edges). It raises an exception inviting the user to convert the
        graph to a simple graph first, before calling the function again.

        Note that this function does not check the existence of loops or
        multiple edges, which would take linear time: it merely checks that the
        graph *does not allow* multiple edges nor loops, which takes a constant
        time.

        INPUT:

        - ``allow_loops`` -- boolean (default: ``False``); whether to tolerate
          loops

        - ``allow_multiple_edges`` -- boolean (default: ``False``); whether to
          tolerate multiple edges

        .. SEEALSO::

            * :meth:`allow_loops`
            * :meth:`allow_multiple_edges`

        EXAMPLES::

            sage: g = graphs.PetersenGraph()

        No scream::

            sage: from itertools import product
            sage: for p, q in product((True, False), repeat=2):
            ....:     g.allow_loops(p)
            ....:     g.allow_multiple_edges(q)
            ....:     g._scream_if_not_simple(p, q)

        A lot of them::

            sage: g.allow_loops(True); g.allow_multiple_edges(True)
            sage: g._scream_if_not_simple()
            Traceback (most recent call last):
            ...
            ValueError: This method is not known to work on graphs with multiedges/loops. Perhaps this method can be updated to handle them, but in the meantime if you want to use it please disallow multiedges/loops using allow_multiple_edges() and allow_loops().
            sage: g._scream_if_not_simple(allow_loops=True)
            Traceback (most recent call last):
            ...
            ValueError: This method is not known to work on graphs with multiedges. Perhaps this method can be updated to handle them, but in the meantime if you want to use it please disallow multiedges using allow_multiple_edges().
            sage: g._scream_if_not_simple(allow_multiple_edges=True)
            Traceback (most recent call last):
            ...
            ValueError: This method is not known to work on graphs with loops. Perhaps this method can be updated to handle them, but in the meantime if you want to use it please disallow loops using allow_loops().

            sage: g.allow_loops(True); g.allow_multiple_edges(False)
            sage: g._scream_if_not_simple()
            Traceback (most recent call last):
            ...
            ValueError: This method is not known to work on graphs with loops. Perhaps this method can be updated to handle them, but in the meantime if you want to use it please disallow loops using allow_loops().
            sage: g._scream_if_not_simple(allow_multiple_edges=True)
            Traceback (most recent call last):
            ...
            ValueError: This method is not known to work on graphs with loops. Perhaps this method can be updated to handle them, but in the meantime if you want to use it please disallow loops using allow_loops().
        """
        pb_with_loops = not allow_loops and self.allows_loops()
        pb_with_multiple_edges = not allow_multiple_edges and self.allows_multiple_edges()
        if pb_with_loops or pb_with_multiple_edges:
            if pb_with_loops and pb_with_multiple_edges:
                name = "multiedges/loops"
                functions = "allow_multiple_edges() and allow_loops()"
            elif pb_with_loops:
                name = "loops"
                functions = "allow_loops()"
            elif pb_with_multiple_edges:
                name = "multiedges"
                functions = "allow_multiple_edges()"
            msg = ("This method is not known to work on graphs with " + name + ". "
                   "Perhaps this method can be updated to handle them, but in the " +
                   "meantime if you want to use it please disallow " + name + " using " +
                   functions + ".")
            raise ValueError(msg)

    def networkx_graph(self, weight_function=None):
        """
        Return a new ``NetworkX`` graph from the Sage graph.

        INPUT:

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight.

        EXAMPLES::

            sage: G = graphs.TetrahedralGraph()
            sage: N = G.networkx_graph()
            sage: type(N)
            <class 'networkx.classes.graph.Graph'>

            sage: def weight_fn(e):
            ....:     return e[2]
            sage: G1 = Graph([(1,2,1), (1,3,4), (2,3,3), (3,4,4)])
            sage: H = G1.networkx_graph(weight_function=weight_fn)
            sage: H.edges(data=True)
            EdgeDataView([(1, 2, {'weight': 1}), (1, 3, {'weight': 4}), (2, 3, {'weight': 3}), (3, 4, {'weight': 4})])
            sage: G2 = DiGraph([(1,2,1), (1,3,4), (2,3,3), (3,4,4), (3,4,5)], multiedges=True)
            sage: H = G2.networkx_graph(weight_function=weight_fn)
            sage: H.edges(data=True)
            OutMultiEdgeDataView([(1, 2, {'weight': 1}), (1, 3, {'weight': 4}), (2, 3, {'weight': 3}), (3, 4, {'weight': 5}), (3, 4, {'weight': 4})])

        """
        if weight_function is not None:
            self._check_weight_function(weight_function)
        import networkx
        if self._directed and self.allows_multiple_edges():
            class_type = networkx.MultiDiGraph
        elif self._directed:
            class_type = networkx.DiGraph
        elif self.allows_multiple_edges():
            class_type = networkx.MultiGraph
        else:
            class_type = networkx.Graph
        N = class_type(selfloops=self.allows_loops(), multiedges=self.allows_multiple_edges(),
                       name=self.name())
        N.add_nodes_from(self)
        from networkx import NetworkXError
        for u, v, l in self.edge_iterator():
            if weight_function is not None:
                N.add_edge(u, v, weight=weight_function((u, v, l)))
            elif l is None:
                N.add_edge(u, v)
            else:
                try:
                    N.add_edge(u, v, l)
                except (TypeError, ValueError, NetworkXError):
                    N.add_edge(u, v, weight=l)
        return N

    def igraph_graph(self, vertex_list=None, vertex_attrs={}, edge_attrs={}):
        r"""
        Return an ``igraph`` graph from the Sage graph.

        Optionally, it is possible to add vertex attributes and edge attributes
        to the output graph.

        .. NOTE::

            This routine needs the optional package igraph to be installed:
            to do so, it is enough to run ``sage -i python_igraph``. For more
            information on the Python version of igraph, see
            http://igraph.org/python/.

        INPUT:

        - ``vertex_list`` -- list (default: ``None``); defines a mapping from
          the vertices of the graph to consecutive integers in ``(0, \ldots,
          n-1)`. Otherwise, the result of :meth:`vertices` will be used
          instead. Because :meth:`vertices` only works if the vertices can be
          sorted, using ``vertex_list`` is useful when working with possibly
          non-sortable objects in Python 3.

        - ``vertex_attrs`` -- dictionary (default: ``{}``); a dictionary where
          the key is a string (the attribute name), and the value is an iterable
          containing in position `i` the label of the `i`-th vertex in the list
          ``vertex_list`` if it is given or in :meth:`vertices` when
          ``vertex_list == None`` (see
          http://igraph.org/python/doc/igraph.Graph-class.html#__init__ for more
          information)

        - ``edge_attrs`` -- dictionary (default: ``{}``); a dictionary where the
          key is a string (the attribute name), and the value is an iterable
          containing in position `i` the label of the `i`-th edge in the list
          outputted by :meth:`edge_iterator` (see
          http://igraph.org/python/doc/igraph.Graph-class.html#__init__ for more
          information)

        .. NOTE::

            In ``igraph``, a graph is weighted if the edge labels have attribute
            ``weight``. Hence, to create a weighted graph, it is enough to add
            this attribute.

        .. NOTE::

            Often, Sage uses its own defined types for integer/floats. These
            types may not be igraph-compatible (see example below).

        EXAMPLES:

        Standard conversion::

            sage: G = graphs.TetrahedralGraph()
            sage: H = G.igraph_graph()          # optional - python_igraph
            sage: H.summary()                   # optional - python_igraph
            'IGRAPH U--- 4 6 -- '
            sage: G = digraphs.Path(3)
            sage: H = G.igraph_graph()          # optional - python_igraph
            sage: H.summary()                   # optional - python_igraph
            'IGRAPH D--- 3 2 -- '

        Adding edge attributes::

            sage: G = Graph([(1, 2, 'a'), (2, 3, 'b')])
            sage: E = list(G.edge_iterator())
            sage: H = G.igraph_graph(edge_attrs={'label': [e[2] for e in E]}) # optional - python_igraph
            sage: H.es['label']                                               # optional - python_igraph
            ['a', 'b']


        If edges have an attribute ``weight``, the igraph graph is considered
        weighted::

            sage: G = Graph([(1, 2, {'weight': 1}), (2, 3, {'weight': 2})])
            sage: E = list(G.edge_iterator())
            sage: H = G.igraph_graph(edge_attrs={'weight': [e[2]['weight'] for e in E]}) # optional - python_igraph
            sage: H.is_weighted()                                                        # optional - python_igraph
            True
            sage: H.es['weight']                                                         # optional - python_igraph
            [1, 2]

        Adding vertex attributes::

            sage: G = graphs.GridGraph([2, 2])
            sage: H = G.igraph_graph(vertex_attrs={'name': G.vertices(sort=True)}) # optional - python_igraph
            sage: H.vs()['name']                                          # optional - python_igraph
            [(0, 0), (0, 1), (1, 0), (1, 1)]

        Providing a mapping from vertices to consecutive integers::

            sage: G = graphs.GridGraph([2, 2])
            sage: V = list(G)
            sage: H = G.igraph_graph(vertex_list=V, vertex_attrs={'name': V}) # optional - python_igraph
            sage: H.vs()['name'] == V                                         # optional - python_igraph
            True

        Sometimes, Sage integer/floats are not compatible with igraph::

            sage: G = Graph([(0, 1, 2)])
            sage: E = list(G.edge_iterator())
            sage: H = G.igraph_graph(edge_attrs={'capacity': [e[2] for e in E]}) # optional - python_igraph
            sage: H.maxflow_value(0, 1, 'capacity')                              # optional - python_igraph
            1.0
            sage: H = G.igraph_graph(edge_attrs={'capacity': [float(e[2]) for e in E]}) # optional - python_igraph
            sage: H.maxflow_value(0, 1, 'capacity')                                     # optional - python_igraph
            2.0

        TESTS:

        Converting a DiGraph back and forth::

            sage: G = DiGraph([('a', 'b', {'w': 1}), ('b', 'c', {'w': 2})])
            sage: vertex_attrs = {'name': G.vertices(sort=False)}
            sage: E = list(G.edge_iterator())
            sage: edge_attrs = {'w': [e[2]['w'] for e in E]}
            sage: H = DiGraph(G.igraph_graph(vertex_attrs=vertex_attrs, edge_attrs=edge_attrs)) # optional - python_igraph
            sage: G == H                                                                        # optional - python_igraph
            True
            sage: G.edges(sort=True) == H.edges(sort=True)                                      # optional - python_igraph
            True
            sage: H = DiGraph(G.igraph_graph(edge_attrs=edge_attrs))                            # optional - python_igraph
            sage: G == H                                                                        # optional - python_igraph
            False

        When checking for equality, edge labels are not taken into account::

            sage: H = DiGraph(G.igraph_graph(vertex_attrs=vertex_attrs)) # optional - python_igraph
            sage: G == H                                                 # optional - python_igraph
            True
            sage: G.edges(sort=True) == H.edges(sort=True)               # optional - python_igraph
            False

        Converting a Graph back and forth::

            sage: G = Graph([('a', 'b', {'w': 1}), ('b', 'c', {'w': 2})])
            sage: vertex_attrs = {'name': G.vertices(sort=False)}
            sage: E = list(G.edge_iterator())
            sage: edge_attrs = {'w': [e[2]['w'] for e in E]}
            sage: H = Graph(G.igraph_graph(vertex_attrs=vertex_attrs, edge_attrs=edge_attrs)) # optional - python_igraph
            sage: G == H                                                                      # optional - python_igraph
            True
            sage: G.edges(sort=True) == H.edges(sort=True)                                    # optional - python_igraph
            True
            sage: H = Graph(G.igraph_graph(edge_attrs=edge_attrs))                            # optional - python_igraph
            sage: G == H                                                                      # optional - python_igraph
            False

        When checking for equality, edge labels are not taken into account::

            sage: H = Graph(G.igraph_graph(vertex_attrs=vertex_attrs)) # optional - python_igraph
            sage: G == H                                               # optional - python_igraph
            True
            sage: G.edges(sort=True) == H.edges(sort=True)             # optional - python_igraph
            False
        """
        if vertex_list is None:
            vertex_list = self.vertices(sort=False)

        v_to_int = {v: i for i, v in enumerate(vertex_list)}
        edges = [(v_to_int[v], v_to_int[w]) for v, w in self.edge_iterator(labels=False)]

        igraph_feature().require()
        import igraph
        return igraph.Graph(n=self.num_verts(),
                            edges=edges,
                            directed=self.is_directed(),
                            vertex_attrs=vertex_attrs,
                            edge_attrs=edge_attrs)

    def to_dictionary(self, edge_labels=False, multiple_edges=False):
        r"""
        Return the graph as a dictionary.

        INPUT:

        - ``edge_labels`` -- boolean (default: ``False``); whether to include
          edge labels in the output

        - ``multiple_edges`` -- boolean (default: ``False``); whether to include
          multiple edges in the output

        OUTPUT:

        The output depends on the input:

        * If ``edge_labels == False`` and ``multiple_edges == False``, the
          output is a dictionary associating to each vertex the list of its
          neighbors.

        * If ``edge_labels == False`` and ``multiple_edges == True``, the output
          is a dictionary the same as previously with one difference: the
          neighbors are listed with multiplicity.

        * If ``edge_labels == True`` and ``multiple_edges == False``, the output
          is a dictionary associating to each vertex `u` [a dictionary
          associating to each vertex `v` incident to `u` the label of edge
          `(u,v)`].

        * If ``edge_labels == True`` and ``multiple_edges == True``, the output
          is a dictionary associating to each vertex `u` [a dictionary
          associating to each vertex `v` incident to `u` [the list of labels of
          all edges between `u` and `v`]].

        .. NOTE::

            When used on directed graphs, the explanations above can be
            understood by replacing the word "neighbors" by "out-neighbors"

        EXAMPLES::

            sage: g = graphs.PetersenGraph().to_dictionary()
            sage: [(key, sorted(g[key])) for key in g]
            [(0, [1, 4, 5]),
             (1, [0, 2, 6]),
             (2, [1, 3, 7]),
             (3, [2, 4, 8]),
             (4, [0, 3, 9]),
             (5, [0, 7, 8]),
             (6, [1, 8, 9]),
             (7, [2, 5, 9]),
             (8, [3, 5, 6]),
             (9, [4, 6, 7])]
            sage: graphs.PetersenGraph().to_dictionary(multiple_edges=True)
            {0: [1, 4, 5], 1: [0, 2, 6],
             2: [1, 3, 7], 3: [2, 4, 8],
             4: [0, 3, 9], 5: [0, 7, 8],
             6: [1, 8, 9], 7: [2, 5, 9],
             8: [3, 5, 6], 9: [4, 6, 7]}
            sage: graphs.PetersenGraph().to_dictionary(edge_labels=True)
            {0: {1: None, 4: None, 5: None},
             1: {0: None, 2: None, 6: None},
             2: {1: None, 3: None, 7: None},
             3: {2: None, 4: None, 8: None},
             4: {0: None, 3: None, 9: None},
             5: {0: None, 7: None, 8: None},
             6: {1: None, 8: None, 9: None},
             7: {2: None, 5: None, 9: None},
             8: {3: None, 5: None, 6: None},
             9: {4: None, 6: None, 7: None}}
            sage: graphs.PetersenGraph().to_dictionary(edge_labels=True,multiple_edges=True)
            {0: {1: [None], 4: [None], 5: [None]},
             1: {0: [None], 2: [None], 6: [None]},
             2: {1: [None], 3: [None], 7: [None]},
             3: {2: [None], 4: [None], 8: [None]},
             4: {0: [None], 3: [None], 9: [None]},
             5: {0: [None], 7: [None], 8: [None]},
             6: {1: [None], 8: [None], 9: [None]},
             7: {2: [None], 5: [None], 9: [None]},
             8: {3: [None], 5: [None], 6: [None]},
             9: {4: [None], 6: [None], 7: [None]}}
        """

        # Returning the results as a dictionary of lists
        #
        # dictionary :
        # {vertex : [list of (out-)neighbors]}

        if not edge_labels and not multiple_edges:
            if self.is_directed():
                d = {u: self.neighbors_out(u) for u in self}
            else:
                d = {u: self.neighbors(u) for u in self}

        # Returning the result as a dictionary of lists
        #
        # dictionary :
        # {vertex : [list of (out-)neighbors, with multiplicity]}
        elif not edge_labels and multiple_edges:
            d = {v: [] for v in self}

            if self.is_directed():
                for u, v in self.edge_iterator(labels=False):
                    d[u].append(v)

            else:
                for u, v in self.edge_iterator(labels=False):
                    d[u].append(v)
                    d[v].append(u)

        # Returning the result as a dictionary of dictionaries
        #
        # Each vertex is associated with the dictionary associating to each of
        # its neighbors the corresponding edge label.
        #
        # dictionary :
        # {v : dictionary                          }
        #      {neighbor u of v : label of edge u,v}

        elif edge_labels and not multiple_edges:
            d = {v: {} for v in self}

            if self.is_directed():
                for u, v, l in self.edge_iterator():
                    d[u][v] = l

            else:
                for u, v, l in self.edge_iterator():
                    d[u][v] = l
                    d[v][u] = l

        # Returning the result as a dictionary of dictionaries
        #
        # Each vertex is associated with the dictionary associating to each of
        # its neighbors the list of edge labels between the two vertices
        #
        # dictionary :
        # {v : dictionary                                          }
        #      {neighbor u of v : [labels of edges between u and v]}

        elif edge_labels and multiple_edges:
            d = {v: {} for v in self}

            if self.is_directed():
                for u, v, l in self.edge_iterator():
                    if v not in d[u]:
                        d[u][v] = []
                    d[u][v].append(l)

            else:
                for u, v, l in self.edge_iterator():
                    if v not in d[u]:
                        d[u][v] = []
                        d[v][u] = []

                    d[u][v].append(l)
                    d[v][u].append(l)

        return d

    def adjacency_matrix(self, sparse=None, vertices=None, *, base_ring=None, **kwds):
        r"""
        Return the adjacency matrix of the (di)graph.

        By default, the matrix returned is over the integers.

        INPUT:

        - ``sparse`` -- boolean (default: ``None``); whether to represent with a
          sparse matrix

        - ``vertices`` -- list (default: ``None``); the ordering of
          the vertices defining how they should appear in the
          matrix. By default, the ordering given by
          :meth:`GenericGraph.vertices` with ``sort=True`` is used.

        - ``base_ring`` -- a ring (default: ``ZZ``); the base ring of the matrix
          space to use.

        - ``**kwds`` -- other keywords to pass to
          :func:`~sage.matrix.constructor.matrix`.

        EXAMPLES::

            sage: G = graphs.CubeGraph(4)
            sage: G.adjacency_matrix()
            [0 1 1 0 1 0 0 0 1 0 0 0 0 0 0 0]
            [1 0 0 1 0 1 0 0 0 1 0 0 0 0 0 0]
            [1 0 0 1 0 0 1 0 0 0 1 0 0 0 0 0]
            [0 1 1 0 0 0 0 1 0 0 0 1 0 0 0 0]
            [1 0 0 0 0 1 1 0 0 0 0 0 1 0 0 0]
            [0 1 0 0 1 0 0 1 0 0 0 0 0 1 0 0]
            [0 0 1 0 1 0 0 1 0 0 0 0 0 0 1 0]
            [0 0 0 1 0 1 1 0 0 0 0 0 0 0 0 1]
            [1 0 0 0 0 0 0 0 0 1 1 0 1 0 0 0]
            [0 1 0 0 0 0 0 0 1 0 0 1 0 1 0 0]
            [0 0 1 0 0 0 0 0 1 0 0 1 0 0 1 0]
            [0 0 0 1 0 0 0 0 0 1 1 0 0 0 0 1]
            [0 0 0 0 1 0 0 0 1 0 0 0 0 1 1 0]
            [0 0 0 0 0 1 0 0 0 1 0 0 1 0 0 1]
            [0 0 0 0 0 0 1 0 0 0 1 0 1 0 0 1]
            [0 0 0 0 0 0 0 1 0 0 0 1 0 1 1 0]

        ::

            sage: matrix(GF(2),G) # matrix over GF(2)
            [0 1 1 0 1 0 0 0 1 0 0 0 0 0 0 0]
            [1 0 0 1 0 1 0 0 0 1 0 0 0 0 0 0]
            [1 0 0 1 0 0 1 0 0 0 1 0 0 0 0 0]
            [0 1 1 0 0 0 0 1 0 0 0 1 0 0 0 0]
            [1 0 0 0 0 1 1 0 0 0 0 0 1 0 0 0]
            [0 1 0 0 1 0 0 1 0 0 0 0 0 1 0 0]
            [0 0 1 0 1 0 0 1 0 0 0 0 0 0 1 0]
            [0 0 0 1 0 1 1 0 0 0 0 0 0 0 0 1]
            [1 0 0 0 0 0 0 0 0 1 1 0 1 0 0 0]
            [0 1 0 0 0 0 0 0 1 0 0 1 0 1 0 0]
            [0 0 1 0 0 0 0 0 1 0 0 1 0 0 1 0]
            [0 0 0 1 0 0 0 0 0 1 1 0 0 0 0 1]
            [0 0 0 0 1 0 0 0 1 0 0 0 0 1 1 0]
            [0 0 0 0 0 1 0 0 0 1 0 0 1 0 0 1]
            [0 0 0 0 0 0 1 0 0 0 1 0 1 0 0 1]
            [0 0 0 0 0 0 0 1 0 0 0 1 0 1 1 0]

        ::

            sage: D = DiGraph({0: [1, 2, 3], 1: [0, 2], 2: [3], 3: [4], 4: [0, 5], 5: [1]})
            sage: D.adjacency_matrix()
            [0 1 1 1 0 0]
            [1 0 1 0 0 0]
            [0 0 0 1 0 0]
            [0 0 0 0 1 0]
            [1 0 0 0 0 1]
            [0 1 0 0 0 0]

        A different ordering of the vertices::

            sage: graphs.PathGraph(5).adjacency_matrix(vertices=[2, 4, 1, 3, 0])
            [0 0 1 1 0]
            [0 0 0 1 0]
            [1 0 0 0 1]
            [1 1 0 0 0]
            [0 0 1 0 0]

        A different base ring::

            sage: graphs.PathGraph(5).adjacency_matrix(base_ring=RDF)
            [0.0 1.0 0.0 0.0 0.0]
            [1.0 0.0 1.0 0.0 0.0]
            [0.0 1.0 0.0 1.0 0.0]
            [0.0 0.0 1.0 0.0 1.0]
            [0.0 0.0 0.0 1.0 0.0]
            sage: type(_)
            <class 'sage.matrix.matrix_real_double_dense.Matrix_real_double_dense'>

        A different matrix implementation::

            sage: graphs.PathGraph(5).adjacency_matrix(sparse=False, implementation='numpy')
            [0 1 0 0 0]
            [1 0 1 0 0]
            [0 1 0 1 0]
            [0 0 1 0 1]
            [0 0 0 1 0]
            sage: type(_)
            <class 'sage.matrix.matrix_numpy_integer_dense.Matrix_numpy_integer_dense'>

        As an immutable matrix::

            sage: M = graphs.PathGraph(5).adjacency_matrix(sparse=False, immutable=True); M
            [0 1 0 0 0]
            [1 0 1 0 0]
            [0 1 0 1 0]
            [0 0 1 0 1]
            [0 0 0 1 0]
            sage: M[2, 2] = 1
            Traceback (most recent call last):
            ...
            ValueError: matrix is immutable; please change a copy instead (i.e., use copy(M) to change a copy of M).

        TESTS::

            sage: graphs.CubeGraph(8).adjacency_matrix().parent()
            Full MatrixSpace of 256 by 256 dense matrices over Integer Ring
            sage: graphs.CubeGraph(9).adjacency_matrix().parent()
            Full MatrixSpace of 512 by 512 sparse matrices over Integer Ring
            sage: Graph([(i,i+1) for i in range(500)]+[(0,1),], multiedges=True).adjacency_matrix().parent()
            Full MatrixSpace of 501 by 501 dense matrices over Integer Ring
            sage: graphs.PathGraph(5).adjacency_matrix(vertices=[0,0,0,0,0])
            Traceback (most recent call last):
            ...
            ValueError: ``vertices`` must be a permutation of the vertices
            sage: graphs.PathGraph(5).adjacency_matrix(vertices=[1,2,3])
            Traceback (most recent call last):
            ...
            ValueError: ``vertices`` must be a permutation of the vertices
        """
        n = self.order()
        if sparse is None:
            sparse = True
            if self.has_multiple_edges() or n <= 256 or self.density() > 0.05:
                sparse = False

        if vertices is None:
            vertices = self.vertices(sort=True)
        elif (len(vertices) != n or
              set(vertices) != set(self.vertex_iterator())):
            raise ValueError("``vertices`` must be a permutation of the vertices")

        new_indices = {v: i for i, v in enumerate(vertices)}
        D = {}
        directed = self._directed
        multiple_edges = self.allows_multiple_edges()
        for u, v, l in self.edge_iterator():
            i = new_indices[u]
            j = new_indices[v]
            if multiple_edges and (i, j) in D:
                D[i, j] += 1
                if not directed and i != j:
                    D[j, i] += 1
            else:
                D[i, j] = 1
                if not directed and i != j:
                    D[j, i] = 1
        from sage.matrix.constructor import matrix
        if base_ring is None:
            base_ring = ZZ
        M = matrix(base_ring, n, n, D, sparse=sparse, **kwds)
        return M

    am = adjacency_matrix  # shorter call makes life easier

    def incidence_matrix(self, oriented=None, sparse=True, vertices=None, edges=None,
                         *, base_ring=None, **kwds):
        r"""
        Return the incidence matrix of the (di)graph.

        Each row is a vertex, and each column is an edge. The vertices are
        ordered as obtained by the method :meth:`vertices`, except when
        parameter ``vertices`` is given (see below), and the edges as obtained
        by the method :meth:`edge_iterator`.

        If the graph is not directed, then return a matrix with entries in
        `\{0,1,2\}`. Each column will either contain two `1` (at the position of
        the endpoint of the edge), or one `2` (if the corresponding edge is a
        loop).

        If the graph is directed return a matrix in `\{-1,0,1\}` where `-1` and
        `+1` correspond respectively to the source and the target of the edge. A
        loop will correspond to a zero column. In particular, it is not possible
        to recover the loops of an oriented graph from its incidence matrix.

        See the :wikipedia:`Incidence_matrix` for more information.

        INPUT:

        - ``oriented`` -- boolean (default: ``None``); when set to ``True``, the
          matrix will be oriented (i.e. with entries in `-1`, `0`, `1`) and if
          set to ``False`` the matrix will be not oriented (i.e. with entries in
          `0`, `1`, `2`). By default, this argument is inferred from the graph
          type.  Note that in the case the graph is not directed and with the
          option ``directed=True``, a somewhat random direction is chosen for
          each edge.

        - ``sparse`` -- boolean (default: ``True``); whether to use a sparse or
          a dense matrix

        - ``vertices`` -- list (default: ``None``); when specified, the `i`-th
          row of the matrix corresponds to the `i`-th vertex in the ordering of
          ``vertices``, otherwise, the `i`-th row of the matrix corresponds to
          the `i`-th vertex in the ordering given by method :meth:`vertices`.

        - ``edges`` -- list (default: ``None``); when specified, the `i`-th
          column of the matrix corresponds to the `i`-th edge in the ordering of
          ``edges``, otherwise, the `i`-th column of the matrix corresponds to
          the `i`-th edge in the ordering given by method :meth:`edge_iterator`.

        - ``base_ring`` -- a ring (default: ``ZZ``); the base ring of the matrix
          space to use.

        - ``**kwds`` -- other keywords to pass to
          :func:`~sage.matrix.constructor.matrix`.

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: G.incidence_matrix()
            [1 1 1 0 0 0 0 0 0 0 0 0 0 0 0]
            [1 0 0 1 1 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 1 0 1 1 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 1 0 1 1 0 0 0 0 0 0]
            [0 1 0 0 0 0 0 1 0 1 0 0 0 0 0]
            [0 0 1 0 0 0 0 0 0 0 1 1 0 0 0]
            [0 0 0 0 1 0 0 0 0 0 0 0 1 1 0]
            [0 0 0 0 0 0 1 0 0 0 1 0 0 0 1]
            [0 0 0 0 0 0 0 0 1 0 0 1 1 0 0]
            [0 0 0 0 0 0 0 0 0 1 0 0 0 1 1]
            sage: G.incidence_matrix(oriented=True)
            [-1 -1 -1  0  0  0  0  0  0  0  0  0  0  0  0]
            [ 1  0  0 -1 -1  0  0  0  0  0  0  0  0  0  0]
            [ 0  0  0  1  0 -1 -1  0  0  0  0  0  0  0  0]
            [ 0  0  0  0  0  1  0 -1 -1  0  0  0  0  0  0]
            [ 0  1  0  0  0  0  0  1  0 -1  0  0  0  0  0]
            [ 0  0  1  0  0  0  0  0  0  0 -1 -1  0  0  0]
            [ 0  0  0  0  1  0  0  0  0  0  0  0 -1 -1  0]
            [ 0  0  0  0  0  0  1  0  0  0  1  0  0  0 -1]
            [ 0  0  0  0  0  0  0  0  1  0  0  1  1  0  0]
            [ 0  0  0  0  0  0  0  0  0  1  0  0  0  1  1]

            sage: G = digraphs.Circulant(4, [1, 3])
            sage: G.incidence_matrix()
            [-1 -1  1  0  0  0  1  0]
            [ 1  0 -1 -1  1  0  0  0]
            [ 0  0  0  1 -1 -1  0  1]
            [ 0  1  0  0  0  1 -1 -1]

            sage: graphs.CompleteGraph(3).incidence_matrix()
            [1 1 0]
            [1 0 1]
            [0 1 1]
            sage: G = Graph([(0, 0), (0, 1), (0, 1)], loops=True, multiedges=True)
            sage: G.incidence_matrix(oriented=False)
            [2 1 1]
            [0 1 1]

        A well known result states that the product of the (oriented) incidence
        matrix with its transpose of a (non-oriented graph) is in fact the
        Kirchhoff matrix::

            sage: G = graphs.PetersenGraph()
            sage: m = G.incidence_matrix(oriented=True)
            sage: m * m.transpose() == G.kirchhoff_matrix()
            True

            sage: K = graphs.CompleteGraph(3)
            sage: m = K.incidence_matrix(oriented=True)
            sage: m * m.transpose() == K.kirchhoff_matrix()
            True

            sage: H = Graph([(0, 0), (0, 1), (0, 1)], loops=True, multiedges=True)
            sage: m = H.incidence_matrix(oriented=True)
            sage: m * m.transpose() == H.kirchhoff_matrix()
            True

        A different ordering of the vertices::

            sage: P5 = graphs.PathGraph(5)
            sage: P5.incidence_matrix()
            [1 0 0 0]
            [1 1 0 0]
            [0 1 1 0]
            [0 0 1 1]
            [0 0 0 1]
            sage: P5.incidence_matrix(vertices=[2, 4, 1, 3, 0])
            [0 1 1 0]
            [0 0 0 1]
            [1 1 0 0]
            [0 0 1 1]
            [1 0 0 0]

        A different ordering of the edges::

            sage: E = list(P5.edge_iterator(labels=False))
            sage: P5.incidence_matrix(edges=E[::-1])
            [0 0 0 1]
            [0 0 1 1]
            [0 1 1 0]
            [1 1 0 0]
            [1 0 0 0]
            sage: P5.incidence_matrix(vertices=[2, 4, 1, 3, 0], edges=E[::-1])
            [0 1 1 0]
            [1 0 0 0]
            [0 0 1 1]
            [1 1 0 0]
            [0 0 0 1]

        A different base ring::

            sage: P5.incidence_matrix(base_ring=RDF)
            [1.0 0.0 0.0 0.0]
            [1.0 1.0 0.0 0.0]
            [0.0 1.0 1.0 0.0]
            [0.0 0.0 1.0 1.0]
            [0.0 0.0 0.0 1.0]

        Creating an immutable matrix::

            sage: m = P5.incidence_matrix(immutable=True); m
            [1 0 0 0]
            [1 1 0 0]
            [0 1 1 0]
            [0 0 1 1]
            [0 0 0 1]
            sage: m[1,2] = 1
            Traceback (most recent call last):
            ...
            ValueError: matrix is immutable; please change a copy instead (i.e., use copy(M) to change a copy of M).

        TESTS::

            sage: P5 = graphs.PathGraph(5)
            sage: P5.incidence_matrix(vertices=[1] * P5.order())
            Traceback (most recent call last):
            ...
            ValueError: ``vertices`` must be a permutation of the vertices
            sage: P5.incidence_matrix(edges=[(0, 1)] * P5.size())
            Traceback (most recent call last):
            ...
            ValueError: ``edges`` must be a permutation of the edges
            sage: P5.incidence_matrix(edges=P5.edges(sort=False, labels=True))
            [1 0 0 0]
            [1 1 0 0]
            [0 1 1 0]
            [0 0 1 1]
            [0 0 0 1]
        """
        if oriented is None:
            oriented = self.is_directed()

        if vertices is None:
            vertices = self.vertices(sort=False)
        elif (len(vertices) != self.num_verts() or
              set(vertices) != set(self.vertex_iterator())):
            raise ValueError("``vertices`` must be a permutation of the vertices")

        verts = {v: i for i, v in enumerate(vertices)}
        if edges is None:
            edges = self.edge_iterator(labels=False)
        elif len(edges) != self.size():
            raise ValueError("``edges`` must be a permutation of the edges")
        else:
            # We check that we have the same set of unlabeled edges
            if oriented:
                i_edges = [(verts[e[0]], verts[e[1]]) for e in edges]
                s_edges = [(verts[u], verts[v]) for u, v in self.edge_iterator(labels=False)]
            else:
                def reorder(u, v):
                    return (u, v) if u <= v else (v, u)
                i_edges = [reorder(verts[e[0]], verts[e[1]]) for e in edges]
                s_edges = [reorder(verts[u], verts[v]) for u, v in self.edge_iterator(labels=False)]
            if sorted(i_edges) != sorted(s_edges):
                raise ValueError("``edges`` must be a permutation of the edges")

        from sage.matrix.constructor import matrix
        if base_ring is None:
            base_ring = ZZ
        immutable = kwds.pop('immutable', False)
        m = matrix(base_ring, self.num_verts(), self.num_edges(), sparse=sparse, **kwds)

        if oriented:
            for i, e in enumerate(edges):
                if e[0] != e[1]:
                    m[verts[e[0]], i] = -1
                    m[verts[e[1]], i] = +1
        else:
            for i, e in enumerate(edges):
                m[verts[e[0]], i] += 1
                m[verts[e[1]], i] += 1

        if immutable:
            m.set_immutable()
        return m

    def distance_matrix(self, vertices=None, *, base_ring=None, **kwds):
        r"""
        Return the distance matrix of (di)graph.

        The (di)graph is expected to be (strongly) connected.

        The distance matrix of a (strongly) connected (di)graph is a matrix
        whose rows and columns are by default (``vertices == None``) indexed
        with the positions of the vertices of the (di)graph in the ordering
        :meth:`vertices`. When ``vertices`` is set, the position of the vertices
        in this ordering is used. The intersection of row `i` and column `j`
        contains the shortest path distance from the vertex at the `i`-th
        position to the vertex at the `j`-th position.

        Note that even when the vertices are consecutive integers starting from
        one, usually the vertex is not equal to its index.

        INPUT:

        - ``vertices`` -- list (default: ``None``); the ordering of the vertices
          defining how they should appear in the matrix. By default, the
          ordering given by :meth:`vertices` is used. Because :meth:`vertices`
          only works if the vertices can be sorted, using ``vertices`` is useful
          when working with possibly non-sortable objects in Python 3.

        - ``base_ring`` -- a ring (default: determined from the weights); the base
          ring of the matrix space to use.

        - ``**kwds`` -- other keywords to pass to the subfunction
          :meth:`distance_all_pairs` or to
          :func:`~sage.matrix.constructor.matrix`

        EXAMPLES::

            sage: d = DiGraph({1: [2, 3], 2: [3], 3: [4], 4: [1]})
            sage: d.distance_matrix()
            [0 1 1 2]
            [3 0 1 2]
            [2 3 0 1]
            [1 2 2 0]
            sage: d.distance_matrix(vertices=[4, 3, 2, 1])
            [0 2 2 1]
            [1 0 3 2]
            [2 1 0 3]
            [2 1 1 0]

            sage: G = graphs.CubeGraph(3)
            sage: G.distance_matrix()
            [0 1 1 2 1 2 2 3]
            [1 0 2 1 2 1 3 2]
            [1 2 0 1 2 3 1 2]
            [2 1 1 0 3 2 2 1]
            [1 2 2 3 0 1 1 2]
            [2 1 3 2 1 0 2 1]
            [2 3 1 2 1 2 0 1]
            [3 2 2 1 2 1 1 0]

        The well known result of Graham and Pollak states that the determinant
        of the distance matrix of any tree of order `n` is
        `(-1)^{n-1}(n-1)2^{n-2}`::

            sage: all(T.distance_matrix().det() == (-1)^9*(9)*2^8 for T in graphs.trees(10))
            True

        .. SEEALSO::

            * :meth:`~sage.graphs.generic_graph.GenericGraph.distance_all_pairs`
              -- computes the distance between any two vertices.

        TESTS:

        Asking for an immutable matrix::

            sage: G = Graph([(0, 1)])
            sage: G.distance_matrix().is_immutable()
            False
            sage: G.distance_matrix(immutable=True).is_immutable()
            True

        Specifying a base ring::

            sage: G = Graph([(0, 1)])
            sage: G.distance_matrix(vertices=[0, 1], base_ring=ZZ)
            [0 1]
            [1 0]
            sage: G.distance_matrix(vertices=[0, 1], base_ring=RDF)
            [0.0 1.0]
            [1.0 0.0]

        Check that distance parameters are not passed to the matrix
        constructor::

            sage: G = Graph([(0, 1)])
            sage: G.distance_matrix(vertices=[0, 1], weight_function=lambda e:2)
            [0 2]
            [2 0]
        """
        from sage.matrix.constructor import matrix

        if ((self.is_directed() and not self.is_strongly_connected()) or
                (not self.is_directed() and not self.is_connected())):
            raise ValueError("input (di)graph must be (strongly) connected")

        if vertices is None:
            vertices = self.vertices(sort=True)
        elif (len(vertices) != self.order() or
              set(vertices) != set(self.vertex_iterator())):
            raise ValueError("``vertices`` must be a permutation of the vertices")

        # We extract from **kwds the arguments for distance_all_pairs
        keys = ['by_weight', 'algorithm', 'weight_function', 'check_weight']
        kwds_dist = {key: kwds.pop(key) for key in keys if key in kwds}

        dist = self.distance_all_pairs(**kwds_dist)

        # We now turn the result to a matrix
        n = self.order()
        set_immutable = kwds.pop('immutable', False)
        if base_ring is None:
            ret = matrix(n, n, **kwds)
        else:
            ret = matrix(base_ring, n, n, **kwds)
        V = vertices

        if self.is_directed():
            for i in range(n):
                dist_i = dist[V[i]]
                for j in range(n):
                    ret[i, j] = dist_i[V[j]]
        else:
            for i in range(n):
                dist_i = dist[V[i]]
                for j in range(i + 1, n):
                    ret[i, j] = ret[j, i] = dist_i[V[j]]

        if set_immutable:
            ret.set_immutable()
        return ret

    def weighted_adjacency_matrix(self, sparse=True, vertices=None,
                                  default_weight=None, *, base_ring=None, **kwds):
        """
        Return the weighted adjacency matrix of the graph.

        By default, each vertex is represented by its position in the list
        returned by method :meth:`vertices`.

        INPUT:

        - ``sparse`` -- boolean (default: ``True``); whether to use a sparse or
          a dense matrix

        - ``vertices`` -- list (default: ``None``); when specified, each vertex
          is represented by its position in the list ``vertices``, otherwise
          each vertex is represented by its position in the list returned by
          method :meth:`vertices`

        - ``default_weight`` -- (default: ``None``); specifies the weight to
          replace any ``None`` edge label. When not specified an error is raised
          if the label of an edge is ``None``.

        - ``base_ring`` -- a ring (default: determined from the weights); the base
          ring of the matrix space to use.

        - ``**kwds`` -- other keywords to pass to
          :func:`~sage.matrix.constructor.matrix`

        EXAMPLES::

            sage: G = Graph(sparse=True, weighted=True)
            sage: G.add_edges([(0, 1, 1), (1, 2, 2), (0, 2, 3), (0, 3, 4)])
            sage: M = G.weighted_adjacency_matrix(); M
            [0 1 3 4]
            [1 0 2 0]
            [3 2 0 0]
            [4 0 0 0]
            sage: H = Graph(data=M, format='weighted_adjacency_matrix', sparse=True)
            sage: H == G
            True
            sage: G.weighted_adjacency_matrix(vertices=[3, 2, 1, 0])
            [0 0 0 4]
            [0 0 2 3]
            [0 2 0 1]
            [4 3 1 0]

        Using a different matrix implementation::

            sage: M = G.weighted_adjacency_matrix(sparse=False, base_ring=ZZ, implementation='numpy'); M
            [0 1 3 4]
            [1 0 2 0]
            [3 2 0 0]
            [4 0 0 0]

        As an immutable matrix::

            sage: M = G.weighted_adjacency_matrix(immutable=True); M
            [0 1 3 4]
            [1 0 2 0]
            [3 2 0 0]
            [4 0 0 0]
            sage: M[2, 2] = 1
            Traceback (most recent call last):
            ...
            ValueError: matrix is immutable; please change a copy instead (i.e., use copy(M) to change a copy of M).

        TESTS:

        The following doctest verifies that :trac:`4888` is fixed::

            sage: G = DiGraph({0:{}, 1:{0:1}, 2:{0:1}}, weighted=True, sparse=True)
            sage: G.weighted_adjacency_matrix()
            [0 0 0]
            [1 0 0]
            [1 0 0]

        Check error message for non numerical edge weights (:trac:`33562`)::

            sage: G = Graph([(0, 1)])
            sage: G.weighted_adjacency_matrix()
            Traceback (most recent call last):
            ...
            ValueError: cannot find the weight of (0, 1, None). Consider setting parameter 'default_weight'
            sage: G.weighted_adjacency_matrix(default_weight=3)
            [0 3]
            [3 0]
            sage: G = Graph([(0, 1, 'a')])
            sage: G.weighted_adjacency_matrix()
            Traceback (most recent call last):
            ...
            TypeError: Cannot convert NoneType to sage.structure.parent.Parent
        """
        if self.has_multiple_edges():
            raise NotImplementedError("don't know how to represent weights for a multigraph")

        if vertices is None:
            vertices = self.vertices(sort=True)
        elif (len(vertices) != self.num_verts() or
              set(vertices) != set(self.vertex_iterator())):
            raise ValueError("``vertices`` must be a permutation of the vertices")

        # Method for checking edge weights and setting default weight
        if default_weight is None:
            def func(u, v, label):
                if label is None:
                    raise ValueError(f"cannot find the weight of ({u}, {v}, None). "
                                     "Consider setting parameter 'default_weight'")
                return label
        else:
            def func(u, v, label):
                if label is None:
                    return default_weight
                return label

        new_indices = {v: i for i,v in enumerate(vertices)}

        D = {}
        if self._directed:
            for u, v, label in self.edge_iterator():
                i = new_indices[u]
                j = new_indices[v]
                D[i, j] = func(u, v, label)
        else:
            for u, v, label in self.edge_iterator():
                i = new_indices[u]
                j = new_indices[v]
                label = func(u, v, label)
                D[i, j] = label
                D[j, i] = label

        from sage.matrix.constructor import matrix
        if base_ring is None:
            M = matrix(self.num_verts(), D, sparse=sparse, **kwds)
        else:
            M = matrix(base_ring, self.num_verts(), D, sparse=sparse, **kwds)
        return M

    def kirchhoff_matrix(self, weighted=None, indegree=True, normalized=False, signless=False, **kwds):
        r"""
        Return the Kirchhoff matrix (a.k.a. the Laplacian) of the graph.

        The Kirchhoff matrix is defined to be `D + M` if signless and `D - M`
        otherwise, where `D` is the diagonal degree matrix (each diagonal entry
        is the degree of the corresponding vertex), and `M` is the adjacency
        matrix.  If ``normalized`` is ``True``, then the returned matrix is
        `D^{-1/2}(D+M)D^{-1/2}` if signless and `D^{-1/2}(D-M)D^{-1/2}`
        otherwise.

        (In the special case of DiGraphs, `D` is defined as the diagonal
        in-degree matrix or diagonal out-degree matrix according to the value of
        ``indegree``)

        INPUT:

        - ``weighted`` -- boolean (default: ``None``);

          - If ``True``, the weighted adjacency matrix is used for `M`, and the
            diagonal matrix `D` takes into account the weight of edges (replace
            in the definition "degree" by "sum of the incident edges")

          - Else, each edge is assumed to have weight 1

          Default is to take weights into consideration if and only if the graph
          is weighted.

        - ``indegree`` -- boolean (default: ``True``); this parameter is
          considered only for digraphs.

          - If ``True``, each diagonal entry of `D` is equal to the in-degree of
            the corresponding vertex

          - Else, each diagonal entry of `D` is equal to the out-degree of the
            corresponding vertex

          By default, ``indegree`` is set to ``True``

        - ``normalized`` -- boolean (default: ``False``);

          - If ``True``, the returned matrix is `D^{-1/2}(D+M)D^{-1/2}` for
            signless and `D^{-1/2}(D-M)D^{-1/2}` otherwise, a normalized
            version of the Laplacian matrix. More accurately, the normalizing
            matrix used is equal to `D^{-1/2}` only for non-isolated vertices.
            If vertex `i` is isolated, then diagonal entry `i` in the matrix is
            1, rather than a division by zero

          - Else, the matrix `D+M` for signless and `D-M` otherwise is returned

        - ``signless`` -- boolean (default: ``False``);

          - If ``True``, `D+M` is used in calculation of Kirchhoff matrix

          - Else, `D-M` is used in calculation of Kirchhoff matrix

        Note that any additional keywords will be passed on to either the
        :meth:`~GenericGraph.adjacency_matrix` or
        :meth:`~GenericGraph.weighted_adjacency_matrix` method.

        AUTHORS:

        - Tom Boothby
        - Jason Grout

        EXAMPLES::

            sage: G = Graph(sparse=True)
            sage: G.add_edges([(0, 1, 1), (1, 2, 2), (0, 2, 3), (0, 3, 4)])
            sage: M = G.kirchhoff_matrix(weighted=True); M
            [ 8 -1 -3 -4]
            [-1  3 -2  0]
            [-3 -2  5  0]
            [-4  0  0  4]
            sage: M = G.kirchhoff_matrix(); M
            [ 3 -1 -1 -1]
            [-1  2 -1  0]
            [-1 -1  2  0]
            [-1  0  0  1]
            sage: M = G.laplacian_matrix(normalized=True); M                                            # optional - sage.symbolic
            [                   1 -1/6*sqrt(3)*sqrt(2) -1/6*sqrt(3)*sqrt(2)         -1/3*sqrt(3)]
            [-1/6*sqrt(3)*sqrt(2)                    1                 -1/2                    0]
            [-1/6*sqrt(3)*sqrt(2)                 -1/2                    1                    0]
            [        -1/3*sqrt(3)                    0                    0                    1]
            sage: M = G.kirchhoff_matrix(weighted=True, signless=True); M
            [8 1 3 4]
            [1 3 2 0]
            [3 2 5 0]
            [4 0 0 4]

            sage: G = Graph({0: [], 1: [2]})
            sage: G.laplacian_matrix(normalized=True)
            [ 0  0  0]
            [ 0  1 -1]
            [ 0 -1  1]
            sage: G.laplacian_matrix(normalized=True,signless=True)
            [0 0 0]
            [0 1 1]
            [0 1 1]

        A weighted directed graph with loops, changing the variable ``indegree`` ::

            sage: G = DiGraph({1: {1: 2, 2: 3}, 2: {1: 4}}, weighted=True, sparse=True)
            sage: G.laplacian_matrix()
            [ 4 -3]
            [-4  3]

        ::

            sage: G = DiGraph({1: {1: 2, 2: 3}, 2: {1: 4}}, weighted=True, sparse=True)
            sage: G.laplacian_matrix(indegree=False)
            [ 3 -3]
            [-4  4]

        A different ordering of the vertices (see :meth:`adjacency_matrix` and
        :meth:`weighted_adjacency_matrix`)::

            sage: G = Graph(sparse=True)
            sage: G.add_edges([(0, 1, 1), (1, 2, 2), (0, 2, 3), (0, 3, 4)])
            sage: M = G.kirchhoff_matrix(vertices=[3, 2, 1, 0]); M
            [ 1  0  0 -1]
            [ 0  2 -1 -1]
            [ 0 -1  2 -1]
            [-1 -1 -1  3]
            sage: M = G.kirchhoff_matrix(weighted=True, vertices=[3, 2, 1, 0]); M
            [ 4  0  0 -4]
            [ 0  5 -2 -3]
            [ 0 -2  3 -1]
            [-4 -3 -1  8]

        When parameter ``immutable=True`` is passed, the output matrix is
        immutable::

            sage: G = Graph([(0, 1)])
            sage: M = G.kirchhoff_matrix(vertices=[0, 1], immutable=True)
            sage: M.is_immutable()
            True
        """
        from sage.matrix.constructor import diagonal_matrix

        set_immutable = kwds.pop('immutable', False)

        if weighted is None:
            weighted = self._weighted

        if weighted:
            M = self.weighted_adjacency_matrix(immutable=True, **kwds)
        else:
            M = self.adjacency_matrix(immutable=True, **kwds)

        D = M.parent(0)

        if M.is_sparse():
            row_sums = {}
            if indegree:
                for (i, j), entry in M.dict().items():
                    row_sums[j] = row_sums.get(j, 0) + entry
            else:
                for (i, j), entry in M.dict().items():
                    row_sums[i] = row_sums.get(i, 0) + entry

            for i in range(M.nrows()):
                D[i, i] += row_sums.get(i, 0)

        else:
            if indegree:
                col_sums = [sum(v) for v in M.columns()]
                for i in range(M.nrows()):
                    D[i, i] += col_sums[i]
            else:
                row_sums = [sum(v) for v in M.rows()]
                for i in range(M.nrows()):
                    D[i, i] += row_sums[i]

        if normalized:
            from sage.misc.functional import sqrt
            Dsqrt = diagonal_matrix([1 / sqrt(D[i, i]) if D[i, i] else 1
                                     for i in range(D.nrows())])
            if signless:
                ret = Dsqrt * (D + M) * Dsqrt
            else:
                ret = Dsqrt * (D - M) * Dsqrt
        else:
            if signless:
                ret = D + M
            else:
                ret = D - M

        if set_immutable:
            ret.set_immutable()
        return ret

    laplacian_matrix = kirchhoff_matrix

    # Attributes

    def set_embedding(self, embedding):
        """
        Set a combinatorial embedding dictionary to ``_embedding`` attribute.

        The dictionary ``embedding`` represents a combinatorial embedding of
        ``self`` and is organized as a mapping from vertex labels to list of
        vertex neighbors in clockwise order.

        Parameter ``embedding`` is error-checked for validity.

        .. WARNING::

            Combinatorial embeddings are defined for simple graphs only (i.e.,
            without loops or multiple edges). Therefore, an error is raised when
            this method is used for a graph with loops or multiple edges.

        INPUT:

        - ``embedding`` -- dictionary representing a combinatorial embedding of
          ``self``. Format: "{v1: [v2,v3], v2: [v1], v3: [v1]}" (clockwise
          ordering of neighbors at each vertex).

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: G.set_embedding({0: [1, 5, 4], 1: [0, 2, 6], 2: [1, 3, 7],
            ....:                  3: [8, 2, 4], 4: [0, 9, 3], 5: [0, 8, 7],
            ....:                  6: [8, 1, 9], 7: [9, 2, 5], 8: [3, 5, 6],
            ....:                  9: [4, 6, 7]})
            sage: G.set_embedding({'s': [1, 5, 4], 1: [0, 2, 6], 2: [1, 3, 7],
            ....:                  3: [8, 2, 4], 4: [0, 9, 3], 5: [0, 8, 7],
            ....:                  6: [8, 1, 9], 7: [9, 2, 5], 8: [3, 5, 6],
            ....:                  9: [4, 6, 7]})
            Traceback (most recent call last):
            ...
            ValueError: vertices in ['s'] from the embedding do not belong to the graph

        TESTS::

            sage: G = Graph([(0, 0)], loops=True)
            sage: G.set_embedding({0: [0]})
            Traceback (most recent call last):
            ...
            ValueError: This method is not known to work on graphs with loops. Perhaps this method can be updated to handle them, but in the meantime if you want to use it please disallow loops using allow_loops().
            sage: G = Graph([(0, 1), (0, 1)], multiedges=True)
            sage: G.set_embedding({0: [1], 1: [0]})
            Traceback (most recent call last):
            ...
            ValueError: This method is not known to work on graphs with multiedges. Perhaps this method can be updated to handle them, but in the meantime if you want to use it please disallow multiedges using allow_multiple_edges().
        """
        self._scream_if_not_simple()
        self._check_embedding_validity(embedding, boolean=False)
        self._embedding = embedding

    def get_embedding(self):
        """
        Return the stored embedding or ``None``.

        If the stored embedding is no longer valid (because of vertex/edge
        additions) then the stored embedding is discarded and ``None`` is
        returned. In case some vertex/edge has been deleted, the stored
        embedding is updated accordingly.

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: G.genus()
            1
            sage: G.get_embedding()
            {0: [1, 4, 5], 1: [0, 2, 6], 2: [1, 3, 7], 3: [2, 4, 8],
             4: [0, 3, 9], 5: [0, 7, 8], 6: [1, 9, 8], 7: [2, 5, 9],
             8: [3, 6, 5], 9: [4, 6, 7]}

        Note that the embeddings gets properly modified on vertex or edge deletion::

            sage: G.delete_edge(0, 1)
            sage: G.delete_vertex(3)
            sage: G.get_embedding()
            {0: [4, 5],
             1: [2, 6],
             2: [1, 7],
             4: [0, 9],
             5: [0, 7, 8],
             6: [1, 9, 8],
             7: [2, 5, 9],
             8: [6, 5],
             9: [4, 6, 7]}

        But not under edge addition::

            sage: G.add_edge(0, 7)
            sage: G.get_embedding() is None
            True
        """
        try:
            embedding = self._embedding
        except AttributeError:
            embedding = None
        if embedding is not None:
            # remove vertices not anymore in the graph
            to_remove = set(v for v in embedding if v not in self)
            if to_remove:
                for v in to_remove:
                    del embedding[v]
                for v in embedding:
                    embedding[v] = [w for w in embedding[v] if w not in to_remove]

            # remove edges not anymore in the graph
            for u in embedding:
                i = 0
                while i < len(embedding[u]):
                    v = embedding[u][i]
                    if not (self.has_edge(u, v) or self.has_edge(v, u)):
                        del embedding[u][i]
                    else:
                        i += 1

            if self._check_embedding_validity():
                return embedding
            else:
                self._embedding = None

        return None

    def _check_embedding_validity(self, embedding=None, boolean=True):
        """
        Check whether an ``_embedding`` attribute is well defined.

        INPUT:

        - ``embedding`` -- dictionary (default: ``None``); the embedding to
          test. If set to ``None`` (default), the test is performed on
          ``_embedding``

        - ``boolean`` -- boolean (default: ``True``); -- whether to return a
          boolean answer or raise a ``ValueError`` exception if the embedding is
          invalid

        EXAMPLES::

            sage: d = {0: [1, 5, 4], 1: [0, 2, 6], 2: [1, 3, 7], 3: [8, 2, 4],
            ....:      4: [0, 9, 3], 5: [0, 8, 7], 6: [8, 1, 9], 7: [9, 2, 5],
            ....:      8: [3, 5, 6], 9: [4, 6, 7]}
            sage: G = graphs.PetersenGraph()
            sage: G._check_embedding_validity(d)
            True

        Exceptions::

            sage: g = graphs.PathGraph(2)
            sage: g._check_embedding_validity(boolean=False)
            Traceback (most recent call last):
            ...
            ValueError: no embedding has been defined
            sage: g._check_embedding_validity({8: [], 9: []}, boolean=False)
            Traceback (most recent call last):
            ...
            ValueError: vertices in [8, 9] from the embedding do not belong to the graph
            sage: g._check_embedding_validity({0: []}, boolean=False)
            Traceback (most recent call last):
            ...
            ValueError: vertices in [1] have no corresponding entry in the embedding
            sage: g._check_embedding_validity({0: [], 1: [0]}, boolean=False)
            Traceback (most recent call last):
            ...
            ValueError: the list associated with vertex 0 has length 0 but d(0)=1
            sage: g._check_embedding_validity({0: [5], 1: [0]}, boolean=False)
            Traceback (most recent call last):
            ...
            ValueError: 5 and 0 are not neighbors but 5 is in the list associated with 0
            sage: graphs.PathGraph(3)._check_embedding_validity({0:[1],1:[0,0],2:[1]},boolean=False)
            Traceback (most recent call last):
            ...
            ValueError: the list associated with vertex 1 contains >1 occurrences of [0]

        """
        if embedding is None:
            try:
                embedding = self._embedding
            except AttributeError:
                pass
        if embedding is None:
            if boolean:
                return False
            raise ValueError("no embedding has been defined")

        if set(embedding) != set(self):
            if boolean:
                return False
            if set(embedding).difference(self):
                raise ValueError("vertices in {} from the embedding do not "
                                 "belong to the graph".format(list(set(embedding).difference(self))))
            else:
                raise ValueError("vertices in {} have no corresponding entry "
                                 "in the embedding".format(list(set(self).difference(embedding))))

        if self._directed:
            def connected(u, v):
                return self.has_edge(u, v) or self.has_edge(v, u)
        else:
            connected = self.has_edge
        for v in embedding:
            if len(embedding[v]) != self.degree(v):
                if boolean:
                    return False
                raise ValueError("the list associated with vertex {} has "
                                 "length {} but d({})={}".format(v, len(embedding[v]),
                                                                 v, self.degree(v)))
            if len(embedding[v]) != len(set(embedding[v])):
                if boolean:
                    return False
                raise ValueError("the list associated with vertex {} contains >1 "
                                 "occurrences of {}".format(v, [x for x in set(embedding[v])
                                                                if embedding[v].count(x) > 1]))
            for u in embedding[v]:
                if not connected(v, u):
                    if boolean:
                        return False
                    raise ValueError("{} and {} are not neighbors but {} is in "
                                     "the list associated with {}".format(u, v, u, v))
        return True

    def has_loops(self):
        """
        Return whether there are loops in the (di)graph

        EXAMPLES::

            sage: G = Graph(loops=True); G
            Looped graph on 0 vertices
            sage: G.has_loops()
            False
            sage: G.allows_loops()
            True
            sage: G.add_edge((0, 0))
            sage: G.has_loops()
            True
            sage: G.loops()
            [(0, 0, None)]
            sage: G.allow_loops(False); G
            Graph on 1 vertex
            sage: G.has_loops()
            False
            sage: G.edges(sort=True)
            []

            sage: D = DiGraph(loops=True); D
            Looped digraph on 0 vertices
            sage: D.has_loops()
            False
            sage: D.allows_loops()
            True
            sage: D.add_edge((0, 0))
            sage: D.has_loops()
            True
            sage: D.loops()
            [(0, 0, None)]
            sage: D.allow_loops(False); D
            Digraph on 1 vertex
            sage: D.has_loops()
            False
            sage: D.edges(sort=True)
            []
        """
        return self.allows_loops() and any(self.has_edge(v, v) for v in self)

    def allows_loops(self):
        """
        Return whether loops are permitted in the (di)graph

        EXAMPLES::

            sage: G = Graph(loops=True); G
            Looped graph on 0 vertices
            sage: G.has_loops()
            False
            sage: G.allows_loops()
            True
            sage: G.add_edge((0, 0))
            sage: G.has_loops()
            True
            sage: G.loops()
            [(0, 0, None)]
            sage: G.allow_loops(False); G
            Graph on 1 vertex
            sage: G.has_loops()
            False
            sage: G.edges(sort=True)
            []

            sage: D = DiGraph(loops=True); D
            Looped digraph on 0 vertices
            sage: D.has_loops()
            False
            sage: D.allows_loops()
            True
            sage: D.add_edge((0, 0))
            sage: D.has_loops()
            True
            sage: D.loops()
            [(0, 0, None)]
            sage: D.allow_loops(False); D
            Digraph on 1 vertex
            sage: D.has_loops()
            False
            sage: D.edges(sort=True)
            []
        """
        return self._backend.loops(None)

    def allow_loops(self, new, check=True):
        """
        Change whether loops are permitted in the (di)graph

        INPUT:

        - ``new`` -- boolean

        - ``check`` -- boolean (default: ``True``); whether to remove existing
          loops from the (di)graph when the new status is ``False``

        EXAMPLES::

            sage: G = Graph(loops=True); G
            Looped graph on 0 vertices
            sage: G.has_loops()
            False
            sage: G.allows_loops()
            True
            sage: G.add_edge((0, 0))
            sage: G.has_loops()
            True
            sage: G.loops()
            [(0, 0, None)]
            sage: G.allow_loops(False); G
            Graph on 1 vertex
            sage: G.has_loops()
            False
            sage: G.edges(sort=True)
            []

            sage: D = DiGraph(loops=True); D
            Looped digraph on 0 vertices
            sage: D.has_loops()
            False
            sage: D.allows_loops()
            True
            sage: D.add_edge((0, 0))
            sage: D.has_loops()
            True
            sage: D.loops()
            [(0, 0, None)]
            sage: D.allow_loops(False); D
            Digraph on 1 vertex
            sage: D.has_loops()
            False
            sage: D.edges(sort=True)
            []
        """
        if new is False and check:
            self.remove_loops()
        self._backend.loops(new)

    def loop_edges(self, labels=True):
        """
        Return a list of all loops in the (di)graph

        INPUT:

        - ``labels`` -- boolean (default: ``True``); whether returned edges have
          labels (``(u,v,l)``) or not (``(u,v)``)

        EXAMPLES::

            sage: G = Graph(loops=True); G
            Looped graph on 0 vertices
            sage: G.has_loops()
            False
            sage: G.allows_loops()
            True
            sage: G.add_edges([(0, 0), (1, 1), (2, 2), (3, 3), (2, 3)])
            sage: G.loop_edges()
            [(0, 0, None), (1, 1, None), (2, 2, None), (3, 3, None)]
            sage: G.loop_edges(labels=False)
            [(0, 0), (1, 1), (2, 2), (3, 3)]
            sage: G.allows_loops()
            True
            sage: G.has_loops()
            True
            sage: G.allow_loops(False)
            sage: G.has_loops()
            False
            sage: G.loop_edges()
            []
            sage: G.edges(sort=True)
            [(2, 3, None)]

            sage: D = DiGraph(loops=True); D
            Looped digraph on 0 vertices
            sage: D.has_loops()
            False
            sage: D.allows_loops()
            True
            sage: D.add_edge((0, 0))
            sage: D.has_loops()
            True
            sage: D.loops()
            [(0, 0, None)]
            sage: D.allow_loops(False); D
            Digraph on 1 vertex
            sage: D.has_loops()
            False
            sage: D.edges(sort=True)
            []

            sage: G = graphs.PetersenGraph()
            sage: G.loops()
            []

        ::

            sage: D = DiGraph(4, loops=True)
            sage: D.add_edges([(0, 0), (1, 1), (2, 2), (3, 3), (2, 3)])
            sage: D.loop_edges()
            [(0, 0, None), (1, 1, None), (2, 2, None), (3, 3, None)]

        ::

            sage: G = Graph(4, loops=True, multiedges=True, sparse=True)
            sage: G.add_edges((i, i) for i in range(4))
            sage: G.loop_edges()
            [(0, 0, None), (1, 1, None), (2, 2, None), (3, 3, None)]
            sage: G.add_edges([(0, 0), (1, 1)])
            sage: G.loop_edges(labels=False)
            [(0, 0), (0, 0), (1, 1), (1, 1), (2, 2), (3, 3)]
        """
        if self.allows_multiple_edges():
            if labels:
                return [(v, v, l) for v in self.loop_vertices() for l in self.edge_label(v, v)]
            else:
                return [(v, v) for v in self.loop_vertices() for l in self.edge_label(v, v)]
        elif labels:
            return [(v, v, self.edge_label(v, v)) for v in self.loop_vertices()]
        else:
            return [(v, v) for v in self.loop_vertices()]

    # As discussed in trac 22911, we make method loops an alias for loop_edges
    loops = loop_edges

    def number_of_loops(self):
        """
        Return the number of edges that are loops

        EXAMPLES::

            sage: G = Graph(4, loops=True)
            sage: G.add_edges([(0, 0), (1, 1), (2, 2), (3, 3), (2, 3)])
            sage: G.edges(sort=True, labels=False)
            [(0, 0), (1, 1), (2, 2), (2, 3), (3, 3)]
            sage: G.number_of_loops()
            4

        ::

            sage: D = DiGraph(4, loops=True)
            sage: D.add_edges([(0, 0), (1, 1), (2, 2), (3, 3), (2, 3)])
            sage: D.edges(sort=True, labels=False)
            [(0, 0), (1, 1), (2, 2), (2, 3), (3, 3)]
            sage: D.number_of_loops()
            4
        """
        return len(self.loop_edges())

    def loop_vertices(self):
        """
        Return a list of vertices with loops

        EXAMPLES::

            sage: G = Graph({0: [0], 1: [1, 2, 3], 2: [3]}, loops=True)
            sage: G.loop_vertices()
            [0, 1]
        """
        if self.allows_loops():
            return [v for v in self if self.has_edge(v, v)]
        else:
            return []

    def has_multiple_edges(self, to_undirected=False):
        """
        Return whether there are multiple edges in the (di)graph.

        INPUT:

        - ``to_undirected`` -- (default: ``False)``; if ``True``, runs the test
          on the undirected version of a DiGraph. Otherwise, treats DiGraph
          edges ``(u, v)`` and ``(v, u)`` as unique individual edges.

        EXAMPLES::

            sage: G = Graph(multiedges=True, sparse=True); G
            Multi-graph on 0 vertices
            sage: G.has_multiple_edges()
            False
            sage: G.allows_multiple_edges()
            True
            sage: G.add_edges([(0, 1)] * 3)
            sage: G.has_multiple_edges()
            True
            sage: G.multiple_edges()
            [(0, 1, None), (0, 1, None), (0, 1, None)]
            sage: G.allow_multiple_edges(False); G
            Graph on 2 vertices
            sage: G.has_multiple_edges()
            False
            sage: G.edges(sort=True)
            [(0, 1, None)]

            sage: D = DiGraph(multiedges=True, sparse=True); D
            Multi-digraph on 0 vertices
            sage: D.has_multiple_edges()
            False
            sage: D.allows_multiple_edges()
            True
            sage: D.add_edges([(0, 1)] * 3)
            sage: D.has_multiple_edges()
            True
            sage: D.multiple_edges()
            [(0, 1, None), (0, 1, None), (0, 1, None)]
            sage: D.allow_multiple_edges(False); D
            Digraph on 2 vertices
            sage: D.has_multiple_edges()
            False
            sage: D.edges(sort=True)
            [(0, 1, None)]

            sage: G = DiGraph({1: {2: 'h'}, 2: {1: 'g'}}, sparse=True)
            sage: G.has_multiple_edges()
            False
            sage: G.has_multiple_edges(to_undirected=True)
            True
            sage: G.multiple_edges()
            []
            sage: G.multiple_edges(to_undirected=True)
            [(1, 2, 'h'), (2, 1, 'g')]

        A loop is not a multiedge::

            sage: g = Graph(loops=True, multiedges=True)
            sage: g.add_edge(0, 0)
            sage: g.has_multiple_edges()
            False
        """
        if self.allows_multiple_edges() or (self._directed and to_undirected):
            if self._directed:
                for u in self:
                    s = set()
                    for a, b in self.outgoing_edge_iterator(u, labels=False):
                        if b in s:
                            return True
                        s.add(b)
                    if to_undirected:
                        for a, b in self.incoming_edge_iterator(u, labels=False):
                            if a in s:
                                return True
                            s.add(a)
            else:
                for u in self:
                    s = set()
                    for a, b in self.edges(vertices=u, labels=False, sort=False):
                        if a is u:
                            if b in s:
                                return True
                            s.add(b)
                        elif b is u:
                            if a in s:
                                return True
                            s.add(a)
        return False

    def allows_multiple_edges(self):
        """
        Return whether multiple edges are permitted in the (di)graph.

        EXAMPLES::

            sage: G = Graph(multiedges=True, sparse=True); G
            Multi-graph on 0 vertices
            sage: G.has_multiple_edges()
            False
            sage: G.allows_multiple_edges()
            True
            sage: G.add_edges([(0, 1)] * 3)
            sage: G.has_multiple_edges()
            True
            sage: G.multiple_edges()
            [(0, 1, None), (0, 1, None), (0, 1, None)]
            sage: G.allow_multiple_edges(False); G
            Graph on 2 vertices
            sage: G.has_multiple_edges()
            False
            sage: G.edges(sort=True)
            [(0, 1, None)]

            sage: D = DiGraph(multiedges=True, sparse=True); D
            Multi-digraph on 0 vertices
            sage: D.has_multiple_edges()
            False
            sage: D.allows_multiple_edges()
            True
            sage: D.add_edges([(0, 1)] * 3)
            sage: D.has_multiple_edges()
            True
            sage: D.multiple_edges()
            [(0, 1, None), (0, 1, None), (0, 1, None)]
            sage: D.allow_multiple_edges(False); D
            Digraph on 2 vertices
            sage: D.has_multiple_edges()
            False
            sage: D.edges(sort=True)
            [(0, 1, None)]
        """
        return self._backend.multiple_edges(None)

    def allow_multiple_edges(self, new, check=True, keep_label='any'):
        """
        Change whether multiple edges are permitted in the (di)graph.

        INPUT:

        - ``new`` -- boolean; if ``True``, the new graph will allow multiple
          edges

        - ``check`` -- boolean (default: ``True``); if ``True`` and ``new`` is
          ``False``, we remove all multiple edges from the graph

        - ``keep_label`` -- string (default: ``'any'``); used only if ``new`` is
          ``False`` and ``check`` is ``True``. If there are multiple edges with
          different labels, this variable defines which label should be kept:

          - ``'any'`` -- any label
          - ``'min'`` -- the smallest label
          - ``'max'`` -- the largest label

        .. WARNING::

            ``'min'`` and ``'max'`` only works if the labels can be compared. A
            ``TypeError`` might be raised when working with non-comparable
            objects in Python 3.

        EXAMPLES:

        The standard behavior with undirected graphs::

            sage: G = Graph(multiedges=True, sparse=True); G
            Multi-graph on 0 vertices
            sage: G.has_multiple_edges()
            False
            sage: G.allows_multiple_edges()
            True
            sage: G.add_edges([(0, 1, 1), (0, 1, 2), (0, 1, 3)])
            sage: G.has_multiple_edges()
            True
            sage: G.multiple_edges(sort=True)
            [(0, 1, 1), (0, 1, 2), (0, 1, 3)]
            sage: G.allow_multiple_edges(False); G
            Graph on 2 vertices
            sage: G.has_multiple_edges()
            False
            sage: G.edges(sort=True)
            [(0, 1, 3)]

        If we ask for the minimum label::

            sage: G = Graph([(0, 1, 1), (0, 1, 2), (0, 1, 3)], multiedges=True, sparse=True)
            sage: G.allow_multiple_edges(False, keep_label='min')
            sage: G.edges(sort=True)
            [(0, 1, 1)]

        If we ask for the maximum label::

            sage: G = Graph([(0, 1, 1), (0, 1, 2), (0, 1, 3)], multiedges=True, sparse=True)
            sage: G.allow_multiple_edges(False, keep_label='max')
            sage: G.edges(sort=True)
            [(0, 1, 3)]

        The standard behavior with digraphs::

            sage: D = DiGraph(multiedges=True, sparse=True); D
            Multi-digraph on 0 vertices
            sage: D.has_multiple_edges()
            False
            sage: D.allows_multiple_edges()
            True
            sage: D.add_edges([(0, 1)] * 3)
            sage: D.has_multiple_edges()
            True
            sage: D.multiple_edges()
            [(0, 1, None), (0, 1, None), (0, 1, None)]
            sage: D.allow_multiple_edges(False); D
            Digraph on 2 vertices
            sage: D.has_multiple_edges()
            False
            sage: D.edges(sort=True)
            [(0, 1, None)]
        """
        if keep_label not in ['any', 'min', 'max']:
            raise ValueError("variable keep_label must be 'any', 'min', or 'max'")

        # TODO: this should be much faster for c_graphs, but for now we just do this
        if self.allows_multiple_edges() and new is False and check:
            seen = dict()
            keep_min = keep_label == 'min'
            keep_max = keep_label == 'max'
            for u, v, l in self.multiple_edges(sort=False):
                if (u, v) not in seen:
                    # This is the first time we see this edge
                    seen[u, v] = l
                else:
                    # This edge has already been seen: we have to remove
                    # something from the graph.
                    oldl = seen[u, v]
                    if (keep_min and l < oldl) or (keep_max and l > oldl):
                        # Keep the new edge, delete the old one
                        self.delete_edge(u, v, oldl)
                        seen[u, v] = l
                    else:
                        # Delete the new edge
                        self.delete_edge(u, v, l)

        self._backend.multiple_edges(new)

    def multiple_edges(self, to_undirected=False, labels=True, sort=False):
        """
        Return any multiple edges in the (di)graph.

        INPUT:

        - ``to_undirected`` -- boolean (default: ``False``)

        - ``labels`` -- boolean (default: ``True``); whether to include labels

        - ``sort`` - boolean (default: ``False``); whether to sort the result

        EXAMPLES::

            sage: G = Graph(multiedges=True, sparse=True); G
            Multi-graph on 0 vertices
            sage: G.has_multiple_edges()
            False
            sage: G.allows_multiple_edges()
            True
            sage: G.add_edges([(0, 1)] * 3)
            sage: G.has_multiple_edges()
            True
            sage: G.multiple_edges(sort=True)
            [(0, 1, None), (0, 1, None), (0, 1, None)]
            sage: G.allow_multiple_edges(False); G
            Graph on 2 vertices
            sage: G.has_multiple_edges()
            False
            sage: G.edges(sort=True)
            [(0, 1, None)]

            sage: D = DiGraph(multiedges=True, sparse=True); D
            Multi-digraph on 0 vertices
            sage: D.has_multiple_edges()
            False
            sage: D.allows_multiple_edges()
            True
            sage: D.add_edges([(0, 1)] * 3)
            sage: D.has_multiple_edges()
            True
            sage: D.multiple_edges(sort=True)
            [(0, 1, None), (0, 1, None), (0, 1, None)]
            sage: D.allow_multiple_edges(False); D
            Digraph on 2 vertices
            sage: D.has_multiple_edges()
            False
            sage: D.edges(sort=True)
            [(0, 1, None)]

            sage: G = DiGraph({1: {2: 'h'}, 2: {1: 'g'}}, sparse=True)
            sage: G.has_multiple_edges()
            False
            sage: G.has_multiple_edges(to_undirected=True)
            True
            sage: G.multiple_edges()
            []
            sage: G.multiple_edges(to_undirected=True, sort=True)
            [(1, 2, 'h'), (2, 1, 'g')]
        """
        multi_edges = []
        seen = set()

        # Method edge_label returns a unique label when
        # self.allows_multiple_edges() is False and a list of labels when
        # self.allows_multiple_edges() is True. So we distinguish several cases
        if not self._directed:
            if not self.allows_multiple_edges():
                return []
            for u in self:
                seen.add(u)
                for v in self.neighbor_iterator(u):
                    if v in seen:
                        continue
                    L = self.edge_label(u, v)
                    if len(L) > 1:
                        if labels:
                            multi_edges.extend((u, v, l) for l in L)
                        else:
                            multi_edges.extend((u, v) for _ in L)

        # self._directed is True
        elif not to_undirected:
            if not self.allows_multiple_edges():
                return []
            for u in self:
                for v in self.neighbor_out_iterator(u):
                    L = self.edge_label(u, v)
                    if len(L) > 1:
                        if labels:
                            multi_edges.extend((u, v, l) for l in L)
                        else:
                            multi_edges.extend((u, v) for _ in L)

        # and to_undirected is True
        elif not self.allows_multiple_edges():
            for u in self:
                seen.add(u)
                for v in self.neighbor_out_iterator(u):
                    if v not in seen and self.has_edge(v, u):
                        if labels:
                            multi_edges.append((u, v, self.edge_label(u, v)))
                            multi_edges.append((v, u, self.edge_label(v, u)))
                        else:
                            multi_edges.append((u, v))
                            multi_edges.append((v, u))

        # and self.allows_multiple_edges() is True
        else:
            for u in self:
                seen.add(u)
                for v in self.neighbor_out_iterator(u):
                    if v not in seen:
                        L_uv = self.edge_label(u, v)
                        L_vu = self.edge_label(v, u) if self.has_edge(v, u) else []
                        if len(L_uv) + len(L_vu) > 1:
                            if labels:
                                multi_edges.extend((u, v, l) for l in L_uv)
                                multi_edges.extend((v, u, l) for l in L_vu)
                            else:
                                multi_edges.extend((u, v) for _ in L_uv)
                                multi_edges.extend((v, u) for _ in L_vu)

                    elif not self.has_edge(v, u):
                        L = self.edge_label(u, v)
                        if len(L) > 1:
                            if labels:
                                multi_edges.extend((u, v, l) for l in L)
                            else:
                                multi_edges.extend((u, v) for _ in L)

        if sort:
            multi_edges.sort()
        return multi_edges

    def name(self, new=None):
        """
        Return or set the graph's name.

        INPUT:

        - ``new`` -- string (default: ``None``); by default (``new == None``),
          the method returns the name of the graph. When ``name`` is set, the
          string representation of that object becomes the new name of the
          (di)graph (``new == ''`` removes any name).

        EXAMPLES::

            sage: d = {0: [1,4,5], 1: [2,6], 2: [3,7], 3: [4,8], 4: [9], 5: [7, 8], 6: [8,9], 7: [9]}
            sage: G = Graph(d); G
            Graph on 10 vertices
            sage: G.name("Petersen Graph"); G
            Petersen Graph: Graph on 10 vertices
            sage: G.name(new=""); G
            Graph on 10 vertices
            sage: G.name()
            ''
            sage: G.name(42); G
            42: Graph on 10 vertices
            sage: G.name()
            '42'

        TESTS:

        Name of an immutable graph :trac:`15681` ::

            sage: g = graphs.PetersenGraph()
            sage: gi = g.copy(immutable=True)
            sage: gi.name()
            'Petersen graph'
            sage: gi.name("Hey")
            Traceback (most recent call last):
            ...
            NotImplementedError: an immutable graph does not change name
        """
        if new is None:
            return getattr(self, '_name', "")

        if self.is_immutable():
            raise NotImplementedError("an immutable graph does not change name")

        self._name = str(new)

    def get_pos(self, dim=2):
        """
        Return the position dictionary.

        The position dictionary specifies the coordinates of each vertex.

        INPUT:

        - ``dim`` -- integer (default: 2); whether to return the position
          dictionary in the plane (``dim == 2``) or in the 3-dimensional space

        EXAMPLES:

        By default, the position of a graph is None::

            sage: G = Graph()
            sage: G.get_pos()
            sage: G.get_pos() is None
            True
            sage: P = G.plot(save_pos=True)
            sage: G.get_pos()
            {}

        Some of the named graphs come with a pre-specified positioning::

            sage: G = graphs.PetersenGraph()
            sage: G.get_pos()
            {0: (0.0, 1.0),
             ...
             9: (0.475..., 0.154...)}

        Note that the position dictionary is modified on vertex removal::

            sage: G.delete_vertex(0)
            sage: G.get_pos()
            {1: (-0.951..., 0.309...),
            ...
             9: (0.475..., 0.154...)}

        But is deleted on vertex addition::

            sage: G.add_vertex(0)
            sage: G.get_pos() is None
            True
        """
        if dim == 2:
            try:
                pos = self._pos
            except AttributeError:
                pos = None
        elif dim == 3:
            try:
                pos = self._pos3d
            except AttributeError:
                pos = None
        else:
            raise ValueError("dim must be 2 or 3")

        if pos is not None:
            # take care of possible vertex removal
            for v in list(pos):
                if v not in self:
                    del pos[v]

            if self._check_pos_validity(dim=dim):
                return pos
            elif dim == 2:
                pos = self._pos = None
            else:
                pos = self._pos3d = None

        return pos

    def _check_pos_validity(self, pos=None, dim=2):
        r"""
        Check whether ``pos`` specifies two (resp. 3) coordinates for every
        vertex of the (di)graph (and no more vertices).

        INPUT:

        - ``pos`` -- dictionary (default: ``None``); a position dictionary for
          the vertices of the (di)graph

        - ``dim`` -- integer (default: 2); the number of coordinates per vertex

        OUTPUT:

        If ``pos`` is ``None`` then the position dictionary of ``self`` is
        investigated, otherwise the position dictionary provided in ``pos`` is
        investigated. The function returns ``True`` if the dictionary is of the
        correct form for ``self``.

        EXAMPLES::

            sage: p = {0: [1, 5], 1: [0, 2], 2: [1, 3], 3: [8, 2], 4: [0, 9], 5: [0, 8], 6: [8, 1], 7: [9, 5], 8: [3, 5], 9: [6, 7]}
            sage: G = graphs.PetersenGraph()
            sage: G._check_pos_validity(p)
            True
        """
        if pos is None:
            if dim == 2:
                try:
                    pos = self._pos
                except AttributeError:
                    pass
            elif dim == 3:
                try:
                    pos = self._pos3d
                except AttributeError:
                    pass
        if pos is None:
            return False
        if len(pos) != self.order():
            return False
        for v in pos:
            if not self.has_vertex(v):
                return False
            if len(pos[v]) != dim:
                return False
        return True

    def set_pos(self, pos, dim=2):
        """
        Set the position dictionary.

        The position dictionary specifies the coordinates of each vertex.

        INPUT:

        - ``pos`` -- a position dictionary for the vertices of the (di)graph

        - ``dim`` -- integer (default: 2); the number of coordinates per vertex

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: G.get_pos()
            {0: (..., ...),
             ...
             9: (..., ...)}

        The method :meth:`get_pos` check the position dictionary so that
        invalid positioning are ignored::

            sage: G.set_pos(dict(enumerate('abcdefghi')))
            sage: P = G.plot()  # positions are ignored
            sage: G.get_pos() is None
            True
        """
        if pos is None:
            return

        if not isinstance(pos, dict):
            raise ValueError('pos must be a dictionary whose keys are vertices and values the positions')
        if dim == 2:
            self._pos = pos
        elif dim == 3:
            self._pos3d = pos
        else:
            raise ValueError("dim must be 2 or 3")

    def weighted(self, new=None):
        """
        Whether the (di)graph is to be considered as a weighted (di)graph.

        INPUT:

        - ``new`` -- boolean (default: ``None``); if it is provided, then the
          weightedness flag is set accordingly. This is not allowed for
          immutable graphs.

        .. NOTE::

            Changing the weightedness flag changes the ``==``-class of a graph
            and is thus not allowed for immutable graphs.

            Edge weightings can still exist for (di)graphs ``G`` where
            ``G.weighted()`` is ``False``.

        EXAMPLES:

        Here we have two graphs with different labels, but ``weighted()`` is
        ``False`` for both, so we just check for the presence of edges::

            sage: G = Graph({0: {1: 'a'}}, sparse=True)
            sage: H = Graph({0: {1: 'b'}}, sparse=True)
            sage: G == H
            True

        Now one is weighted and the other is not, and thus the graphs are not
        equal::

            sage: G.weighted(True)
            sage: H.weighted()
            False
            sage: G == H
            False

        However, if both are weighted, then we finally compare 'a' to 'b'::

            sage: H.weighted(True)
            sage: G == H
            False

        TESTS:

        Ensure that :trac:`10490` is fixed: allows a weighted graph to be set as
        unweighted::

            sage: G = Graph({1: {2: 3}})
            sage: G.weighted()
            False
            sage: G.weighted(True)
            sage: G.weighted()
            True
            sage: G.weighted(False)
            sage: G.weighted()
            False

        Ensure that graphs using the static sparse backend cannot be mutated
        using this method, as fixed in :trac:`15278`::

            sage: G = graphs.PetersenGraph()
            sage: G.weighted()
            False
            sage: H = copy(G)
            sage: H == G
            True
            sage: H.weighted(True)
            sage: H == G
            False
            sage: G_imm = Graph(G, data_structure="static_sparse")
            sage: G_imm == G
            True
            sage: G_imm.weighted()
            False
            sage: G_imm.weighted(True)
            Traceback (most recent call last):
            ...
            TypeError: This graph is immutable and can thus not be changed.
            Create a mutable copy, e.g., by `copy(g)`
            sage: G_mut = copy(G)
            sage: G_mut == G_imm
            True
            sage: G_mut.weighted(True)
            sage: G_mut == G_imm
            False
            sage: G_mut == H
            True

        """
        if new is not None:
            if self.is_immutable():
                raise TypeError("This graph is immutable and can thus not be changed. "
                                "Create a mutable copy, e.g., by `copy(g)`")
            if new in [True, False]:
                self._weighted = new
            else:
                raise ValueError("'new' must be a boolean")
        else:
            return bool(self._weighted)

    # Properties

    def antisymmetric(self):
        r"""
        Check whether the graph is antisymmetric.

        A graph represents an antisymmetric relation if the existence of a path
        from a vertex `x` to a vertex `y` implies that there is not a path from
        `y` to `x` unless `x = y`.

        EXAMPLES:

        A directed acyclic graph is antisymmetric::

            sage: G = digraphs.RandomDirectedGNR(20, 0.5)
            sage: G.antisymmetric()
            True

        Loops are allowed::

            sage: G.allow_loops(True)
            sage: G.add_edge(0, 0)
            sage: G.antisymmetric()
            True

        An undirected graph is never antisymmetric unless it is just a union of
        isolated vertices (with possible loops)::

            sage: graphs.RandomGNP(20, 0.5).antisymmetric()
            False
            sage: Graph(3).antisymmetric()
            True
            sage: Graph([(i, i) for i in range(3)], loops=True).antisymmetric()
            True
            sage: DiGraph([(i, i) for i in range(3)], loops=True).antisymmetric()
            True
        """
        if not self._directed:
            # An undirected graph is antisymmetric only if all its edges are
            # loops
            return self.size() == len(self.loop_edges())
        if self.has_loops():
            g = self.transitive_closure()
            g.allow_loops(False)
            return g.is_directed_acyclic()
        else:
            return self.is_directed_acyclic()

    def density(self):
        """
        Return the density of the (di)graph.

        The density of a (di)graph is defined as the number of edges divided by
        number of possible edges.

        In the case of a multigraph, raises an error, since there is an infinite
        number of possible edges.

        EXAMPLES::

            sage: d = {0: [1,4,5], 1: [2,6], 2: [3,7], 3: [4,8], 4: [9], 5: [7, 8], 6: [8,9], 7: [9]}
            sage: G = Graph(d); G.density()
            1/3
            sage: G = Graph({0: [1, 2], 1: [0]}); G.density()
            2/3
            sage: G = DiGraph({0: [1, 2], 1: [0]}); G.density()
            1/2

        Note that there are more possible edges on a looped graph::

            sage: G.allow_loops(True)
            sage: G.density()
            1/3
        """
        if self.has_multiple_edges():
            raise TypeError("density is not well-defined for multigraphs")
        n = self.order()
        if self.allows_loops():
            if not n:
                return Rational(0)
            if self._directed:
                return Rational(self.size()) / Rational(n ** 2)
            else:
                return Rational(self.size()) / Rational((n ** 2 + n) / 2)
        else:
            if n < 2:
                return Rational(0)
            if self._directed:
                return Rational(self.size()) / Rational((n ** 2 - n))
            else:
                return Rational(self.size()) / Rational((n ** 2 - n) / 2)

    def is_bipartite(self, certificate=False):
        r"""
        Check whether the graph is bipartite.

        Traverse the graph `G` with breadth-first-search and color nodes.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate. If set to ``True``, the certificate returned is a proper
          2-coloring when `G` is bipartite, and an odd cycle otherwise.

        EXAMPLES::

            sage: graphs.CycleGraph(4).is_bipartite()
            True
            sage: graphs.CycleGraph(5).is_bipartite()
            False
            sage: graphs.RandomBipartite(10, 10, 0.7).is_bipartite()
            True

        A random graph is very rarely bipartite::

            sage: g = graphs.PetersenGraph()
            sage: g.is_bipartite()
            False
            sage: false, oddcycle = g.is_bipartite(certificate=True)
            sage: len(oddcycle) % 2
            1

        The method works identically with oriented graphs::

            sage: g = DiGraph({0: [1, 2, 3], 2: [1], 3: [4]})
            sage: g.is_bipartite()
            False
            sage: false, oddcycle = g.is_bipartite(certificate=True)
            sage: len(oddcycle) % 2
            1

            sage: graphs.CycleGraph(4).random_orientation().is_bipartite()
            True
            sage: graphs.CycleGraph(5).random_orientation().is_bipartite()
            False

        TESTS::

            sage: G = Graph(loops=True)
            sage: G.add_edge(0, 0)
            sage: G.is_bipartite()
            False
            sage: G.is_bipartite(certificate=True)
            (False, [0])
        """
        if self.allows_loops():
            # We use the first found loop as certificate, if any
            for u in self:
                if self.has_edge(u, u):
                    if certificate:
                        return (False, [u])
                    else:
                        return False

        color = {}
        # inheritance of colors along the DFS to recover an odd
        # cycle when certificate=True
        tree = {}

        # For any uncolored vertex in the graph (to ensure we do the right job
        # when the graph is not connected !)
        for u in self:
            if u in color:
                continue

            # Let us run a BFS starting from u
            queue = [u]
            color[u] = 1
            tree[u] = None
            while queue:
                v = queue.pop(0)
                c = 1 - color[v]
                for w in self.neighbor_iterator(v):

                    # If the vertex has already been colored
                    if w in color:

                        # The graph is not bipartite !
                        if color[w] == color[v]:

                            # Should we return an odd cycle ?
                            if certificate:
                                w_to_root = []
                                s = w
                                while s is not None:
                                    w_to_root.append(s)
                                    s = tree[s]

                                v_to_root = []
                                s = v
                                while s is not None:
                                    v_to_root.append(s)
                                    s = tree[s]

                                # Remove the common part of v -> root and w -> root
                                while v_to_root and w_to_root and v_to_root[-1] == w_to_root[-1]:
                                    r = v_to_root.pop()
                                    w_to_root.pop()

                                cycle = v_to_root + [r] + w_to_root[::-1]

                                return False, cycle

                            else:
                                return False

                    # We color a new vertex
                    else:
                        color[w] = c
                        tree[w] = v
                        queue.append(w)

        if certificate:
            return True, color
        else:
            return True

    def is_eulerian(self, path=False):
        r"""
        Check whether the graph is Eulerian.

        A graph is Eulerian if it has a (closed) tour that visits each edge
        exactly once.

        INPUT:

        - ``path`` -- boolean (default: ``False``); by default this function
          finds if the graph contains a closed tour visiting each edge once,
          i.e. an Eulerian cycle. If you want to test the existence of an
          Eulerian path, set this argument to ``True``. Graphs with this
          property are sometimes called semi-Eulerian.

        OUTPUT:

        ``True`` or ``False`` for the closed tour case. For an open tour search
        (``path``=``True``) the function returns ``False`` if the graph is not
        semi-Eulerian, or a tuple (u, v) in the other case. This tuple defines
        the edge that would make the graph Eulerian, i.e. close an existing open
        tour.  This edge may or may not be already present in the graph.

        EXAMPLES::

            sage: graphs.CompleteGraph(4).is_eulerian()
            False
            sage: graphs.CycleGraph(4).is_eulerian()
            True
            sage: g = DiGraph({0:[1,2], 1:[2]}); g.is_eulerian()
            False
            sage: g = DiGraph({0:[2], 1:[3], 2:[0,1], 3:[2]}); g.is_eulerian()
            True
            sage: g = DiGraph({0:[1], 1:[2], 2:[0], 3:[]}); g.is_eulerian()
            True
            sage: g = Graph([(1,2), (2,3), (3,1), (4,5), (5,6), (6,4)]); g.is_eulerian()
            False

        ::

            sage: g = DiGraph({0: [1]}); g.is_eulerian(path=True)
            (1, 0)
            sage: graphs.CycleGraph(4).is_eulerian(path=True)
            False
            sage: g = DiGraph({0: [1], 1: [2,3], 2: [4]}); g.is_eulerian(path=True)
            False

        ::

            sage: g = Graph({0:[1,2,3], 1:[2,3], 2:[3,4], 3:[4]}, multiedges=True)
            sage: g.is_eulerian()
            False
            sage: e = g.is_eulerian(path=True); e
            (0, 1)
            sage: g.add_edge(e)
            sage: g.is_eulerian(path=False)
            True
            sage: g.is_eulerian(path=True)
            False

        TESTS::

            sage: g = Graph({0:[], 1:[], 2:[], 3:[]}); g.is_eulerian()
            True

        Issue :trac:`35168` is fixed::

            sage: Graph([[0, 42, 'John'], [(42, 0)]]).is_eulerian()
            False
            sage: Graph([[0, 42, 'John'], [(42, 'John')]]).is_eulerian()
            False
        """
        # unconnected graph can still be Eulerian if all components
        # up to one doesn't contain any edge
        nontrivial_components = 0
        for cc in self.connected_components(sort=False):
            if len(cc) > 1:
                nontrivial_components += 1
            if nontrivial_components > 1:
                return False

        uv = [None, None]
        if self._directed:
            for v in self:
                # loops don't matter since they count in both the in and out degree.
                if self.in_degree(v) != self.out_degree(v):
                    if path:
                        diff = self.out_degree(v) - self.in_degree(v)
                        if abs(diff) > 1:
                            return False
                        else:
                            # if there was another vertex with the same sign of difference...
                            if uv[(diff + 1) // 2] is not None:
                                return False  # ... the graph is not semi-Eulerian
                            else:
                                uv[(diff + 1) // 2] = v
                    else:
                        return False
        else:
            for v in self:
                # loops don't matter since they add an even number to the degree
                if self.degree(v) % 2:
                    if not path:
                        return False
                    else:
                        if uv[0] is None or uv[1] is None:
                            uv[0 if uv[0] is None else 1] = v
                        else:
                            return False

        if path and None in uv:
            return False

        return True if not path else tuple(uv)

    def order(self):
        """
        Return the number of vertices.

        Note that ``len(G)`` and :meth:`num_verts` also return the number of
        vertices in `G`.

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: G.order()
            10

        ::

            sage: G = graphs.TetrahedralGraph()
            sage: len(G)
            4
        """
        return self._backend.num_verts()

    __len__ = order

    num_verts = order

    def size(self):
        """
        Return the number of edges.

        Note that :meth:`num_edges` also returns the number of edges in `G`.

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: G.size()
            15
        """
        return self._backend.num_edges(self._directed)

    num_edges = size

    # Orientations

    def eulerian_orientation(self):
        r"""
        Return a DiGraph which is an Eulerian orientation of the current graph.

        An Eulerian graph being a graph such that any vertex has an even degree,
        an Eulerian orientation of a graph is an orientation of its edges such
        that each vertex `v` verifies `d^+(v)=d^-(v)=d(v)/2`, where `d^+` and
        `d^-` respectively represent the out-degree and the in-degree of a
        vertex.

        If the graph is not Eulerian, the orientation verifies for any vertex
        `v` that `| d^+(v)-d^-(v) | \leq 1`.

        ALGORITHM:

        This algorithm is a random walk through the edges of the graph, which
        orients the edges according to the walk. When a vertex is reached which
        has no non-oriented edge (this vertex must have odd degree), the walk
        resumes at another vertex of odd degree, if any.

        This algorithm has complexity `O(m)`, where `m` is the number of edges
        in the graph.

        EXAMPLES:

        The CubeGraph with parameter 4, which is regular of even degree, has an
        Eulerian orientation such that `d^+ = d^-`::

            sage: g = graphs.CubeGraph(4)
            sage: g.degree()
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
            sage: o = g.eulerian_orientation()
            sage: o.in_degree()
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
            sage: o.out_degree()
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

        Secondly, the Petersen Graph, which is 3 regular has an orientation such
        that the difference between `d^+` and `d^-` is at most 1::

            sage: g = graphs.PetersenGraph()
            sage: o = g.eulerian_orientation()
            sage: o.in_degree()
            [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
            sage: o.out_degree()
            [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]

        TESTS::

            sage: E0 = Graph(); E4 = Graph(4)  # See trac #21741
            sage: E0.eulerian_orientation()
            Digraph on 0 vertices
            sage: E4.eulerian_orientation()
            Digraph on 4 vertices
        """
        from sage.graphs.digraph import DiGraph

        d = DiGraph()
        d.add_vertices(self.vertex_iterator())

        if not self.size():
            return d

        g = copy(self)

        # list of vertices of odd degree
        odd = [x for x in g.vertex_iterator() if g.degree(x) % 2]

        # Picks the first vertex, which is preferably an odd one
        if odd:
            v = odd.pop()
        else:
            v = next(g.edge_iterator(labels=None))[0]
            odd.append(v)
        # Stops when there is no edge left
        while True:

            # If there is an edge adjacent to the current one
            if g.degree(v):
                e = next(g.edge_iterator(v))
                g.delete_edge(e)
                if e[0] != v:
                    e = (e[1], e[0], e[2])
                d.add_edge(e)
                v = e[1]

            # The current vertex is isolated
            else:
                odd.remove(v)

                # jumps to another odd vertex if possible
                if odd:
                    v = odd.pop()
                # Else jumps to an even vertex which is not isolated
                elif g.size():
                    v = next(g.edge_iterator())[0]
                    odd.append(v)
                # If there is none, we are done !
                else:
                    return d

    def eulerian_circuit(self, return_vertices=False, labels=True, path=False):
        r"""
        Return a list of edges forming an Eulerian circuit if one exists.

        If no Eulerian circuit is found, the method returns ``False``.

        This is implemented using Hierholzer's algorithm.

        INPUT:

        - ``return_vertices`` -- boolean (default: ``False``); optionally
           provide a list of vertices for the path

        - ``labels`` -- boolean (default: ``True``); whether to return edges
           with labels (3-tuples)

        - ``path`` -- boolean (default: ``False``); find an Eulerian path
           instead

        OUTPUT:

        either ([edges], [vertices]) or [edges] of an Eulerian circuit (or path)

        EXAMPLES::

            sage: g = graphs.CycleGraph(5)
            sage: g.eulerian_circuit()
            [(0, 4, None), (4, 3, None), (3, 2, None), (2, 1, None), (1, 0, None)]
            sage: g.eulerian_circuit(labels=False)
            [(0, 4), (4, 3), (3, 2), (2, 1), (1, 0)]

        ::

            sage: g = graphs.CompleteGraph(7)
            sage: edges, vertices = g.eulerian_circuit(return_vertices=True)
            sage: vertices
            [0, 6, 5, 4, 6, 3, 5, 2, 4, 3, 2, 6, 1, 5, 0, 4, 1, 3, 0, 2, 1, 0]

        ::

            sage: graphs.CompleteGraph(4).eulerian_circuit()
            False

        A disconnected graph can be Eulerian::

            sage: g = Graph({0: [], 1: [2], 2: [3], 3: [1], 4: []})
            sage: g.eulerian_circuit(labels=False)
            [(1, 3), (3, 2), (2, 1)]

        ::

            sage: g = DiGraph({0: [1], 1: [2, 4], 2:[3], 3:[1]})
            sage: g.eulerian_circuit(labels=False, path=True)
            [(0, 1), (1, 2), (2, 3), (3, 1), (1, 4)]

        ::

            sage: g = Graph({0:[1,2,3], 1:[2,3], 2:[3,4], 3:[4]})
            sage: g.is_eulerian(path=True)
            (0, 1)
            sage: g.eulerian_circuit(labels=False, path=True)
            [(1, 3), (3, 4), (4, 2), (2, 3), (3, 0), (0, 2), (2, 1), (1, 0)]

        TESTS::

            sage: G = Graph([['D', 'G', 'H', 'L'],
            ....:            [('D', 'H'), ('D', 'L'), ('G', 'H'), ('G', 'L'), ('H', 'L'), ('H', 'L')]],
            ....:           multiedges=True)
            sage: G.eulerian_circuit(labels=False)
            [('D', 'L'), ('L', 'H'), ('H', 'L'), ('L', 'G'), ('G', 'H'), ('H', 'D')]
            sage: Graph({0: [0, 1, 1, 1, 1]}).eulerian_circuit(labels=False)
            [(0, 1), (1, 0), (0, 1), (1, 0), (0, 0)]

        Check graphs without edges (:trac:`28451`)::

            sage: G = Graph()
            sage: G.add_vertex(0)
            sage: G.eulerian_circuit()
            []
            sage: G = Graph()
            sage: G.add_vertices(range(10))
            sage: G.eulerian_circuit(return_vertices=True)
            ([], [])
        """
        # trivial case
        if not self.size():
            return ([], []) if return_vertices else []

        # check if the graph has proper properties to be Eulerian
        edge = self.is_eulerian(path=path)
        if not edge:
            return False
        if path:
            start_vertex = edge[0]

        edges = []
        vertices = []

        # we'll remove edges as we go, so let's preserve the graph structure
        if self.is_directed():
            g = self.reverse()  # so the output will be in the proper order
        else:
            g = copy(self)

        if not path:
            # get the first vertex with degree > 0
            start_vertex = None
            for v in g:
                if g.degree(v):
                    start_vertex = v
                    break

        # (where to return?, what was the way?)
        stack = [(start_vertex, None)]

        if self.is_directed():
            g_degree = g.out_degree
            g_edge_iter = g.outgoing_edge_iterator
        else:
            g_degree = g.degree
            g_edge_iter = g.edge_iterator

        while stack:
            v, e = stack.pop()

            degr = g_degree(v)
            if not degr:
                vertices.append(v)
                if e is not None:
                    edges.append(e if labels else (e[0], e[1]))
            else:
                next_edge = next(g_edge_iter(v))

                if next_edge[0] == v:
                    # in the undirected case we want to save the
                    # direction of traversal
                    next_edge_new = (next_edge[1], next_edge[0], next_edge[2])
                else:
                    next_edge_new = next_edge
                next_vertex = next_edge_new[0]

                stack.append((v, e))
                stack.append((next_vertex, next_edge_new))

                g.delete_edge(next_edge)

        if return_vertices:
            return edges, vertices
        else:
            return edges

    def min_spanning_tree(self,
                          weight_function=None,
                          algorithm="Prim_Boost",
                          starting_vertex=None,
                          check=False,
                          by_weight=False,
                          check_weight=True):
        r"""
        Return the edges of a minimum spanning tree.

        At the moment, no algorithm for directed graph is implemented: if the
        graph is directed, a minimum spanning tree of the corresponding
        undirected graph is returned.

        We expect all weights of the graph to be convertible to float.
        Otherwise, an exception is raised.

        INPUT:

        - ``algorithm`` -- string (default: ``"Prim_Boost"``); the algorithm to
          use in computing a minimum spanning tree of ``G``. The following
          algorithms are supported:

          - ``"Prim_Boost"`` -- Prim's algorithm (Boost implementation)

          - ``"Prim_fringe"`` -- a variant of Prim's algorithm that ignores the
            labels on the edges

          - ``"Prim_edge"`` -- a variant of Prim's algorithm

          - ``"Kruskal"`` -- Kruskal's algorithm

          - ``"Filter_Kruskal"`` -- a variant of Kruskal's algorithm [OSS2009]_

          - ``"Kruskal_Boost"`` -- Kruskal's algorithm (Boost implementation)

          - ``"Boruvka"`` -- Boruvka's algorithm

          - ``NetworkX`` -- uses NetworkX's minimum spanning tree
            implementation

        - ``starting_vertex`` -- a vertex (default: ``None``); the vertex from
          which to begin the search for a minimum spanning tree (available only
          for ``Prim_fringe`` and ``Prim_edge``).

        - ``check`` -- boolean (default: ``False``); whether to first perform
          sanity checks on the input graph ``G``. If appropriate, ``check`` is
          passed on to any minimum spanning tree functions that are invoked from
          the current method. See the documentation of the corresponding
          functions for details on what sort of sanity checks will be performed.

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l`` , if ``l``
          is not ``None``, else ``1`` as a weight. The ``weight_function`` can
          be used to transform the label into a weight (note that, if the weight
          returned is not convertible to a float, an error is raised)

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
          in the graph are weighted, otherwise all edges have weight 1

        - ``check_weight`` -- boolean (default: ``True``); whether to check that
          the ``weight_function`` outputs a number for each edge.

        OUTPUT:

        The edges of a minimum spanning tree of ``G``, if one exists, otherwise
        returns the empty list.

        .. SEEALSO::

            - :func:`sage.graphs.spanning_tree.kruskal`
            - :func:`sage.graphs.spanning_tree.filter_kruskal`
            - :func:`sage.graphs.spanning_tree.boruvka`
            - :func:`sage.graphs.base.boost_graph.min_spanning_tree`

        EXAMPLES:

        Kruskal's algorithm::

            sage: g = graphs.CompleteGraph(5)
            sage: len(g.min_spanning_tree())
            4
            sage: weight = lambda e: 1 / ((e[0] + 1) * (e[1] + 1))
            sage: sorted(g.min_spanning_tree(weight_function=weight))
            [(0, 4, None), (1, 4, None), (2, 4, None), (3, 4, None)]
            sage: sorted(g.min_spanning_tree(weight_function=weight, algorithm='Kruskal_Boost'))
            [(0, 4, None), (1, 4, None), (2, 4, None), (3, 4, None)]
            sage: g = graphs.PetersenGraph()
            sage: g.allow_multiple_edges(True)
            sage: g.add_edges(g.edge_iterator())
            sage: sorted(g.min_spanning_tree())
            [(0, 1, None), (0, 4, None), (0, 5, None), (1, 2, None), (1, 6, None), (3, 8, None), (5, 7, None), (5, 8, None), (6, 9, None)]

        Boruvka's algorithm::

            sage: sorted(g.min_spanning_tree(algorithm='Boruvka'))
            [(0, 1, None), (0, 4, None), (0, 5, None), (1, 2, None),  (1, 6, None), (2, 3, None), (2, 7, None),  (3, 8, None), (4, 9, None)]

        Prim's algorithm::

            sage: g = graphs.CompleteGraph(5)
            sage: sorted(g.min_spanning_tree(algorithm='Prim_edge', starting_vertex=2, weight_function=weight))
            [(0, 4, None), (1, 4, None), (2, 4, None), (3, 4, None)]
            sage: sorted(g.min_spanning_tree(algorithm='Prim_fringe', starting_vertex=2, weight_function=weight))
            [(0, 4, None), (1, 4, None), (2, 4, None), (3, 4, None)]
            sage: sorted(g.min_spanning_tree(weight_function=weight, algorithm='Prim_Boost'))
            [(0, 4, None), (1, 4, None), (2, 4, None), (3, 4, None)]

        NetworkX algorithm::

            sage: sorted(g.min_spanning_tree(algorithm='NetworkX'))
            [(0, 1, None), (0, 2, None), (0, 3, None), (0, 4, None)]

        More complicated weights::

            sage: G = Graph([(0,1,{'name':'a','weight':1}), (0,2,{'name':'b','weight':3}), (1,2,{'name':'b','weight':1})])
            sage: sorted(G.min_spanning_tree(weight_function=lambda e: e[2]['weight']))
            [(0, 1, {'name': 'a', 'weight': 1}), (1, 2, {'name': 'b', 'weight': 1})]

        If the graph is not weighted, edge labels are not considered, even if
        they are numbers::

            sage: g = Graph([(1, 2, 1), (1, 3, 2), (2, 3, 1)])
            sage: sorted(g.min_spanning_tree())
            [(1, 2, 1), (1, 3, 2)]

        In order to use weights, we need either to set variable ``weighted`` to
        ``True``, or to specify a weight function or set by_weight to ``True``::

            sage: g.weighted(True)
            sage: sorted(g.min_spanning_tree())
            [(1, 2, 1), (2, 3, 1)]
            sage: g.weighted(False)
            sage: sorted(g.min_spanning_tree())
            [(1, 2, 1), (1, 3, 2)]
            sage: sorted(g.min_spanning_tree(by_weight=True))
            [(1, 2, 1), (2, 3, 1)]
            sage: sorted(g.min_spanning_tree(weight_function=lambda e: e[2]))
            [(1, 2, 1), (2, 3, 1)]

        TESTS:

        Check that, if ``weight_function`` is not provided, then edge weights
        are used::

            sage: g = Graph(weighted=True)
            sage: g.add_edges([[0, 1, 1], [1, 2, 1], [2, 0, 10]])
            sage: sorted(g.min_spanning_tree())
            [(0, 1, 1), (1, 2, 1)]
            sage: sorted(g.min_spanning_tree(algorithm='Filter_Kruskal'))
            [(0, 1, 1), (1, 2, 1)]
            sage: sorted(g.min_spanning_tree(algorithm='Kruskal_Boost'))
            [(0, 1, 1), (1, 2, 1)]
            sage: sorted(g.min_spanning_tree(algorithm='Prim_fringe'))
            [(0, 1, 1), (1, 2, 1)]
            sage: sorted(g.min_spanning_tree(algorithm='Prim_edge'))
            [(0, 1, 1), (1, 2, 1)]
            sage: sorted(g.min_spanning_tree(algorithm='Prim_Boost'))
            [(0, 1, 1), (1, 2, 1)]
            sage: sorted(g.min_spanning_tree(algorithm='NetworkX'))
            [(0, 1, 1), (1, 2, 1)]
            sage: sorted(g.min_spanning_tree(algorithm='Boruvka'))
            [(0, 1, 1), (1, 2, 1)]

        Check that, if ``weight_function`` is provided, it overrides edge
        weights::

            sage: g = Graph([[0, 1, 1], [1, 2, 1], [2, 0, 10]], weighted=True)
            sage: weight = lambda e: 3 - e[0] - e[1]
            sage: sorted(g.min_spanning_tree(weight_function=weight))
            [(0, 2, 10), (1, 2, 1)]
            sage: sorted(g.min_spanning_tree(algorithm='Filter_Kruskal', weight_function=weight))
            [(0, 2, 10), (1, 2, 1)]
            sage: sorted(g.min_spanning_tree(algorithm='Kruskal_Boost', weight_function=weight))
            [(0, 2, 10), (1, 2, 1)]
            sage: sorted(g.min_spanning_tree(algorithm='Prim_fringe', weight_function=weight))
            [(0, 2, 10), (1, 2, 1)]
            sage: sorted(g.min_spanning_tree(algorithm='Prim_edge', weight_function=weight))
            [(0, 2, 10), (1, 2, 1)]
            sage: sorted(g.min_spanning_tree(algorithm='Prim_Boost', weight_function=weight))
            [(0, 2, 10), (1, 2, 1)]
            sage: sorted(g.min_spanning_tree(algorithm='NetworkX', weight_function=weight))
            [(0, 2, 10), (1, 2, 1)]
            sage: sorted(g.min_spanning_tree(algorithm='Boruvka', weight_function=weight))
            [(0, 2, 10), (1, 2, 1)]

        If the graph is directed, it is transformed into an undirected graph::

            sage: g = digraphs.Circuit(3)
            sage: sorted(g.min_spanning_tree(weight_function=weight))
            [(0, 2, None), (1, 2, None)]
            sage: sorted(g.to_undirected().min_spanning_tree(weight_function=weight))
            [(0, 2, None), (1, 2, None)]

        If at least an edge weight is not convertible to a float, an error is
        raised::

            sage: g = Graph([(0, 1, 1), (1, 2, 'a')], weighted=True)
            sage: g.min_spanning_tree()
            Traceback (most recent call last):
            ...
            ValueError: the weight function cannot find the weight of (1, 2, 'a')
            sage: g = Graph([(0, 1, 1), (1, 2, [1, 2, 3])], weighted=True)
            sage: g.min_spanning_tree()
            Traceback (most recent call last):
            ...
            ValueError: the weight function cannot find the weight of (1, 2, [1, 2, 3])

        Special case of the empty graph::

            sage: graphs.EmptyGraph().min_spanning_tree()
            []
        """
        if not self.order():
            return []

        # for weighted graphs
        if self.weighted():
            by_weight = True

        by_weight, weight_function = self._get_weight_function(by_weight=by_weight,
                                                               weight_function=weight_function,
                                                               check_weight=check_weight)

        def wfunction_float(e):
            return float(weight_function(e))

        if algorithm in ["Kruskal", "Filter_Kruskal", "Kruskal_Boost", "Prim_Boost", "Boruvka"]:
            if self.is_directed():
                g = self.to_undirected()
            else:
                g = self

            if algorithm == "Kruskal":
                from .spanning_tree import kruskal
                return kruskal(g, weight_function=wfunction_float, check_weight=False, check=check)
            if algorithm == "Filter_Kruskal":
                from .spanning_tree import filter_kruskal
                return filter_kruskal(g, weight_function=wfunction_float, check_weight=False, check=check)
            elif algorithm == "Boruvka":
                from .spanning_tree import boruvka
                return boruvka(g, weight_function=wfunction_float, check_weight=False, check=check)
            else:
                from sage.graphs.base.boost_graph import min_spanning_tree
                return min_spanning_tree(g,
                                         weight_function=wfunction_float,
                                         algorithm=algorithm.split("_")[0])

        if algorithm == "Prim_fringe":
            if starting_vertex is None:
                v = next(self.vertex_iterator())
            else:
                v = starting_vertex
            tree = set([v])
            edges = []
            # Initialize fringe_list with v's neighbors. Fringe_list
            # contains fringe_vertex: (weight, vertex_in_tree) for each
            # fringe vertex.
            fringe_list = {e[0] if e[0] != v else e[1]: (wfunction_float(e), v) for e in self.edges_incident(v)}

            def cmp_fun(x):
                return fringe_list[x][0]

            for i in range(self.order() - 1):
                # find the smallest-weight fringe vertex
                u = min(fringe_list, key=cmp_fun)
                x = fringe_list[u][1]
                if hash(u) < hash(x):
                    edges.append((u, x, self.edge_label(u, x)))
                else:
                    edges.append((x, u, self.edge_label(x, u)))
                tree.add(u)
                fringe_list.pop(u)
                # update fringe list
                for e in self.edges_incident(u):
                    neighbor = e[0] if e[0] != u else e[1]
                    if neighbor in tree:
                        continue
                    w = wfunction_float(e)
                    if neighbor not in fringe_list or fringe_list[neighbor][0] > w:
                        fringe_list[neighbor] = (w, u)
            return edges

        elif algorithm == "Prim_edge":
            if starting_vertex is None:
                v = next(self.vertex_iterator())
            else:
                v = starting_vertex
            sorted_edges = sorted(self.edges(sort=False), key=wfunction_float)
            tree = set([v])
            edges = []
            for _ in range(self.order() - 1):
                # Find a minimum-weight edge connecting a vertex in the tree to
                # something outside the tree. Remove the edges between tree
                # vertices for efficiency.
                i = 0
                while True:
                    e = sorted_edges[i]
                    v0, v1 = e[0], e[1]
                    if v0 in tree:
                        del sorted_edges[i]
                        if v1 in tree:
                            continue
                        edges.append(e)
                        tree.add(v1)
                        break
                    elif v1 in tree:
                        del sorted_edges[i]
                        edges.append(e)
                        tree.add(v0)
                        break
                    else:
                        i += 1
            return edges

        elif algorithm == "NetworkX":
            import networkx
            G = networkx.Graph([(e[0], e[1], {'weight': wfunction_float(e)}) for e in self.edge_iterator()])
            E = networkx.minimum_spanning_edges(G, data=False)
            return [(u, v, self.edge_label(u, v)) if hash(u) < hash(v) else (v, u, self.edge_label(u, v))
                    for u, v in E]
        else:
            raise NotImplementedError("minimum spanning tree algorithm '%s' is not implemented" % algorithm)

    def spanning_trees_count(self, root_vertex=None):
        r"""
        Return the number of spanning trees in a graph.

        In the case of a digraph, counts the number of spanning out-trees rooted
        in ``root_vertex``.  Default is to set first vertex as root.

        This computation uses Kirchhoff's Matrix Tree Theorem [1] to calculate
        the number of spanning trees. For complete graphs on `n` vertices the
        result can also be reached using Cayley's formula: the number of
        spanning trees are `n^(n-2)`.

        For digraphs, the augmented Kirchhoff Matrix as defined in [2] is used
        for calculations. Here the result is the number of out-trees rooted at a
        specific vertex.

        INPUT:

        - ``root_vertex`` -- a vertex (default: ``None``); the vertex that will
          be used as root for all spanning out-trees if the graph is a directed
          graph. Otherwise, the first vertex returned by :meth:`vertex_iterator`
          is used. This argument is ignored if the graph is not a digraph.

        .. SEEALSO::

            :meth:`~sage.graphs.graph.Graph.spanning_trees` -- enumerates all
            spanning trees of a graph


        REFERENCES:

        - [1] http://mathworld.wolfram.com/MatrixTreeTheorem.html

        - [2] Lih-Hsing Hsu, Cheng-Kuan Lin, "Graph Theory and
          Interconnection Networks"

        AUTHORS:

        - Anders Jonsson (2009-10-10)

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: G.spanning_trees_count()
            2000

        ::

            sage: n = 11
            sage: G = graphs.CompleteGraph(n)
            sage: ST = G.spanning_trees_count()
            sage: ST == n ^ (n - 2)
            True

        ::

            sage: M = matrix(3, 3, [0, 1, 0, 0, 0, 1, 1, 1, 0])
            sage: D = DiGraph(M)
            sage: D.spanning_trees_count()
            1
            sage: D.spanning_trees_count(0)
            1
            sage: D.spanning_trees_count(2)
            2
        """
        if not self.order():
            return 0

        vertices = list(self)
        if not self.is_directed():
            M = self.kirchhoff_matrix(vertices=vertices)
            M.subdivide(1, 1)
            M2 = M.subdivision(1, 1)
            return M2.determinant()
        else:
            if root_vertex is None:
                root_vertex = vertices[0]
                index = 0
            elif root_vertex not in vertices:
                raise ValueError("vertex (%s) not in the graph" % root_vertex)
            else:
                index = vertices.index(root_vertex)

            M = self.kirchhoff_matrix(vertices=vertices)
            M[index, index] += 1
            return abs(M.determinant())

    def cycle_basis(self, output='vertex'):
        r"""
        Return a list of cycles which form a basis of the cycle space of
        ``self``.

        A basis of cycles of a graph is a minimal collection of cycles
        (considered as sets of edges) such that the edge set of any cycle in the
        graph can be written as a `Z/2Z` sum of the cycles in the basis.

        See the :wikipedia:`Cycle_basis` for more information.

        INPUT:

        - ``output`` -- string (default: ``'vertex'``); whether every cycle is
          given as a list of vertices (``output == 'vertex'``) or a list of
          edges (``output == 'edge'``)

        OUTPUT:

        A list of lists, each of them representing the vertices (or the edges)
        of a cycle in a basis.

        ALGORITHM:

        Uses the NetworkX library for graphs without multiple edges.

        Otherwise, by the standard algorithm using a spanning tree.

        EXAMPLES:

        A cycle basis in Petersen's Graph ::

            sage: g = graphs.PetersenGraph()
            sage: g.cycle_basis()
            [[1, 6, 8, 5, 0], [4, 9, 6, 8, 5, 0], [7, 9, 6, 8, 5], [4, 3, 8, 5, 0], [1, 2, 3, 8, 5, 0], [7, 2, 3, 8, 5]]

        One can also get the result as a list of lists of edges::

            sage: g.cycle_basis(output='edge')
            [[(1, 6, None), (6, 8, None), (8, 5, None), (5, 0, None),
            (0, 1, None)], [(4, 9, None), (9, 6, None), (6, 8, None),
            (8, 5, None), (5, 0, None), (0, 4, None)], [(7, 9, None),
            (9, 6, None), (6, 8, None), (8, 5, None), (5, 7, None)],
            [(4, 3, None), (3, 8, None), (8, 5, None), (5, 0, None),
            (0, 4, None)], [(1, 2, None), (2, 3, None), (3, 8, None),
            (8, 5, None), (5, 0, None), (0, 1, None)], [(7, 2, None),
            (2, 3, None), (3, 8, None), (8, 5, None), (5, 7, None)]]

        Checking the given cycles are algebraically free::

            sage: g = graphs.RandomGNP(30, .4)
            sage: basis = g.cycle_basis()

        Building the space of (directed) edges over `Z/2Z`. On the way, building
        a dictionary associating a unique vector to each undirected edge::

            sage: m = g.size()
            sage: edge_space = VectorSpace(FiniteField(2), m)
            sage: edge_vector = dict(zip(g.edges(labels=False, sort=False), edge_space.basis()))
            sage: for (u, v), vec in list(edge_vector.items()):
            ....:    edge_vector[(v, u)] = vec

        Defining a lambda function associating a vector to the vertices of a
        cycle::

            sage: vertices_to_edges = lambda x: zip(x, x[1:] + [x[0]])
            sage: cycle_to_vector = lambda x: sum(edge_vector[e] for e in vertices_to_edges(x))

        Finally checking the cycles are a free set::

            sage: basis_as_vectors = [cycle_to_vector(_) for _ in basis]
            sage: edge_space.span(basis_as_vectors).rank() == len(basis)
            True

        For undirected graphs with multiple edges::

            sage: G = Graph([(0, 2, 'a'), (0, 2, 'b'), (0, 1, 'c'), (1, 2, 'd')], multiedges=True)
            sage: G.cycle_basis()
            [[0, 2], [2, 1, 0]]
            sage: G.cycle_basis(output='edge')
            [[(0, 2, 'a'), (2, 0, 'b')], [(2, 1, 'd'), (1, 0, 'c'), (0, 2, 'a')]]
            sage: H = Graph([(1, 2), (2, 3), (2, 3), (3, 4), (1, 4), (1, 4), (4, 5), (5, 6), (4, 6), (6, 7)], multiedges=True)
            sage: H.cycle_basis()
            [[1, 4], [2, 3], [4, 3, 2, 1], [6, 5, 4]]

        Disconnected graph::

            sage: G.add_cycle(["Hey", "Wuuhuu", "Really ?"])
            sage: [sorted(c) for c in G.cycle_basis()]
            [['Hey', 'Really ?', 'Wuuhuu'], [0, 2], [0, 1, 2]]
            sage: [sorted(c) for c in G.cycle_basis(output='edge')]
            [[('Hey', 'Wuuhuu', None),
              ('Really ?', 'Hey', None),
              ('Wuuhuu', 'Really ?', None)],
             [(0, 2, 'a'), (2, 0, 'b')],
             [(0, 2, 'b'), (1, 0, 'c'), (2, 1, 'd')]]

        Graph that allows multiple edges but does not contain any::

            sage: G = graphs.CycleGraph(3)
            sage: G.allow_multiple_edges(True)
            sage: G.cycle_basis()
            [[2, 1, 0]]

        Not yet implemented for directed graphs::

            sage: G = DiGraph([(0, 2, 'a'), (0, 1, 'c'), (1, 2, 'd')])
            sage: G.cycle_basis()
            Traceback (most recent call last):
            ...
            NotImplementedError: not implemented for directed graphs

        TESTS:

        :trac:`27538`::

            sage: G= Graph([(1, 2, 'a'), (2, 3, 'b'), (2, 3, 'c'), (3, 4, 'd'), (3, 4, 'e'), (4, 1, 'f')], multiedges=True)
            sage: G.cycle_basis()
            [[2, 3], [4, 3, 2, 1], [4, 3, 2, 1]]
            sage: G.cycle_basis(output='edge')
            [[(2, 3, 'b'), (3, 2, 'c')],
             [(4, 3, 'd'), (3, 2, 'b'), (2, 1, 'a'), (1, 4, 'f')],
             [(4, 3, 'e'), (3, 2, 'b'), (2, 1, 'a'), (1, 4, 'f')]]

        """
        if output not in ['vertex', 'edge']:
            raise ValueError('output must be either vertex or edge')

        if self.is_directed():
            raise NotImplementedError('not implemented for directed graphs')

        if self.allows_multiple_edges():
            if not self.is_connected():
                return sum([g.cycle_basis(output=output)
                            for g in self.connected_components_subgraphs()],
                           [])

            from sage.graphs.graph import Graph
            T = Graph(self.min_spanning_tree(), multiedges=True, format='list_of_edges')
            H = self.copy()
            H.delete_edges(T.edge_iterator())
            L = []
            for e in H.edge_iterator():
                T.add_edge(e)
                L.append(T.is_tree(certificate=True, output=output)[1])
                T.delete_edge(e)
            return L

        # second case: there are no multiple edges
        import networkx
        cycle_basis_v = networkx.cycle_basis(self.networkx_graph())
        if output == 'vertex':
            return cycle_basis_v

        def vertices_to_edges(x):
            return [(u[0], u[1], self.edge_label(u[0], u[1]))
                    for u in zip(x, x[1:] + [x[0]])]
        return [vertices_to_edges(_) for _ in cycle_basis_v]

    def minimum_cycle_basis(self, algorithm=None, weight_function=None, by_weight=False, check_weight=True):
        r"""
        Return a minimum weight cycle basis of the graph.

        A cycle basis is a list of cycles (list of vertices forming a cycle) of
        ``self``. Note that the vertices are not necessarily returned in the
        order in which they appear in the cycle.

        A minimum weight cycle basis is a cycle basis that minimizes the sum of
        the weights (length for unweighted graphs) of its cycles.

        Not implemented for directed graphs and multigraphs.

        INPUT:

        - ``algorithm`` -- string (default: ``None``); algorithm to use:

          * If ``algorithm = "NetworkX"``, use networkx implementation

          * If ``algorithm = None``, use Sage Cython implementation

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l``, if ``l``
          is not ``None``, else ``1`` as a weight.

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
          in the graph are weighted, otherwise all edges have weight 1

        - ``check_weight`` -- boolean (default: ``True``); whether to check that
          the ``weight_function`` outputs a number for each edge.

        EXAMPLES::

            sage: g = Graph([(1, 2, 3), (2, 3, 5), (3, 4, 8), (4, 1, 13), (1, 3, 250), (5, 6, 9), (6, 7, 17), (7, 5, 20)])
            sage: sorted(g.minimum_cycle_basis(by_weight=True))
            [[1, 2, 3], [1, 2, 3, 4], [5, 6, 7]]
            sage: sorted(g.minimum_cycle_basis(by_weight=False))
            [[1, 2, 3], [1, 3, 4], [5, 6, 7]]
            sage: sorted(g.minimum_cycle_basis(by_weight=True, algorithm='NetworkX'))
            [[1, 2, 3], [1, 2, 3, 4], [5, 6, 7]]
            sage: g.minimum_cycle_basis(by_weight=False, algorithm='NetworkX')
            [[1, 2, 3], [1, 3, 4], [5, 6, 7]]

        ::

            sage: g = Graph([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (5, 3)])
            sage: sorted(g.minimum_cycle_basis(by_weight=False))
            [[1, 2, 3, 5], [3, 4, 5]]
            sage: sorted(g.minimum_cycle_basis(by_weight=False, algorithm='NetworkX'))
            [[1, 2, 3, 5], [3, 4, 5]]

        TESTS::

            sage: g = Graph([(0, 1, 1), (1, 2, 'a')])
            sage: g.min_spanning_tree(by_weight=True)
            Traceback (most recent call last):
            ...
            ValueError: the weight function cannot find the weight of (1, 2, 'a')


        .. SEEALSO::

            * :meth:`~cycle_basis`
            * :wikipedia:`Cycle_basis`
        """
        if not self.order():
            return []
        # Sanity checks
        if self.is_directed():
            raise NotImplementedError("not implemented for directed graphs")
        self._scream_if_not_simple()

        by_weight, weight_function = self._get_weight_function(by_weight=by_weight,
                                                               weight_function=weight_function,
                                                               check_weight=check_weight)

        if algorithm:
            algorithm = algorithm.lower()
        if algorithm == "networkx":
            import networkx
            G = networkx.Graph([(e[0], e[1], {'weight': weight_function(e)}) for e in self.edge_iterator()])
            return networkx.minimum_cycle_basis(G, weight='weight')
        elif algorithm is None:
            from sage.graphs.base.boost_graph import min_cycle_basis
            if self.is_connected():
                CC = [self]
            else:
                CC = self.connected_components_subgraphs()
            basis = []
            for comp in CC:
                # calling Cython implementation from backend
                basis.append(min_cycle_basis(comp, weight_function=weight_function,
                                             by_weight=by_weight))
            return sum(basis, [])
        else:
            raise NotImplementedError("only 'NetworkX' and Cython implementation is supported")

    # Planarity

    def is_planar(self, on_embedding=None, kuratowski=False, set_embedding=False, set_pos=False):
        r"""
        Check whether the graph is planar.

        This wraps the reference implementation provided by John Boyer of the
        linear time planarity algorithm by edge addition due to Boyer
        Myrvold. (See reference code in :mod:`~sage.graphs.planarity`).

        .. NOTE::

            The argument on_embedding takes precedence over
            ``set_embedding``. This means that only the ``on_embedding``
            combinatorial embedding will be tested for planarity and no
            ``_embedding`` attribute will be set as a result of this function
            call, unless ``on_embedding`` is None.

        REFERENCE:

        [BM2004]_

        .. SEEALSO::

            - "Almost planar graph": :meth:`~Graph.is_apex`
            - "Measuring non-planarity": :meth:`~genus`, :meth:`~crossing_number`
            - :meth:`planar_dual`
            - :meth:`faces`
            - :meth:`~sage.graphs.graph.Graph.is_polyhedral`

        INPUT:

        - ``on_embedding`` -- dictionary (default: ``None``); the embedding
          dictionary to test planarity on (i.e.: will return ``True`` or
          ``False`` only for the given embedding)

        - ``kuratowski`` -- boolean (default: ``False``); whether to return a
          tuple with boolean as first entry. If the graph is nonplanar, will
          return the Kuratowski subgraph (i.e. an edge subdivision of `K_5` or
          `K_{3,3}`) as the second tuple entry.  If the graph is planar, returns
          ``None`` as the second entry. When set to ``False``, only a boolean
          answer is returned.

        - ``set_embedding`` -- boolean (default: ``False``); whether to set the
          instance field variable that contains a combinatorial embedding
          (clockwise ordering of neighbors at each vertex). This value will only
          be set if a planar embedding is found. It is stored as a Python dict:
          ``v1: [n1,n2,n3]`` where ``v1`` is a vertex and ``n1,n2,n3`` are its
          neighbors.

        - ``set_pos`` -- boolean (default: ``False``); whether to set the
          position dictionary (for plotting) to reflect the combinatorial
          embedding.  Note that this value will default to False if set_emb is
          set to False. Also, the position dictionary will only be updated if a
          planar embedding is found.

        EXAMPLES::

            sage: g = graphs.CubeGraph(4)
            sage: g.is_planar()
            False

        ::

            sage: g = graphs.CircularLadderGraph(4)
            sage: g.is_planar(set_embedding=True)
            True
            sage: g.get_embedding()
            {0: [1, 4, 3],
             1: [2, 5, 0],
             2: [3, 6, 1],
             3: [0, 7, 2],
             4: [0, 5, 7],
             5: [1, 6, 4],
             6: [2, 7, 5],
             7: [4, 6, 3]}

        ::

            sage: g = graphs.PetersenGraph()
            sage: (g.is_planar(kuratowski=True))[1].adjacency_matrix()
            [0 1 0 0 0 1 0 0 0]
            [1 0 1 0 0 0 1 0 0]
            [0 1 0 1 0 0 0 1 0]
            [0 0 1 0 0 0 0 0 1]
            [0 0 0 0 0 0 1 1 0]
            [1 0 0 0 0 0 0 1 1]
            [0 1 0 0 1 0 0 0 1]
            [0 0 1 0 1 1 0 0 0]
            [0 0 0 1 0 1 1 0 0]

        ::

            sage: k43 = graphs.CompleteBipartiteGraph(4, 3)
            sage: result = k43.is_planar(kuratowski=True); result
            (False, Graph on 6 vertices)
            sage: result[1].is_isomorphic(graphs.CompleteBipartiteGraph(3, 3))
            True

        Multi-edged and looped graphs are partially supported::

            sage: G = Graph({0: [1, 1]}, multiedges=True)
            sage: G.is_planar()
            True
            sage: G.is_planar(on_embedding={})
            Traceback (most recent call last):
            ...
            NotImplementedError: cannot compute with embeddings of multiple-edged or looped graphs
            sage: G.is_planar(set_pos=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: cannot compute with embeddings of multiple-edged or looped graphs
            sage: G.is_planar(set_embedding=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: cannot compute with embeddings of multiple-edged or looped graphs
            sage: G.is_planar(kuratowski=True)
            (True, None)

        ::

            sage: G = graphs.CompleteGraph(5)
            sage: G = Graph(G, multiedges=True)
            sage: G.add_edge(0, 1)
            sage: G.is_planar()
            False
            sage: b,k = G.is_planar(kuratowski=True)
            sage: b
            False
            sage: k.vertices(sort=True)
            [0, 1, 2, 3, 4]

        TESTS:

        :trac:`18045`::

            sage: g = graphs.CompleteGraph(4)
            sage: g.is_planar(set_embedding=True)
            True
            sage: emb = {0 : [2,3,1], 1: [2,3,0], 2: [1,3,0], 3:[0,1,2]}
            sage: g.is_planar(on_embedding=emb)
            False

        :trac:`19193`::

            sage: posets.BooleanLattice(3).cover_relations_graph().is_planar()
            True

        :trac:`33759`::

            sage: G = Graph([(1, 2)])
            sage: for set_embedding, set_pos in ((True,True), (True,False), (False, True), (False, False)):
            ....:     G = Graph([(1, 2)])
            ....:     assert G.is_planar(set_embedding=set_embedding, set_pos=set_pos)
            ....:     assert (hasattr(G, '_embedding') and G._embedding is not None) == set_embedding, (set_embedding, set_pos)
            ....:     assert (hasattr(G, '_pos') and G._pos is not None) == set_pos, (set_embedding, set_pos)

        :trac:`34122`::

            sage: G = DiGraph([[1, 2], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5],
            ....:              [3, 4], [3, 5], [4, 5], [5, 1]])
            sage: G.is_planar()
            True

        Corner cases::

            sage: graphs.EmptyGraph().is_planar()
            True
            sage: Graph(1).is_planar()
            True
        """
        # Quick check first
        if (on_embedding is None and not kuratowski and not set_embedding and not set_pos
                and not self.allows_loops() and not self.allows_multiple_edges()
                and not self.is_directed()):
            if self.order() > 4 and self.size() > 3 * self.order() - 6:
                return False

        if self.has_multiple_edges() or self.has_loops():
            if set_embedding or (on_embedding is not None) or set_pos:
                raise NotImplementedError("cannot compute with embeddings of multiple-edged or looped graphs")
            else:
                return self.to_simple().is_planar(kuratowski=kuratowski)

        if on_embedding is not None:
            self._check_embedding_validity(on_embedding, boolean=False)
            return (0 == self.genus(minimal=False, set_embedding=False, on_embedding=on_embedding))
        else:
            from sage.graphs.planarity import is_planar
            G = self.to_undirected()
            if hasattr(G, '_immutable'):
                G = copy(G)
            planar = is_planar(G, kuratowski=kuratowski, set_pos=set_pos, set_embedding=set_embedding)
            if kuratowski:
                bool_result = planar[0]
            else:
                bool_result = planar
            if bool_result:
                if set_pos:
                    self._pos = G._pos
                if set_embedding:
                    self._embedding = G._embedding
            return planar

    def is_circular_planar(self, on_embedding=None, kuratowski=False,
                           set_embedding=True, boundary=None,
                           ordered=False, set_pos=False):
        r"""
        Check whether the graph is circular planar (outerplanar)

        A graph is circular planar if it has a planar embedding in which all
        vertices can be drawn in order on a circle. This method can also be used
        to check the existence of a planar embedding in which the vertices of a
        specific set (the *boundary*) can be drawn on a circle, all other
        vertices being drawn inside of the circle. An order can be defined on
        the vertices of the boundary in order to define how they are to appear
        on the circle.

        INPUT:

        - ``on_embedding`` -- dictionary (default: ``None``); the embedding
          dictionary to test planarity on (i.e.: will return ``True`` or
          ``False`` only for the given embedding)

        - ``kuratowski`` -- boolean (default: ``False``); whether to return a
          tuple with boolean first entry and the Kuratowski subgraph (i.e. an
          edge subdivision of `K_5` or `K_{3,3}`) as the second entry (see
          OUTPUT below)

        - ``set_embedding`` -- boolean (default: ``True``); whether or not to
          set the instance field variable that contains a combinatorial
          embedding (clockwise ordering of neighbors at each vertex). This value
          will only be set if a circular planar embedding is found. It is stored
          as a Python dict: ``v1: [n1,n2,n3]`` where ``v1`` is a vertex and
          ``n1,n2,n3`` are its neighbors.

        - ``boundary`` -- list (default: ``None``); an ordered list of vertices
          that are required to be drawn on the circle, all others being drawn
          inside of it. It is set to ``None`` by default, meaning that *all*
          vertices should be drawn on the boundary.

        - ``ordered`` -- boolean (default: ``False``); whether or not to
          consider the order of the boundary. It required ``boundary`` to be
          defined.

        - ``set_pos`` -- boolean (default: ``False``); whether or not to set the
          position dictionary (for plotting) to reflect the combinatorial
          embedding. Note that this value will default to ``False`` if
          ``set_embedding`` is set to ``False``. Also, the position dictionary
          will only be updated if a circular planar embedding is found.

        OUTPUT:

        The method returns ``True`` if the graph is circular planar, and
        ``False`` if it is not.

        If ``kuratowski`` is set to ``True``, then this function will return a
        tuple, whose first entry is a boolean and whose second entry is the
        Kuratowski subgraph (i.e. an edge subdivision of `K_5` or `K_{3,3}`)
        isolated by the Boyer-Myrvold algorithm. Note that this graph might
        contain a vertex or edges that were not in the initial graph.  These
        would be elements referred to below as parts of the wheel and the star,
        which were added to the graph to require that the boundary can be drawn
        on the boundary of a disc, with all other vertices drawn inside (and no
        edge crossings).

        ALGORITHM:

        This is a linear time algorithm to test for circular planarity. It
        relies on the edge-addition planarity algorithm due to Boyer-Myrvold. We
        accomplish linear time for circular planarity by modifying the graph
        before running the general planarity algorithm.

        REFERENCE:

        [BM2004]_

        EXAMPLES::

            sage: g439 = Graph({1: [5, 7], 2: [5, 6], 3: [6, 7], 4: [5, 6, 7]})
            sage: g439.show()
            sage: g439.is_circular_planar(boundary=[1, 2, 3, 4])
            False
            sage: g439.is_circular_planar(kuratowski=True, boundary=[1, 2, 3, 4])
            (False, Graph on 8 vertices)
            sage: g439.is_circular_planar(kuratowski=True, boundary=[1, 2, 3])
            (True, None)
            sage: g439.get_embedding()
            {1: [5, 7],
             2: [6, 5],
             3: [7, 6],
             4: [5, 6, 7],
             5: [2, 4, 1],
             6: [3, 4, 2],
             7: [1, 4, 3]}

        Order matters::

            sage: K23 = graphs.CompleteBipartiteGraph(2, 3)
            sage: K23.is_circular_planar(boundary=[0, 1, 2, 3])
            True
            sage: K23.is_circular_planar(ordered=True, boundary=[0, 1, 2, 3])
            False

        With a different order::

            sage: K23.is_circular_planar(set_embedding=True, boundary=[0, 2, 1, 3])
            True

        TESTS:

        Non-simple graphs::

            sage: Graph([(1, 1)], loops=True).is_circular_planar(set_embedding=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: cannot compute with embeddings of multiple-edged or looped graphs

        Argument saving::

            sage: G = Graph([(1, 2)])
            sage: for set_embedding, set_pos in ((True,True), (True,False), (False, True), (False, False)):
            ....:     G = Graph([(1, 2)])
            ....:     assert G.is_circular_planar(set_embedding=set_embedding, set_pos=set_pos)
            ....:     assert (hasattr(G, '_embedding') and G._embedding is not None) == set_embedding, (set_embedding, set_pos)
            ....:     assert (hasattr(G, '_pos') and G._pos is not None) == set_pos, (set_embedding, set_pos)

        Corner cases::

            sage: graphs.EmptyGraph().is_circular_planar()
            True
            sage: Graph(1).is_circular_planar()
            True
        """
        if ordered and boundary is None:
            raise ValueError("boundary must be set when ordered is True")

        # Quick check first
        if (on_embedding is None and not kuratowski and set_embedding and
                boundary is None and not ordered and not set_pos and
                not self.allows_loops() and not self.allows_multiple_edges()):
            if self.order() > 3 and self.size() > 2 * self.order() - 3:
                return False

        if self.has_multiple_edges() or self.has_loops():
            if set_embedding or (on_embedding is not None) or set_pos:
                raise NotImplementedError("cannot compute with embeddings of multiple-edged or looped graphs")
            else:
                return self.to_simple().is_circular_planar(kuratowski=kuratowski, boundary=boundary, ordered=ordered)

        if boundary is None:
            boundary = self

        # A local copy of self
        from sage.graphs.graph import Graph
        from sage.graphs.planarity import is_planar
        graph = Graph(self)
        if hasattr(graph, '_embedding'):
            del graph._embedding

        # Adds a new vertex to the graph and connects it to all vertices of the
        # boundary
        extra = graph.add_vertex()
        graph.add_edges((vertex, extra) for vertex in boundary)

        extra_edges = []

        # When ordered is True, we need a way to make sure that the ordering is
        # respected.
        if ordered:

            # We add edges between consecutive vertices of the boundary (only
            # len(boundary)-1 are actually sufficient)
            for u, v in zip(boundary[:-1], boundary[1:]):
                if not graph.has_edge(u, v):
                    extra_edges.append((u, v))

            graph.add_edges(extra_edges)

        result = is_planar(graph, kuratowski=kuratowski, set_embedding=set_embedding, set_pos=set_pos)

        if kuratowski:
            bool_result = result[0]
        else:
            bool_result = result

        if bool_result:
            if set_embedding:
                # strip the embedding to fit original graph
                del graph._embedding[extra]
                for u, v in extra_edges:
                    graph._embedding[u].remove(v)
                    graph._embedding[v].remove(u)
                for v in boundary:
                    graph._embedding[v].remove(extra)
                self._embedding = graph._embedding

            if set_pos:
                # strip the position
                del graph._pos[extra]
                self._pos = graph._pos

        return result

    def layout_planar(self, set_embedding=False, on_embedding=None,
                      external_face=None, test=False, circular=False,
                      **options):
        """
        Compute a planar layout of the graph using Schnyder's algorithm.

        If ``set_embedding`` is set, a new combinatorial embedding is computed
        for the layout. Otherwise: if ``on_embedding`` is provided, then that
        combinatorial embedding is used for the layout. Otherwise: if a
        combinatorial embedding is set to the instance field variable of the
        graph (e.g. using
        :meth:`~sage/graphs/generic_graph.GenericGraph.set_embedding`), then
        that one is used, and if no combinatorial embedding is set, then one is
        computed.

        If the graph is not planar, an error is raised.

        INPUT:

        - ``set_embedding`` -- boolean (default: ``False``); whether to set the
          instance field variable that contains a combinatorial embedding to the
          combinatorial embedding used for the planar layout (see
          :meth:`~sage/graphs/generic_graph.GenericGraph.get_embedding`)

        - ``on_embedding`` -- dictionary (default: ``None``); provide a
          combinatorial embedding

        - ``external_face`` -- a pair `(u,v)` of vertices (default: ``None``);
          the external face of the drawing is chosen in such a way that `u` and
          `v` are consecutive vertices in the clockwise traversal of the
          external face, in particular `uv` has to be an edge of the graph. If
          ``external_face == None``, an arbitrary external face is chosen.

        - ``test`` -- boolean (default: ``False``); whether to perform sanity
          tests along the way

        - ``circular`` -- ignored

        EXAMPLES::

            sage: g = graphs.PathGraph(10)
            sage: g.layout(layout='planar', save_pos=True, test=True)
            {0: [0, 8],
             1: [8, 1],
             2: [1, 0],
             3: [7, 1],
             4: [1, 1],
             5: [5, 3],
             6: [2, 3],
             7: [2, 4],
             8: [1, 6],
             9: [2, 5]}
            sage: g = graphs.BalancedTree(3, 4)
            sage: pos = g.layout(layout='planar', save_pos=True, test=True)
            sage: pos[0]
            [0, 119]
            sage: pos[120]
            [21, 37]
            sage: g = graphs.CycleGraph(7)
            sage: g.layout(layout='planar', save_pos=True, test=True)
            {0: [0, 5], 1: [5, 1], 2: [1, 0], 3: [4, 1], 4: [1, 1], 5: [2, 2], 6: [1, 2]}
            sage: g = graphs.CompleteGraph(5)
            sage: g.layout(layout='planar', save_pos=True, test=True, set_embedding=True)
            Traceback (most recent call last):
            ...
            ValueError: Complete graph is not a planar graph

        Choose the external face of the drawing::

            sage: g = graphs.CompleteGraph(4)
            sage: g.layout(layout='planar', external_face=(0,1))
            {0: [0, 2], 1: [2, 1], 2: [1, 0], 3: [1, 1]}
            sage: g.layout(layout='planar', external_face=(3,1))
            {0: [2, 1], 1: [0, 2], 2: [1, 1], 3: [1, 0]}

        Choose the embedding:

            sage: H = graphs.LadderGraph(4)
            sage: em = {0:[1,4], 4:[0,5], 1:[5,2,0], 5:[4,6,1], 2:[1,3,6], 6:[7,5,2], 3:[7,2], 7:[3,6]}
            sage: p = H.layout_planar(on_embedding=em)
            sage: p # random
            {2: [8.121320343559642, 1],
            3: [2.1213203435596424, 6],
            7: [3.1213203435596424, 0],
            0: [5.121320343559642, 3],
            1: [3.1213203435596424, 5],
            4: [4.121320343559642, 3],
            5: [4.121320343559642, 2],
            6: [3.1213203435596424, 1],
            9: [9.698670612749268, 1],
            8: [8.698670612749268, 1],
            10: [9.698670612749268, 0]}

        TESTS::

            sage: G = Graph([[0, 1, 2, 3], [[0, 1], [0, 2], [0, 3]]])
            sage: G.layout(layout='planar', external_face=(1, 2))
            Traceback (most recent call last):
            ...
            ValueError: (1, 2) is not an edge of Graph on 4 vertices but has been provided as an edge of the external face

        Check the dependence of the computed position on the given combinatorial
        embedding (:trac:`28152`)::

            sage: G = Graph([[0, 1, 2, 3], [[0, 1], [0, 2], [0, 3]]])
            sage: G.set_embedding({0: [1, 2, 3], 1: [0], 2: [0], 3: [0]})
            sage: pos1 = G.layout('planar', save_pos=True)
            sage: G._check_embedding_validity()
            True
            sage: G.set_embedding({0: [3, 2, 1], 1: [0], 2: [0], 3: [0]})
            sage: pos2 = G.layout('planar', save_pos=True)
            sage: pos1 == pos2
            False

        Check that the function handles disconnected graphs and small
        graphs (:trac:`29522`)::

            sage: G = graphs.CycleGraph(4) + graphs.CycleGraph(5)
            sage: G.layout_planar() # random
            {1: [3.0, 1],
             0: [1.0, 2],
             2: [2.0, 0],
             3: [2.0, 1],
             5: [6.0, 1],
             4: [4.0, 2],
             6: [5.0, 0],
             7: [5.0, 1]}
            sage: K1 = graphs.CompleteGraph(1)
            sage: K1.layout_planar()
            {0: [0, 0]}
            sage: K2 = graphs.CompleteGraph(2)
            sage: K2.layout_planar()
            {0: [0, 0], 1: [0, 1]}

        Check that the embedding can be specified for disconnected
        graphs (:trac:`29522`)::

            sage: H = graphs.LadderGraph(4) + graphs.CompleteGraph(3)
            sage: em = {0:[1,4], 4:[0,5], 1:[5,2,0], 5:[4,6,1], 2:[1,3,6], 6:[7,5,2], 3:[7,2], 7:[3,6], 8:[10,9], 9:[8,10], 10:[8,9]}
            sage: p = H.layout_planar(on_embedding=em)

        Check that an exception is raised if the input graph is not planar::

            sage: G = graphs.PetersenGraph()
            sage: G.layout(layout='planar')
            Traceback (most recent call last):
            ...
            ValueError: Petersen graph is not a planar graph

        """
        from sage.graphs.graph import Graph
        from sage.graphs.schnyder import _triangulate, _normal_label, _realizer, _compute_coordinates

        G = Graph(self)

        # Trivial cases
        if len(G) <= 2:
            verts = G.vertex_iterator()
            pos = dict()
            embedding = dict()
            if len(G) >= 1:
                v1 = next(verts)
                pos[v1] = [0, 0]
                embedding[v1] = []
            if len(G) == 2:
                v2 = next(verts)
                pos[v2] = [0, 1]
                embedding[v1] = [v2]
                embedding[v2] = [v1]
            if set_embedding:
                self.set_embedding(embedding)
            return pos

        if not self.is_connected():
            if external_face:
                raise NotImplementedError('cannot fix the external face for a'
                                          'disconnected graph')
            # Compute the layout component by component
            pos = layout_split(G.__class__.layout_planar,
                               G,
                               set_embedding=set_embedding,
                               on_embedding=on_embedding,
                               external_face=None,
                               test=test,
                               **options)
            if set_embedding:
                self.set_embedding(G.get_embedding())
            return pos

        # Now the graph is connected and has at least 3 vertices

        try:
            G._embedding = self._embedding
        except AttributeError:
            pass
        embedding_copy = None
        if set_embedding:
            if not G.is_planar(set_embedding=True):
                raise ValueError('%s is not a planar graph' % self)
            embedding_copy = {v: neighbors[:] for v, neighbors in G._embedding.items()}
        else:
            if on_embedding is not None:
                G._check_embedding_validity(on_embedding, boolean=False)
                if not G.is_planar(on_embedding=on_embedding):
                    raise ValueError('provided embedding is not a planar '
                                     'embedding for %s' % self)
                G.set_embedding(on_embedding)
            else:
                if hasattr(G, '_embedding'):
                    if G._check_embedding_validity():
                        if not G.is_planar(on_embedding=G._embedding):
                            raise ValueError('%s has nonplanar _embedding attribute. '
                                             'Try putting set_embedding=True' % self)
                        embedding_copy = {v: neighbors[:] for v, neighbors in G._embedding.items()}
                    else:
                        raise ValueError('provided embedding is not a valid '
                                         'embedding for %s. Try putting '
                                         'set_embedding=True' % self)
                else:
                    if not G.is_planar(set_embedding=True):
                        raise ValueError('%s is not a planar graph' % self)

        if external_face:
            if not self.has_edge(external_face):
                raise ValueError('{} is not an edge of {} but has been '
                                 'provided as an edge of the external face'
                                 ''.format(external_face, self))

        _triangulate(G, G._embedding)

        # Optional error-checking
        if test:
            if G._check_embedding_validity():
                if not G.is_planar(on_embedding=G._embedding):
                    raise ValueError('%s has nonplanar _embedding attribute. '
                                     'Try putting set_embedding=True' % self)
            test_faces = G.faces(G._embedding)
            for face in test_faces:
                if len(face) != 3:
                    raise RuntimeError('BUG: Triangulation returned face: %s' % face)

        faces = G.faces(G._embedding)
        outer_face = faces[0]
        if external_face:
            for face in faces:
                if external_face in face:
                    outer_face = face
                    break
        label = _normal_label(G, G._embedding, outer_face)

        # Get dictionary of tree nodes from the realizer
        tree_nodes = _realizer(G, label)

        # Compute the coordinates and store in position dictionary (attr self._pos)
        _compute_coordinates(G, tree_nodes)

        # Delete all the edges added to the graph
        #G.delete_edges( extra_edges )
        #self.delete_edges( other_added_edges )

        if embedding_copy is not None:
            self._embedding = embedding_copy

        return G._pos

    def is_drawn_free_of_edge_crossings(self):
        """
        Check whether the position dictionary for this graph is set and that
        position dictionary gives a planar embedding.

        This simply checks all pairs of edges that don't share a vertex to
        make sure that they don't intersect.

        .. NOTE::

           This function require that ``_pos`` attribute is set (Returns False
           otherwise)

        EXAMPLES::

            sage: D = graphs.DodecahedralGraph()
            sage: pos = D.layout(layout='planar', save_pos=True)
            sage: D.is_drawn_free_of_edge_crossings()
            True
        """
        if self._pos is None:
            return False

        G = self.to_undirected()
        for edge1 in G.edge_iterator(labels=False):
            for edge2 in G.edge_iterator(labels=False):
                if edge1[0] == edge2[0] or edge1[0] == edge2[1] or edge1[1] == edge2[0] or edge1[1] == edge2[1]:
                    continue
                p1, p2 = self._pos[edge1[0]], self._pos[edge1[1]]
                dy = Rational(p2[1] - p1[1])
                dx = Rational(p2[0] - p1[0])
                q1, q2 = self._pos[edge2[0]], self._pos[edge2[1]]
                db = Rational(q2[1] - q1[1])
                da = Rational(q2[0] - q1[0])
                if da * dy == db * dx:
                    if dx:
                        t1 = Rational(q1[0] - p1[0]) / dx
                        t2 = Rational(q2[0] - p1[0]) / dx
                        if (0 <= t1 and t1 <= 1) or (0 <= t2 and t2 <= 1):
                            if p1[1] + t1 * dy == q1[1] or p1[1] + t2 * dy == q2[1]:
                                return False
                    else:
                        t1 = Rational(q1[1] - p1[1]) / dy
                        t2 = Rational(q2[1] - p1[1]) / dy
                        if (0 <= t1 and t1 <= 1) or (0 <= t2 and t2 <= 1):
                            if p1[0] + t1 * dx == q1[0] or p1[0] + t2 * dx == q2[0]:
                                return False
                else:
                    s = (dx * Rational(q1[1] - p1[1]) + dy * Rational(p1[0] - q1[0])) / (da * dy - db * dx)
                    t = (da * Rational(p1[1] - q1[1]) + db * Rational(q1[0] - p1[0])) / (db * dx - da * dy)

                    if 0 <= s and s <= 1 and 0 <= t and t <= 1:
                        print('fail on', p1, p2, ' : ', q1, q2)
                        print(edge1, edge2)
                        return False
        return True

    def genus(self, set_embedding=True, on_embedding=None, minimal=True, maximal=False, circular=None, ordered=True):
        r"""
        Return the minimal genus of the graph.

        The genus of a compact surface is the number of handles it has. The
        genus of a graph is the minimal genus of the surface it can be embedded
        into. It can be seen as a measure of non-planarity; a planar graph has
        genus zero.

        .. NOTE::

            This function uses Euler's formula and thus it is necessary to
            consider only connected graphs.

        INPUT:

        - ``set_embedding`` -- boolean (default: ``True``); whether or not to
          store an embedding attribute of the computed (minimal) genus of the
          graph

        - ``on_embedding`` -- two kinds of input are allowed (default:
           ``None``):

          - a dictionary representing a combinatorial embedding on which the
            genus should be computed. Note that this must be a valid embedding
            for the graph. The dictionary structure is given by: ``vertex1:
            [neighbor1, neighbor2, neighbor3], vertex2: [neighbor]`` where there
            is a key for each vertex in the graph and a (clockwise) ordered list
            of each vertex's neighbors as values. The value of ``on_embedding``
            takes precedence over a stored ``_embedding`` attribute if
            ``minimal`` is set to ``False``.

          - The value ``True``, in order to indicate that the embedding stored
            as ``_embedding`` should be used (see examples).

        - ``minimal`` -- boolean (default: ``True``); whether or not to compute
          the minimal genus of the graph (i.e., testing all embeddings). If
          minimal is ``False``, then either ``maximal`` must be ``True`` or
          ``on_embedding`` must not be ``None``. If ``on_embedding`` is not
          ``None``, it will take priority over ``minimal``. Similarly, if
          ``maximal`` is ``True``, it will take priority over ``minimal``.

        - ``maximal`` -- boolean (default: ``False``); whether or not to compute
          the maximal genus of the graph (i.e., testing all embeddings). If
          ``maximal`` is ``False``, then either ``minimal`` must be ``True`` or
          ``on_embedding`` must not be ``None``. If ``on_embedding`` is not
          ``None``, it will take priority over ``maximal``. However, ``maximal``
          takes priority over the default ``minimal``.

        - ``circular`` -- list (default: ``None``); if ``circular`` is a list of
          vertices, the method computes the genus preserving a planar embedding
          of the this list. If ``circular`` is defined, ``on_embedding`` is not
          a valid option.

        - ``ordered`` -- boolean (default: ``True``); if ``circular`` is
          ``True``, then whether or not the boundary order may be permuted
          (default is ``True``, which means the boundary order is preserved)

        EXAMPLES::

            sage: g = graphs.PetersenGraph()
            sage: g.genus() # tests for minimal genus by default
            1
            sage: g.genus(on_embedding=True, maximal=True) # on_embedding overrides minimal and maximal arguments
            1
            sage: g.genus(maximal=True) # setting maximal to True overrides default minimal=True
            3
            sage: g.genus(on_embedding=g.get_embedding()) # can also send a valid combinatorial embedding dict
            3
            sage: (graphs.CubeGraph(3)).genus()
            0
            sage: K23 = graphs.CompleteBipartiteGraph(2,3)
            sage: K23.genus()
            0
            sage: K33 = graphs.CompleteBipartiteGraph(3,3)
            sage: K33.genus()
            1

        Using the circular argument, we can compute the minimal genus preserving
        a planar, ordered boundary::

            sage: cube = graphs.CubeGraph(2)
            sage: cube.genus(circular=['01','10'])
            0
            sage: cube.is_circular_planar()
            True
            sage: cube.genus(circular=['01','10'])
            0
            sage: cube.genus(circular=['01','10'], on_embedding=True)
            Traceback (most recent call last):
            ...
            ValueError: on_embedding is not a valid option when circular is defined
            sage: cube.genus(circular=['01','10'], maximal=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: cannot compute the maximal genus of a genus respecting a boundary

        Note: not everything works for multigraphs, looped graphs or digraphs.
        But the minimal genus is ultimately computable for every connected graph
        -- but the embedding we obtain for the simple graph can't be easily
        converted to an embedding of a non-simple graph.  Also, the maximal
        genus of a multigraph does not trivially correspond to that of its
        simple graph::

            sage: G = DiGraph({0: [0, 1, 1, 1], 1: [2, 2, 3, 3], 2: [1, 3, 3], 3: [0, 3]})
            sage: G.genus()
            Traceback (most recent call last):
            ...
            NotImplementedError: cannot work with embeddings of non-simple graphs
            sage: G.to_simple().genus()
            0
            sage: G.genus(set_embedding=False)
            0
            sage: G.genus(maximal=True, set_embedding=False)
            Traceback (most recent call last):
            ...
            NotImplementedError: cannot compute the maximal genus of a graph with loops or multiple edges

        We break graphs with cut vertices into their blocks, which greatly
        speeds up computation of minimal genus. This is not implemented for
        maximal genus::

            sage: G = graphs.RandomBlockGraph(10, 5)
            sage: G.genus()
            10

        """
        if not self.is_connected():
            raise TypeError("the input Graph must be connected to use Euler's Formula to compute minimal genus")

        G = self.to_simple(immutable=False)
        verts = G.order()
        edges = G.size()

        if maximal:
            minimal = False

        if circular is not None:
            if not isinstance(circular, list):
                raise ValueError("'circular' is expected to be a list")
            if maximal:
                raise NotImplementedError("cannot compute the maximal genus of a genus respecting a boundary")
            if on_embedding is not None:
                raise ValueError("on_embedding is not a valid option when circular is defined")
            boundary = circular
            if hasattr(G, '_embedding'):
                del(G._embedding)

            extra = G.add_vertex()
            G.add_edges((vertex, extra) for vertex in boundary)
            verts += 1

            extra_edges = []
            if ordered:  # WHEEL
                for e in zip(boundary[-1], boundary[1:]):
                    if not G.has_edge(e):
                        G.add_edge(e)
                        extra_edges.append(e)
                if not G.has_edge(boundary[-1], boundary[0]):
                    G.add_edge(boundary[-1], boundary[0])
                    extra_edges.append((boundary[-1], boundary[0]))
                # else STAR (empty list of extra edges)

            edges = G.size()

        if on_embedding is not None:
            if self.has_loops() or self.is_directed() or self.has_multiple_edges():
                raise NotImplementedError("cannot work with embeddings of non-simple graphs")

            if isinstance(on_embedding, dict):
                faces = len(self.faces(on_embedding))
                return (2 - verts + edges - faces) // 2
            elif on_embedding:
                try:
                    faces = len(self.faces(self._embedding))
                except AttributeError:
                    raise AttributeError('graph must have attribute _embedding set to compute current (embedded) genus')
                return (2 - verts + edges - faces) // 2
        else:  # then compute either maximal or minimal genus of all embeddings
            from . import genus

            if set_embedding:
                if self.has_loops() or self.is_directed() or self.has_multiple_edges():
                    raise NotImplementedError("cannot work with embeddings of non-simple graphs")
                if minimal:
                    B, C = G.blocks_and_cut_vertices()
                    embedding = {}
                    g = 0
                    for block in B:
                        H = G.subgraph(block)
                        g += genus.simple_connected_graph_genus(H, set_embedding=True, check=False, minimal=True)
                        emb = H.get_embedding()
                        for v in emb:
                            if v in embedding:
                                embedding[v] += emb[v]
                            else:
                                embedding[v] = emb[v]
                    self._embedding = embedding
                else:
                    g = genus.simple_connected_graph_genus(G, set_embedding=True, check=False, minimal=minimal)
                    self._embedding = G._embedding
                return g
            else:
                if maximal and (self.has_multiple_edges() or self.has_loops()):
                    raise NotImplementedError("cannot compute the maximal genus of a graph with loops or multiple edges")
                if minimal:
                    B, C = G.blocks_and_cut_vertices()
                    g = 0
                    for block in B:
                        H = G.subgraph(block)
                        g += genus.simple_connected_graph_genus(H, set_embedding=False, check=False, minimal=True)
                    return g
                else:
                    return genus.simple_connected_graph_genus(G, set_embedding=False, check=False, minimal=minimal)

    def crossing_number(self):
        r"""
        Return the crossing number of the graph.

        The crossing number of a graph is the minimum number of edge crossings
        needed to draw the graph on a plane. It can be seen as a measure of
        non-planarity; a planar graph has crossing number zero.

        See the :wikipedia:`Crossing_number` for more information.

        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: P.crossing_number()
            2

        ALGORITHM:

        This is slow brute force implementation: for every `k` pairs of edges
        try adding a new vertex for a crossing point for them. If the result is
        not planar in any of those, try `k+1` pairs.

        Computing the crossing number is NP-hard problem.

        TESTS:

        Empty graph, graph without edges::

            sage: E = graphs.EmptyGraph()
            sage: E.crossing_number()
            0

            sage: g = Graph(5)
            sage: g.crossing_number()
            0

        Planar graph::

            sage: C4 = graphs.CompleteGraph(4)
            sage: C4.crossing_number()
            0

        Non-connected graph::

            sage: C5x2 = graphs.CompleteGraph(5) * 2
            sage: C5x2.crossing_number()
            2

        Test the "un-splitting edges" optimization::

            sage: g = graphs.CompleteGraph(4)
            sage: g.subdivide_edges(g.edges(sort=True), 1)
            sage: g.add_edge(0, g.add_vertex())
            sage: g.crossing_number()
            0

            sage: g = graphs.CompleteGraph(5)
            sage: g.subdivide_edges(g.edges(sort=False), 2)
            sage: g.add_edge(0, g.add_vertex())
            sage: g.crossing_number()
            1
        """
        def _crossing_number(G):
            """
            Return the crossing number of a biconnected non-planar graph ``G``.
            """
            from sage.combinat.subset import Subsets

            # Splitting an edge does not increase the crossing number, so
            # reversedly we can shrink those. We must check that un-splitting
            # would not create multiple edges.
            two = [v for v in G if G.degree(v) == 2]
            for v in two:
                u, w = G.neighbors(v)
                if not G.has_edge(u, w):
                    G.add_edge(u, w)
                    G.delete_vertex(v)

            edgepairs = Subsets(G.edge_iterator(labels=False), 2)
            edgepairs = [x for x in edgepairs if x[0][0] not in [x[1][0], x[1][1]] and
                         x[0][1] not in [x[1][0], x[1][1]]]

            k = 1
            while True:
                for edges in Subsets(edgepairs, k):
                    g = copy(G)
                    for pair in edges:
                        g.delete_edges(pair)
                    for edge in edges:
                        v = g.add_vertex()
                        g.add_edge(edge[0][0], v)
                        g.add_edge(v, edge[0][1])
                        g.add_edge(edge[1][0], v)
                        g.add_edge(v, edge[1][1])
                    if g.is_planar():
                        return k
                k += 1

        self._scream_if_not_simple(allow_loops=True)

        blocks = self.blocks_and_cut_vertices()[0]
        k = 0
        for block in blocks:
            if len(block) > 4:
                g = self.subgraph(block)
                if not g.is_planar():
                    k += _crossing_number(g)
        return k

    def faces(self, embedding=None):
        """
        Return the faces of an embedded graph.

        A combinatorial embedding of a graph is a clockwise ordering of the
        neighbors of each vertex. From this information one can define the faces
        of the embedding, which is what this method returns.

        If no embedding is provided or stored as ``self._embedding``, this
        method will compute the set of faces from the embedding returned by
        :meth:`is_planar` (if the graph is, of course, planar).

        .. WARNING::

            This method is not well defined when the graph is not connected.
            Indeed, the result may contain several faces corresponding to the
            external face.

        INPUT:

        - ``embedding`` -- dictionary (default: ``None``); a combinatorial
          embedding dictionary. Format: ``{v1: [v2,v3], v2: [v1], v3: [v1]}``
          (clockwise ordering of neighbors at each vertex). If set to ``None``
          (default) the method will use the embedding stored as
          ``self._embedding``. If none is stored, the method will compute the
          set of faces from the embedding returned by :meth:`is_planar` (if the
          graph is, of course, planar).

        .. NOTE::

            ``embedding`` is an ordered list based on the hash order of the
            vertices of graph. To avoid confusion, it might be best to set the
            rot_sys based on a 'nice_copy' of the graph.

        .. SEEALSO::

            * :meth:`set_embedding`
            * :meth:`get_embedding`
            * :meth:`is_planar`
            * :meth:`planar_dual`

        EXAMPLES:

        Providing an embedding::

            sage: T = graphs.TetrahedralGraph()
            sage: T.faces({0: [1, 3, 2], 1: [0, 2, 3], 2: [0, 3, 1], 3: [0, 1, 2]})
            [[(0, 1), (1, 2), (2, 0)],
             [(0, 2), (2, 3), (3, 0)],
             [(0, 3), (3, 1), (1, 0)],
             [(1, 3), (3, 2), (2, 1)]]

        With no embedding provided::

            sage: graphs.TetrahedralGraph().faces()
            [[(0, 1), (1, 2), (2, 0)],
             [(0, 2), (2, 3), (3, 0)],
             [(0, 3), (3, 1), (1, 0)],
             [(1, 3), (3, 2), (2, 1)]]

        With no embedding provided (non-planar graph)::

            sage: graphs.PetersenGraph().faces()
            Traceback (most recent call last):
            ...
            ValueError: no embedding is provided and the graph is not planar

        TESTS:

        The empty graph and a graph without edge have no face::

            sage: Graph().faces()
            []
            sage: Graph(1).faces()
            []

        The Path Graph has a single face::

            sage: graphs.PathGraph(3).faces()
            [[(0, 1), (1, 2), (2, 1), (1, 0)]]
        """
        if not self.order() or not self.size():
            return []

        # Which embedding should we use ?
        if embedding is None:
            # Is self._embedding available ?
            if self._check_embedding_validity():
                embedding = self._embedding
            else:
                if self.is_planar(set_embedding=True):
                    embedding = self._embedding
                    self._embedding = None
                else:
                    raise ValueError("no embedding is provided and the graph is not planar")

        # Establish set of possible edges
        edgeset = set()
        for u, v in self.edge_iterator(labels=0):
            edgeset.add((u, v))
            edgeset.add((v, u))

        # Storage for face paths
        faces = []
        minedge = min(edgeset)
        path = [minedge]
        edgeset.discard(minedge)

        # Trace faces
        while edgeset:
            u, v = path[-1]
            neighbors = embedding[v]
            next_node = neighbors[(neighbors.index(u) + 1) % len(neighbors)]
            e = (v, next_node)
            if e == path[0]:
                faces.append(path)
                minedge = min(edgeset)
                path = [minedge]
                edgeset.discard(minedge)
            else:
                path.append(e)
                edgeset.discard(e)
        if path:
            faces.append(path)
        return faces

    def num_faces(self, embedding=None):
        """
        Return the number of faces of an embedded graph.

        If no embedding is provided or stored as ``self._embedding``, this
        method uses Euler's formula (see the :wikipedia:`Euler_characteristic`)
        to determine the number of faces if the graph is planar. If the graph is
        not planar, an error is raised.

        If an embedding is provided or stored as ``self._embedding``, this
        method calls method :meth:`faces` to get the list of faces induced by
        the embedding in each connected component of the graph. Then it returns
        the sum of size of these lists minus the number of connected components
        plus one to ensure that the external face is counted only once.

        INPUT:

        - ``embedding`` -- dictionary (default: ``None``); a combinatorial
          embedding dictionary. Format: ``{v1: [v2,v3], v2: [v1], v3: [v1]}``
          (clockwise ordering of neighbors at each vertex). If set to ``None``
          (default) the method will use the embedding stored as
          ``self._embedding``. If none is stored, the method will compute the
          set of faces from the embedding returned by :meth:`is_planar` (if the
          graph is, of course, planar).

        EXAMPLES::

            sage: T = graphs.TetrahedralGraph()
            sage: T.num_faces()
            4

        The external face of a disconnected graph is counted only once::

            sage: (T + T).num_faces()
            7
            sage: (T + T + T).num_faces()
            10

        Trees and forests have a single face::

            sage: T = graphs.RandomTree(10)
            sage: T.num_faces()
            1
            sage: (T + T).num_faces()
            1

        TESTS::

            sage: G = graphs.CompleteBipartiteGraph(3, 3)
            sage: G.num_faces()
            Traceback (most recent call last):
            ...
            ValueError: no embedding is provided and the graph is not planar

        Issue :trac:`22003` is fixed:

            sage: Graph(1).num_faces()
            1
        """
        if not self:
            return 0
        if self.is_connected():
            if self.order() == self.size() + 1:
                # a tree has a single face
                return 1
            return len(self.faces(embedding))

        if embedding is None:
            # Is self._embedding available ?
            if self._check_embedding_validity():
                embedding = self._embedding
            else:
                if self.is_planar():
                    # We use Euler's formula: V-E+F-C=1
                    C = len(self.connected_components())
                    return self.size() - self.order() + C + 1
                else:
                    raise ValueError("no embedding is provided and the graph is not planar")

        # We compute the number Fc of faces of each connected component c.
        # The number of faces of the graph is the sum of the Fc values minus the
        # number of connected components minus 1 to ensure that the external
        # face is counted only once. That is,  1 + sum_{c} (Fc - 1).
        F = 1
        for g in self.connected_components_subgraphs():
            emb = None if embedding is None else {v: embedding[v] for v in g}
            F += g.num_faces(emb) - 1
        return F

    def planar_dual(self, embedding=None):
        """
        Return the planar dual of an embedded graph.

        A combinatorial embedding of a graph is a clockwise ordering of the
        neighbors of each vertex. From this information one can obtain the dual
        of a plane graph, which is what the method returns. The vertices of the
        dual graph correspond to faces of the primal graph.

        INPUT:

        - ``embedding`` -- dictionary (default: ``None``); a combinatorial
          embedding dictionary. Format: ``{v1: [v2,v3], v2: [v1], v3: [v1]}``
          (clockwise ordering of neighbors at each vertex). If set to ``None``
          (default) the method will use the embedding stored as
          ``self._embedding``. If none is stored, the method will compute the
          set of faces from the embedding returned by :meth:`is_planar` (if the
          graph is, of course, planar).

        EXAMPLES::

            sage: C = graphs.CubeGraph(3)
            sage: C.planar_dual()
            Graph on 6 vertices
            sage: graphs.IcosahedralGraph().planar_dual().is_isomorphic(graphs.DodecahedralGraph())
            True

        The planar dual of the planar dual is isomorphic to the graph itself::

            sage: g = graphs.BuckyBall()
            sage: g.planar_dual().planar_dual().is_isomorphic(g)
            True

        .. SEEALSO::

            * :meth:`faces`
            * :meth:`set_embedding`
            * :meth:`get_embedding`
            * :meth:`is_planar`

        TESTS::

            sage: G = graphs.CompleteBipartiteGraph(3, 3)
            sage: G.planar_dual()
            Traceback (most recent call last):
            ...
            ValueError: no embedding is provided and the graph is not planar
            sage: G = Graph([[1, 2, 3, 4], [[1, 2], [2, 3], [3, 1], [3, 2], [1, 4], [2, 4], [3, 4]]], multiedges=True)
            sage: G.planar_dual()
            Traceback (most recent call last):
            ...
            ValueError: This method is not known to work on graphs with multiedges. Perhaps this method can be updated to handle them, but in the meantime if you want to use it please disallow multiedges using allow_multiple_edges().
            sage: G = graphs.CompleteGraph(3)
            sage: G.planar_dual()
            Traceback (most recent call last):
            ...
            NotImplementedError: the graph must be 3-vertex-connected

        This also keeps track of edge labels::

            sage: label_dict = {('000', '001'): 1, ('001', '101'): 2, ('101', '100'): 3, ('100', '000'): 4}
            sage: g = graphs.CubeGraph(3)
            sage: for e in label_dict:
            ....:     g.set_edge_label(e[0], e[1], label_dict[e])
            sage: gd = g.planar_dual()
            sage: incident_labels = []
            sage: for v in gd:
            ....:     incident_labels.append(sorted([l for _, _, l in gd.edges_incident(v) if l]))
            sage: sorted(incident_labels)
            [[], [1], [1, 2, 3, 4], [2], [3], [4]]

        .. TODO::

            Implement the method for graphs that are not 3-vertex-connected,
            or at least have a faster 3-vertex-connectivity test (:trac:`24635`).

        """
        self._scream_if_not_simple()

        if not self.vertex_connectivity(k=3):
            raise NotImplementedError("the graph must be 3-vertex-connected")

        from sage.graphs.graph import Graph
        from itertools import combinations
        verts = [tuple(f) for f in self.faces(embedding=embedding)]
        edges = []
        for v1, v2 in combinations(verts, 2):
            e = set([tuple(reversed(e)) for e in v1]).intersection(v2)
            if e:
                e = e.pop()  # just one edge since self and its dual are simple
                edges.append([v1, v2, self.edge_label(e[0], e[1])])
        return Graph([verts, edges])

    # Connectivity

    def steiner_tree(self, vertices, weighted=False, solver=None, verbose=0,
                     *, integrality_tolerance=1e-3):
        r"""
        Return a tree of minimum weight connecting the given set of vertices.

        Definition :

        Computing a minimum spanning tree in a graph can be done in `n \log(n)`
        time (and in linear time if all weights are equal) where `n = V + E`. On
        the other hand, if one is given a large (possibly weighted) graph and a
        subset of its vertices, it is NP-Hard to find a tree of minimum weight
        connecting the given set of vertices, which is then called a Steiner
        Tree.

        See the :wikipedia:`Steiner_tree_problem` for more information.

        INPUT:

        - ``vertices`` -- the vertices to be connected by the Steiner
          Tree.

        - ``weighted`` -- boolean (default: ``False``); whether to consider the
          graph as weighted, and use each edge's label as a weight, considering
          ``None`` as a weight of `1`. If ``weighted=False`` (default) all edges
          are considered to have a weight of `1`.

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.


        .. NOTE::

            * This problem being defined on undirected graphs, the orientation
              is not considered if the current graph is actually a digraph.

            * The graph is assumed not to have multiple edges.

        ALGORITHM:

        Solved through Linear Programming.

        COMPLEXITY:

        NP-Hard.

        Note that this algorithm first checks whether the given set of vertices
        induces a connected graph, returning one of its spanning trees if
        ``weighted`` is set to ``False``, and thus answering very quickly in
        some cases

        EXAMPLES:

        The Steiner Tree of the first 5 vertices in a random graph is, of
        course, always a tree::

            sage: g = graphs.RandomGNP(30, .5)
            sage: first5 = g.vertices(sort=True)[:5]
            sage: st = g.steiner_tree(first5)
            sage: st.is_tree()
            True

        And all the 5 vertices are contained in this tree ::

            sage: all(v in st for v in first5)
            True

        An exception is raised when the problem is impossible, i.e.  if the
        given vertices are not all included in the same connected component::

            sage: g = 2 * graphs.PetersenGraph()
            sage: st = g.steiner_tree([5, 15])
            Traceback (most recent call last):
            ...
            EmptySetError: the given vertices do not all belong to the same connected component. This problem has no solution !
        """
        self._scream_if_not_simple(allow_loops=True)

        if self.is_directed():
            from sage.graphs.graph import Graph
            g = Graph(self)
        else:
            g = self

        # Can the problem be solved ? Are all the vertices in the same
        # connected component ?
        cc = g.connected_component_containing_vertex(vertices[0])
        if any(v not in cc for v in vertices):
            from sage.categories.sets_cat import EmptySetError
            raise EmptySetError("the given vertices do not all belong to the "
                                "same connected component. This problem has "
                                "no solution !")

        # Can it be solved using the min spanning tree algorithm ?
        if not weighted:
            gg = g.subgraph(vertices)
            if gg.is_connected():
                st = g.subgraph(edges=gg.min_spanning_tree(), immutable=False)
                st.delete_vertices([v for v in g if not st.degree(v)])
                return st

        # Then, LP formulation
        from sage.numerical.mip import MixedIntegerLinearProgram
        p = MixedIntegerLinearProgram(maximization=False, solver=solver)

        # edges used in the Steiner Tree
        edges = p.new_variable(binary=True)

        # relaxed edges to test for acyclicity
        r_edges = p.new_variable(nonnegative=True)

        # Whether a vertex is in the Steiner Tree
        vertex = p.new_variable(binary=True)
        for v in g:
            for e in g.edges_incident(v, labels=False):
                p.add_constraint(vertex[v] - edges[frozenset(e)], min=0)

        # We must have the given vertices in our tree
        for v in vertices:
            p.add_constraint(p.sum(edges[frozenset(e)] for e in g.edges_incident(v, labels=False)), min=1)

        # The number of edges is equal to the number of vertices in our tree minus 1
        p.add_constraint(p.sum(vertex[v] for v in g)
                         - p.sum(edges[frozenset(e)] for e in g.edge_iterator(labels=False)), max=1, min=1)

        # There are no cycles in our graph

        for u, v in g.edge_iterator(labels=False):
            p.add_constraint(r_edges[u, v] + r_edges[v, u] - edges[frozenset((u, v))], min=0)

        eps = 1 / (5 * Integer(g.order()))
        for v in g:
            p.add_constraint(p.sum(r_edges[u, v] for u in g.neighbor_iterator(v)), max=1 - eps)

        # Objective
        if weighted:
            p.set_objective(p.sum((l if l is not None else 1) * edges[frozenset((u, v))]
                                  for u, v, l in g.edge_iterator()))
        else:
            p.set_objective(p.sum(edges[frozenset(e)] for e in g.edge_iterator(labels=False)))

        p.solve(log=verbose)

        edges = p.get_values(edges, convert=bool, tolerance=integrality_tolerance)

        st = g.subgraph(edges=[e for e in g.edge_iterator(labels=False) if edges[frozenset(e)]],
                        immutable=False)
        st.delete_vertices(v for v in g if not st.degree(v))
        return st

    def edge_disjoint_spanning_trees(self, k, algorithm=None, root=None, solver=None, verbose=0,
                                     *, integrality_tolerance=1e-3):
        r"""
        Return the desired number of edge-disjoint spanning trees/arborescences.

        INPUT:

        - ``k`` -- integer; the required number of edge-disjoint spanning
          trees/arborescences

        - ``algorithm`` -- string (default: ``None``); specify the
          algorithm to use among:

          * ``"Roskind-Tarjan"`` -- use the algorithm proposed by Roskind and
            Tarjan [RT1985]_ for finding edge-disjoint spanning-trees in
            undirected simple graphs in time `O(m\log{m} + k^2n^2)`.

          * ``"MILP"`` -- use a mixed integer linear programming
            formulation. This is the default method for directed graphs.

          * ``None`` -- use ``"Roskind-Tarjan"`` for undirected graphs and
            ``"MILP"`` for directed graphs.

        - ``root`` -- vertex (default: ``None``); root of the disjoint
          arborescences when the graph is directed.  If set to ``None``, the
          first vertex in the graph is picked.

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        ALGORITHM:

        Mixed Integer Linear Program.

        There are at least two possible rewritings of this method which do not
        use Linear Programming:

            * The algorithm presented in the paper entitled "A short proof of
              the tree-packing theorem", by Thomas Kaiser [Kai2012]_.

            * The implementation of a Matroid class and of the Matroid Union
              Theorem (see section 42.3 of [Sch2003]_), applied to the
              cycle Matroid (see chapter 51 of [Sch2003]_).

        EXAMPLES:

        The Petersen Graph does have a spanning tree (it is connected)::

            sage: g = graphs.PetersenGraph()
            sage: [T] = g.edge_disjoint_spanning_trees(1)
            sage: T.is_tree()
            True

        Though, it does not have 2 edge-disjoint trees (as it has less than
        `2(|V|-1)` edges)::

            sage: g.edge_disjoint_spanning_trees(2)
            Traceback (most recent call last):
            ...
            EmptySetError: this graph does not contain the required number of trees/arborescences

        By Edmond's theorem, a graph which is `k`-connected always has `k`
        edge-disjoint arborescences, regardless of the root we pick::

            sage: g = digraphs.RandomDirectedGNP(11, .3)  # reduced from 30 to 11, cf. #32169
            sage: k = Integer(g.edge_connectivity())
            sage: while not k:
            ....:     g = digraphs.RandomDirectedGNP(11, .3)
            ....:     k = Integer(g.edge_connectivity())
            sage: arborescences = g.edge_disjoint_spanning_trees(k)  # long time (up to 15s on sage.math, 2011)
            sage: all(a.is_directed_acyclic() for a in arborescences)  # long time
            True
            sage: all(a.is_connected() for a in arborescences)  # long time
            True

        In the undirected case, we can only ensure half of it::

            sage: g = graphs.RandomGNP(14, .3)  # reduced from 30 to 14, see #32169
            sage: while not g.is_biconnected():
            ....:     g = graphs.RandomGNP(14, .3)
            sage: k = Integer(g.edge_connectivity()) // 2
            sage: trees = g.edge_disjoint_spanning_trees(k)
            sage: all(t.is_tree() for t in trees)
            True

        Check the validity of the algorithms for undirected graphs::

            sage: g = graphs.RandomGNP(12, .7)
            sage: k = Integer(g.edge_connectivity()) // 2
            sage: trees = g.edge_disjoint_spanning_trees(k, algorithm="MILP")
            sage: all(t.is_tree() for t in trees)
            True
            sage: all(g.order() == t.size() + 1 for t in trees)
            True
            sage: trees = g.edge_disjoint_spanning_trees(k, algorithm="Roskind-Tarjan")
            sage: all(t.is_tree() for t in trees)
            True
            sage: all(g.order() == t.size() + 1 for t in trees)
            True

        Example of :trac:`32169`::

            sage: d6 = r'[E_S?_hKIH@eos[BSg???Q@FShGC?hTHUGM?IPug?JOEYCdOzdkQGo'
            sage: d6 += r'@ADA@AAg?GAQW?[aIaSwHYcD@qQb@Dd?\hJTI@OHlJ_?C_OEIKoeC'
            sage: d6 += r'R@_BC?Q??YBFosqITEA?IvCU_'
            sage: G = DiGraph(d6, format='dig6')
            sage: G.edge_connectivity()
            5
            sage: G.edge_disjoint_spanning_trees(5)  # long time
            [Digraph on 28 vertices,
             Digraph on 28 vertices,
             Digraph on 28 vertices,
             Digraph on 28 vertices,
             Digraph on 28 vertices]

        Small cases::

            sage: Graph().edge_disjoint_spanning_trees(0)
            []
            sage: Graph(1).edge_disjoint_spanning_trees(0)
            []
            sage: Graph(2).edge_disjoint_spanning_trees(0)
            []
            sage: Graph([(0, 1)]).edge_disjoint_spanning_trees(0)
            []
            sage: Graph([(0, 1)]).edge_disjoint_spanning_trees(1)
            [Graph on 2 vertices]
            sage: Graph([(0, 1)]).edge_disjoint_spanning_trees(2)
            Traceback (most recent call last):
            ...
            EmptySetError: this graph does not contain the required number of trees/arborescences

        TESTS:

        Choice of the algorithm::

            sage: Graph().edge_disjoint_spanning_trees(0, algorithm=None)
            []
            sage: Graph().edge_disjoint_spanning_trees(0, algorithm="Roskind-Tarjan")
            []
            sage: Graph().edge_disjoint_spanning_trees(0, algorithm="MILP")
            []
            sage: Graph().edge_disjoint_spanning_trees(0, algorithm="foo")
            Traceback (most recent call last):
            ...
            ValueError: algorithm must be None, "Rosking-Tarjan" or "MILP" for undirected graphs
            sage: DiGraph().edge_disjoint_spanning_trees(0, algorithm=None)
            []
            sage: DiGraph().edge_disjoint_spanning_trees(0, algorithm="MILP")
            []
            sage: DiGraph().edge_disjoint_spanning_trees(0, algorithm="foo")
            Traceback (most recent call last):
            ...
            ValueError: algorithm must be None or "MILP" for directed graphs
        """
        self._scream_if_not_simple()
        from sage.graphs.digraph import DiGraph
        from sage.graphs.graph import Graph
        from sage.numerical.mip import MixedIntegerLinearProgram, MIPSolverException
        from sage.categories.sets_cat import EmptySetError

        if self.is_directed():
            if algorithm is not None and algorithm != "MILP":
                raise ValueError('algorithm must be None or "MILP" for directed graphs')
        else:
            if algorithm is None or algorithm == "Roskind-Tarjan":
                from sage.graphs.spanning_tree import edge_disjoint_spanning_trees
                return edge_disjoint_spanning_trees(self, k)
            elif algorithm != "MILP":
                raise ValueError('algorithm must be None, "Rosking-Tarjan" or "MILP" '
                                 'for undirected graphs')

        G = self
        n = G.order()

        if not n or not k:
            return []

        if root is None:
            root = next(G.vertex_iterator())

        if k == 1:
            E = G.min_spanning_tree(starting_vertex=root)
            if not E:
                raise EmptySetError("this graph does not contain the required "
                                    "number of trees/arborescences")
            return [DiGraph(E) if G.is_directed() else Graph(E)]

        D = G if G.is_directed() else DiGraph(G)

        # The colors we can use (one color per tree)
        colors = list(range(k))

        p = MixedIntegerLinearProgram(solver=solver)

        # edges[e, c] is equal to one if and only if edge e has color c
        edge = p.new_variable(binary=True)

        # Define partial ordering of the vertices in each tree to avoid cycles
        pos = p.new_variable()

        # An edge belongs to a single tree
        if G.is_directed():
            for e in D.edge_iterator(labels=False):
                p.add_constraint(p.sum(edge[e, c] for c in colors) <= 1)
        else:
            for u, v in G.edge_iterator(labels=False):
                p.add_constraint(p.sum(edge[(u, v), c] + edge[(v, u), c] for c in colors) <= 1)

        # Constraints defining a spanning tree in D for each color c
        for c in colors:
            # A tree has n-1 edges
            p.add_constraint(p.sum(edge[e, c] for e in D.edge_iterator(labels=False)) == n - 1)

            # Each vertex has 1 incoming edge, except the root which has none
            for u in D:
                if u == root:
                    p.add_constraint(p.sum(edge[e, c] for e in D.incoming_edge_iterator(root, labels=False)) == 0)
                else:
                    p.add_constraint(p.sum(edge[e, c] for e in D.incoming_edge_iterator(u, labels=False)) == 1)

            # A vertex has at least one incident edge
            for u in D:
                p.add_constraint(p.sum(edge[e, c] for e in D.incoming_edge_iterator(u, labels=False))
                                 + p.sum(edge[e, c] for e in D.outgoing_edge_iterator(u, labels=False))
                                 >= 1)

            # We use the Miller-Tucker-Zemlin subtour elimination constraints
            # combined with the Desrosiers-Langevin strengthening constraints
            for u, v in D.edge_iterator(labels=False):
                if D.has_edge(v, u):
                    # DL
                    p.add_constraint(pos[u, c] + (n - 1)*edge[(u, v), c] + (n - 3)*edge[(v, u), c]
                                     <= pos[v, c] + n - 2)
                else:
                    # MTZ: If edge uv is selected, v is after u in the partial ordering
                    p.add_constraint(pos[u, c] + 1 - n * (1 - edge[(u, v), c]) <= pos[v, c])

            # and extra strengthening constraints on the minimum distance
            # between the root of the spanning tree and any vertex
            BFS = dict(D.breadth_first_search(root, report_distance=True))
            for u in D:
                p.add_constraint(pos[root, c] + BFS[u] <= pos[u, c])

        # We now solve this program and extract the solution
        try:
            p.solve(log=verbose)
        except MIPSolverException:
            raise EmptySetError("this graph does not contain the required number of trees/arborescences")

        H = DiGraph() if G.is_directed() else Graph()
        H.add_vertices(G.vertex_iterator())
        H.set_pos(G.get_pos())
        classes = [H.copy() for c in colors]

        edges = p.get_values(edge, convert=bool, tolerance=integrality_tolerance)
        for (e, c), b in edges.items():
            if b:
                classes[c].add_edge(e)

        return classes

    def edge_cut(self, s, t, value_only=True, use_edge_labels=False, vertices=False,
                 algorithm="FF", solver=None, verbose=0, *, integrality_tolerance=1e-3):
        r"""
        Return a minimum edge cut between vertices `s` and `t`.

        A minimum edge cut between two vertices `s` and `t` of self is a set `A`
        of edges of minimum weight such that the graph obtained by removing `A`
        from the graph is disconnected. For more information, see the
        :wikipedia:`Cut_(graph_theory)`.

        INPUT:

        - ``s`` -- source vertex

        - ``t`` -- sink vertex

        - ``value_only`` -- boolean (default: ``True``); whether to return only
          the weight of a minimum cut (``True``) or a list of edges of a minimum
          cut (``False``)

        - ``use_edge_labels`` -- boolean (default: ``False``); whether to
          compute a weighted minimum edge cut where the weight of an edge is
          defined by its label (if an edge has no label, `1` is assumed), or to
          compute a cut of minimum cardinality (i.e., edge weights are set to 1)

        - ``vertices`` -- boolean (default: ``False``); whether set to ``True``,
          return a list of edges in the edge cut and the two sets of vertices
          that are disconnected by the cut

          Note: ``vertices=True`` implies ``value_only=False``.

        - ``algorithm`` -- string (default: ``'FF'``); algorithm to use:

          * If ``algorithm = "FF"``, a Python implementation of the
            Ford-Fulkerson algorithm is used

          * If ``algorithm = "LP"``, the problem is solved using Linear
            Programming.

          * If ``algorithm = "igraph"``, the igraph implementation of the
            Goldberg-Tarjan algorithm is used (only available when ``igraph`` is
            installed)

          * If ``algorithm = None``, the problem is solved using the default
            maximum flow algorithm (see :meth:`flow`)

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        .. NOTE::

            The use of Linear Programming for non-integer problems may possibly
            mean the presence of a (slight) numerical noise.

        OUTPUT:

        Real number or tuple, depending on the given arguments (examples are
        given below).

        EXAMPLES:

        A basic application in the Pappus graph::

           sage: g = graphs.PappusGraph()
           sage: g.edge_cut(1, 2, value_only=True)
           3

        Or on Petersen's graph, with the corresponding bipartition of the vertex
        set::

           sage: g = graphs.PetersenGraph()
           sage: g.edge_cut(0, 3, vertices=True)
           [3, [(0, 1, None), (0, 4, None), (0, 5, None)], [[0], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]

        If the graph is a path with randomly weighted edges::

           sage: g = graphs.PathGraph(15)
           sage: for u,v in g.edge_iterator(labels=None):
           ....:    g.set_edge_label(u, v, random())

        The edge cut between the two ends is the edge of minimum weight::

           sage: minimum = min(g.edge_labels())
           sage: minimum == g.edge_cut(0, 14, use_edge_labels=True)
           True
           sage: [value, [e]] = g.edge_cut(0, 14, use_edge_labels=True, value_only=False)
           sage: g.edge_label(e[0], e[1]) == minimum
           True

        The two sides of the edge cut are obviously shorter paths::

           sage: value,edges,[set1,set2] = g.edge_cut(0, 14, use_edge_labels=True, vertices=True)
           sage: g.subgraph(set1).is_isomorphic(graphs.PathGraph(len(set1)))
           True
           sage: g.subgraph(set2).is_isomorphic(graphs.PathGraph(len(set2)))
           True
           sage: len(set1) + len(set2) == g.order()
           True

        TESTS:

        If algorithm is set to an exotic value::

           sage: g = graphs.PetersenGraph()
           sage: g.edge_cut(0, 1, algorithm="Divination")
           Traceback (most recent call last):
           ...
           ValueError: the algorithm argument has to be equal to "FF", "LP", "igraph", or None

        Same result for all three methods::

           sage: g = graphs.RandomGNP(20,.3)
           sage: for u,v in g.edges(sort=True, labels=False):
           ....:    g.set_edge_label(u,v,round(random(),5))
           sage: g.edge_cut(0, 1, algorithm="FF") == g.edge_cut(0, 1, algorithm="LP")
           True
           sage: g.edge_cut(0, 1, algorithm="FF") == g.edge_cut(0, 1, algorithm="igraph") # optional - python_igraph
           True

        Rounded return value when using the LP method::

           sage: g = graphs.PappusGraph()
           sage: g.edge_cut(1, 2, value_only=True, algorithm="LP")
           3

        :trac:`12797`::

            sage: G = Graph([(0, 3, 1), (0, 4, 1), (1, 2, 1), (2, 3, 1), (2, 4, 1)])
            sage: G.edge_cut(0, 1, value_only=False, use_edge_labels=True)
            [1, [(1, 2, 1)]]
            sage: G = DiGraph([(0, 3, 1), (0, 4, 1), (2, 1, 1), (3, 2, 1), (4, 2, 1)])
            sage: G.edge_cut(0, 1, value_only=False, use_edge_labels=True)
            [1, [(2, 1, 1)]]
            sage: G.edge_cut(0, 1, value_only=False, use_edge_labels=True, algorithm='LP')
            (1, [(2, 1)])
        """
        self._scream_if_not_simple(allow_loops=True)
        if vertices:
            value_only = False

        if use_edge_labels:
            def weight(x):
                return x if (x != {} and x is not None) else 1
        else:
            def weight(x):
                return 1

        if algorithm in ["FF", "igraph", None]:
            if value_only:
                return self.flow(s, t, value_only=value_only, use_edge_labels=use_edge_labels, algorithm=algorithm)

            from sage.graphs.digraph import DiGraph
            g = DiGraph(self)

            flow_value, flow_graph = self.flow(s, t, value_only=value_only, use_edge_labels=use_edge_labels, algorithm=algorithm)

            for u, v, l in flow_graph.edge_iterator():
                g.add_edge(v, u)
                if (not use_edge_labels or
                        weight(g.edge_label(u, v)) == weight(l)):
                    g.delete_edge(u, v)

            return_value = [flow_value]

            reachable_from_s = list(g.breadth_first_search(s))

            return_value.append(self.edge_boundary(reachable_from_s))

            if vertices:
                return_value.append([reachable_from_s, list(set(self).difference(reachable_from_s))])

            return return_value

        if algorithm != "LP":
            raise ValueError("the algorithm argument has to be equal to \"FF\", " +
                             "\"LP\", \"igraph\", or None")

        from sage.numerical.mip import MixedIntegerLinearProgram
        g = self
        p = MixedIntegerLinearProgram(maximization=False, solver=solver)
        b = p.new_variable(binary=True)
        v = p.new_variable(binary=True)

        # Helper function to ensure that we use arcs when g is directed and
        # frozensets otherwise
        if g.is_directed():
            def good_edge(e):
                return e
        else:
            good_edge = frozenset

        # Some vertices belong to part 1, others to part 0
        p.add_constraint(v[s], min=0, max=0)
        p.add_constraint(v[t], min=1, max=1)

        if g.is_directed():

            # we minimize the number of edges
            p.set_objective(p.sum(weight(w) * b[good_edge((x, y))] for x, y, w in g.edge_iterator()))

            # Adjacent vertices can belong to different parts only if the
            # edge that connects them is part of the cut
            for x, y in g.edge_iterator(labels=None):
                p.add_constraint(v[x] + b[good_edge((x, y))] - v[y], min=0)

        else:
            # we minimize the number of edges
            p.set_objective(p.sum(weight(w) * b[good_edge((x, y))] for x, y, w in g.edge_iterator()))
            # Adjacent vertices can belong to different parts only if the
            # edge that connects them is part of the cut
            for x, y in g.edge_iterator(labels=None):
                p.add_constraint(v[x] + b[good_edge((x, y))] - v[y], min=0)
                p.add_constraint(v[y] + b[good_edge((x, y))] - v[x], min=0)

        p.solve(log=verbose)
        b = p.get_values(b, convert=bool, tolerance=integrality_tolerance)
        if use_edge_labels:
            obj = sum(weight(w) for x, y, w in g.edge_iterator() if b[good_edge((x, y))])
        else:
            obj = Integer(sum(1 for e in g.edge_iterator(labels=False) if b[good_edge(e)]))

        if value_only:
            return obj

        answer = [obj]
        answer.append([e for e in g.edge_iterator(labels=False) if b[good_edge(e)]])

        if vertices:
            v = p.get_values(v, convert=bool, tolerance=integrality_tolerance)
            l0 = []
            l1 = []
            for x in g:
                if v.get(x, False):
                    l1.append(x)
                else:
                    l0.append(x)
            answer.append([l0, l1])
        return tuple(answer)

    def vertex_cut(self, s, t, value_only=True, vertices=False, solver=None, verbose=0,
                   *, integrality_tolerance=1e-3):
        r"""
        Return a minimum vertex cut between non-adjacent vertices `s` and `t`
        represented by a list of vertices.

        A vertex cut between two non-adjacent vertices is a set `U` of vertices
        of ``self`` such that the graph obtained by removing `U` from ``self``
        is disconnected. For more information, see the
        :wikipedia:`Cut_(graph_theory)`.

        INPUT:

        - ``value_only`` -- boolean (default: ``True``); whether to return only
          the size of the minimum cut, or to also return the set `U` of vertices
          of the cut

        - ``vertices`` -- boolean (default: ``False``); whether to also return
          the two sets of vertices that are disconnected by the cut. Implies
          ``value_only`` set to ``False``.

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        OUTPUT:

        Real number or tuple, depending on the given arguments
        (examples are given below).

        EXAMPLES:

        A basic application in the Pappus graph::

           sage: g = graphs.PappusGraph()
           sage: g.vertex_cut(1, 16, value_only=True)
           3

        In the bipartite complete graph `K_{2,8}`, a cut between the two
        vertices in the size `2` part consists of the other `8` vertices::

           sage: g = graphs.CompleteBipartiteGraph(2, 8)
           sage: [value, vertices] = g.vertex_cut(0, 1, value_only=False)
           sage: print(value)
           8
           sage: vertices == list(range(2, 10))
           True

        Clearly, in this case the two sides of the cut are singletons::

           sage: [value, vertices, [set1, set2]] = g.vertex_cut(0, 1, vertices=True)
           sage: len(set1) == 1
           True
           sage: len(set2) == 1
           True
        """
        from sage.numerical.mip import MixedIntegerLinearProgram
        g = self
        if g.has_edge(s, t):
            from sage.categories.sets_cat import EmptySetError
            raise EmptySetError("there can be no vertex cut between adjacent vertices")
        if vertices:
            value_only = False

        p = MixedIntegerLinearProgram(maximization=False, solver=solver)
        b = p.new_variable(binary=True)
        v = p.new_variable(binary=True)

        # Some vertices belong to part 1, some others to part 0
        p.add_constraint(v[s] == 0)
        p.add_constraint(v[t] == 1)

        # b indicates whether the vertices belong to the cut
        p.add_constraint(b[s] == 0)
        p.add_constraint(b[t] == 0)

        p.set_objective(p.sum(b[x] for x in g))

        if g.is_directed():
            # adjacent vertices belong to the same part except if one of them
            # belongs to the cut
            for x, y in g.edge_iterator(labels=None):
                p.add_constraint(v[x] + b[y] - v[y], min=0)

        else:
            # adjacent vertices belong to the same part except if one of them
            # belongs to the cut
            for x, y in g.edge_iterator(labels=None):
                p.add_constraint(v[x] + b[y] >= v[y])
                p.add_constraint(v[y] + b[x] >= v[x])

        p.solve(log=verbose)
        b = p.get_values(b, convert=bool, tolerance=integrality_tolerance)
        obj = Integer(sum(1 for x in g if b[x]))

        if value_only:
            return obj

        answer = [obj, [x for x in g if b[x]]]
        if vertices:
            v = p.get_values(v, convert=bool, tolerance=integrality_tolerance)
            l0 = []
            l1 = []
            for x in g:
                # if the vertex is not in the cut
                if not b.get(x, False):
                    if v.get(x, False):
                        l1.append(x)
                    else:
                        l0.append(x)
            answer.append([l0, l1])
        return tuple(answer)

    def multiway_cut(self, vertices, value_only=False, use_edge_labels=False,
                     solver=None, verbose=0, *, integrality_tolerance=1e-3):
        r"""
        Return a minimum edge multiway cut.

        A multiway cut for a vertex set `S` in a graph or a digraph `G` is a set
        `C` of edges such that any two vertices `u,v` in `S` are disconnected
        when removing the edges of `C` from `G`.
        ( cf. http://www.d.kth.se/~viggo/wwwcompendium/node92.html )

        Such a cut is said to be minimum when its cardinality (or weight) is
        minimum.

        INPUT:

        - ``vertices`` -- iterable; the set of vertices

        - ``value_only`` -- boolean (default: ``False``); whether to return only
          the size of the minimum multiway cut, or to return the list of edges
          of the multiway cut

        - ``use_edge_labels`` -- boolean (default: ``False``); whether to
          compute a weighted minimum multiway cut where the weight of an edge is
          defined by its label (if an edge has no label, `1` is assumed), or to
          compute a cut of minimum cardinality (i.e., edge weights are set to 1)

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        EXAMPLES:

        Of course, a multiway cut between two vertices correspond to a minimum
        edge cut::

            sage: g = graphs.PetersenGraph()
            sage: g.edge_cut(0,3) == g.multiway_cut([0,3], value_only = True)
            True

        As Petersen's graph is `3`-regular, a minimum multiway cut between three
        vertices contains at most `2\times 3` edges (which could correspond to
        the neighborhood of 2 vertices)::

            sage: g.multiway_cut([0,3,9], value_only = True) == 2*3
            True

        In this case, though, the vertices are an independent set.  If we pick
        instead vertices `0,9,` and `7`, we can save `4` edges in the multiway
        cut::

            sage: g.multiway_cut([0,7,9], value_only = True) == 2*3 - 1
            True

        This example, though, does not work in the directed case anymore, as it
        is not possible in Petersen's graph to mutualise edges::

            sage: g = DiGraph(g)
            sage: g.multiway_cut([0,7,9], value_only = True) == 3*3
            True

        Of course, a multiway cut between the whole vertex set contains all the
        edges of the graph::

            sage: C = g.multiway_cut(g.vertices(sort=False))
            sage: set(C) == set(g.edges(sort=False))
            True
        """
        self._scream_if_not_simple(allow_loops=True)
        from sage.numerical.mip import MixedIntegerLinearProgram
        from itertools import combinations, chain

        p = MixedIntegerLinearProgram(maximization=False, solver=solver)

        # height[c,v] represents the height of vertex v for commodity c
        height = p.new_variable(nonnegative=True)

        # cut[e] represents whether e is in the cut
        cut = p.new_variable(binary=True)

        # Helper function to correctly index variables cut
        if self.is_directed():
            def good_edge(e):
                return e
        else:
            good_edge = frozenset

        # Weight function
        if use_edge_labels:
            def weight(l):
                return l if l is not None else 1
        else:
            def weight(l):
                return 1

        p.set_objective(p.sum(weight(l) * cut[good_edge((u, v))] for u, v, l in self.edge_iterator()))

        if self.is_directed():
            for s, t in chain(combinations(vertices, 2), [(y, x) for x, y in combinations(vertices, 2)]):
                # For each commodity, the source is at height 0
                # and the destination is at height 1
                p.add_constraint(height[(s, t), s], min=0, max=0)
                p.add_constraint(height[(s, t), t], min=1, max=1)

                # given a commodity (s,t), the height of two adjacent vertices u,v
                # can differ of at most the value of the edge between them
                for u, v in self.edge_iterator(labels=False):
                    p.add_constraint(height[(s, t), u] - height[(s, t), v] - cut[good_edge((u, v))], max=0)

        else:
            for s, t in combinations(vertices, 2):
                # For each commodity, the source is at height 0
                # and the destination is at height 1
                p.add_constraint(height[(s, t), s], min=0, max=0)
                p.add_constraint(height[(s, t), t], min=1, max=1)

                # given a commodity (s,t), the height of two adjacent vertices u,v
                # can differ of at most the value of the edge between them
                for u, v in self.edge_iterator(labels=False):
                    p.add_constraint(height[(s, t), u] - height[(s, t), v] - cut[good_edge((u, v))], max=0)
                    p.add_constraint(height[(s, t), v] - height[(s, t), u] - cut[good_edge((u, v))], max=0)

        p.solve(log=verbose)
        cut = p.get_values(cut, convert=bool, tolerance=integrality_tolerance)

        if value_only:
            if use_edge_labels:
                return sum(weight(l) for u, v, l in self.edge_iterator() if cut[good_edge((u, v))])
            else:
                return Integer(sum(1 for e in self.edge_iterator(labels=False) if cut[good_edge(e)]))

        return [e for e in self.edge_iterator() if cut[good_edge((e[0], e[1]))]]

    def max_cut(self, value_only=True, use_edge_labels=False, vertices=False,
                solver=None, verbose=0, *, integrality_tolerance=1e-3):
        r"""
        Return a maximum edge cut of the graph.

        For more information, see the :wikipedia:`Maximum_cut`.

        INPUT:

        - ``value_only`` -- boolean (default: ``False``); whether to return only
          the size of the maximum edge cut, or to also return the list of edges
          of the maximum edge cut

        - ``use_edge_labels`` -- boolean (default: ``False``); whether to
          compute a weighted maximum cut where the weight of an edge is defined
          by its label (if an edge has no label, `1` is assumed), or to compute
          a cut of maximum cardinality (i.e., edge weights are set to 1)

        - ``vertices`` -- boolean (default: ``False``); whether to return the
          two sets of vertices that are disconnected by the cut. This implies
          ``value_only=False``.

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        EXAMPLES:

        Quite obviously, the max cut of a bipartite graph is the number of
        edges, and the two sets of vertices are the two sides::

            sage: g = graphs.CompleteBipartiteGraph(5,6)
            sage: [ value, edges, [ setA, setB ]] = g.max_cut(vertices=True)
            sage: value == 5*6
            True
            sage: bsetA, bsetB  = map(list,g.bipartite_sets())
            sage: (bsetA == setA and bsetB == setB ) or ((bsetA == setB and bsetB == setA ))
            True

        The max cut of a Petersen graph::

           sage: g=graphs.PetersenGraph()
           sage: g.max_cut()
           12

        TESTS::

            sage: graphs.EmptyGraph().max_cut()
            Traceback (most recent call last):
            ...
            ValueError: max cut is not defined for the empty graph
        """
        self._scream_if_not_simple(allow_loops=True)
        g = self

        if not self.order():
            raise ValueError("max cut is not defined for the empty graph")

        if vertices:
            value_only = False

        if use_edge_labels:
            from sage.rings.real_mpfr import RR

            def weight(x):
                return x if x in RR else 1
        else:
            def weight(x):
                return 1

        if g.is_directed():
            def good_edge(e):
                return e
        else:
            good_edge = frozenset

        from sage.numerical.mip import MixedIntegerLinearProgram

        p = MixedIntegerLinearProgram(maximization=True, solver=solver)

        in_set = p.new_variable(binary=True)
        in_cut = p.new_variable(binary=True)

        # A vertex has to be in some set
        for v in g:
            p.add_constraint(in_set[0, v] + in_set[1, v], max=1, min=1)

        # There is no empty set
        p.add_constraint(p.sum(in_set[1, v] for v in g), min=1)
        p.add_constraint(p.sum(in_set[0, v] for v in g), min=1)

        if g.is_directed():
            # There is no edge from set 0 to set 1 which is not in the cut.
            # Besides, an edge can only be in the cut if its vertices
            # belong to different sets
            for u, v in g.edge_iterator(labels=None):
                p.add_constraint(in_set[0, u] + in_set[1, v] - in_cut[u, v], max=1)
                p.add_constraint(in_set[0, u] + in_set[0, v] + in_cut[u, v], max=2)
                p.add_constraint(in_set[1, u] + in_set[1, v] + in_cut[u, v], max=2)

        else:
            # Two adjacent vertices are in different sets if and only if
            # the edge between them is in the cut
            for u, v in g.edge_iterator(labels=None):
                fuv = good_edge((u, v))
                p.add_constraint(in_set[0, u] + in_set[1, v] - in_cut[fuv], max=1)
                p.add_constraint(in_set[1, u] + in_set[0, v] - in_cut[fuv], max=1)
                p.add_constraint(in_set[0, u] + in_set[0, v] + in_cut[fuv], max=2)
                p.add_constraint(in_set[1, u] + in_set[1, v] + in_cut[fuv], max=2)

        p.set_objective(p.sum(weight(l) * in_cut[good_edge((u, v))] for u, v, l in g.edge_iterator()))

        p.solve(log=verbose)

        in_cut = p.get_values(in_cut, convert=bool, tolerance=integrality_tolerance)
        if use_edge_labels:
            obj = sum(weight(l) for u, v, l in g.edge_iterator() if in_cut[good_edge((u, v))])
        else:
            obj = Integer(sum(1 for e in g.edge_iterator(labels=False) if in_cut[good_edge(e)]))

        if value_only:
            return obj
        else:
            edges = [(u, v, l) for u, v, l in g.edge_iterator() if in_cut[good_edge((u, v))]]
            val = [obj, edges]

            if vertices:
                in_set = p.get_values(in_set, convert=bool, tolerance=integrality_tolerance)
                a = []
                b = []
                for v in g:
                    if in_set[0, v]:
                        a.append(v)
                    else:
                        b.append(v)
                val.append([a, b])

            return val

    def longest_path(self, s=None, t=None, use_edge_labels=False, algorithm="MILP",
                     solver=None, verbose=0, *, integrality_tolerance=1e-3):
        r"""
        Return a longest path of ``self``.

        INPUT:

        - ``s`` -- a vertex (default: ``None``); forces the source of the path
          (the method then returns the longest path starting at ``s``). The
          argument is set to ``None`` by default, which means that no constraint
          is set upon the first vertex in the path.

        - ``t`` -- a vertex (default: ``None``); forces the destination of the
          path (the method then returns the longest path ending at ``t``). The
          argument is set to ``None`` by default, which means that no constraint
          is set upon the last vertex in the path.

        - ``use_edge_labels`` -- boolean (default: ``False``); whether to
          compute a path with maximum weight where the weight of an edge is
          defined by its label (a label set to ``None`` or ``{}`` being
          considered as a weight of `1`), or to compute a path with the longest
          possible number of edges (i.e., edge weights are set to 1)

        - ``algorithm`` -- string (default: ``"MILP"``); the algorithm to use
          among ``"MILP"`` and ``"backtrack"``. Two remarks on this respect:

          * While the MILP formulation returns an exact answer, the backtrack
            algorithm is a randomized heuristic.

          * As the backtrack algorithm does not support edge weighting, setting
            ``use_edge_labels=True`` will force the use of the MILP algorithm.

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        .. NOTE::

            The length of a path is assumed to be the number of its edges, or
            the sum of their labels (when ``use_edge_labels == True``).

        OUTPUT:

        A subgraph of ``self`` corresponding to a (directed if ``self`` is
        directed) longest path. If ``use_edge_labels == True``, a pair ``weight,
        path`` is returned.

        ALGORITHM:

        Mixed Integer Linear Programming (this problem is known to be NP-Hard).

        EXAMPLES:

        Petersen's graph being hypohamiltonian, it has a longest path of length
        `n - 2`::

            sage: g = graphs.PetersenGraph()
            sage: lp = g.longest_path()
            sage: lp.order() >= g.order() - 2
            True

        The heuristic totally agrees::

            sage: g = graphs.PetersenGraph()
            sage: p = g.longest_path(algorithm="backtrack").edges(sort=True, labels=False)
            sage: len(p)
            9

        .. PLOT::

            g = graphs.PetersenGraph()
            sphinx_plot(g.plot(edge_colors={"red": g.longest_path().edges(sort=False)}))

        Let us compute the longest path on a random graph with random
        weights, and ensure the resulting graph is indeed a path::

            sage: g = graphs.RandomGNP(15, 0.3)
            sage: for u, v in g.edge_iterator(labels=False):
            ....:     g.set_edge_label(u, v, random())
            sage: lp = g.longest_path()
            sage: (not lp.is_forest() or not max(lp.degree()) <= 2
            ....:  or not lp.is_connected())
            False

        TESTS:

        The argument ``algorithm`` must be either ``'backtrack'`` or
        ``'MILP'``::

            sage: graphs.PetersenGraph().longest_path(algorithm="abc")
            Traceback (most recent call last):
            ...
            ValueError: algorithm must be either 'backtrack' or 'MILP'

        Disconnected graphs not weighted::

            sage: g1 = graphs.PetersenGraph()
            sage: g2 = 2 * g1
            sage: lp1 = g1.longest_path()
            sage: lp2 = g2.longest_path()
            sage: len(lp1) == len(lp2)
            True

        Disconnected graphs weighted::

            sage: g1 = graphs.PetersenGraph()
            sage: for u,v in g.edge_iterator(labels=False):
            ....:     g.set_edge_label(u, v, random())
            sage: g2 = 2 * g1
            sage: lp1 = g1.longest_path(use_edge_labels=True)
            sage: lp2 = g2.longest_path(use_edge_labels=True)
            sage: lp1[0] == lp2[0]
            True

        Empty graphs::

            sage: Graph().longest_path()
            Graph on 0 vertices
            sage: Graph().longest_path(use_edge_labels=True)
            [0, Graph on 0 vertices]
            sage: graphs.EmptyGraph().longest_path()
            Graph on 0 vertices
            sage: graphs.EmptyGraph().longest_path(use_edge_labels=True)
            [0, Graph on 0 vertices]

        Trivial graphs::

            sage: G = Graph()
            sage: G.add_vertex(0)
            sage: G.longest_path()
            Graph on 0 vertices
            sage: G.longest_path(use_edge_labels=True)
            [0, Graph on 0 vertices]
            sage: graphs.CompleteGraph(1).longest_path()
            Graph on 0 vertices
            sage: graphs.CompleteGraph(1).longest_path(use_edge_labels=True)
            [0, Graph on 0 vertices]

        Random test for digraphs::

            sage: g = digraphs.RandomDirectedGNP(15, 0.3)
            sage: for u, v in g.edge_iterator(labels=False):
            ....:     g.set_edge_label(u, v, random())
            sage: lp = g.longest_path()
            sage: (not lp.is_directed_acyclic() or
            ....:  not max(lp.out_degree()) <= 1 or
            ....:  not max(lp.in_degree()) <= 1 or
            ....:  not lp.is_connected())
            False

        :trac:`13019`::

            sage: g = graphs.CompleteGraph(5).to_directed()
            sage: g.longest_path(s=1, t=2)
            Subgraph of (Complete graph): Digraph on 5 vertices

        :trac:`14412`::

            sage: l = [(0, 1), (0, 3), (2, 0), (3, 4)]
            sage: G = DiGraph(l)
            sage: H = {(0, 3), (2, 0), (3, 4)}
            sage: H == {x for x in G.longest_path().edge_iterator(labels=False)}
            True
        """
        self._scream_if_not_simple()

        if use_edge_labels:
            algorithm = "MILP"
        if algorithm not in ("backtrack", "MILP"):
            raise ValueError("algorithm must be either 'backtrack' or 'MILP'")

        # Quick improvement
        if not self.is_connected():
            if use_edge_labels:
                return max((g.longest_path(s=s, t=t,
                                           use_edge_labels=use_edge_labels,
                                           algorithm=algorithm)
                            for g in self.connected_components_subgraphs()),
                           key=lambda x: x[0])
            else:
                return max((g.longest_path(s=s, t=t,
                                           use_edge_labels=use_edge_labels,
                                           algorithm=algorithm)
                            for g in self.connected_components_subgraphs()),
                           key=lambda x: x.order())

        # Stupid cases
        # - Graph having <= 1 vertex.
        #
        # - The source has outdegree 0 in a directed graph, or
        #   degree 0, or is not a vertex of the graph.
        #
        # - The destination has indegree 0 in a directed graph, or
        #   degree 0, or is not a vertex of the graph.
        #
        # - Both s and t are specified, but there is no path between
        #   the two in a directed graph (the graph is connected).
        if (self.order() <= 1 or
            (s is not None and (
                    (s not in self) or
                    (self._directed and not self.out_degree(s)) or
                    (not self._directed and not self.degree(s)))) or
            (t is not None and (
                    (t not in self) or
                    (self._directed and not self.in_degree(t)) or
                    (not self._directed and not self.degree(t)))) or
            (self._directed and (s is not None) and (t is not None) and
             not self.shortest_path(s, t))):
            if self._directed:
                from sage.graphs.digraph import DiGraph
                return [0, DiGraph()] if use_edge_labels else DiGraph()
            from sage.graphs.graph import Graph
            return [0, Graph()] if use_edge_labels else Graph()

        # Calling the backtrack heuristic if asked
        if algorithm == "backtrack":
            from sage.graphs.generic_graph_pyx import find_hamiltonian as fh
            x = fh(self, find_path=True)[1]
            return self.subgraph(vertices=x, edges=list(zip(x[:-1], x[1:])))

        ##################
        # LP Formulation #
        ##################

        # Epsilon... Must be less than 1/(n+1), but we want to avoid
        # numerical problems...
        epsilon = 1 / (2 * float(self.order()))

        # Associating a weight to a label
        if use_edge_labels:
            def weight(x):
                return x if (x is not None and x != {}) else 1
        else:
            def weight(x):
                return 1

        from sage.numerical.mip import MixedIntegerLinearProgram
        p = MixedIntegerLinearProgram(solver=solver)

        # edge_used[(u,v)] == 1 if (u,v) is used
        edge_used = p.new_variable(binary=True)

        # relaxed version of the previous variable, to prevent the
        # creation of cycles
        r_edge_used = p.new_variable(nonnegative=True)

        # vertex_used[v] == 1 if vertex v is used
        vertex_used = p.new_variable(binary=True)

        if self._directed:

            # if edge uv is used, vu cannot be
            for u, v in self.edge_iterator(labels=False):
                if self.has_edge(v, u):
                    p.add_constraint(edge_used[u, v] + edge_used[v, u] <= 1)

            # A vertex is used if one of its incident edges is
            for u, v in self.edge_iterator(labels=False):
                p.add_constraint(vertex_used[v] >= edge_used[u, v])
                p.add_constraint(vertex_used[u] >= edge_used[u, v])

            # A path is a tree. If n vertices are used, at most n-1 edges are
            p.add_constraint(p.sum(vertex_used[v] for v in self)
                             - p.sum(edge_used[e] for e in self.edge_iterator(labels=False))
                             == 1)

            # A vertex has at most one incoming used edge and at most
            # one outgoing used edge
            for v in self:
                p.add_constraint(p.sum(edge_used[u, v] for u in self.neighbor_in_iterator(v)) <= 1)
                p.add_constraint(p.sum(edge_used[v, u] for u in self.neighbor_out_iterator(v)) <= 1)

            # r_edge_used is "more" than edge_used, though it ignores
            # the direction
            for u, v in self.edge_iterator(labels=False):
                p.add_constraint(r_edge_used[u, v] + r_edge_used[v, u]
                                 >= edge_used[u, v])

            # No cycles
            for v in self:
                p.add_constraint(p.sum(r_edge_used[u, v] for u in self.neighbor_iterator(v))
                                 <= 1 - epsilon)

            # Enforcing the source if asked.. If s is set, it has no
            # incoming edge and exactly one son
            if s is not None:
                p.add_constraint(p.sum(edge_used[u, s] for u in self.neighbor_in_iterator(s)),
                                 max=0, min=0)
                p.add_constraint(p.sum(edge_used[s, u] for u in self.neighbor_out_iterator(s)),
                                 min=1, max=1)

            # Enforcing the destination if asked.. If t is set, it has
            # no outgoing edge and exactly one parent
            if t is not None:
                p.add_constraint(p.sum(edge_used[u, t] for u in self.neighbor_in_iterator(t)),
                                 min=1, max=1)
                p.add_constraint(p.sum(edge_used[t, u] for u in self.neighbor_out_iterator(t)),
                                 max=0, min=0)

            # Defining the objective
            p.set_objective(p.sum(weight(l) * edge_used[u, v]
                                  for u, v, l in self.edge_iterator()))
        else:
            # We use edge_used[frozenset((u, v))] to avoid having two different
            # variables for edge (u, v)

            # A vertex is used if one of its incident edges is
            for v in self:
                for u in self.neighbor_iterator(v):
                    p.add_constraint(vertex_used[v] - edge_used[frozenset((u, v))], min=0)
            # A path is a tree. If n vertices are used, at most n-1 edges are
            p.add_constraint(p.sum(vertex_used[v] for v in self)
                             - p.sum(edge_used[frozenset((u, v))]
                                     for u, v in self.edge_iterator(labels=False)),
                             min=1, max=1)
            # A vertex has at most two incident edges used
            for v in self:
                p.add_constraint(p.sum(edge_used[frozenset((u, v))] for u in self.neighbor_iterator(v)),
                                 max=2)
            # r_edge_used is "more" than edge_used
            for u, v in self.edge_iterator(labels=False):
                p.add_constraint(r_edge_used[u, v]
                                 + r_edge_used[v, u]
                                 - edge_used[frozenset((u, v))],
                                 min=0)
            # No cycles
            for v in self:
                p.add_constraint(p.sum(r_edge_used[u, v] for u in self.neighbor_iterator(v)),
                                 max=1 - epsilon)
            # Enforcing the destination if asked.. If s or t are set,
            # they have exactly one incident edge
            if s is not None:
                p.add_constraint(p.sum(edge_used[frozenset((s, u))] for u in self.neighbor_iterator(s)),
                                 max=1, min=1)
            if t is not None:
                p.add_constraint(p.sum(edge_used[frozenset((t, u))] for u in self.neighbor_iterator(t)),
                                 max=1, min=1)
            # Defining the objective
            p.set_objective(p.sum(weight(l) * edge_used[frozenset((u, v))]
                                  for u, v, l in self.edge_iterator()))

        # Computing the result. No exception has to be raised, as this
        # problem always has a solution (there is at least one edge,
        # and a path from s to t if they are specified).
        p.solve(log=verbose)
        edge_used = p.get_values(edge_used, convert=bool, tolerance=integrality_tolerance)
        vertex_used = p.get_values(vertex_used, convert=bool, tolerance=integrality_tolerance)
        if self._directed:
            g = self.subgraph(vertices=(v for v in self if vertex_used[v]),
                              edges=((u, v, l) for u, v, l in self.edge_iterator()
                                     if edge_used[u, v]))
        else:
            g = self.subgraph(
                vertices=(v for v in self if vertex_used[v]),
                edges=((u, v, l) for u, v, l in self.edge_iterator()
                       if edge_used[frozenset((u, v))]))
        if use_edge_labels:
            return sum(map(weight, g.edge_labels())), g
        else:
            return g

    def hamiltonian_path(self, s=None, t=None, use_edge_labels=False,
                         maximize=False, algorithm='MILP', solver=None, verbose=0,
                         *, integrality_tolerance=1e-3):
        r"""
        Return a Hamiltonian path of the current graph/digraph.

        A path is Hamiltonian if it goes through all the vertices exactly
        once. Computing a Hamiltonian path being NP-Complete, this
        algorithm could run for some time depending on the instance.

        When ``use_edge_labels == True``, this method returns either a minimum
        weight hamiltonian path or a maximum weight Hamiltonian path (if
        ``maximize == True``).

        .. SEEALSO::

            - :meth:`~GenericGraph.longest_path`
            - :meth:`~GenericGraph.hamiltonian_cycle`

        INPUT:

        - ``s`` -- vertex (default: ``None``); if specified, then forces the
          source of the path (the method then returns a Hamiltonian path
          starting at ``s``)

        - ``t`` -- vertex (default: ``None``); if specified, then forces the
          destination of the path (the method then returns a Hamiltonian path
          ending at ``t``)

        - ``use_edge_labels`` -- boolean (default: ``False``); whether to
          compute a weighted hamiltonian path where the weight of an edge is
          defined by its label (a label set to ``None`` or ``{}`` being
          considered as a weight of `1`), or a non-weighted hamiltonian path

        - ``maximize`` -- boolean (default: ``False``); whether to compute a
          minimum (default) or a maximum (when ``maximize == True``) weight
          hamiltonian path. This parameter is considered only if
          ``use_edge_labels == True``.

        - ``algorithm`` -- string (default: ``"MILP"``); the algorithm the use
          among ``"MILP"`` and ``"backtrack"``; two remarks on this respect:

          * While the MILP formulation returns an exact answer, the backtrack
            algorithm is a randomized heuristic.

          * The backtrack algorithm does not support edge weighting, so setting
            ``use_edge_labels=True`` will force the use of the MILP algorithm.

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        OUTPUT:

        A subgraph of ``self`` corresponding to a (directed if ``self`` is
        directed) hamiltonian path. If no hamiltonian path is found, return
        ``None``. If ``use_edge_labels == True``, a pair ``weight, path`` is
        returned.

        EXAMPLES:

        The `3 \times 3`-grid has an Hamiltonian path, an hamiltonian path
        starting from vertex `(0, 0)` and ending at vertex `(2, 2)`, but no
        Hamiltonian path starting from `(0, 0)` and ending at `(0, 1)`::

            sage: g = graphs.Grid2dGraph(3, 3)
            sage: g.hamiltonian_path()
            Hamiltonian path from 2D Grid Graph for [3, 3]: Graph on 9 vertices
            sage: g.hamiltonian_path(s=(0, 0), t=(2, 2))
            Hamiltonian path from 2D Grid Graph for [3, 3]: Graph on 9 vertices
            sage: g.hamiltonian_path(s=(0, 0), t=(2, 2), use_edge_labels=True)
            (8, Hamiltonian path from 2D Grid Graph for [3, 3]: Graph on 9 vertices)
            sage: g.hamiltonian_path(s=(0, 0), t=(0, 1)) is None
            True
            sage: g.hamiltonian_path(s=(0, 0), t=(0, 1), use_edge_labels=True)
            (0, None)

        TESTS:

        Empty and one-element graphs::

            sage: g = Graph()
            sage: g.hamiltonian_path()
            Traceback (most recent call last):
            ...
            ValueError: the Hamiltonian path problem is not well defined
             for empty and one-element (di)graphs
            sage: g = Graph(1)
            sage: g.hamiltonian_path()
            Traceback (most recent call last):
            ...
            ValueError: the Hamiltonian path problem is not well defined
             for empty and one-element (di)graphs

        A non-connected (di)graph has no hamiltonian path::

            sage: g = Graph(2)
            sage: g.hamiltonian_path() is None
            True
            sage: g.hamiltonian_path(use_edge_labels=True)
            (0, None)
            sage: g = DiGraph(2)
            sage: g.hamiltonian_path() is None
            True

        Asking for a minimum (resp., maximum) weight Hamiltonian path::

            sage: G = Graph([(0, 1, 1), (0, 2, 2), (0, 3, 1), (1, 2, 1), (1, 3, 2), (2, 3, 1)])
            sage: print(G.hamiltonian_path(s=0, t=1, use_edge_labels=True, maximize=False)[0])
            3
            sage: print(G.hamiltonian_path(s=0, t=1, use_edge_labels=True, maximize=True)[0])
            5

        Parameter ``algorithm`` must be either ``'backtrack'`` or ``'MILP'``::

            sage: Graph().hamiltonian_path(algorithm='noname')
            Traceback (most recent call last):
            ...
            ValueError: algorithm must be either 'backtrack' or 'MILP'
        """
        if use_edge_labels or algorithm is None:
            # We force the algorithm to 'MILP'
            algorithm = 'MILP'
        elif algorithm not in ['MILP', 'backtrack']:
            raise ValueError("algorithm must be either 'backtrack' or 'MILP'")

        if self.order() < 2:
            raise ValueError('the Hamiltonian path problem is not well ' +
                             'defined for empty and one-element (di)graphs')

        if not self.is_connected():
            return (0, None) if use_edge_labels else None

        #
        # Deal with loops and multiple edges
        #
        if self.has_loops() or self.has_multiple_edges():
            keep_label = 'max' if (use_edge_labels and maximize) else 'min'
            g = self.to_simple(to_undirected=False, keep_label=keep_label, immutable=False)
        else:
            g = self.copy(immutable=False)

        new_s, new_t = s, t
        if g.is_directed():
            #
            # Deal with vertices with no in|out-neighbors
            #
            zeros = [u for u in g if not g.in_degree(u)]
            if len(zeros) > 1:
                return (0, None) if use_edge_labels else None
            elif len(zeros) == 1:
                if new_s is None:
                    new_s = zeros.pop()
                elif new_s not in zeros:
                    return (0, None) if use_edge_labels else None

            zeros = [u for u in g if not g.out_degree(u)]
            if len(zeros) > 1:
                return (0, None) if use_edge_labels else None
            elif len(zeros) == 1:
                if new_t is None:
                    new_t = zeros.pop()
                elif new_t not in zeros:
                    return (0, None) if use_edge_labels else None

        else:
            #
            # Deal with vertices of degree one
            #
            ones = [u for u in g if g.degree(u) == 1]
            if len(ones) > 2:
                return (0, None) if use_edge_labels else None

            elif len(ones) == 2:
                if new_s is not None and new_s not in ones:
                    return (0, None) if use_edge_labels else None
                if new_t is not None and new_t not in ones:
                    return (0, None) if use_edge_labels else None

                # Set new_s and new_t if possible
                if new_s is None and new_t is None:
                    new_s, new_t = ones
                elif new_s is not None and new_t is None:
                    new_t = ones[1] if new_s == ones[0] else ones[0]
                elif new_s is None and new_t is not None:
                    new_s = ones[1] if new_t == ones[0] else ones[0]

            elif len(ones) == 1:
                if new_s is not None and new_t is not None and not (new_s in ones or new_t in ones):
                    return (0, None) if use_edge_labels else None
                elif new_s is None and (new_t is None or (new_t is not None and new_t not in ones)):
                    new_s = ones.pop()
                elif new_t is None and new_s is not None and new_s not in ones:
                    new_t = ones.pop()

        if not use_edge_labels and algorithm == "backtrack":
            path = g.longest_path(s=new_s, t=new_t, algorithm="backtrack")
            return path if path.order() == g.order() else None

        #
        # We modify the graph to turn the Hamiltonian Path problem into a
        # Hamiltonian Cycle problem. The modification ensures that the computed
        # Hamiltonian Cycle will visit new_s (if determined) right after new_t
        # (if determined). Hence the extraction of the Hamiltonian Path is easy.
        #
        extra_vertices = []
        if new_s is None:
            # If the source is not specified or determined, we add a virtual
            # source and an edge from it to each vertex of the (di)graph.
            new_s = g.add_vertex()
            extra_vertices.append(new_s)
            for u in self:  # in original set of vertices
                g.add_edge(new_s, u, 0)

        if new_t is None:
            # If the source is not specified or determined, we add a virtual
            # destination and an edge from each vertex of the (di)graph to it.
            new_t = g.add_vertex()
            extra_vertices.append(new_t)
            for u in self:
                g.add_edge(u, new_t, 0)

        # We force the Hamiltonian cycle to visit new_s right after new_t by
        # inserting an intermediate vertex
        v = g.add_vertex()
        extra_vertices.append(v)
        g.add_edge(new_t, v, 0)
        g.add_edge(v, new_s, 0)

        #
        # We now search for an Hamiltonian Cycle in g
        #
        from sage.categories.sets_cat import EmptySetError
        try:
            tsp = g.traveling_salesman_problem(use_edge_labels=use_edge_labels,
                                               maximize=maximize,
                                               solver=solver, verbose=verbose,
                                               integrality_tolerance=integrality_tolerance)
        except EmptySetError:
            return (0, None) if use_edge_labels else None

        tsp.delete_vertices(extra_vertices)
        tsp.name("Hamiltonian path from {}".format(self.name()))

        def weight(label):
            return 1 if label is None else label
        return (sum(map(weight, tsp.edge_labels())), tsp) if use_edge_labels else tsp

    def traveling_salesman_problem(self, use_edge_labels=False, maximize=False,
                                   solver=None, constraint_generation=None,
                                   verbose=0, verbose_constraints=False,
                                   *, integrality_tolerance=1e-3):
        r"""
        Solve the traveling salesman problem (TSP)

        Given a graph (resp. a digraph) `G` with weighted edges, the traveling
        salesman problem consists in finding a Hamiltonian cycle (resp. circuit)
        of the graph of minimum cost.

        This TSP is one of the most famous NP-Complete problems, this function
        can thus be expected to take some time before returning its result.

        INPUT:

        - ``use_edge_labels`` -- boolean (default: ``False``); whether to solve
          the weighted traveling salesman problem where the weight of an edge is
          defined by its label (a label set to ``None`` or ``{}`` being
          considered as a weight of `1`), or the non-weighted version (i.e., the
          Hamiltonian cycle problem)

        - ``maximize`` -- boolean (default: ``False``); whether to compute a
          minimum (default) or a maximum (when ``maximize == True``) weight tour
          (or Hamiltonian cycle). This parameter is considered only if
          ``use_edge_labels == True``.

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``constraint_generation`` -- boolean (default: ``None``); whether to
          use constraint generation when solving the Mixed Integer Linear
          Program.

          When ``constraint_generation = None``, constraint generation is used
          whenever the graph has a density larger than 70%.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``verbose_constraints`` -- boolean (default: ``False``); whether to
          display which constraints are being generated

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        OUTPUT:

        A solution to the TSP, as a ``Graph`` object whose vertex set is `V(G)`,
        and whose edges are only those of the solution.

        ALGORITHM:

        This optimization problem is solved through the use of Linear
        Programming.

        .. NOTE::

            This function is correctly defined for both graph and digraphs. In
            the second case, the returned cycle is a circuit of optimal cost.

        EXAMPLES:

        The Heawood graph is known to be Hamiltonian::

            sage: g = graphs.HeawoodGraph()
            sage: tsp = g.traveling_salesman_problem()
            sage: tsp
            TSP from Heawood graph: Graph on 14 vertices

        The solution to the TSP has to be connected::

            sage: tsp.is_connected()
            True

        It must also be a `2`-regular graph::

            sage: tsp.is_regular(k=2)
            True

        And obviously it is a subgraph of the Heawood graph::

            sage: tsp.is_subgraph(g, induced=False)
            True

        On the other hand, the Petersen Graph is known not to be Hamiltonian::

            sage: g = graphs.PetersenGraph()
            sage: tsp = g.traveling_salesman_problem()
            Traceback (most recent call last):
            ...
            EmptySetError: the given graph is not Hamiltonian

        One easy way to change it is obviously to add to this graph the edges
        corresponding to a Hamiltonian cycle. If we do this by setting the cost
        of these new edges to `2`, while the others are set to `1`, we notice
        that not all the edges we added are used in the optimal solution ::

            sage: for u, v in g.edge_iterator(labels=None):
            ....:    g.set_edge_label(u, v, 1)

            sage: cycle = graphs.CycleGraph(10)
            sage: for u,v in cycle.edges(labels=None, sort=False):
            ....:    if not g.has_edge(u, v):
            ....:        g.add_edge(u, v)
            ....:    g.set_edge_label(u, v, 2)

            sage: tsp = g.traveling_salesman_problem(use_edge_labels=True)
            sage: sum( tsp.edge_labels() ) < 2 * 10
            True

        If we pick `1/2` instead of `2` as a cost for these new edges, they
        clearly become the optimal solution::

            sage: for u, v in cycle.edges(labels=None, sort=False):
            ....:    g.set_edge_label(u,v,1/2)

            sage: tsp = g.traveling_salesman_problem(use_edge_labels=True)
            sage: sum(tsp.edge_labels()) == (1/2) * 10
            True

        Search for a minimum and a maximum weight Hamiltonian cycle::

            sage: G = Graph([(0, 1, 1), (0, 2, 2), (0, 3, 1), (1, 2, 1), (1, 3, 2), (2, 3, 1)])
            sage: tsp = G.traveling_salesman_problem(use_edge_labels=True, maximize=False)
            sage: print(sum(tsp.edge_labels()))
            4
            sage: tsp = G.traveling_salesman_problem(use_edge_labels=True, maximize=True)
            sage: print(sum(tsp.edge_labels()))
            6

        TESTS:

        Comparing the results returned according to the value of
        ``constraint_generation``. First, for graphs::

            sage: from operator import itemgetter
            sage: n = 20
            sage: g = Graph()
            sage: g.allow_multiple_edges(False)
            sage: for u, v in graphs.RandomGNP(n,.2).edges(labels=False, sort=False):
            ....:      g.add_edge(u, v, ZZ.random_element(1,100000))
            sage: for u, v in graphs.CycleGraph(n).edges(labels=False, sort=False):
            ....:      if not g.has_edge(u, v):
            ....:          g.add_edge(u, v, ZZ.random_element(1,100000))
            sage: v1 = g.traveling_salesman_problem(constraint_generation=False, use_edge_labels=True)
            sage: v2 = g.traveling_salesman_problem(use_edge_labels=True)
            sage: sum(v1.edge_labels()) == sum(v2.edge_labels())
            True

        Then for digraphs::

            sage: from operator import itemgetter
            sage: n = 20
            sage: g = DiGraph()
            sage: g.allow_multiple_edges(False)
            sage: for u, v in digraphs.RandomDirectedGNP(n, .2).edges(labels=False, sort=False):
            ....:      g.add_edge(u, v, ZZ.random_element(1,100000))
            sage: for u, v in digraphs.Circuit(n).edges(labels=False, sort=False):
            ....:      if not g.has_edge(u, v):
            ....:          g.add_edge(u, v, ZZ.random_element(1,100000))
            sage: v2 = g.traveling_salesman_problem(use_edge_labels=True)
            sage: v1 = g.traveling_salesman_problem(constraint_generation=False, use_edge_labels=True)
            sage: sum(v1.edge_labels()) == sum(v2.edge_labels())
            True

        Simple tests for multiple edges and loops::

            sage: G = DiGraph(multiedges=True, loops=True)
            sage: G.is_hamiltonian()
            False
            sage: G.add_vertex(0)
            sage: G.is_hamiltonian()
            False
            sage: G.add_edge(0, 0, 1)
            sage: G.add_edge(0, 0, 2)
            sage: tsp = G.traveling_salesman_problem(use_edge_labels=True)
            Traceback (most recent call last):
            ...
            EmptySetError: the given graph is not Hamiltonian
            sage: G.add_vertex(1)
            sage: G.is_hamiltonian()
            False
            sage: G.add_edge(0, 1, 2)
            sage: G.add_edge(0, 1, 3)
            sage: G.add_edge(1, 1, 1)
            sage: G.add_edge(1, 0, 2)
            sage: G.is_hamiltonian()
            True
            sage: tsp = G.traveling_salesman_problem(use_edge_labels=True)
            sage: sum(tsp.edge_labels())
            4

        Graphs on 2 vertices::

            sage: Graph([(0, 1), (0, 1)], multiedges=True).is_hamiltonian()
            True
            sage: DiGraph([(0, 1), (0, 1)], multiedges=True).is_hamiltonian()
            False
            sage: DiGraph([(0, 1), (1, 0)], multiedges=True).is_hamiltonian()
            True
            sage: G = digraphs.Complete(2, loops=True)
            sage: G.is_hamiltonian()
            True
            sage: G.remove_loops()
            sage: G.is_hamiltonian()
            True
            sage: G.allow_loops(False)
            sage: G.is_hamiltonian()
            True

        Check that weight 0 edges are handled correctly (see :trac:`16214`)::

            sage: G = Graph([(0, 1, 1), (0, 2, 0), (0, 3, 1), (1, 2, 1), (1, 3, 0), (2, 3, 1)])
            sage: tsp = G.traveling_salesman_problem(use_edge_labels=True)
            sage: sum(tsp.edge_labels())
            2
        """
        from sage.categories.sets_cat import EmptySetError

        # Associating a weight to a label
        if use_edge_labels:
            def weight(label):
                return 1 if label is None else label
        else:
            def weight(label):
                return 1

        ########################
        # 0 or 1 vertex graphs #
        ########################

        if self.order() < 2:
            raise EmptySetError("the given graph is not Hamiltonian")

        #####################
        # 2-vertices graphs #
        #####################

        if self.order() == 2:
            uu, vv = list(self)
            if self.is_directed():
                if self.has_edge(uu, vv) and self.has_edge(vv, uu):
                    if self.allows_multiple_edges():
                        if maximize:
                            edges = [(uu, vv, max(self.edge_label(uu, vv), key=weight)),
                                     (vv, uu, max(self.edge_label(vv, uu), key=weight))]
                        else:
                            edges = [(uu, vv, min(self.edge_label(uu, vv), key=weight)),
                                     (vv, uu, min(self.edge_label(vv, uu), key=weight))]
                    else:
                        edges = [(uu, vv, self.edge_label(uu, vv)),
                                 (vv, uu, self.edge_label(vv, uu))]
                    answer = self.subgraph(edges=edges, immutable=self.is_immutable())
                    answer.set_pos(self.get_pos())
                    answer.name("TSP from "+self.name())
                    return answer
            else:
                if self.allows_multiple_edges() and len(self.edge_label(uu, vv)) > 1:
                    if maximize:
                        edges = self.edges(sort=True, key=weight)[-2:]
                    else:
                        edges = self.edges(sort=True, key=weight)[:2]
                    answer = self.subgraph(edges=edges, immutable=self.is_immutable())
                    answer.set_pos(self.get_pos())
                    answer.name("TSP from " + self.name())
                    return answer

            raise EmptySetError("the given graph is not Hamiltonian")

        ################################
        # Quick checks of connectivity #
        ################################

        # TODO : Improve it by checking vertex-connectivity instead of
        # edge-connectivity.... But calling the vertex_connectivity (which
        # builds a LP) is way too slow. These tests only run traversals written
        # in Cython --> hence FAST

        if self.is_directed():
            if not self.is_strongly_connected():
                raise EmptySetError("the given graph is not Hamiltonian")

        else:
            # Checks whether the graph is 2-connected
            if not self.strong_orientation().is_strongly_connected():
                raise EmptySetError("the given graph is not Hamiltonian")

        ######################################
        # Deal with loops and multiple edges #
        ######################################

        if self.has_loops() or self.has_multiple_edges():
            keep_label = 'max' if (use_edge_labels and maximize) else 'min'
            g = self.to_simple(to_undirected=False, keep_label=keep_label, immutable=False)
        else:
            g = self

        if constraint_generation is None:
            if g.density() > .7:
                constraint_generation = False
            else:
                constraint_generation = True

        from sage.numerical.mip import MixedIntegerLinearProgram
        from sage.numerical.mip import MIPSolverException

        ####################################################
        # Constraint-generation formulation of the problem #
        ####################################################

        if constraint_generation:

            p = MixedIntegerLinearProgram(maximization=maximize,
                                          solver=solver,
                                          constraint_generation=True)

            # Directed Case #
            #################
            if g.is_directed():

                from sage.graphs.digraph import DiGraph
                b = p.new_variable(binary=True)

                # Objective function
                if use_edge_labels:
                    p.set_objective(p.sum(weight(l) * b[u, v] for u, v, l in g.edge_iterator()))

                # All the vertices have in-degree 1 and out-degree 1
                for v in g:
                    p.add_constraint(p.sum(b[u, v] for u in g.neighbor_in_iterator(v)),
                                     min=1, max=1)
                    p.add_constraint(p.sum(b[v, u] for u in g.neighbor_out_iterator(v)),
                                     min=1, max=1)

                # Initial Solve
                try:
                    p.solve(log=verbose)
                except MIPSolverException:
                    raise EmptySetError("the given graph is not Hamiltonian")

                while True:
                    # We build the DiGraph representing the current solution
                    h = DiGraph()
                    b_val = p.get_values(b, convert=bool, tolerance=integrality_tolerance)
                    for u, v, l in g.edge_iterator():
                        if b_val[u, v]:
                            h.add_edge(u, v, l)

                    # If there is only one circuit, we are done !
                    cc = h.connected_components(sort=False)
                    if len(cc) == 1:
                        break

                    # Adding the corresponding constraints
                    for c in cc:
                        if verbose_constraints:
                            print("Adding a constraint on set", c)
                        p.add_constraint(p.sum(b[u, v] for u, v in g.edge_boundary(c, labels=False)),
                                         min=1)

                    try:
                        p.solve(log=verbose)
                    except MIPSolverException:
                        raise EmptySetError("the given graph is not Hamiltonian")

            # Undirected Case #
            ###################
            else:

                from sage.graphs.graph import Graph
                b = p.new_variable(binary=True)

                # Objective function
                if use_edge_labels:
                    p.set_objective(p.sum(weight(l) * b[frozenset((u, v))] for u, v, l in g.edge_iterator()))

                # All the vertices have degree 2
                for v in g:
                    p.add_constraint(p.sum(b[frozenset((u, v))] for u in g.neighbor_iterator(v)),
                                     min=2, max=2)

                # Initial Solve
                try:
                    p.solve(log=verbose)
                except MIPSolverException:
                    raise EmptySetError("the given graph is not Hamiltonian")

                while True:
                    # We build the DiGraph representing the current solution
                    h = Graph()
                    b_val = p.get_values(b, convert=bool, tolerance=integrality_tolerance)
                    h.add_edges((u, v, l) for u, v, l in g.edge_iterator() if b_val[frozenset((u, v))])

                    # If there is only one circuit, we are done !
                    cc = h.connected_components(sort=False)
                    if len(cc) == 1:
                        break

                    # Adding the corresponding constraints
                    for c in cc:
                        if verbose_constraints:
                            print("Adding a constraint on set", c)
                        p.add_constraint(p.sum(b[frozenset((u, v))] for u, v in g.edge_boundary(c, labels=False)),
                                         min=2)

                    try:
                        p.solve(log=verbose)
                    except MIPSolverException:
                        raise EmptySetError("the given graph is not Hamiltonian")

            # We can now return the TSP !
            answer = self.subgraph(edges=h.edges(sort=False), immutable=self.is_immutable())
            answer.set_pos(self.get_pos())
            answer.name("TSP from "+g.name())
            return answer

        #################################################
        # ILP formulation without constraint generation #
        #################################################

        p = MixedIntegerLinearProgram(maximization=maximize, solver=solver)

        f = p.new_variable(binary=True)
        r = p.new_variable(nonnegative=True)

        eps = 1 / (2*Integer(g.order()))
        x = next(g.vertex_iterator())

        if g.is_directed():
            # All the vertices have in-degree 1 and out-degree 1
            for v in g:
                p.add_constraint(p.sum(f[u, v] for u in g.neighbor_in_iterator(v)),
                                 min=1, max=1)

                p.add_constraint(p.sum(f[v, u] for u in g.neighbor_out_iterator(v)),
                                 min=1, max=1)

            # r is greater than f
            vertex_to_int = {u: i for i, u in enumerate(g)}
            for u, v in g.edge_iterator(labels=None):
                if g.has_edge(v, u):
                    if vertex_to_int[u] < vertex_to_int[v]:
                        p.add_constraint(r[u, v] + r[v, u] - f[u, v] - f[v, u], min=0)

                        # no 2-cycles
                        p.add_constraint(f[u, v] + f[v, u], max=1)

                else:
                    p.add_constraint(r[u, v] + r[v, u] - f[u, v], min=0)

            if use_edge_labels:
                p.set_objective(p.sum(weight(l) * f[u, v] for u, v, l in g.edge_iterator()))

            # defining the answer when g is directed
            from sage.graphs.digraph import DiGraph
            tsp = DiGraph()

        else:
            # All the vertices have degree 2
            for v in g:
                p.add_constraint(p.sum(f[frozenset((u, v))] for u in g.neighbor_iterator(v)),
                                 min=2, max=2)

            # r is greater than f
            for u, v in g.edge_iterator(labels=None):
                p.add_constraint(r[u, v] + r[v, u] - f[frozenset((u, v))], min=0)

            if use_edge_labels:
                p.set_objective(p.sum(weight(l) * f[frozenset((u, v))] for u, v, l in g.edge_iterator()))

            from sage.graphs.graph import Graph

            # defining the answer when g is not directed
            tsp = Graph()

        # no cycle which does not contain x
        for v in g:
            if v != x:
                p.add_constraint(p.sum(r[u, v] for u in g.neighbor_iterator(v)), max=1 - eps)

        try:
            p.solve(log=verbose)
            f_val = p.get_values(f, convert=bool, tolerance=integrality_tolerance)
            tsp.add_vertices(g.vertex_iterator())
            tsp.set_pos(g.get_pos())
            tsp.name("TSP from " + g.name())
            if g.is_directed():
                tsp.add_edges((u, v, l) for u, v, l in g.edge_iterator() if f_val[u, v] == 1)
            else:
                tsp.add_edges((u, v, l) for u, v, l in g.edge_iterator() if f_val[frozenset((u, v))] == 1)

            return tsp

        except MIPSolverException:
            raise EmptySetError("the given graph is not Hamiltonian")

    def hamiltonian_cycle(self, algorithm='tsp', solver=None, constraint_generation=None,
                          verbose=0, verbose_constraints=False,
                          *, integrality_tolerance=1e-3):
        r"""
        Return a Hamiltonian cycle/circuit of the current graph/digraph.

        A graph (resp. digraph) is said to be Hamiltonian if it contains as a
        subgraph a cycle (resp. a circuit) going through all the vertices.

        Computing a Hamiltonian cycle/circuit being NP-Complete, this algorithm
        could run for some time depending on the instance.

        ALGORITHM:

        See :meth:`~GenericGraph.traveling_salesman_problem` for 'tsp'
        algorithm and
        :meth:`~sage.graphs.generic_graph_pyx.find_hamiltonian` from
        :mod:`sage.graphs.generic_graph_pyx` for 'backtrack' algorithm.

        INPUT:

        - ``algorithm`` -- string (default: ``'tsp'``); one of 'tsp' or
          'backtrack'

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``constraint_generation`` -- boolean (default: ``None``); whether to
          use constraint generation when solving the Mixed Integer Linear
          Program.

          When ``constraint_generation = None``, constraint generation is used
          whenever the graph has a density larger than 70%.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``verbose_constraints`` -- boolean (default: ``False``); whether to
          display which constraints are being generated

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        OUTPUT:

        If using the ``'tsp'`` algorithm, returns a Hamiltonian cycle/circuit if
        it exists; otherwise, raises a ``EmptySetError`` exception. If using the
        ``'backtrack'`` algorithm, returns a pair ``(B, P)``. If ``B`` is
        ``True`` then ``P`` is a Hamiltonian cycle and if ``B`` is ``False``,
        ``P`` is a longest path found by the algorithm. Observe that if ``B`` is
        ``False``, the graph may still be Hamiltonian.  The ``'backtrack'``
        algorithm is only implemented for undirected graphs.

        .. WARNING::

            The ``'backtrack'`` algorithm may loop endlessly on graphs with
            vertices of degree 1.

        NOTE:

        This function, as :meth:`is_hamiltonian`, computes a Hamiltonian cycle
        if it exists: the user should *NOT* test for Hamiltonicity using
        :meth:`is_hamiltonian` before calling this function, as it would result
        in computing it twice.

        The backtrack algorithm is only implemented for undirected graphs.

        EXAMPLES:

        The Heawood Graph is known to be Hamiltonian ::

            sage: g = graphs.HeawoodGraph()
            sage: g.hamiltonian_cycle()
            TSP from Heawood graph: Graph on 14 vertices

        The Petersen Graph, though, is not ::

            sage: g = graphs.PetersenGraph()
            sage: g.hamiltonian_cycle()
            Traceback (most recent call last):
            ...
            EmptySetError: the given graph is not Hamiltonian

        Now, using the backtrack algorithm in the Heawood graph ::

            sage: G=graphs.HeawoodGraph()
            sage: G.hamiltonian_cycle(algorithm='backtrack')
            (True, [...])

        And now in the Petersen graph ::

            sage: G=graphs.PetersenGraph()
            sage: B, P = G.hamiltonian_cycle(algorithm='backtrack')
            sage: B
            False
            sage: len(P)
            10
            sage: G.has_edge(P[0], P[-1])
            False

        Finally, we test the algorithm in a cube graph, which is Hamiltonian ::

            sage: G=graphs.CubeGraph(3)
            sage: G.hamiltonian_cycle(algorithm='backtrack')
            (True, [...])

        """
        if self.order() < 2:
            raise ValueError("the traveling salesman problem is not defined for empty or one-element graph")

        if algorithm == 'tsp':
            from sage.numerical.mip import MIPSolverException
            try:
                return self.traveling_salesman_problem(use_edge_labels=False, solver=solver,
                                                       constraint_generation=constraint_generation,
                                                       verbose=verbose, verbose_constraints=verbose_constraints,
                                                       integrality_tolerance=integrality_tolerance)
            except MIPSolverException:
                from sage.categories.sets_cat import EmptySetError
                raise EmptySetError("the given graph is not Hamiltonian")

        elif algorithm == 'backtrack':
            from sage.graphs.generic_graph_pyx import find_hamiltonian as fh
            return fh(self)

        else:
            raise ValueError("algorithm (%s) should be 'tsp' or 'backtrack'." % (algorithm))

    def feedback_vertex_set(self, value_only=False, solver=None, verbose=0,
                            constraint_generation=True, *, integrality_tolerance=1e-3):
        r"""
        Return the minimum feedback vertex set of a (di)graph.

        The minimum feedback vertex set of a (di)graph is a set of vertices that
        intersect all of its cycles.  Equivalently, a minimum feedback vertex
        set of a (di)graph is a set `S` of vertices such that the digraph `G-S`
        is acyclic. For more information, see the
        :wikipedia:`Feedback_vertex_set`.

        INPUT:

        - ``value_only`` -- boolean (default: ``False``); whether to return only
          the minimum cardinal of a minimum vertex set, or the ``Set`` of
          vertices of a minimal feedback vertex set

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``constraint_generation`` -- boolean (default: ``True``); whether to
          use constraint generation when solving the Mixed Integer Linear
          Program

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        ALGORITHMS:

        (Constraints generation)

        When the parameter ``constraint_generation`` is enabled (default) the
        following MILP formulation is used to solve the problem:

        .. MATH::

            \mbox{Minimize : }&\sum_{v\in G} b_{v}\\
            \mbox{Such that : }&\\
            &\forall C\text{ circuits }\subseteq G, \sum_{v\in C}b_{v}\geq 1\\

        As the number of circuits contained in a graph is exponential, this LP
        is solved through constraint generation. This means that the solver is
        sequentially asked to solve the problem, knowing only a portion of the
        circuits contained in `G`, each time adding to the list of its
        constraints the circuit which its last answer had left intact.

        (Another formulation based on an ordering of the vertices)

        When the graph is directed, a second (and very slow) formulation is
        available, which should only be used to check the result of the first
        implementation in case of doubt.

        .. MATH::

            \mbox{Minimize : }&\sum_{v\in G} b_v\\
            \mbox{Such that : }&\\
            &\forall (u,v)\in G, d_u-d_v+nb_u+nb_v\geq 0\\
            &\forall u\in G, 0\leq d_u\leq |G|\\

        A brief explanation:

        An acyclic digraph can be seen as a poset, and every poset has a linear
        extension. This means that in any acyclic digraph the vertices can be
        ordered with a total order `<` in such a way that if `(u,v)\in G`, then
        `u<v`.  Thus, this linear program is built in order to assign to each
        vertex `v` a number `d_v\in [0,\dots,n-1]` such that if there exists an
        edge `(u,v)\in G` then either `d_v<d_u` or one of `u` or `v` is removed.
        The number of vertices removed is then minimized, which is the
        objective.

        EXAMPLES:

        The necessary example::

            sage: g = graphs.PetersenGraph()
            sage: fvs = g.feedback_vertex_set()
            sage: len(fvs)
            3
            sage: g.delete_vertices(fvs)
            sage: g.is_forest()
            True

        In a digraph built from a graph, any edge is replaced by arcs going in
        the two opposite directions, thus creating a cycle of length two.
        Hence, to remove all the cycles from the graph, each edge must see one
        of its neighbors removed: a feedback vertex set is in this situation a
        vertex cover::

            sage: cycle = graphs.CycleGraph(5)
            sage: dcycle = DiGraph(cycle)
            sage: cycle.vertex_cover(value_only=True)
            3
            sage: feedback = dcycle.feedback_vertex_set()
            sage: len(feedback)
            3
            sage: u,v = next(cycle.edge_iterator(labels=None))
            sage: u in feedback or v in feedback
            True

        For a circuit, the minimum feedback arc set is clearly `1`::

            sage: circuit = digraphs.Circuit(5)
            sage: circuit.feedback_vertex_set(value_only=True) == 1
            True

        TESTS:

        Comparing with/without constraint generation::

            sage: g = digraphs.RandomDirectedGNP(10, .3)
            sage: x = g.feedback_vertex_set(value_only=True)
            sage: y = g.feedback_vertex_set(value_only=True,
            ....:          constraint_generation=False)
            sage: x == y
            True

        Bad algorithm::

            sage: g = graphs.PetersenGraph()
            sage: g.feedback_vertex_set(constraint_generation=False)
            Traceback (most recent call last):
            ...
            ValueError: the only implementation available for undirected graphs is with constraint_generation set to True
        """
        if not constraint_generation and not self.is_directed():
            raise ValueError("the only implementation available for "
                             "undirected graphs is with constraint_generation "
                             "set to True")

        # It would be a pity to start a LP if the graph is already acyclic
        if ((not self.is_directed() and self.is_forest()) or
                (self.is_directed() and self.is_directed_acyclic())):
            if value_only:
                return 0
            return []

        from sage.numerical.mip import MixedIntegerLinearProgram

        ########################################
        # Constraint Generation Implementation #
        ########################################
        if constraint_generation:

            p = MixedIntegerLinearProgram(constraint_generation=True,
                                          maximization=False, solver=solver)

            # A variable for each vertex
            b = p.new_variable(binary=True)

            # Variables are binary, and their coefficient in the objective is 1
            p.set_objective(p.sum(b[v] for v in self))

            # For as long as we do not break because the digraph is acyclic....
            while True:

                p.solve(log=verbose)

                # Building the graph without the vertices removed by the LP
                b_val = p.get_values(b, convert=bool, tolerance=integrality_tolerance)
                h = self.subgraph([v for v in self if not b_val[v]])

                # Is the graph acyclic ?
                if self.is_directed():
                    isok, certificate = h.is_directed_acyclic(certificate=True)
                else:
                    isok, certificate = h.is_forest(certificate=True)

                # If so, we are done !
                if isok:
                    if value_only:
                        return Integer(self.order() - h.order())
                    else:
                        return [v for v in self if b_val[v]]

                # There is a circuit left. Let's add the corresponding
                # constraint !
                while not isok:

                    p.add_constraint(p.sum(b[v] for v in certificate), min=1)
                    if verbose:
                        print("Adding a constraint on circuit: ", certificate)

                    # Let's search for a vertex disjoint circuit, if any
                    h.delete_vertices(certificate)
                    if self.is_directed():
                        isok, certificate = h.is_directed_acyclic(certificate=True)
                    else:
                        isok, certificate = h.is_forest(certificate=True)

        else:

            ######################################
            # Ordering-based MILP Implementation #
            ######################################

            p = MixedIntegerLinearProgram(maximization=False, solver=solver)

            b = p.new_variable(binary=True)
            d = p.new_variable(integer=True, nonnegative=True)
            n = self.order()

            # The removed vertices cover all the back arcs ( third condition )
            for u, v in self.edge_iterator(labels=None):
                p.add_constraint(d[u] - d[v] + n * (b[u] + b[v]), min=1)

            for u in self:
                p.add_constraint(d[u], max=n)

            p.set_objective(p.sum(b[v] for v in self))

            p.solve(log=verbose)
            b_sol = p.get_values(b, convert=bool, tolerance=integrality_tolerance)
            if value_only:
                return Integer(sum(1 for v in self if b_sol[v]))
            else:
                return [v for v in self if b_sol[v]]

    def flow(self, x, y, value_only=True, integer=False, use_edge_labels=True,
             vertex_bound=False, algorithm=None, solver=None, verbose=0,
             *, integrality_tolerance=1e-3):
        r"""
        Return a maximum flow in the graph from ``x`` to ``y``.

        The returned flow is represented by an optimal valuation of the edges.
        For more information, see the :wikipedia:`Max_flow`.

        As an optimization problem, is can be expressed this way :

        .. MATH::

            \mbox{Maximize : }&\sum_{e\in G.edges()} w_e b_e\\
            \mbox{Such that : }&\forall v \in G, \sum_{(u,v)\in G.edges()} b_{(u,v)}\leq 1\\
            &\forall x\in G, b_x\mbox{ is a binary variable}

        Observe that the integrality of the flow variables is automatic for all
        available solvers when all capacities are integers.

        INPUT:

        - ``x`` -- source vertex

        - ``y`` -- sink vertex

        - ``value_only`` -- boolean (default: ``True``); whether to return only
          the value of a maximal flow, or to also return a flow graph (a copy of
          the current graph, such that each edge has the flow using it as a
          label, the edges without flow being omitted)

        - ``integer`` -- boolean (default: ``True``); whether to compute an
          optimal solution under the constraint that the flow going through an
          edge has to be an integer, or without this constraint

        - ``use_edge_labels`` -- boolean (default: ``False``); whether to
          compute a maximum flow where each edge has a capacity defined by its
          label (if an edge has no label, capacity `1` is assumed), or to use
          default edge capacity of `1`

        - ``vertex_bound`` -- boolean (default: ``False``); when set to
          ``True``, sets the maximum flow leaving a vertex different from `x` to
          `1` (useful for vertex connectivity parameters)

        - ``algorithm`` -- string (default: ``None``); the algorithm to use
          among:

          * ``"FF"``, a Python implementation of the Ford-Fulkerson algorithm
            (only available when ``vertex_bound = False``)

          * ``"LP"``, the flow problem is solved using Linear Programming

          * ``"igraph"``, the ``igraph`` implementation of the Goldberg-Tarjan
            algorithm is used (only available when ``igraph`` is installed and
            ``vertex_bound = False``)

          When ``algorithm = None`` (default), we use ``LP`` if ``vertex_bound =
          True``, otherwise, we use ``igraph`` if it is available, ``FF`` if it
          is not available.

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

          Only useful when algorithm ``"LP"`` is used to solve the flow problem.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

          Only useful when algorithm ``"LP"`` is used to solve the flow problem.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

          Only useful when ``algorithm == "LP"`` and ``integer == True``.

        .. NOTE::

            Even though the three different implementations are meant to return
            the same Flow values, they cannot be expected to return the same
            Flow graphs.

            Besides, the use of Linear Programming may possibly mean a (slight)
            numerical noise.

        EXAMPLES:

        Two basic applications of the flow method for the ``PappusGraph`` and the
        ``ButterflyGraph`` with parameter `2` ::

           sage: g=graphs.PappusGraph()
           sage: int(g.flow(1,2))
           3

        ::

           sage: b=digraphs.ButterflyGraph(2)
           sage: int(b.flow(('00', 1), ('00', 2)))
           1

        The flow method can be used to compute a matching in a bipartite graph
        by linking a source `s` to all the vertices of the first set and linking
        a sink `t` to all the vertices of the second set, then computing
        a maximum `s-t` flow ::

            sage: g = DiGraph()
            sage: g.add_edges(('s', i) for i in range(4))
            sage: g.add_edges((i, 4 + j) for i in range(4) for j in range(4))
            sage: g.add_edges((4 + i, 't') for i in range(4))
            sage: [cardinal, flow_graph] = g.flow('s', 't', integer=True, value_only=False)
            sage: flow_graph.delete_vertices(['s', 't'])
            sage: flow_graph.size()
            4

        The undirected case::

            sage: g = Graph()
            sage: g.add_edges(('s', i) for i in range(4))
            sage: g.add_edges((i, 4 + j) for i in range(4) for j in range(4))
            sage: g.add_edges((4 + i, 't') for i in range(4))
            sage: [cardinal, flow_graph] = g.flow('s', 't', integer=True, value_only=False)
            sage: flow_graph.delete_vertices(['s', 't'])
            sage: flow_graph.size()
            4

        TESTS:

        An exception if raised when forcing "FF" or "igraph" with ``vertex_bound
        = True``::

            sage: g = graphs.PetersenGraph()
            sage: g.flow(0, 1, vertex_bound=True, algorithm="FF")
            Traceback (most recent call last):
            ...
            ValueError: this method does not support both vertex_bound=True and algorithm='FF'
            sage: g.flow(0, 1, vertex_bound=True, algorithm="igraph")
            Traceback (most recent call last):
            ...
            ValueError: this method does not support both vertex_bound=True and algorithm='igraph'

        Or if the method is different from the expected values::

            sage: g.flow(0, 1, algorithm="Divination")
            Traceback (most recent call last):
            ...
            ValueError: the algorithm argument has to be equal to either "FF", "LP", "igraph", or None

        The two algorithms are indeed returning the same results (possibly with
        some numerical noise, cf. :trac:`12362`)::

           sage: g = graphs.RandomGNP(20, .3)
           sage: for u, v in g.edge_iterator(labels=False):
           ....:    g.set_edge_label(u, v, round(random(), 5))
           sage: flow_ff = g.flow(0, 1, algorithm="FF")
           sage: flow_lp = g.flow(0, 1, algorithm="LP")
           sage: abs(flow_ff - flow_lp) < 0.01
           True
           sage: flow_igraph = g.flow(0, 1, algorithm="igraph") # optional python_igraph
           sage: abs(flow_ff - flow_igraph) < 0.00001           # optional python_igraph
           True
        """
        self._scream_if_not_simple(allow_loops=True)
        if vertex_bound and algorithm in ["FF", "igraph"]:
            raise ValueError("this method does not support both "
                             "vertex_bound=True and algorithm='" + algorithm + "'")
        if use_edge_labels:
            from sage.rings.real_mpfr import RR
            if integer:
                from math import floor

                def capacity(z):
                    return floor(z) if z in RR else 1
            else:
                def capacity(z):
                    return z if z in RR else 1
        else:
            def capacity(z):
                return 1

        if algorithm is None:
            if vertex_bound:
                algorithm = "LP"
            elif igraph_feature().is_present():
                algorithm = "igraph"
            else:
                algorithm = "FF"

        if (algorithm == "FF"):
            return self._ford_fulkerson(x, y, value_only=value_only, integer=integer, use_edge_labels=use_edge_labels)
        elif (algorithm == 'igraph'):
            vertices = list(self)
            x_int = vertices.index(x)
            y_int = vertices.index(y)
            if use_edge_labels:
                g_igraph = self.igraph_graph(vertex_list=vertices,
                                             edge_attrs={'capacity': [float(capacity(e[2]))
                                                                      for e in self.edge_iterator()]})
                maxflow = g_igraph.maxflow(x_int, y_int, 'capacity')
            else:
                g_igraph = self.igraph_graph(vertex_list=vertices)
                maxflow = g_igraph.maxflow(x_int, y_int)

            if value_only:
                return maxflow.value
            else:
                from sage.graphs.digraph import DiGraph
                flow_digraph = DiGraph()
                if self.is_directed():
                    for e in g_igraph.es():
                        f = maxflow.flow[e.index]
                        if f:
                            flow_digraph.add_edge(e.source, e.target, f)
                else:
                    # If the graph is undirected, the output of igraph is a list
                    # of weights: a positive weight means that the flow is from
                    # the vertex with minimum label to the vertex with maximum
                    # label, a negative weight means the converse.
                    for e in g_igraph.es():
                        f = maxflow.flow[e.index]
                        if (f > 0 and e.source < e.target) or (f < 0 and e.source > e.target):
                            flow_digraph.add_edge(e.source, e.target, abs(f))
                        elif f:
                            flow_digraph.add_edge(e.target, e.source, abs(f))
                flow_digraph.relabel({i: vertices[i] for i in flow_digraph})
                return [maxflow.value, flow_digraph]

        if algorithm != "LP":
            raise ValueError("the algorithm argument has to be equal to either "
                             "\"FF\", \"LP\", \"igraph\", or None")

        from sage.numerical.mip import MixedIntegerLinearProgram
        g = self
        p = MixedIntegerLinearProgram(maximization=True, solver=solver)
        flow = p.new_variable(integer=integer, nonnegative=True)
        obj = p.new_variable(integer=integer, nonnegative=True)

        if g.is_directed():
            # This function return the balance of flow at X
            def flow_sum(X):
                return (p.sum(flow[X, v] for u, v in g.outgoing_edge_iterator([X], labels=None))
                        - p.sum(flow[u, X] for u, v in g.incoming_edge_iterator([X], labels=None)))

            # The flow leaving x
            def flow_leaving(X):
                return p.sum(flow[uu, vv] for uu, vv in g.outgoing_edge_iterator([X], labels=None))

            # The flow to be considered when defining the capacity constraints
            def capacity_sum(u, v):
                return flow[u, v]

        else:
            # This function return the balance of flow at X
            def flow_sum(X):
                return p.sum(flow[X, v] - flow[v, X] for v in g[X])

            # The flow leaving x
            def flow_leaving(X):
                return p.sum(flow[X, vv] for vv in g[X])

            # The flow to be considered when defining the capacity constraints
            def capacity_sum(u, v):
                return flow[u, v] + flow[v, u]

        # Maximizes the flow leaving x
        p.add_constraint(flow_sum(x) == obj[0])
        p.set_objective(obj[0])

        # Elsewhere, the flow is equal to 0
        for v in g:
            if v != x and v != y:
                p.add_constraint(flow_sum(v), min=0, max=0)

        # Capacity constraints
        for u, v, w in g.edge_iterator():
            p.add_constraint(capacity_sum(u, v), max=capacity(w))

        # No vertex except the sources can send more than 1
        if vertex_bound:
            for v in g:
                if v != x and v != y:
                    p.add_constraint(flow_leaving(v), max=1)

        p.solve(log=verbose)

        # If integer is True, flow variables will be converted to integers.
        # Otherwise, the base ring of the MILP solver is used
        flow = p.get_values(flow, convert=True, tolerance=integrality_tolerance)

        if not integer and use_edge_labels is False:
            obj = p.get_values(obj[0], convert=ZZ, tolerance=integrality_tolerance)
        else:
            obj = p.get_values(obj[0], convert=True, tolerance=integrality_tolerance)

        if value_only:
            return obj

        # Builds a clean flow Draph
        flow_graph = g._build_flow_graph(flow, integer=integer)

        # Which could be a Graph
        if not self.is_directed():
            from sage.graphs.graph import Graph
            flow_graph = Graph(flow_graph)

        return [obj, flow_graph]

    def nowhere_zero_flow(self, k=None, solver=None, verbose=0, *, integrality_tolerance=1e-3):
        r"""
        Return a ``k``-nowhere zero flow of the (di)graph.

        A flow on a graph `G = (V, E)` is a pair `(D, f)` such that `D`
        is an orientation of `G` and `f` is a function on `E` satisfying

        .. MATH::

            \sum_{u \in N^-_D(v)} f(uv) = \sum_{w \in N^+_D(v)} f(vw),
            \ \forall v \in V.

        A ``nowhere zero flow`` on a graph `G = (V, E)` is a flow `(D, f)`
        such that `f(e) \neq 0` for every `e \in E`. For a positive
        integer `k`, a `k`-flow on a graph `G = (V, E)` is a flow `(D, f)`
        such that `f: E \to Z` and `-(k - 1) \leq f(e) \leq k - 1` for
        every `e \in E`. A `k`-flow is positive if `f(e) > 0` for every
        `e \in E`. A `k`-flow which is nowhere zero is called a
        `k`-*nowhere zero flow* (or `k`-NZF).

        The following are equivalent.

        - `G` admits a positive `k`-flow.
        - `G` admits a `k`-NZF.
        - Every orientation of `G` admits a `k`-NZF.

        Furthermore, a (di)graph admits a `k`-NZF if and only if it
        is bridgeless and every bridgeless graph admits a `6`-NZF [Sey1981]_.
        See the :wikipedia:`Nowhere-zero_flow` for more details.

        ALGORITHM:

        If ``self`` is not directed, we search for a `k`-NZF on any orientation
        of ``self`` and then build a positive `k`-NZF by reverting edges with
        negative flow.

        INPUT:

        - ``k`` -- integer (default: ``6``); when set to a positive integer
          `\geq 2`, search for a `k`-nowhere zero flow

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        OUTPUT:

        A digraph with flow values stored as edge labels if a `k`-nowhere zero
        flow is found. If ``self`` is undirected, the edges of this digraph
        indicate the selected orientation. If no feasible solution is found, an
        error is raised.

        EXAMPLES:

        The Petersen graph admits a (positive) 5-nowhere zero flow, but no
        4-nowhere zero flow::

            sage: g = graphs.PetersenGraph()
            sage: h = g.nowhere_zero_flow(k=5)
            sage: sorted(set(h.edge_labels()))
            [1, 2, 3, 4]
            sage: h = g.nowhere_zero_flow(k=3)
            Traceback (most recent call last):
            ...
            EmptySetError: the problem has no feasible solution

        The de Bruijn digraph admits a 2-nowhere zero flow::

            sage: g = digraphs.DeBruijn(2, 3)
            sage: h = g.nowhere_zero_flow(k=2)
            sage: sorted(set(h.edge_labels()))
            [-1, 1]

        TESTS:

        Empty graph::

            sage: G = Graph()
            sage: G.nowhere_zero_flow()
            Digraph on 0 vertices

        Graph with one vertex::

            sage: G = Graph([[1], []])
            sage: G
            Graph on 1 vertex
            sage: G.nowhere_zero_flow()
            Digraph on 1 vertex

        Loops and multiple edges::

            sage: g = Graph([(0, 0), (0, 0)], loops=True, multiedges=True)
            sage: g.nowhere_zero_flow().edges(sort=True)
            [(0, 0, 1), (0, 0, 1)]
            sage: g = Graph([(0, 0), (0, 1), (0, 1)], loops=True, multiedges=True)
            sage: g.nowhere_zero_flow(k=2).edges(sort=True)
            [(0, 0, 1), (0, 1, 1), (1, 0, 1)]
            sage: g = DiGraph([(0, 0), (0, 0)], loops=True, multiedges=True)
            sage: g.nowhere_zero_flow().edges(sort=True)
            [(0, 0, 1), (0, 0, 1)]
            sage: g = DiGraph([(0, 0), (0, 1), (0, 1)], loops=True, multiedges=True)
            sage: g.nowhere_zero_flow(k=2).edges(sort=True)
            [(0, 0, 1), (0, 1, -1), (0, 1, 1)]

        Multiple connected components::

            sage: g = graphs.CycleGraph(3) * 2
            sage: h = g.nowhere_zero_flow()
            sage: h.connected_components_sizes()
            [3, 3]

        (Di)Graphs with bridges::

            sage: g = graphs.PathGraph(2)
            sage: g.nowhere_zero_flow()
            Traceback (most recent call last):
            ...
            EmptySetError: (di)graphs with bridges have no feasible solution
            sage: g = digraphs.Path(2)
            sage: g.nowhere_zero_flow()
            Traceback (most recent call last):
            ...
            EmptySetError: (di)graphs with bridges have no feasible solution

        Too small value of ``k``::

            sage: Graph().nowhere_zero_flow(k=1)
            Traceback (most recent call last):
            ...
            ValueError: parameter 'k' must be at least 2
        """
        if k is None:
            k = 6  # See [Sey1981]_
        elif k < 2:
            raise ValueError("parameter 'k' must be at least 2")

        from sage.graphs.digraph import DiGraph
        from sage.categories.sets_cat import EmptySetError

        # If the (di)graph is not connected, we solve the problem on each
        #   of its connected components
        if not self.is_connected():
            solution = DiGraph(loops=self.allows_loops(),
                               multiedges=self.allows_multiple_edges())
            solution.add_vertices(self.vertex_iterator())
            for g in self.connected_components_subgraphs():
                solution.add_edges(g.nowhere_zero_flow(k=k, solver=solver,
                                                       verbose=verbose).edge_iterator())
            return solution

        # If the (di)graph has bridges, the problem is not feasible
        if ((self.is_directed() and not self.is_strongly_connected() and next(self.to_undirected().bridges(), False))
                or (not self.is_directed() and next(self.bridges(), False))):
            raise EmptySetError("(di)graphs with bridges have no feasible solution")

        #
        # We deal with loops and multiple edges, if any
        #
        if self.has_loops() or self.has_multiple_edges():
            G = copy(self) if self.is_directed() else next(self.orientations())

            # We assign flow 1 to loops, if any
            solution = DiGraph([list(G), [(u, v, 1) for u, v in G.loops(labels=False)]],
                               loops=G.has_loops(),
                               multiedges=G.has_multiple_edges())
            G.allow_loops(False)

            # We ensure that multiple edges have distinct labels
            multiedges = {(u, v, i) for i, (u, v) in enumerate(G.multiple_edges(labels=0))}
            G.delete_edges(G.multiple_edges())
            G.add_edges(multiedges)

        else:
            G = self if self.is_directed() else next(self.orientations())
            solution = DiGraph([list(G), []])

        if G.order() <= 1:
            return solution

        #
        # We use a MIP formulation to solve the problem
        #
        from sage.numerical.mip import MixedIntegerLinearProgram, MIPSolverException
        p = MixedIntegerLinearProgram(solver=solver)
        f = p.new_variable(nonnegative=False, integer=True)
        b = p.new_variable(nonnegative=True, binary=True)

        # flow conservation constraints
        for u in G:
            p.add_constraint(p.sum(f[e] for e in G.incoming_edge_iterator(u)) ==
                             p.sum(f[e] for e in G.outgoing_edge_iterator(u)))

        # The flow on edge e has value in {-k+1,..., -1, 1, ..., k-1}
        for e in G.edge_iterator():
            p.add_constraint(p.sum(b[e, i] for i in range(1 - k, k) if i) == 1)
            p.add_constraint(f[e] == p.sum(i * b[e, i] for i in range(1 - k, k) if i))

        # We solve the MIP.
        try:
            p.solve(log=verbose)
        except MIPSolverException:
            raise EmptySetError("the problem has no feasible solution")

        # Extract and return the solution. If the graph is not directed, we
        # reverse edges with a negative flow to obtain a positive k-NZF
        f_val = p.get_values(f, convert=True, tolerance=integrality_tolerance)
        for (u, v, _), val in f_val.items():
            if self.is_directed() or val > 0:
                solution.add_edge(u, v, val)
            else:
                solution.add_edge(v, u, -val)

        return solution

    def _ford_fulkerson(self, s, t, use_edge_labels=False, integer=False, value_only=True):
        r"""
        Python implementation of the Ford-Fulkerson algorithm.

        This method is a Python implementation of the Ford-Fulkerson max-flow
        algorithm, which is (slightly) faster than the LP implementation.

        INPUT:

        - ``s`` -- source vertex

        - ``t`` -- sink vertex

        - ``value_only`` -- boolean (default: ``True``); whether to return only
          the value of a maximal flow, or to also return a flow graph (a copy of
          the current graph, such that each edge has the flow using it as a
          label, the edges without flow being omitted)

        - ``integer`` -- boolean (default: ``True``); whether to compute an
          optimal solution under the constraint that the flow going through an
          edge has to be an integer, or without this constraint

        - ``use_edge_labels`` -- boolean (default: ``False``); whether to
          compute a maximum flow where each edge has a capacity defined by its
          label (if an edge has no label, capacity `1` is assumed), or to use
          default edge capacity of `1`

        EXAMPLES:

        Two basic applications of the flow method for the ``PappusGraph`` and the
        ``ButterflyGraph`` with parameter `2` ::

           sage: g = graphs.PappusGraph()
           sage: g._ford_fulkerson(1, 2)
           3

        ::

           sage: b=digraphs.ButterflyGraph(2)
           sage: b._ford_fulkerson(('00', 1), ('00', 2))
           1

        The flow method can be used to compute a matching in a bipartite graph
        by linking a source `s` to all the vertices of the first set and linking
        a sink `t` to all the vertices of the second set, then computing
        a maximum `s-t` flow ::

            sage: g = DiGraph()
            sage: g.add_edges(('s', i) for i in range(4))
            sage: g.add_edges((i, 4 + j) for i in range(4) for j in range(4))
            sage: g.add_edges((4 + i, 't') for i in range(4))
            sage: [cardinal, flow_graph] = g._ford_fulkerson('s', 't', integer=True, value_only=False)
            sage: flow_graph.delete_vertices(['s', 't'])
            sage: flow_graph.size()
            4

        TESTS:

        Graph with an isolated vertex (:trac:`24925`)::

            sage: G = Graph({0: [], 1: []})
            sage: G.flow(0, 1, algorithm='FF')
            0
            sage: G = Graph([[0, 1, 2], [(0, 1)]])
            sage: G.flow(0, 2, algorithm='FF')
            0
        """
        from sage.graphs.digraph import DiGraph
        from sage.arith.misc import integer_floor as floor

        # Whether we should consider the edges labeled
        if use_edge_labels:
            def l_capacity(x):
                return 1 if (x is None or x == {}) else (floor(x) if integer else x)
        else:
            def l_capacity(x):
                return 1

        directed = self.is_directed()

        # Associates to each edge (u,v) of the flow graph its capacity
        capacity = {}
        # Associates to each edge (u,v) of the graph the (directed) flow going
        # through it
        flow = {}

        # Residual graph. Only contains edge on which some flow can be
        # sent. This can happen both when the flow going through the current
        # edge is strictly less than its capacity, or when there exists a back
        # arc with non-null flow
        residual = DiGraph()
        residual.add_vertices(self)

        # Initializing the variables
        if directed:
            for u, v, l in self.edge_iterator():
                if l_capacity(l) > 0:
                    capacity[u, v] = l_capacity(l) + capacity.get((u, v), 0)
                    capacity[v, u] = capacity.get((v, u), 0)
                    residual.add_edge(u, v)
                    flow[u, v] = 0
                    flow[v, u] = 0
        else:
            for u, v, l in self.edge_iterator():
                if l_capacity(l) > 0:
                    capacity[u, v] = l_capacity(l) + capacity.get((u, v), 0)
                    capacity[v, u] = l_capacity(l) + capacity.get((v, u), 0)
                    residual.add_edge(u, v)
                    residual.add_edge(v, u)
                    flow[u, v] = 0
                    flow[v, u] = 0

        # Rewrites a path as a list of edges :
        # ex : [0,1,2,3,4,5] becomes [(0,1), (1,2), (2,3), (3,4), (4,5)]
        def path_to_edges(P):
            return zip(P[:-1], P[1:])

        # Rewrites a path as a list of edges labeled with their
        # available capacity
        def path_to_labelled_edges(P):
            return [(x_y[0], x_y[1], capacity[x_y[0], x_y[1]] - flow[x_y[0], x_y[1]] + flow[x_y[1], x_y[0]])
                    for x_y in path_to_edges(P)]

        # Total flow going from s to t
        flow_intensity = 0

        while True:

            # If there is a shortest path from s to t
            path = residual.shortest_path(s, t)
            if not path:
                break

            # We are rewriting the shortest path as a sequence of
            # edges whose labels are their available capacities
            edges = path_to_labelled_edges(path)

            # minimum capacity available on the whole path
            epsilon = min(x[2] for x in edges)

            flow_intensity = flow_intensity + epsilon

            # Updating variables
            for uu, vv, ll in edges:

                # The flow on the back arc
                other = flow[vv, uu]
                flow[uu, vv] = flow[uu, vv] + max(0, epsilon - other)
                flow[vv, uu] = other - min(other, epsilon)

                # If the current edge is fully used, we do not need it
                # anymore in the residual graph
                if capacity[uu, vv] - flow[uu, vv] + flow[vv, uu] == 0:
                    residual.delete_edge(uu, vv)

                # If the back arc does not exist, it now does as the
                # edge (uu,vv) has a flow of at least epsilon>0
                if not residual.has_edge(vv, uu):
                    residual.add_edge(vv, uu, epsilon)

        if value_only:
            return flow_intensity

        # Building and returning the flow graph
        g = DiGraph()
        g.add_edges((x, y, l) for (x, y), l in flow.items() if l > 0)
        g.set_pos(self.get_pos())

        return flow_intensity, g

    def multicommodity_flow(self, terminals, integer=True, use_edge_labels=False,
                            vertex_bound=False, solver=None, verbose=0,
                            *, integrality_tolerance=1e-3):
        r"""
        Solve a multicommodity flow problem.

        In the multicommodity flow problem, we are given a set of pairs `(s_i,
        t_i)`, called terminals meaning that `s_i` is willing some flow to
        `t_i`.

        Even though it is a natural generalisation of the flow problem this
        version of it is NP-Complete to solve when the flows are required to be
        integer.

        For more information, see the :wikipedia:`Multi-commodity_flow_problem`.

        INPUT:

        - ``terminals`` -- a list of pairs `(s_i, t_i)` or triples `(s_i, t_i,
          w_i)` representing a flow from `s_i` to `t_i` of intensity `w_i`. When
          the pairs are of size `2`, an intensity of `1` is assumed.

        - ``integer`` boolean (default: ``True``); whether to require an integer
          multicommodity flow

        - ``use_edge_labels`` -- boolean (default: ``False``); whether to
          compute a multicommodity flow where each edge has a capacity defined
          by its label (if an edge has no label, capacity `1` is assumed), or to
          use default edge capacity of `1`

        - ``vertex_bound`` -- boolean (default: ``False``); whether to require
          that a vertex can stand at most `1` commodity of flow through it of
          intensity `1`. Terminals can obviously still send or receive several
          units of flow even though ``vertex_bound`` is set to ``True``, as this
          parameter is meant to represent topological properties.

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

          Only useful when parameter ``ìnteger`` is ``True``.

        ALGORITHM:

        (Mixed Integer) Linear Program, depending on the value of ``integer``.

        EXAMPLES:

        An easy way to obtain a satisfiable multicommodity flow is to compute a
        matching in a graph, and to consider the paired vertices as terminals ::

            sage: g = graphs.PetersenGraph()
            sage: matching = [(u,v) for u,v,_ in g.matching()]
            sage: h = g.multicommodity_flow(matching)
            sage: len(h)
            5

        We could also have considered ``g`` as symmetric and computed the
        multicommodity flow in this version instead. In this case, however edges
        can be used in both directions at the same time::

            sage: h = DiGraph(g).multicommodity_flow(matching)
            sage: len(h)
            5

        An exception is raised when the problem has no solution ::

            sage: h = g.multicommodity_flow([(u,v,3) for u,v in matching])
            Traceback (most recent call last):
            ...
            EmptySetError: the multicommodity flow problem has no solution
        """
        self._scream_if_not_simple(allow_loops=True)
        from sage.numerical.mip import MixedIntegerLinearProgram
        g = self
        p = MixedIntegerLinearProgram(maximization=True, solver=solver)

        # Adding the intensity if not present
        terminals = [(x if len(x) == 3 else (x[0], x[1], 1)) for x in terminals]

        # defining the set of terminals
        set_terminals = set()
        for s, t, _ in terminals:
            set_terminals.add(s)
            set_terminals.add(t)

        # flow[i,(u,v)] is the flow of commodity i going from u to v
        flow = p.new_variable(nonnegative=True, integer=integer)

        # Whether to use edge labels
        if use_edge_labels:
            from sage.rings.real_mpfr import RR

            def capacity(x):
                return x if x in RR else 1
        else:
            def capacity(x):
                return 1

        if g.is_directed():
            # This function return the balance of flow at X
            def flow_sum(i, X):
                return (p.sum(flow[i, (X, v)] for u, v in g.outgoing_edge_iterator([X], labels=None))
                        - p.sum(flow[i, (u, X)] for u, v in g.incoming_edge_iterator([X], labels=None)))

            # The flow leaving x
            def flow_leaving(i, X):
                return p.sum(flow[i, (uu, vv)] for uu, vv in g.outgoing_edge_iterator([X], labels=None))

            # the flow to consider when defining the capacity constraints
            def capacity_sum(i, u, v):
                return flow[i, (u, v)]

        else:
            # This function return the balance of flow at X
            def flow_sum(i, X):
                return p.sum(flow[i, (X, v)] - flow[i, (v, X)] for v in g.neighbor_iterator(X))

            # The flow leaving x
            def flow_leaving(i, X):
                return sum(flow[i, (X, vv)] for vv in g.neighbor_iterator(X))

            # the flow to consider when defining the capacity constraints
            def capacity_sum(i, u, v):
                return flow[i, (u, v)] + flow[i, (v, u)]

        # Flow constraints
        for i, (s, t, l) in enumerate(terminals):
            for v in g:
                if v == s:
                    p.add_constraint(flow_sum(i, v), min=l, max=l)
                elif v == t:
                    p.add_constraint(flow_sum(i, v), min=-l, max=-l)
                else:
                    p.add_constraint(flow_sum(i, v), min=0, max=0)

        # Capacity constraints
        for u, v, w in g.edge_iterator():
            p.add_constraint(p.sum(capacity_sum(i, u, v) for i in range(len(terminals))), max=capacity(w))

        if vertex_bound:

            # Any vertex
            for v in g:

                # which is an endpoint
                if v in set_terminals:
                    for i, (s, t, _) in enumerate(terminals):

                        # only tolerates the commodities of which it is an endpoint
                        if not (v == s or v == t):
                            p.add_constraint(flow_leaving(i, v), max=0)

                # which is not an endpoint
                else:
                    # can stand at most 1 unit of flow through itself
                    p.add_constraint(p.sum(flow_leaving(i, v) for i in range(len(terminals))), max=1)

        p.set_objective(None)

        from sage.numerical.mip import MIPSolverException

        try:
            p.solve(log=verbose)
        except MIPSolverException:
            from sage.categories.sets_cat import EmptySetError
            raise EmptySetError("the multicommodity flow problem has no solution")

        # If integer is True, flow variables will be converted to integers.
        # Otherwise, the base ring of the MILP solver is used
        flow = p.get_values(flow, convert=True, tolerance=integrality_tolerance)

        # building clean flow digraphs
        flow_graphs = [g._build_flow_graph({e: f for (ii, e), f in flow.items() if ii == i}, integer=integer)
                       for i in range(len(terminals))]

        # which could be .. graphs !
        if not self.is_directed():
            from sage.graphs.graph import Graph
            flow_graphs = [Graph(_) for _ in flow_graphs]

        return flow_graphs

    def _build_flow_graph(self, flow, integer):
        r"""
        Build a "clean" flow graph

        This method first builds the flow graph, and then looks for circuits and
        removes them.

        INPUT:

        - ``flow`` -- a dictionary associating positive numerical values to
          edges

        - ``integer`` -- boolean; whether the values from ``flow`` are the
          solution of an integer flow. In this case, a value of less than .5 is
          assumed to be 0

        EXAMPLES:

        This method is tested in :meth:`flow` and :meth:`multicommodity_flow`::

            sage: g = Graph()
            sage: g.add_edge(0,1)
            sage: f = g._build_flow_graph({(0, 1): 1}, True)

        The method removes zero-cost flow cycles and updates the values
        accordingly::

            sage: g = digraphs.DeBruijn(2,3)
            sage: flow = {('001', '010'): 1, ('010', '100'): 1, ('010', '101'): 1, ('101', '010'): 1}
            sage: flow_graph = g._build_flow_graph(flow, True)
            sage: flow_graph.edges(sort=True)
            [('001', '010', 1), ('010', '100', 1)]
            sage: flow = {('001', '010'): 2, ('010', '101'): 3, ('101', '011'): 2, ('101', '010'): 1}
            sage: flow_graph = g._build_flow_graph(flow, True)
            sage: flow_graph.edges(sort=True)
            [('001', '010', 2), ('010', '101', 2), ('101', '011', 2)]

        Isolated zero-cost flow cycles are also removed::

            sage: g = digraphs.DeBruijn(2, 3)
            sage: flow = {('000', '001'): 1, ('010', '101'): 1, ('101', '010'): 1}
            sage: flow_graph = g._build_flow_graph(flow, True)
            sage: flow_graph.edges(sort=True)
            [('000', '001', 1)]
        """
        from sage.graphs.digraph import DiGraph
        g = DiGraph()

        # add significant edges
        for (u, v), l in flow.items():
            if l:
                g.add_edge(u, v, l)

        while True:
            # Check if the flow graph is acyclic
            is_acyclic, cycle = g.is_directed_acyclic(certificate=True)
            if is_acyclic:
                break

            # Find the minimum flow value along the cycle
            cycle.append(cycle[0])
            m = min(g.edge_label(u, v) for u, v in zip(cycle[:-1], cycle[1:]))

            # Remove it from all the edges of the cycle
            for u, v in zip(cycle[:-1], cycle[1:]):
                l = g.edge_label(u, v) - m

                # An edge with flow 0 is removed
                if not l:
                    g.delete_edge(u, v)
                else:
                    g.set_edge_label(u, v, l)

        # returning a graph with the same embedding, the corresponding name, etc ...
        h = self.subgraph(edges=[], immutable=False)
        h.delete_vertices(v for v in self if (v not in g) or not g.degree(v))
        h.add_edges(g.edge_iterator())

        return h

    def disjoint_routed_paths(self, pairs, solver=None, verbose=0,
                              *, integrality_tolerance=1e-3):
        r"""
        Return a set of disjoint routed paths.

        Given a set of pairs `(s_i,t_i)`, a set of disjoint routed paths is a
        set of `s_i-t_i` paths which can intersect at their endpoints and are
        vertex-disjoint otherwise.

        INPUT:

        - ``pairs`` -- list of pairs of vertices

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        EXAMPLES:

        Given a grid, finding two vertex-disjoint paths, the first one from the
        top-left corner to the bottom-left corner, and the second from the
        top-right corner to the bottom-right corner is easy::

            sage: g = graphs.Grid2dGraph(5, 5)
            sage: p1,p2 = g.disjoint_routed_paths([((0, 0), (0, 4)), ((4, 4), (4, 0))])

        Though there is obviously no solution to the problem in which each
        corner is sending information to the opposite one::

            sage: g = graphs.Grid2dGraph(5, 5)
            sage: p1,p2 = g.disjoint_routed_paths([((0, 0), (4, 4)), ((0, 4), (4, 0))])
            Traceback (most recent call last):
            ...
            EmptySetError: the disjoint routed paths do not exist
        """
        from sage.categories.sets_cat import EmptySetError
        try:
            return self.multicommodity_flow(pairs, integer=True, vertex_bound=True,
                                            solver=solver, verbose=verbose,
                                            integrality_tolerance=integrality_tolerance)
        except EmptySetError:
            raise EmptySetError("the disjoint routed paths do not exist")

    def edge_disjoint_paths(self, s, t, algorithm="FF", solver=None, verbose=False,
                            *, integrality_tolerance=1e-3):
        r"""
        Return a list of edge-disjoint paths between two vertices.

        The edge version of Menger's theorem asserts that the size of the
        minimum edge cut between two vertices `s` and`t` (the minimum number of
        edges whose removal disconnects `s` and `t`) is equal to the maximum
        number of pairwise edge-independent paths from `s` to `t`.

        This function returns a list of such paths.

        INPUT:

        - ``algorithm`` -- string (default: ``"FF"``); the algorithm to use
          among:

          * ``"FF"``, a Python implementation of the Ford-Fulkerson algorithm

          * ``"LP"``, the flow problem is solved using Linear Programming

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

          Only used when `àlgorithm`` is ``"LP"``.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

          Only used when `àlgorithm`` is ``"LP"``.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

          Only used when `àlgorithm`` is ``"LP"``.

        .. NOTE::

            This function is topological: it does not take the eventual weights
            of the edges into account.

        EXAMPLES:

        In a complete bipartite graph ::

            sage: g = graphs.CompleteBipartiteGraph(2, 3)
            sage: g.edge_disjoint_paths(0, 1)
            [[0, 2, 1], [0, 3, 1], [0, 4, 1]]
        """
        [obj, flow_graph] = self.flow(s, t, value_only=False, integer=True, use_edge_labels=False,
                                      algorithm=algorithm, solver=solver, verbose=verbose,
                                      integrality_tolerance=integrality_tolerance)

        paths = []

        while True:
            path = flow_graph.shortest_path(s, t)
            if not path:
                break
            edges = list(zip(path[:-1], path[1:]))
            flow_graph.delete_edges(edges)
            paths.append(path)

        return paths

    def vertex_disjoint_paths(self, s, t, solver=None, verbose=0,
                              *, integrality_tolerance=1e-3):
        r"""
        Return a list of vertex-disjoint paths between two vertices.

        The vertex version of Menger's theorem asserts that the size of the
        minimum vertex cut between two vertices `s` and `t` (the minimum number
        of vertices whose removal disconnects `s` and `t`) is equal to the
        maximum number of pairwise vertex-independent paths from `s` to `t`.

        This function returns a list of such paths.

        INPUT:

        - ``s,t`` -- two vertices of the graph.

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        EXAMPLES:

        In a complete bipartite graph ::

            sage: g = graphs.CompleteBipartiteGraph(2, 3)
            sage: g.vertex_disjoint_paths(0, 1)
            [[0, 2, 1], [0, 3, 1], [0, 4, 1]]

        TESTS:

        Fix issues reported in :trac:`22990`::

            sage: g = digraphs.Path(2)
            sage: g.vertex_disjoint_paths(0, 1)
            [[0, 1]]
            sage: g.vertex_disjoint_paths(1, 0)
            []
        """
        obj, flow_graph = self.flow(s, t, value_only=False, integer=True, use_edge_labels=False,
                                    vertex_bound=True, solver=solver, verbose=verbose,
                                    integrality_tolerance=integrality_tolerance)

        paths = []
        if not obj:
            return paths
        if flow_graph.has_edge(s, t):
            flow_graph.delete_edge(s, t)
            paths.append([s, t])

        while True:
            path = flow_graph.shortest_path(s, t)
            if not path:
                break
            flow_graph.delete_vertices(path[1:-1])
            paths.append(path)

        return paths

    def pagerank(self, alpha=0.85, personalization=None, by_weight=False,
                 weight_function=None, check_weight=True,
                 dangling=None, algorithm='scipy'):
        r"""
        Return the PageRank of the vertices of ``self``.

        PageRank is a centrality measure earlier used to rank web pages.
        The PageRank algorithm outputs the probability distribution that
        a random walker in the graph visits a vertex.

        See the :wikipedia:`PageRank` for more information.

        INPUT:

        - ``alpha`` -- float (default: ``0.85``); damping parameter for
          PageRank. ``alpha`` is the click-through probability useful for
          preventing sinks. The probability at any step, that an imaginary
          surfer who is randomly clicking on links will continue is a damping
          factor d.

        - ``personalization`` -- dict (default: ``None``); a dictionary keyed
          by vertices associating to each vertex a value. The personalization
          can be specified for a subset of the vertices, if not specified a
          nodes personalization value will be taken as zero. The sum of the
          values must be nonzero.
          By default (``None``), a uniform distribution is used.

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
          in the graph are weighted, otherwise all edges have weight 1

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l``, if ``l``
          is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); whether to check that
          the ``weight_function`` outputs a number for each edge.

        - ``dangling`` -- dict (default: ``None``); a dictionary keyed by a
          vertex the outedge of "dangling" vertices, (i.e., vertices without
          any outedges) points to and the dict value is the weight of that
          outedge. By default, dangling vertices are given outedges according
          to the personalization vector (uniform if not specified). It may be
          common to have the dangling dict to be the same as the personalization
          dict.

        - ``algorithm`` -- string (default: ``None``); the algorithm to use in
           computing PageRank of ``G``. The following algorithms are
           supported:

          - ``NetworkX`` -- uses NetworkX's default implementation (Scipy as of 2.6)

          - ``"Scipy"`` -- uses Scipy's PageRank algorithm implementation

          - ``"igraph"`` -- uses igraph's PageRank algorithm implementation

          - ``"None"`` -- uses best implementation available

        OUTPUT: a dictionary containing the PageRank value of each node

        .. NOTE::

            Parameters ``alpha``, ``by_weight`` and ``weight_function`` are common
            to all algorithms. Parameters ``personalization`` and ``dangling``
            are used only by algorithms ``NetworkX``, ``Numpy`` and ``Scipy``.

        EXAMPLES::

            sage: G = graphs.CycleGraph(4)
            sage: G.pagerank(algorithm="Networkx")
            {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25}
            sage: G.pagerank(alpha=0.50, algorithm="igraph")  # optional - python_igraph # abs tol 1e-9
            {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25}
            sage: G = Graph([(1, 2, 40), (2, 3, 50), (3, 4, 60), (1, 4, 70), (4, 5, 80), (5, 6, 20)])
            sage: G.pagerank(algorithm="NetworkX") # abs tol 1e-9
            {1: 0.16112205885619563,
             2: 0.1619531043247219,
             3: 0.16112205885619563,
             4: 0.2374999999999999,
             5: 0.17775588228760858,
             6: 0.100546895675278}
            sage: G.pagerank(algorithm="NetworkX", by_weight=True) # abs tol 1e-9
            {1: 0.16459583718588994,
             2: 0.13977928595154515,
             3: 0.16539840184339605,
             4: 0.3063198690713853,
             5: 0.1700057609707141,
             6: 0.05390084497706962}
            sage: G.pagerank(algorithm="Scipy") # abs tol 1e-9
            {1: 0.16112205885619563,
             2: 0.1619531043247219,
             3: 0.16112205885619563,
             4: 0.2374999999999999,
             5: 0.17775588228760858,
             6: 0.100546895675278}
            sage: G.pagerank(algorithm="Scipy", by_weight=True) # abs tol 1e-9
            {1: 0.16459583718588994,
             2: 0.13977928595154515,
             3: 0.16539840184339605,
             4: 0.3063198690713853,
             5: 0.1700057609707141,
             6: 0.05390084497706962}
            sage: G.pagerank(algorithm="igraph")  # optional - python_igraph # abs tol 1e-9
            {1: 0.16112198303979128,
             2: 0.16195368558382262,
             3: 0.16112198303979125,
             4: 0.23749999999999993,
             5: 0.17775603392041744,
             6: 0.10054631441617742}
            sage: G.pagerank() # abs tol 1e-9
            {1: 0.16112205885619563,
             2: 0.1619531043247219,
             3: 0.16112205885619563,
             4: 0.2374999999999999,
             5: 0.17775588228760858,
             6: 0.100546895675278}
            sage: G.pagerank(by_weight=True) # abs tol 1e-9
            {1: 0.16459583718588994,
             2: 0.13977928595154515,
             3: 0.16539840184339605,
             4: 0.3063198690713853,
             5: 0.1700057609707141,
             6: 0.05390084497706962}

        TESTS::

            sage: G = Graph([(1, 2), (2, 3), (3, 4), (1, 3)])
            sage: G.pagerank(algorithm="NetworkX", personalization={1:0, 2:3, 3:-2, 4:-1})
            Traceback (most recent call last):
            ...
            ZeroDivisionError...

        .. SEEALSO::

            * :wikipedia:`PageRank`

        """
        if not self.order():
            return {}

        by_weight, weight_function = self._get_weight_function(by_weight=by_weight,
                                                               weight_function=weight_function,
                                                               check_weight=check_weight)

        if by_weight:
            weight = "weight"
        else:
            weight = None

        if algorithm:
            algorithm = algorithm.lower()
        if algorithm == 'networkx' or algorithm == 'scipy':
            import networkx
            gnx = self.networkx_graph(weight_function=weight_function)
            return networkx.pagerank(gnx, alpha=alpha,
                                     personalization=personalization,
                                     weight=weight, dangling=dangling)
        elif algorithm == 'igraph':
            # An error will be raised if igraph is not installed
            if personalization:
                raise ValueError('personalization parameter is not used in igraph implementation')
            if dangling:
                raise ValueError('dangling parameter is not used in igraph implementation')
            if by_weight:
                I = self.igraph_graph(edge_attrs={'weight': [weight_function(e)
                                                  for e in self.edge_iterator()]})
            else:
                I = self.igraph_graph()
            page_rank = I.pagerank(damping=alpha, weights=weight)
            return {v: page_rank[i] for i, v in enumerate(self)}
        else:
            raise NotImplementedError("only 'NetworkX', 'Scipy', and 'igraph' are supported")

    # Vertex handlers

    def add_vertex(self, name=None):
        r"""
        Create an isolated vertex.

        If the vertex already exists, then nothing is done.

        INPUT:

        - ``name`` -- an immutable object (default: ``None``); when no name is
          specified (default), then the new vertex will be represented by the least
          integer not already representing a vertex. ``name`` must be an immutable
          object (e.g., an integer, a tuple, etc.).

        As it is implemented now, if a graph `G` has a large number of vertices
        with numeric labels, then ``G.add_vertex()`` could potentially be slow,
        if ``name=None``.

        OUTPUT:

        If ``name=None``, the new vertex name is returned. ``None`` otherwise.

        EXAMPLES::

            sage: G = Graph(); G.add_vertex(); G
            0
            Graph on 1 vertex

        ::

            sage: D = DiGraph(); D.add_vertex(); D
            0
            Digraph on 1 vertex

        """
        return self._backend.add_vertex(name)

    def add_vertices(self, vertices):
        """
        Add vertices to the (di)graph from an iterable container of vertices.

        Vertices that already exist in the graph will not be added again.

        INPUT:

        - ``vertices`` -- iterator container of vertex labels. A new label is
          created, used and returned in the output list for all ``None`` values
          in ``vertices``.

        OUTPUT:

        Generated names of new vertices if there is at least one ``None`` value
        present in ``vertices``. ``None`` otherwise.

        EXAMPLES::

            sage: d = {0: [1,4,5], 1: [2,6], 2: [3,7], 3: [4,8], 4: [9], 5: [7,8], 6: [8,9], 7: [9]}
            sage: G = Graph(d)
            sage: G.add_vertices([10,11,12])
            sage: G.vertices(sort=True)
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            sage: G.add_vertices(graphs.CycleGraph(25).vertex_iterator())
            sage: G.vertices(sort=True)
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

        ::

            sage: G = Graph()
            sage: G.add_vertices([1, 2, 3])
            sage: G.add_vertices([4, None, None, 5])
            [0, 6]

        """
        return self._backend.add_vertices(vertices)

    def delete_vertex(self, vertex, in_order=False):
        """
        Delete vertex, removing all incident edges.

        Deleting a non-existent vertex will raise an exception.

        INPUT:

        - ``in_order`` -- boolean (default: ``False``); if ``True``, this
          deletes the `i`-th vertex in the sorted list of vertices, i.e.
          ``G.vertices(sort=True)[i]``

        EXAMPLES::

            sage: G = Graph(graphs.WheelGraph(9))
            sage: G.delete_vertex(0); G.show()

        ::

            sage: D = DiGraph({0: [1, 2, 3, 4, 5], 1: [2], 2: [3], 3: [4], 4: [5], 5: [1]})
            sage: D.delete_vertex(0); D
            Digraph on 5 vertices
            sage: D.vertices(sort=True)
            [1, 2, 3, 4, 5]
            sage: D.delete_vertex(0)
            Traceback (most recent call last):
            ...
            ValueError: vertex (0) not in the graph

        ::

            sage: G = graphs.CompleteGraph(4).line_graph(labels=False)
            sage: G.vertices(sort=True)
            [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
            sage: G.delete_vertex(0, in_order=True)
            sage: G.vertices(sort=True)
            [(0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
            sage: G = graphs.PathGraph(5)
            sage: G.set_vertices({0: 'no delete', 1: 'delete'})
            sage: G.delete_vertex(1)
            sage: G.get_vertices()
            {0: 'no delete', 2: None, 3: None, 4: None}
            sage: G.get_pos()
            {0: (0, 0), 2: (2, 0), 3: (3, 0), 4: (4, 0)}

        TESTS:

        Test that :trac:`33759` is fixed::

            sage: G = Graph([(1, 4), (2, 3)])
            sage: G.is_planar(set_embedding=True)
            True
            sage: G.delete_vertex(3)
            sage: G.is_planar()
            True
        """
        if in_order:
            vertex = self.vertices(sort=True)[vertex]
        if vertex not in self:
            raise ValueError("vertex (%s) not in the graph" % str(vertex))

        # TODO: remove this update from this method which should be as fast
        # as possible
        try:
            assoc = self._assoc
        except AttributeError:
            assoc = None
        if assoc is not None:
            assoc.pop(vertex, None)

        # NOTE: we do not update _embedding, _pos or _pos3d as this is done in
        # the get_embedding and get_pos methods

        self._backend.del_vertex(vertex)

    def delete_vertices(self, vertices):
        """
        Delete vertices from the (di)graph taken from an iterable container of
        vertices.

        Deleting a non-existent vertex will raise an exception, in which case
        none of the vertices in ``vertices`` is deleted.


        EXAMPLES::

            sage: D = DiGraph({0: [1, 2, 3, 4, 5], 1: [2], 2: [3], 3: [4], 4: [5], 5: [1]})
            sage: D.delete_vertices([1, 2, 3, 4, 5]); D
            Digraph on 1 vertex
            sage: D.vertices(sort=False)
            [0]
            sage: D.delete_vertices([1])
            Traceback (most recent call last):
            ...
            ValueError: vertex (1) not in the graph

        TESTS:

        Test that :trac:`33759` is fixed::

            sage: G = Graph([(1, 4), (2, 3)])
            sage: G.is_planar(set_embedding=True)
            True
            sage: G.delete_vertices([3])
            sage: G.is_planar()
            True
        """
        vertices = list(vertices)
        for v in vertices:
            if v not in self:
                raise ValueError("vertex (%s) not in the graph" % str(v))

        # TODO: remove this update from this method which should be as fast
        # as possible
        try:
            assoc = self._assoc
        except AttributeError:
            assoc = None
        if assoc is not None:
            for v in vertices:
                assoc.pop(v, None)

        # NOTE: the _embedding, _pos and _pos3d attributes are modified directly
        # in get_embedding and get_pos methods

        self._backend.del_vertices(vertices)

    def has_vertex(self, vertex):
        """
        Check if ``vertex`` is one of the vertices of this graph.

        INPUT:

        - ``vertex`` -- the name of a vertex (see :meth:`add_vertex`)

        EXAMPLES::

            sage: g = Graph({0: [1, 2, 3], 2: [4]}); g
            Graph on 5 vertices
            sage: 2 in g
            True
            sage: 10 in g
            False
            sage: graphs.PetersenGraph().has_vertex(99)
            False
        """
        try:
            hash(vertex)
        except Exception:
            return False
        return self._backend.has_vertex(vertex)

    __contains__ = has_vertex

    def random_vertex(self, **kwds):
        r"""
        Return a random vertex of ``self``.

        INPUT:

        - ``**kwds`` -- arguments to be passed down to the
          :meth:`vertex_iterator` method

        EXAMPLES:

        The returned value is a vertex of self::

            sage: g = graphs.PetersenGraph()
            sage: v = g.random_vertex()
            sage: v in g
            True

        TESTS::

            sage: graphs.EmptyGraph().random_vertex()
            Traceback (most recent call last):
            ...
            ValueError: cannot get a random vertex from the empty graph
        """
        if not self.order():
            raise ValueError("cannot get a random vertex from the empty graph")
        from sage.misc.prandom import randint
        it = self.vertex_iterator(**kwds)
        for i in range(0, randint(0, self.order() - 1)):
            next(it)
        return next(it)

    def random_vertex_iterator(self, *args, **kwds):
        r"""
        Return an iterator over random vertices of ``self``.

        The returned iterator enables to amortize the cost of accessing random
        vertices, as can be done with multiple calls to method
        :meth:`random_vertex`.

        INPUT:

        - ``*args`` and ``**kwds`` -- arguments to be passed down to the
          :meth:`vertex_iterator` method

        EXAMPLES:

        The returned value is an iterator over the vertices of ``self``::

            sage: g = graphs.PetersenGraph()
            sage: it = g.random_vertex_iterator()
            sage: [next(it) in g for _ in range(5)]
            [True, True, True, True, True]

        TESTS:

        Empty Graph::

            sage: empty_graph = Graph()
            sage: list(empty_graph.random_vertex_iterator())
            []
            sage: it = empty_graph.random_vertex_iterator()
            sage: next(it)
            Traceback (most recent call last):
            ...
            StopIteration
        """
        from sage.misc.prandom import choice
        if self.order():
            V = list(self.vertex_iterator(*args, **kwds))
            while True:
                yield choice(V)

    def random_edge(self, **kwds):
        r"""
        Return a random edge of ``self``.

        INPUT:

        - ``**kwds`` -- arguments to be passed down to the :meth:`edge_iterator`
          method

        EXAMPLES:

        The returned value is an edge of ``self``::

            sage: g = graphs.PetersenGraph()
            sage: u,v = g.random_edge(labels=False)
            sage: g.has_edge(u,v)
            True

        As the :meth:`edges` method would, this function returns by default a
        triple ``(u, v, l)`` of values, in which ``l`` is the label of edge
        ``(u, v)``::

            sage: g.random_edge()  # random
            (3, 4, None)

        TESTS::

            sage: graphs.EmptyGraph().random_edge()
            Traceback (most recent call last):
            ...
            ValueError: cannot get a random edge from a graph without edges
        """
        if not self.size():
            raise ValueError("cannot get a random edge from a graph without edges")

        from sage.misc.prandom import randint
        it = self.edge_iterator(**kwds)
        for i in range(0, randint(0, self.size() - 1)):
            next(it)
        return next(it)

    def random_edge_iterator(self, *args, **kwds):
        r"""
        Return an iterator over random edges of ``self``.

        The returned iterator enables to amortize the cost of accessing random
        edges, as can be done with multiple calls to method :meth:`random_edge`.

        INPUT:

        - ``*args`` and ``**kwds`` -- arguments to be passed down to the
          :meth:`edge_iterator` method.

        EXAMPLES:

        The returned value is an iterator over the edges of ``self``::

            sage: g = graphs.PetersenGraph()
            sage: it = g.random_edge_iterator()
            sage: [g.has_edge(next(it)) for _ in range(5)]
            [True, True, True, True, True]

        As the :meth:`edges` method would, this function returns by default a
        triple ``(u, v, l)`` of values, in which ``l`` is the label of edge
        ``(u,v)``::

            sage: print(next(g.random_edge_iterator())) # random
            (0, 5, None)
            sage: print(next(g.random_edge_iterator(labels=False))) # random
            (5, 7)

        TESTS:

        Graph without edge::

            sage: empty_graph = Graph()
            sage: list(empty_graph.random_edge_iterator())
            []
            sage: it = empty_graph.random_edge_iterator()
            sage: next(it)
            Traceback (most recent call last):
            ...
            StopIteration
        """
        from sage.misc.prandom import choice
        if self.size():
            E = list(self.edge_iterator(*args, **kwds))
            while True:
                yield choice(E)

    def vertex_boundary(self, vertices1, vertices2=None):
        r"""
        Return a list of all vertices in the external boundary of ``vertices1``,
        intersected with ``vertices2``.

        If ``vertices2`` is ``None``, then ``vertices2`` is the complement of
        ``vertices1``. This is much faster if ``vertices1`` is smaller than
        ``vertices2``.

        The external boundary of a set of vertices is the union of the
        neighborhoods of each vertex in the set. Note that in this
        implementation, since ``vertices2`` defaults to the complement of
        ``vertices1``, if a vertex `v` has a loop, then ``vertex_boundary(v)``
        will not contain `v`.

        In a digraph, the external boundary of a vertex `v` are those vertices
        `u` with an arc `(v, u)`.

        EXAMPLES::

            sage: G = graphs.CubeGraph(4)
            sage: l = ['0111', '0000', '0001', '0011', '0010', '0101', '0100', '1111', '1101', '1011', '1001']
            sage: sorted(G.vertex_boundary(['0000', '1111'], l))
            ['0001', '0010', '0100', '0111', '1011', '1101']

        ::

            sage: D = DiGraph({0: [1, 2], 3: [0]})
            sage: D.vertex_boundary([0])
            [1, 2]

        TESTS:

        When ``vertices2`` is ``None``, then ``vertices2`` is the complement of
        ``vertices1``. Corrected in issue :trac:`20479`::

            sage: P = graphs.PathGraph(3)
            sage: P.vertex_boundary([0, 1])
            [2]
            sage: P.vertex_boundary([0, 1], set(P.vertex_iterator()).difference([0, 1]))
            [2]
            sage: Q = DiGraph(P)
            sage: Q.vertex_boundary([0, 1])
            [2]
            sage: Q.vertex_boundary([0, 1], set(Q.vertex_iterator()).difference([0, 1]))
            [2]
        """
        vertices1 = [v for v in vertices1 if v in self]
        output = set()
        if self._directed:
            for v in vertices1:
                output.update(self.neighbor_out_iterator(v))
        else:
            for v in vertices1:
                output.update(self.neighbor_iterator(v))
        if vertices2 is None:
            output.difference_update(vertices1)
        else:
            output.intersection_update(vertices2)
        return list(output)

    def set_vertices(self, vertex_dict):
        """
        Associate arbitrary objects with each vertex, via an association
        dictionary.

        INPUT:

        - ``vertex_dict`` -- the association dictionary

        EXAMPLES::

            sage: d = {0: graphs.DodecahedralGraph(), 1: graphs.FlowerSnark(), 2: graphs.MoebiusKantorGraph(), 3: graphs.PetersenGraph()}
            sage: d[2]
            Moebius-Kantor Graph: Graph on 16 vertices
            sage: T = graphs.TetrahedralGraph()
            sage: T.vertices(sort=True)
            [0, 1, 2, 3]
            sage: T.set_vertices(d)
            sage: T.get_vertex(1)
            Flower Snark: Graph on 20 vertices
        """
        if hasattr(self, '_assoc') is False:
            self._assoc = {}

        self._assoc.update(vertex_dict)

    def set_vertex(self, vertex, object):
        """
        Associate an arbitrary object with a vertex.

        INPUT:

        - ``vertex`` -- which vertex

        - ``object`` -- object to associate to vertex


        EXAMPLES::

            sage: T = graphs.TetrahedralGraph()
            sage: T.vertices(sort=True)
            [0, 1, 2, 3]
            sage: T.set_vertex(1, graphs.FlowerSnark())
            sage: T.get_vertex(1)
            Flower Snark: Graph on 20 vertices
            sage: T.set_vertex(4, 'foo')
            Traceback (most recent call last):
            ...
            ValueError: vertex (4) not in the graph
        """
        if not self.has_vertex(vertex):
            raise ValueError('vertex (%s) not in the graph' % str(vertex))

        try:
            assoc = self._assoc
        except AttributeError:
            assoc = self._assoc = {}

        assoc[vertex] = object

    def get_vertex(self, vertex):
        """
        Retrieve the object associated with a given vertex.

        If no associated object is found, ``None`` is returned.

        INPUT:

        - ``vertex`` -- the given vertex

        EXAMPLES::

            sage: d = {0: graphs.DodecahedralGraph(), 1: graphs.FlowerSnark(), 2: graphs.MoebiusKantorGraph(), 3: graphs.PetersenGraph()}
            sage: d[2]
            Moebius-Kantor Graph: Graph on 16 vertices
            sage: T = graphs.TetrahedralGraph()
            sage: T.vertices(sort=True)
            [0, 1, 2, 3]
            sage: T.set_vertices(d)
            sage: T.get_vertex(1)
            Flower Snark: Graph on 20 vertices
        """
        if hasattr(self, '_assoc') is False:
            return None

        return self._assoc.get(vertex, None)

    def get_vertices(self, verts=None):
        """
        Return a dictionary of the objects associated to each vertex.

        INPUT:

        - ``verts`` -- iterable container of vertices

        EXAMPLES::

            sage: d = {0: graphs.DodecahedralGraph(), 1: graphs.FlowerSnark(), 2: graphs.MoebiusKantorGraph(), 3: graphs.PetersenGraph()}
            sage: T = graphs.TetrahedralGraph()
            sage: T.set_vertices(d)
            sage: T.get_vertices([1, 2])
            {1: Flower Snark: Graph on 20 vertices,
             2: Moebius-Kantor Graph: Graph on 16 vertices}
        """
        if verts is None:
            verts = list(self)

        if not hasattr(self, '_assoc'):
            return dict.fromkeys(verts, None)

        return {v: self._assoc.get(v, None) for v in verts}

    def vertex_iterator(self, vertices=None, degree=None, vertex_property=None):
        """
        Return an iterator over the given vertices.

        Returns ``False`` if not given a vertex, sequence, iterator or
        ``None``. ``None`` is equivalent to a list of every vertex. Note that
        ``for v in G`` syntax is allowed.

        INPUT:

        - ``vertices`` -- iterated vertices are these intersected with the
          vertices of the (di)graph

        - ``degree`` -- a nonnegative integer (default: ``None``);
          a vertex ``v`` is kept if ``degree(v) == degree``

        - ``vertex_property`` -- function (default: ``None``); a function
          that inputs a vertex and outputs a boolean value, i.e., a vertex
          ``v`` is kept if ``vertex_property(v) == True``

        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: for v in P.vertex_iterator():
            ....:     print(v)
            0
            1
            2
            ...
            8
            9

        ::

            sage: G = graphs.TetrahedralGraph()
            sage: for i in G:
            ....:     print(i)
            0
            1
            2
            3

        ::

            sage: H = graphs.PathGraph(5)
            sage: prop = lambda l: l % 3 == 1
            sage: for v in H.vertex_iterator(degree=1, vertex_property=prop):
            ....:     print(v)
            4

        Note that since the intersection option is available, the
        vertex_iterator() function is sub-optimal, speed-wise, but note the
        following optimization::

            sage: timeit V = P.vertices(sort=False)         # not tested
            100000 loops, best of 3: 8.85 [micro]s per loop
            sage: timeit V = list(P.vertex_iterator())      # not tested
            100000 loops, best of 3: 5.74 [micro]s per loop
        """
        if degree:
            if vertex_property is not None:
                for v, d in self.degree_iterator(labels=True):
                    if d == degree and vertex_property(v):
                        yield v
            else:
                for v, d in self.degree_iterator(labels=True):
                    if d == degree:
                        yield v

        elif vertex_property is not None:
            for v in self._backend.iterator_verts(vertices):
                if vertex_property(v):
                    yield v

        else:
            yield from self._backend.iterator_verts(vertices)

    __iter__ = vertex_iterator

    def neighbor_iterator(self, vertex, closed=False):
        """
        Return an iterator over neighbors of ``vertex``.

        When ``closed`` is set to ``True``, the returned iterator also
        contains ``vertex``.

        INPUT:

        - ``vertex`` -- a vertex of ``self``

        - ``closed`` -- a boolean (default: ``False``); whether to
          return the closed neighborhood of ``vertex``, i.e., including
          ``vertex``, or the open neighborhood in which ``vertex``
          is included only if there is a loop on that vertex.

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: for i in G.neighbor_iterator(0):
            ....:     print(i)
            1
            4
            5
            sage: D = G.to_directed()
            sage: for i in D.neighbor_iterator(0):
            ....:     print(i)
            1
            4
            5

        ::

            sage: D = DiGraph({0: [1, 2], 3: [0]})
            sage: sorted(D.neighbor_iterator(0))
            [1, 2, 3]

        ::

            sage: g = graphs.CubeGraph(3)
            sage: sorted(g.neighbor_iterator('010', closed=True))
            ['000', '010', '011', '110']

        ::

            sage: g = Graph(3, loops = True)
            sage: g.add_edge(0,1)
            sage: g.add_edge(0,0)
            sage: list(g.neighbor_iterator(0, closed=True))
            [0, 1]
            sage: list(g.neighbor_iterator(2, closed=True))
            [2]

        TESTS::

            sage: G = graphs.CubeGraph(3)
            sage: list(G.neighbor_iterator('013', closed=True))
            Traceback (most recent call last):
            ...
            LookupError: vertex (013) is not a vertex of the graph
        """

        if closed:
            if not self.has_vertex(vertex):
                raise LookupError(
                    'vertex ({0}) is not a vertex of the graph'.format(vertex))
            if not self.has_edge(vertex, vertex):
                yield vertex

        for u in self._backend.iterator_nbrs(vertex):
            yield u

    def vertices(self, sort=None, key=None, degree=None, vertex_property=None):
        r"""
        Return a list of the vertices.

        INPUT:

        - ``sort`` -- boolean (default: ``None``); if ``True``, vertices are
          sorted according to the default ordering

          As of :trac:`22349`, this argument must be explicitly
          specified (unless a ``key`` is given); otherwise a warning
          is printed and ``sort=True`` is used. The default will
          eventually be changed to ``False``.

        - ``key`` -- a function (default: ``None``); a function that takes a
          vertex as its one argument and returns a value that can be used for
          comparisons in the sorting algorithm (we must have ``sort=True``)

        - ``degree`` -- a nonnegative integer (default: ``None``);
          a vertex ``v`` is kept if ``degree(v) == degree``

        - ``vertex_property`` -- function (default: ``None``); a function
          that inputs a vertex and outputs a boolean value, i.e., a vertex
          ``v`` is kept if ``vertex_property(v) == True``

        OUTPUT:

        The list of vertices of the (di)graph.

        .. WARNING::

            Since any object may be a vertex, there is no guarantee that any two
            vertices will be comparable. With default objects for vertices (all
            integers), or when all the vertices are of the same simple type,
            then there should not be a problem with how the vertices will be
            sorted.  However, if you need to guarantee a total order for the
            sorting of the edges, use the ``key`` argument, as illustrated in
            the examples below.


        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: P.vertices(sort=True)
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        If you do not care about sorted output and you are concerned about the
        time taken to sort, consider the following alternative::

            sage: timeit V = P.vertices(sort=True)            # not tested
            625 loops, best of 3: 3.86 [micro]s per loop
            sage: timeit V = P.vertices(sort=False)           # not tested
            625 loops, best of 3: 2.06 [micro]s per loop
            sage: timeit V = list(P.vertex_iterator())        # not tested
            625 loops, best of 3: 2.05 [micro]s per loop
            sage: timeit('V = list(P)')                       # not tested
            625 loops, best of 3: 1.98 [micro]s per loop

        We illustrate various ways to use a ``key`` to sort the list::

            sage: H = graphs.HanoiTowerGraph(3, 3, labels=False)
            sage: H.vertices(sort=True)
            [0, 1, 2, 3, 4, ... 22, 23, 24, 25, 26]
            sage: H.vertices(sort=True, key=lambda x: -x)
            [26, 25, 24, 23, 22, ... 4, 3, 2, 1, 0]

        ::

            sage: G = graphs.HanoiTowerGraph(3, 3)
            sage: G.vertices(sort=True)
            [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), ... (2, 2, 1), (2, 2, 2)]
            sage: G.vertices(sort=True, key = lambda x: (x[1], x[2], x[0]))
            [(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 0, 1), ... (1, 2, 2), (2, 2, 2)]

        The discriminant of a polynomial is a function that returns an integer.
        We build a graph whose vertices are polynomials, and use the
        discriminant function to provide an ordering. Note that since functions
        are first-class objects in Python, we can specify precisely the function
        from the Sage library that we wish to use as the key::

            sage: t = polygen(QQ, 't')
            sage: K = Graph({5*t: [t^2], t^2: [t^2+2], t^2+2: [4*t^2-6], 4*t^2-6: [5*t]})
            sage: dsc = sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_flint.discriminant
            sage: verts = K.vertices(sort=True, key=dsc)
            sage: verts
            [t^2 + 2, t^2, 5*t, 4*t^2 - 6]
            sage: [x.discriminant() for x in verts]
            [-8, 0, 1, 96]

        TESTS:

        When parameter ``key`` is set, parameter ``sort`` must be ``True``::

            sage: G = Graph(2)
            sage: G.vertices(sort=False, key=lambda x: x)
            Traceback (most recent call last):
            ...
            ValueError: sort keyword is False, yet a key function is given

        Deprecation warning for ``sort=None`` (:trac:`22349`)::

            sage: G = graphs.HouseGraph()
            sage: G.vertices()
            doctest:...: DeprecationWarning: parameter 'sort' will be set to False by default in the future
            See https://github.com/sagemath/sage/issues/22349 for details.
            [0, 1, 2, 3, 4]
        """
        if sort is None:
            if key is None:
                deprecation(22349, "parameter 'sort' will be set to False by default in the future")
            sort = True

        if (not sort) and key:
            raise ValueError('sort keyword is False, yet a key function is given')

        if sort:
            return sorted(self.vertex_iterator(degree=degree, vertex_property=vertex_property), key=key)
        return list(self.vertex_iterator(degree=degree, vertex_property=vertex_property))

    def neighbors(self, vertex, closed=False):
        """
        Return a list of neighbors (in and out if directed) of ``vertex``.

        ``G[vertex]`` also works.
        When ``closed`` is set to ``True``, the returned iterator also
        contains ``vertex``.

        INPUT:

        - ``vertex`` -- a vertex of ``self``

        - ``closed`` -- a boolean (default: ``False``); whether to
          return the closed neighborhood of ``vertex``, i.e., including
          ``vertex``, or the open neighborhood in which ``vertex``
          is included only if there is a loop on that vertex.

        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: sorted(P.neighbors(3))
            [2, 4, 8]
            sage: sorted(P[4])
            [0, 3, 9]
            sage: sorted(P.neighbors(3, closed=True))
            [2, 3, 4, 8]
        """
        return list(self.neighbor_iterator(vertex, closed))

    __getitem__ = neighbors

    def merge_vertices(self, vertices):
        r"""
        Merge vertices.

        This function replaces a set `S` of vertices by a single vertex
        `v_{new}`, such that the edge `uv_{new}` exists if and only if
        `\exists v'\in S: (u,v')\in G`.

        The new vertex is named after the first vertex in the list given in
        argument. If this first name is `None`, a new vertex is created.

        In the case of multigraphs, the multiplicity is preserved.

        INPUT:

        - ``vertices`` -- the list of vertices to be merged

        .. NOTE::

            If ``u`` and ``v`` are distinct vertices in ``vertices``, any edges
            between ``u`` and ``v`` will be lost.

        EXAMPLES::

            sage: g = graphs.CycleGraph(3)
            sage: g.merge_vertices([0, 1])
            sage: g.edges(sort=True)
            [(0, 2, None)]

            sage: P = graphs.PetersenGraph()
            sage: P.merge_vertices([5, 7])
            sage: P.vertices(sort=True)
            [0, 1, 2, 3, 4, 5, 6, 8, 9]

        When the first vertex in ``vertices`` is ``None``, a new vertex is
        created::

            sage: g = graphs.CycleGraph(5)
            sage: g.vertices(sort=True)
            [0, 1, 2, 3, 4]
            sage: g.merge_vertices([None, 1, 3])
            sage: g.edges(sort=True, labels=False)
            [(0, 4), (0, 5), (2, 5), (4, 5)]

        With a Multigraph ::

            sage: g = graphs.CycleGraph(3)
            sage: g.allow_multiple_edges(True)
            sage: g.merge_vertices([0, 1])
            sage: g.edges(sort=True, labels=False)
            [(0, 2), (0, 2)]

        TESTS:

        Check that :trac:`23290` was fixed::

            sage: edgelist = [(0, 0, 'a'), (0, 1, 'b'), (1, 1, 'c')]
            sage: G = Graph(edgelist, loops=True, multiedges=True)
            sage: G.merge_vertices([0, 1]); G.edges(sort=True)
            [(0, 0, 'a'), (0, 0, 'c')]
            sage: D = DiGraph(edgelist, loops=True, multiedges=True)
            sage: D.merge_vertices([0, 1]); D.edges(sort=True)
            [(0, 0, 'a'), (0, 0, 'c')]

        Without multiedges::

            sage: edgelist = [(0, 0, 'a'), (0, 1, 'b'), (1, 1, 'c')]
            sage: G = Graph(edgelist, loops=True, multiedges=False)
            sage: G.merge_vertices([0, 1]); G.edges(sort=True)
            [(0, 0, 'c')]
            sage: edgelist = [(0, 0, 'a'), (0, 1, 'b'), (1, 1, 'c'), (1, 2, 'd'), (2, 2, 'e')]
            sage: G = Graph(edgelist, loops=True, multiedges=False)
            sage: G.merge_vertices([0, 1, 2]); G.edges(sort=True)
            [(0, 0, 'e')]
            sage: G = Graph(edgelist, loops=True, multiedges=False)
            sage: G.merge_vertices([0, 2, 1]); G.edges(sort=True)
            [(0, 0, 'c')]

        """
        if len(vertices) <= 1:
            return None
        if vertices[0] is None:
            vertices[0] = self.add_vertex()

        u = vertices[0]
        if self.allows_loops():
            for v in vertices[1:]:
                if self.has_edge(v, v):
                    if self.allows_multiple_edges():
                        for l in self.edge_label(v, v):
                            self.add_edge(u, u, l)
                    else:
                        self.add_edge(u, u, self.edge_label(v, v))

        if self.is_directed():
            out_edges = self.edge_boundary(vertices)
            in_edges = self.edge_boundary([v for v in self
                                           if v not in vertices])
            self.delete_vertices(vertices[1:])
            self.add_edges((u, v0, l) for (u0, v0, l) in out_edges if u0 != u)
            self.add_edges((v0, u, l) for (v0, u0, l) in in_edges if u0 != u)
        else:
            edges = self.edge_boundary(vertices)
            self.delete_vertices(vertices[1:])
            add_edges = []
            for u0, v0, l in edges:
                if v0 in vertices and v0 != u:
                    add_edges.append((u, u0, l))
                if u0 in vertices and u0 != u:
                    add_edges.append((u, v0, l))
            self.add_edges(add_edges)

    # Edge handlers

    def add_edge(self, u, v=None, label=None):
        r"""
        Add an edge from ``u`` to ``v``.

        INPUT: The following forms are all accepted:

        - G.add_edge( 1, 2 )
        - G.add_edge( (1, 2) )
        - G.add_edges( [ (1, 2) ])
        - G.add_edge( 1, 2, 'label' )
        - G.add_edge( (1, 2, 'label') )
        - G.add_edges( [ (1, 2, 'label') ] )

        WARNING: The following intuitive input results in nonintuitive output::

            sage: G = Graph()
            sage: G.add_edge((1, 2), 'label')
            sage: G.edges(sort=False)
            [('label', (1, 2), None)]

        You must either use the ``label`` keyword::

            sage: G = Graph()
            sage: G.add_edge((1, 2), label="label")
            sage: G.edges(sort=False)
            [(1, 2, 'label')]

        Or use one of these::

            sage: G = Graph()
            sage: G.add_edge(1, 2, 'label')
            sage: G.edges(sort=False)
            [(1, 2, 'label')]
            sage: G = Graph()
            sage: G.add_edge((1, 2, 'label'))
            sage: G.edges(sort=False)
            [(1, 2, 'label')]

        Vertex name cannot be ``None``, so::

            sage: G = Graph()
            sage: G.add_edge(None, 4)
            sage: G.vertices(sort=True)
            [0, 4]
        """
        if label is None:
            if v is None:
                try:
                    u, v, label = u
                except Exception:
                    try:
                        u, v = u
                    except Exception:
                        pass
        else:
            if v is None:
                try:
                    u, v = u
                except Exception:
                    pass

        self._backend.add_edge(u, v, label, self._directed)

    def add_edges(self, edges, loops=True):
        """
        Add edges from an iterable container.

        INPUT:

        - ``edges`` -- an iterable of edges, given either as ``(u, v)``
          or ``(u, v, label)``.

        - ``loops`` -- boolean (default: ``True``); if ``False``, remove all
          loops ``(v, v)`` from the input iterator. If ``None``, remove loops
          unless the graph allows loops.

        EXAMPLES::

            sage: G = graphs.DodecahedralGraph()
            sage: H = Graph()
            sage: H.add_edges(G.edge_iterator()); H
            Graph on 20 vertices
            sage: G = graphs.DodecahedralGraph().to_directed()
            sage: H = DiGraph()
            sage: H.add_edges(G.edge_iterator()); H
            Digraph on 20 vertices
            sage: H.add_edges(iter([]))

            sage: H = Graph()
            sage: H.add_edges([(0, 1), (0, 2, "label")])
            sage: H.edges(sort=True)
            [(0, 1, None), (0, 2, 'label')]

        We demonstrate the ``loops`` argument::

            sage: H = Graph()
            sage: H.add_edges([(0, 0)], loops=False); H.edges(sort=True)
            []
            sage: H.add_edges([(0, 0)], loops=None); H.edges(sort=True)
            []
            sage: H.add_edges([(0, 0)]); H.edges(sort=True)
            Traceback (most recent call last):
            ...
            ValueError: cannot add edge from 0 to 0 in graph without loops
            sage: H = Graph(loops=True)
            sage: H.add_edges([(0, 0)], loops=False); H.edges(sort=True)
            []
            sage: H.add_edges([(0, 0)], loops=None); H.edges(sort=True)
            [(0, 0, None)]
            sage: H.add_edges([(0, 0)]); H.edges(sort=True)
            [(0, 0, None)]

        TESTS::

            sage: H.add_edges([(0,1,2,3)])
            Traceback (most recent call last):
            ...
            ValueError: too many values to unpack (expected 2)
            sage: H.add_edges([1234])
            Traceback (most recent call last):
            ...
            TypeError: object of type 'sage.rings.integer.Integer' has no len()
        """
        if loops is None:
            loops = self.allows_loops()
        self._backend.add_edges(edges, self._directed, remove_loops=not loops)

    def subdivide_edge(self, *args):
        r"""
        Subdivide an edge `k` times.

        INPUT:

        The following forms are all accepted to subdivide `8` times the edge
        between vertices `1` and `2` labeled with ``"my_label"``.

        - ``G.subdivide_edge( 1, 2, 8 )``
        - ``G.subdivide_edge( (1, 2), 8 )``
        - ``G.subdivide_edge( (1, 2, "my_label"), 8 )``

        .. NOTE::

            * If the given edge is labelled with `l`, all the edges created by
              the subdivision will have the same label

            * If no label is given, the label used will be the one returned by
              the method :meth:`edge_label` on the pair ``u,v``

        EXAMPLES:

        Subdividing `5` times an edge in a path of length `3` makes it a path of
        length `8`::

            sage: g = graphs.PathGraph(3)
            sage: edge = next(g.edge_iterator())
            sage: g.subdivide_edge(edge, 5)
            sage: g.is_isomorphic(graphs.PathGraph(8))
            True

        Subdividing a labelled edge in two ways::

            sage: g = Graph()
            sage: g.add_edge(0, 1, "label1")
            sage: g.add_edge(1, 2, "label2")
            sage: print(g.edges(sort=True))
            [(0, 1, 'label1'), (1, 2, 'label2')]

        Specifying the label::

            sage: g.subdivide_edge(0, 1, "label1", 3)
            sage: print(g.edges(sort=True))
            [(0, 3, 'label1'), (1, 2, 'label2'), (1, 5, 'label1'), (3, 4, 'label1'), (4, 5, 'label1')]

        The lazy way::

            sage: g.subdivide_edge(1, 2, "label2", 5)
            sage: print(g.edges(sort=True))
            [(0, 3, 'label1'), (1, 5, 'label1'), (1, 6, 'label2'),
             (2, 10, 'label2'), (3, 4, 'label1'), (4, 5, 'label1'),
             (6, 7, 'label2'), (7, 8, 'label2'), (8, 9, 'label2'),
             (9, 10, 'label2')]

        If too many arguments are given, an exception is raised ::

            sage: g.subdivide_edge(0,1,1,1,1,1,1,1,1,1,1)
            Traceback (most recent call last):
            ...
            ValueError: this method takes at most 4 arguments

        The same goes when the given edge does not exist::

            sage: g.subdivide_edge(0, 1, "fake_label", 5)
            Traceback (most recent call last):
            ...
            ValueError: the given edge does not exist

        .. SEEALSO::

            - :meth:`subdivide_edges` -- subdivides multiples edges at a time

        TESTS:

        :trac:`15895` is fixed::

            sage: F = graphs.PathGraph(3)
            sage: S = 'S'; F.add_vertex(S)
            sage: F.add_edge(S, 0)
            sage: F2 = Graph(F)
            sage: F2.subdivide_edges(list(F2.edge_iterator(labels=False)), 2)
            sage: 0 in F2.degree()
            False
        """
        if len(args) == 2:
            edge, k = args

            if len(edge) == 2:
                u, v = edge
                l = self.edge_label(u, v)
            elif len(edge) == 3:
                u, v, l = edge

        elif len(args) == 3:
            u, v, k = args
            l = self.edge_label(u, v)

        elif len(args) == 4:
            u, v, l, k = args

        else:
            raise ValueError("this method takes at most 4 arguments")

        if not self.has_edge(u, v, l):
            raise ValueError("the given edge does not exist")

        new_verts = [self.add_vertex() for i in range(k)]

        self.delete_edge(u, v, l)

        edges = []
        for uu in new_verts + [v]:
            edges.append((u, uu, l))
            u = uu

        self.add_edges(edges)

    def subdivide_edges(self, edges, k):
        r"""
        Subdivide `k` times edges from an iterable container.

        For more information on the behaviour of this method, please refer to
        the documentation of :meth:`subdivide_edge`.

        INPUT:

        - ``edges`` -- a list of edges

        - ``k`` -- integer; common length of the subdivisions

        .. NOTE::

            If a given edge is labelled with `l`, all the edges created by its
            subdivision will have the same label.

        EXAMPLES:

        If we are given the disjoint union of several paths::

            sage: paths = [2, 5, 9]
            sage: paths = map(graphs.PathGraph, paths)
            sage: g = Graph()
            sage: for P in paths:
            ....:   g = g + P

        Subdividing edges in each of them will only change their lengths::

            sage: edges = [next(P.edge_iterator()) for P in g.connected_components_subgraphs()]
            sage: k = 6
            sage: g.subdivide_edges(edges, k)

        Let us check this by creating the graph we expect to have built through
        subdivision::

            sage: paths2 = [2 + k, 5 + k, 9 + k]
            sage: paths2 = map(graphs.PathGraph, paths2)
            sage: g2 = Graph()
            sage: for P in paths2:
            ....:   g2 = g2 + P
            sage: g.is_isomorphic(g2)
            True

        .. SEEALSO::

            - :meth:`subdivide_edge` -- subdivides one edge
        """
        if isinstance(edges, EdgesView):
            edges = tuple(edges)
        for e in edges:
            self.subdivide_edge(e, k)

    def delete_edge(self, u, v=None, label=None):
        r"""
        Delete the edge from ``u`` to ``v``.

        This method returns silently if vertices or edge does not
        exist.

        INPUT: The following forms are all accepted:

        - G.delete_edge( 1, 2 )
        - G.delete_edge( (1, 2) )
        - G.delete_edges( [ (1, 2) ] )
        - G.delete_edge( 1, 2, 'label' )
        - G.delete_edge( (1, 2, 'label') )
        - G.delete_edges( [ (1, 2, 'label') ] )

        EXAMPLES::

            sage: G = graphs.CompleteGraph(9)
            sage: G.size()
            36
            sage: G.delete_edge( 1, 2 )
            sage: G.delete_edge( (3, 4) )
            sage: G.delete_edges( [ (5, 6), (7, 8) ] )
            sage: G.size()
            32

        ::

            sage: G.delete_edge( 2, 3, 'label' )
            sage: G.delete_edge( (4, 5, 'label') )
            sage: G.delete_edges( [ (6, 7, 'label') ] )
            sage: G.size()
            32
            sage: G.has_edge( (4, 5) ) # correct!
            True
            sage: G.has_edge( (4, 5, 'label') ) # correct!
            False

        ::

            sage: C = digraphs.Complete(9)
            sage: C.size()
            72
            sage: C.delete_edge( 1, 2 )
            sage: C.delete_edge( (3, 4) )
            sage: C.delete_edges( [ (5, 6), (7, 8) ] )
            sage: C.size()
            68

        ::

            sage: C.delete_edge( 2, 3, 'label' )
            sage: C.delete_edge( (4, 5, 'label') )
            sage: C.delete_edges( [ (6, 7, 'label') ] )
            sage: C.size() # correct!
            68
            sage: C.has_edge( (4, 5) ) # correct!
            True
            sage: C.has_edge( (4, 5, 'label') ) # correct!
            False

        """
        if label is None:
            if v is None:
                try:
                    u, v, label = u
                except Exception:
                    u, v = u
                    label = None

        self._backend.del_edge(u, v, label, self._directed)

    def delete_edges(self, edges):
        """
        Delete edges from an iterable container.

        EXAMPLES::

            sage: K12 = graphs.CompleteGraph(12)
            sage: K4 = graphs.CompleteGraph(4)
            sage: K12.size()
            66
            sage: K12.delete_edges(K4.edge_iterator())
            sage: K12.size()
            60

        ::

            sage: K12 = digraphs.Complete(12)
            sage: K4 = digraphs.Complete(4)
            sage: K12.size()
            132
            sage: K12.delete_edges(K4.edge_iterator())
            sage: K12.size()
            120
        """
        self._backend.del_edges(edges, self._directed)

    def contract_edge(self, u, v=None, label=None):
        r"""
        Contract an edge from ``u`` to ``v``.

        This method returns silently if the edge does not exist.

        INPUT: The following forms are all accepted:

        - G.contract_edge( 1, 2 )
        - G.contract_edge( (1, 2) )
        - G.contract_edge( [ (1, 2) ] )
        - G.contract_edge( 1, 2, 'label' )
        - G.contract_edge( (1, 2, 'label') )
        - G.contract_edge( [ (1, 2, 'label') ] )

        EXAMPLES::

            sage: G = graphs.CompleteGraph(4)
            sage: G.contract_edge((0, 1)); G.edges(sort=True)
            [(0, 2, None), (0, 3, None), (2, 3, None)]
            sage: G = graphs.CompleteGraph(4)
            sage: G.allow_loops(True); G.allow_multiple_edges(True)
            sage: G.contract_edge((0, 1)); G.edges(sort=True)
            [(0, 2, None), (0, 2, None), (0, 3, None), (0, 3, None), (2, 3, None)]
            sage: G.contract_edge((0, 2)); G.edges(sort=True)
            [(0, 0, None), (0, 3, None), (0, 3, None), (0, 3, None)]

        ::

            sage: G = graphs.CompleteGraph(4).to_directed()
            sage: G.allow_loops(True)
            sage: G.contract_edge(0, 1); G.edges(sort=True)
            [(0, 0, None),
             (0, 2, None),
             (0, 3, None),
             (2, 0, None),
             (2, 3, None),
             (3, 0, None),
             (3, 2, None)]

        TESTS:

        Make sure loops don't get lost::

            sage: edgelist = [(0, 0, 'a'), (0, 1, 'b'), (1, 1, 'c')]
            sage: G = Graph(edgelist, loops=True, multiedges=True)
            sage: G.contract_edge(0, 1, 'b'); G.edges(sort=True)
            [(0, 0, 'a'), (0, 0, 'c')]
            sage: D = DiGraph(edgelist, loops=True, multiedges=True)
            sage: D.contract_edge(0, 1, 'b'); D.edges(sort=True)
            [(0, 0, 'a'), (0, 0, 'c')]

        With labeled edges::

            sage: G = graphs.CompleteGraph(4)
            sage: G.allow_loops(True); G.allow_multiple_edges(True)
            sage: for e in G.edges(sort=False):
            ....:     G.set_edge_label(e[0], e[1], (e[0] + e[1]))
            sage: G.contract_edge(0, 1); G.edges(sort=True)
            [(0, 2, 2), (0, 2, 3), (0, 3, 3), (0, 3, 4), (2, 3, 5)]
            sage: G.contract_edge(0, 2, 4); G.edges(sort=True)
            [(0, 2, 2), (0, 2, 3), (0, 3, 3), (0, 3, 4), (2, 3, 5)]
        """
        # standard code to allow 3 arguments or a single tuple:
        if label is None:
            if v is None:
                try:
                    u, v, label = u
                except Exception:
                    u, v = u
                    label = None
        # unlike delete_edge(), we must be careful about contracting non-edges
        if not self.has_edge(u, v, label):
            return
        self.delete_edge(u, v, label)
        # if the edge was a loop, stop
        # this could potentially leave isolated vertices
        if u == v:
            return

        if (self.allows_loops() and
                (self.allows_multiple_edges() or not self.has_edge(u, u))):
            # add loops
            for x, y, l in self.edges_incident(v):
                if set([x, y]) == set([u, v]):
                    self.add_edge(u, u, l)

        self.merge_vertices([u, v])

    def contract_edges(self, edges):
        r"""
        Contract edges from an iterable container.

        If `e` is an edge that is not contracted but the vertices of `e` are
        merged by contraction of other edges, then `e` will become a loop.

        INPUT:

        - ``edges`` -- a list containing 2-tuples or 3-tuples that represent
          edges

        EXAMPLES::

            sage: G = graphs.CompleteGraph(4)
            sage: G.allow_loops(True); G.allow_multiple_edges(True)
            sage: G.contract_edges([(0, 1), (1, 2), (0, 2)]); G.edges(sort=True)
            [(0, 3, None), (0, 3, None), (0, 3, None)]
            sage: G.contract_edges([(1, 3), (2, 3)]); G.edges(sort=True)
            [(0, 3, None), (0, 3, None), (0, 3, None)]
            sage: G = graphs.CompleteGraph(4)
            sage: G.allow_loops(True); G.allow_multiple_edges(True)
            sage: G.contract_edges([(0, 1), (1, 2), (0, 2), (1, 3), (2, 3)]); G.edges(sort=True)
            [(0, 0, None)]

        ::

            sage: D = digraphs.Complete(4)
            sage: D.allow_loops(True); D.allow_multiple_edges(True)
            sage: D.contract_edges([(0, 1), (1, 0), (0, 2)]); D.edges(sort=True)
            [(0, 0, None),
             (0, 0, None),
             (0, 0, None),
             (0, 3, None),
             (0, 3, None),
             (0, 3, None),
             (3, 0, None),
             (3, 0, None),
             (3, 0, None)]

        TESTS:

        With non-edges in the input::

            sage: G = graphs.BullGraph(); G.add_edge(3, 4); G.edges(sort=True)
            [(0, 1, None),
             (0, 2, None),
             (1, 2, None),
             (1, 3, None),
             (2, 4, None),
             (3, 4, None)]
            sage: G.contract_edges([(1, 3), (1, 4)]); G.edges(sort=True)
            [(0, 1, None), (0, 2, None), (1, 2, None), (1, 4, None), (2, 4, None)]

        With loops in a digraph::

            sage: D = DiGraph([(0, 0), (0, 1), (1, 1)], loops=True, multiedges=True)
            sage: D.contract_edges([(1, 0)]); D.edges(sort=True)
            [(0, 0, None), (0, 1, None), (1, 1, None)]
            sage: D.contract_edges([(0, 1)]); D.edges(sort=True)
            [(0, 0, None), (0, 0, None)]

        ::

            sage: edgelist = [(0, 1, 0), (0, 1, 1), (0, 1, 2)]
            sage: G = Graph(edgelist, loops=True, multiedges=True)
            sage: G.contract_edges([(0, 1), (0, 1, 2)]); G.edges(sort=True)
            Traceback (most recent call last):
            ...
            ValueError: edge tuples in input should have the same length

        ::

            sage: G = graphs.CompleteGraph(4)
            sage: G.allow_loops(True); G.allow_multiple_edges(True)
            sage: for e in G.edges(sort=False):
            ....:     G.set_edge_label(e[0], e[1], (e[0] + e[1]))
            sage: H = G.copy()
            sage: G.contract_edges([(0, 1), (0, 2)]); G.edges(sort=True)
            [(0, 0, 3), (0, 3, 3), (0, 3, 4), (0, 3, 5)]
            sage: H.contract_edges([(0, 1, 1), (0, 2, 3)]); H.edges(sort=True)
            [(0, 2, 2), (0, 2, 3), (0, 3, 3), (0, 3, 4), (2, 3, 5)]
        """
        if len(set(len(e) for e in edges)) > 1:
            raise ValueError("edge tuples in input should have the same length")
        edge_list = []
        vertices = set()
        for e in edges:
            # try to get the vertices and label of e as distinct variables
            try:
                u, v, label = e
            except Exception:
                u, v = e
                label = None
            if self.has_edge(u, v, label):
                edge_list.append((u, v, label))
                vertices.add(u)
                vertices.add(v)
        if not edge_list:
            return

        # implementation of union_find using DisjointSet
        from sage.sets.disjoint_set import DisjointSet
        DS = DisjointSet(self.vertex_iterator())

        for u, v, label in edge_list:
            DS.union(u, v)

        self.delete_edges(edge_list)
        edges_incident = []
        vertices = [v for v in vertices if v != DS.find(v)]
        if self.is_directed():
            for v in vertices:
                out_edges = self.edge_boundary([v])
                edges_incident.extend(out_edges)
                edges_incident.extend(self.incoming_edge_iterator(v))
                self.delete_vertex(v)
        else:
            for v in vertices:
                edges_incident.extend(self.edges_incident(v, sort=False))
                self.delete_vertex(v)

        for (u, v, label) in edges_incident:
            root_u = DS.find(u)
            root_v = DS.find(v)
            if root_v != root_u or self.allows_loops():
                self.add_edge(root_u, root_v, label)

    def delete_multiedge(self, u, v):
        r"""
        Delete all edges from ``u`` to ``v``.

        EXAMPLES::

            sage: G = Graph(multiedges=True, sparse=True)
            sage: G.add_edges([(0, 1), (0, 1), (0, 1), (1, 2), (2, 3)])
            sage: G.edges(sort=True)
            [(0, 1, None), (0, 1, None), (0, 1, None), (1, 2, None), (2, 3, None)]
            sage: G.delete_multiedge(0, 1)
            sage: G.edges(sort=True)
            [(1, 2, None), (2, 3, None)]

        ::

            sage: D = DiGraph(multiedges=True, sparse=True)
            sage: D.add_edges([(0, 1, 1), (0, 1, 2), (0, 1, 3), (1, 0, None), (1, 2, None), (2, 3, None)])
            sage: D.edges(sort=True)
            [(0, 1, 1), (0, 1, 2), (0, 1, 3), (1, 0, None), (1, 2, None), (2, 3, None)]
            sage: D.delete_multiedge(0, 1)
            sage: D.edges(sort=True)
            [(1, 0, None), (1, 2, None), (2, 3, None)]
        """
        if self.allows_multiple_edges():
            for l in self.edge_label(u, v):
                self.delete_edge(u, v, l)
        else:
            self.delete_edge(u, v)

    def set_edge_label(self, u, v, l):
        """
        Set the edge label of a given edge.

        .. NOTE::

           There can be only one edge from u to v for this to make
           sense. Otherwise, an error is raised.

        INPUT:

        - ``u, v`` -- the vertices (and direction if digraph) of the edge

        -  ``l`` -- the new label

        EXAMPLES::

            sage: d = {1: [18, 2], 2: [5, 3], 3: [4, 6], 4: [7, 2], 5: [4],
            ....:      6: [13, 12], 7: [18, 8, 10], 8: [6, 9, 10], 9: [6],
            ....:      10: [11, 13], 11: [12], 12: [13], 13: [17, 14],
            ....:      14: [16, 15], 15: [2], 16: [13], 17: [15, 13], 18: [13]}
            sage: SD = DiGraph(d, sparse=True)
            sage: SD.set_edge_label(1, 18, 'discrete')
            sage: SD.set_edge_label(4, 7, 'discrete')
            sage: SD.set_edge_label(2, 5, 'h = 0')
            sage: SD.set_edge_label(7, 18, 'h = 0')
            sage: SD.set_edge_label(7, 10, 'aut')
            sage: SD.set_edge_label(8, 10, 'aut')
            sage: SD.set_edge_label(8, 9, 'label')
            sage: SD.set_edge_label(8, 6, 'no label')
            sage: SD.set_edge_label(13, 17, 'k > h')
            sage: SD.set_edge_label(13, 14, 'k = h')
            sage: SD.set_edge_label(17, 15, 'v_k finite')
            sage: SD.set_edge_label(14, 15, 'v_k m.c.r.')
            sage: posn = {1: [3, -3], 2: [0, 2], 3: [0, 13], 4: [3, 9],
            ....:         5: [3, 3], 6: [16, 13], 7: [6, 1], 8: [6, 6],
            ....:         9: [6, 11], 10: [9, 1], 11: [10, 6], 12: [13, 6],
            ....:         13: [16, 2], 14: [10, -6], 15: [0, -10], 16: [14, -6],
            ....:         17: [16, -10], 18: [6, -4]}
            sage: SD.plot(pos=posn, vertex_size=400, vertex_colors={'#FFFFFF':list(range(1,19))}, edge_labels=True).show() # long time

        ::

            sage: G = graphs.HeawoodGraph()
            sage: for u,v,l in G.edges(sort=False):
            ....:  G.set_edge_label(u, v, '(' + str(u) + ',' + str(v) + ')')
            sage: G.edges(sort=True)
                [(0, 1, '(0,1)'),
                 (0, 5, '(0,5)'),
                 (0, 13, '(0,13)'),
                 ...
                 (11, 12, '(11,12)'),
                 (12, 13, '(12,13)')]

        ::

            sage: g = Graph({0: [0, 1, 1, 2]}, loops=True, multiedges=True, sparse=True)
            sage: g.set_edge_label(0, 0, 'test')
            sage: g.edges(sort=True)
            [(0, 0, 'test'), (0, 1, None), (0, 1, None), (0, 2, None)]
            sage: g.add_edge(0, 0, 'test2')
            sage: g.set_edge_label(0,0,'test3')
            Traceback (most recent call last):
            ...
            RuntimeError: cannot set edge label, since there are multiple edges from 0 to 0

        ::

            sage: dg = DiGraph({0: [1], 1: [0]}, sparse=True)
            sage: dg.set_edge_label(0, 1, 5)
            sage: dg.set_edge_label(1, 0, 9)
            sage: dg.outgoing_edges(1)
            [(1, 0, 9)]
            sage: dg.incoming_edges(1)
            [(0, 1, 5)]
            sage: dg.outgoing_edges(0)
            [(0, 1, 5)]
            sage: dg.incoming_edges(0)
            [(1, 0, 9)]

        ::

            sage: G = Graph({0: {1: 1}}, sparse=True)
            sage: G.num_edges()
            1
            sage: G.set_edge_label(0, 1, 1)
            sage: G.num_edges()
            1
        """
        if self.allows_multiple_edges():
            if len(self.edge_label(u, v)) > 1:
                raise RuntimeError("cannot set edge label, since there are "
                                   "multiple edges from %s to %s" % (u, v))
        self._backend.set_edge_label(u, v, l, self._directed)

    def has_edge(self, u, v=None, label=None):
        r"""
        Check whether ``(u, v)`` is an edge of the (di)graph.

        INPUT: The following forms are accepted:

        - G.has_edge( 1, 2 )
        - G.has_edge( (1, 2) )
        - G.has_edge( 1, 2, 'label' )
        - G.has_edge( (1, 2, 'label') )

        EXAMPLES::

            sage: graphs.EmptyGraph().has_edge(9, 2)
            False
            sage: DiGraph().has_edge(9, 2)
            False
            sage: G = Graph(sparse=True)
            sage: G.add_edge(0, 1, "label")
            sage: G.has_edge(0, 1, "different label")
            False
            sage: G.has_edge(0, 1, "label")
            True
        """
        if label is None:
            if v is None:
                try:
                    u, v, label = u
                except Exception:
                    u, v = u
                    label = None
        return self._backend.has_edge(u, v, label)

    def edges(self, vertices=None, labels=True, sort=None, key=None,
              ignore_direction=False, sort_vertices=True):
        r"""
        Return a :class:`~EdgesView` of edges.

        Each edge is a triple ``(u, v, l)`` where ``u`` and ``v`` are vertices
        and ``l`` is a label. If the parameter ``labels`` is ``False`` then a
        list of couple ``(u, v)`` is returned where ``u`` and ``v`` are
        vertices.

        The returned :class:`~EdgesView` is over the edges incident with any
        vertex given in the parameter ``vertices`` (all edges if ``None``). If
        ``self`` is directed, iterates over outgoing edges only, unless
        parameter ``ignore_direction`` is ``True`` in which case it searches
        across edges in either direction.

        INPUT:

        - ``vertices`` -- object (default: ``None``); a vertex, a list of
          vertices or ``None``

        - ``labels`` -- boolean (default: ``True``); if ``False``, each edge is
          simply a pair ``(u, v)`` of vertices

        - ``sort`` -- boolean (default: ``None``); if ``True``, edges are sorted
          according to the default ordering

          As of :trac:`22349`, this argument must be explicitly
          specified (unless a ``key`` is given); otherwise a warning
          is printed and ``sort=True`` is used. The default will
          eventually be changed to ``False``.

        - ``key`` -- a function (default: ``None``); a function that takes an
          edge (a pair or a triple, according to the ``labels`` keyword) as its
          one argument and returns a value that can be used for comparisons in
          the sorting algorithm

        - ``ignore_direction`` -- boolean (default: ``False``); only applies to
           directed graphs. If ``True``, searches across edges in either
           direction.

        - ``sort_vertices`` -- boolean (default: ``True``); only applies to
          undirected graphs. If ``True``, sort the ends of the edges.
          Not sorting the ends is faster.


        OUTPUT: A :class:`~EdgesView`.

        .. WARNING::

            Since any object may be a vertex, there is no guarantee that any two
            vertices will be comparable, and thus no guarantee how two edges may
            compare.  With default objects for vertices (all integers), or when
            all the vertices are of the same simple type, then there should not
            be a problem with how the vertices will be sorted.  However, if you
            need to guarantee a total order for the sorting of the edges, use
            the ``key`` argument, as illustrated in the examples below.

        EXAMPLES::

            sage: graphs.DodecahedralGraph().edges(sort=True)
            [(0, 1, None), (0, 10, None), (0, 19, None), (1, 2, None),
             (1, 8, None), (2, 3, None), (2, 6, None), (3, 4, None),
             (3, 19, None), (4, 5, None), (4, 17, None), (5, 6, None),
             (5, 15, None), (6, 7, None), (7, 8, None), (7, 14, None),
             (8, 9, None), (9, 10, None), (9, 13, None), (10, 11, None),
             (11, 12, None), (11, 18, None), (12, 13, None), (12, 16, None),
             (13, 14, None), (14, 15, None), (15, 16, None), (16, 17, None),
             (17, 18, None), (18, 19, None)]

        ::

            sage: graphs.DodecahedralGraph().edges(sort=True, labels=False)
            [(0, 1), (0, 10), (0, 19), (1, 2), (1, 8), (2, 3), (2, 6), (3, 4),
             (3, 19), (4, 5), (4, 17), (5, 6), (5, 15), (6, 7), (7, 8), (7, 14),
             (8, 9), (9, 10), (9, 13), (10, 11), (11, 12), (11, 18), (12, 13),
             (12, 16), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18),
             (18, 19)]

        ::

            sage: D = graphs.DodecahedralGraph().to_directed()
            sage: D.edges(sort=True)
            [(0, 1, None), (0, 10, None), (0, 19, None), (1, 0, None),
             (1, 2, None), (1, 8, None), (2, 1, None), (2, 3, None),
             (2, 6, None), (3, 2, None), (3, 4, None), (3, 19, None),
             (4, 3, None), (4, 5, None), (4, 17, None), (5, 4, None),
             (5, 6, None), (5, 15, None), (6, 2, None), (6, 5, None),
             (6, 7, None), (7, 6, None), (7, 8, None), (7, 14, None),
             (8, 1, None), (8, 7, None), (8, 9, None), (9, 8, None),
             (9, 10, None), (9, 13, None), (10, 0, None), (10, 9, None),
             (10, 11, None), (11, 10, None), (11, 12, None), (11, 18, None),
             (12, 11, None), (12, 13, None), (12, 16, None), (13, 9, None),
             (13, 12, None), (13, 14, None), (14, 7, None), (14, 13, None),
             (14, 15, None), (15, 5, None), (15, 14, None), (15, 16, None),
             (16, 12, None), (16, 15, None), (16, 17, None), (17, 4, None),
             (17, 16, None), (17, 18, None), (18, 11, None), (18, 17, None),
             (18, 19, None), (19, 0, None), (19, 3, None), (19, 18, None)]
            sage: D.edges(sort=True, labels=False)
            [(0, 1), (0, 10), (0, 19), (1, 0), (1, 2), (1, 8), (2, 1), (2, 3),
             (2, 6), (3, 2), (3, 4), (3, 19), (4, 3), (4, 5), (4, 17), (5, 4),
             (5, 6), (5, 15), (6, 2), (6, 5), (6, 7), (7, 6), (7, 8), (7, 14),
             (8, 1), (8, 7), (8, 9), (9, 8), (9, 10), (9, 13), (10, 0), (10, 9),
             (10, 11), (11, 10), (11, 12), (11, 18), (12, 11), (12, 13),
             (12, 16), (13, 9), (13, 12), (13, 14), (14, 7), (14, 13), (14, 15),
             (15, 5), (15, 14), (15, 16), (16, 12), (16, 15), (16, 17), (17, 4),
             (17, 16), (17, 18), (18, 11), (18, 17), (18, 19), (19, 0), (19, 3),
             (19, 18)]

        The default is to sort the returned list in the default fashion, as in
        the above examples. This can be overridden by specifying a key
        function. This first example just ignores the labels in the third
        component of the triple::

            sage: G = graphs.CycleGraph(5)
            sage: G.edges(sort=True, key=lambda x: (x[1], -x[0]))
            [(0, 1, None), (1, 2, None), (2, 3, None), (3, 4, None), (0, 4, None)]

        We set the labels to characters and then perform a default sort followed
        by a sort according to the labels::

            sage: G = graphs.CycleGraph(5)
            sage: for e in G.edges(sort=False):
            ....:   G.set_edge_label(e[0], e[1], chr(ord('A') + e[0] + 5 * e[1]))
            sage: G.edges(sort=True)
            [(0, 1, 'F'), (0, 4, 'U'), (1, 2, 'L'), (2, 3, 'R'), (3, 4, 'X')]
            sage: G.edges(key=lambda x: x[2])
            [(0, 1, 'F'), (1, 2, 'L'), (2, 3, 'R'), (0, 4, 'U'), (3, 4, 'X')]

        We can restrict considered edges to those incident to a given set::

            sage: for i in graphs.PetersenGraph().edges(sort=True, vertices=[0]):
            ....:     print(i)
            (0, 1, None)
            (0, 4, None)
            (0, 5, None)
            sage: D = DiGraph({0: [1, 2], 1: [0]})
            sage: for i in D.edges(sort=True, vertices=[0]):
            ....:     print(i)
            (0, 1, None)
            (0, 2, None)

        Ignoring the direction of edges::

            sage: D = DiGraph({1: [0], 2: [0]})
            sage: D.edges(sort=True, vertices=0)
            []
            sage: D.edges(sort=True, vertices=0, ignore_direction=True)
            [(1, 0, None), (2, 0, None)]
            sage: D.edges(sort=True, vertices=[0], ignore_direction=True)
            [(1, 0, None), (2, 0, None)]

        Not sorting the ends of the edges::

            sage: G = Graph()
            sage: G = Graph()
            sage: G.add_edges([[1,2], [2,3], [0,3]])
            sage: list(G.edge_iterator(sort_vertices=False))
            [(3, 0, None), (2, 1, None), (3, 2, None)]

        TESTS:

        It is an error to turn off sorting while providing a key function for
        sorting::

            sage: P = graphs.PetersenGraph()
            sage: P.edges(sort=False, key=lambda x: x)
            Traceback (most recent call last):
            ...
            ValueError: sort keyword is not True, yet a key function is given

            sage: G = Graph()
            sage: G.add_edge(0, 1, [7])
            sage: G.add_edge(0, 2, [7])
            sage: G.edge_label(0, 1)[0] += 1
            sage: G.edges(sort=True)
            [(0, 1, [8]), (0, 2, [7])]

        Deprecation warning for ``sort=None`` (:trac:`27408`)::

            sage: G = graphs.HouseGraph()
            sage: G.edges(sort=None)
            doctest:...: DeprecationWarning: parameter 'sort' will be set to False by default in the future
            See https://github.com/sagemath/sage/issues/27408 for details.
            [(0, 1, None), (0, 2, None), (1, 3, None), (2, 3, None), (2, 4, None), (3, 4, None)]
        """
        if sort is None:
            if key is None:
                deprecation(27408, "parameter 'sort' will be set to False by default in the future")
            sort = True

        if vertices is not None and vertices in self:
            vertices = [vertices]

        return EdgesView(self, vertices=vertices, labels=labels, sort=sort, key=key,
                         ignore_direction=ignore_direction, sort_vertices=sort_vertices)

    def edge_boundary(self, vertices1, vertices2=None, labels=True, sort=False):
        r"""
        Return a list of edges ``(u,v,l)`` with ``u`` in ``vertices1``
        and ``v`` in ``vertices2``.

        If ``vertices2`` is ``None``, then it is set to the complement of
        ``vertices1``.

        In a digraph, the external boundary of a vertex `v` are those vertices
        `u` with an arc `(v, u)`.

        INPUT:

        - ``labels`` -- boolean (default: ``True``); if ``False``, each edge is
          a tuple `(u,v)` of vertices

        - ``sort`` -- boolean (default: ``False``); whether to sort the result

        EXAMPLES::

            sage: K = graphs.CompleteBipartiteGraph(9, 3)
            sage: len(K.edge_boundary([0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11]))
            27
            sage: K.size()
            27

        Note that the edge boundary preserves direction::

            sage: K = graphs.CompleteBipartiteGraph(9, 3).to_directed()
            sage: len(K.edge_boundary([0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11]))
            27
            sage: K.size()
            54

        ::

            sage: D = DiGraph({0: [1, 2], 3: [0]})
            sage: D.edge_boundary([0], sort=True)
            [(0, 1, None), (0, 2, None)]
            sage: D.edge_boundary([0], labels=False, sort=True)
            [(0, 1), (0, 2)]

        TESTS::

            sage: G = graphs.DiamondGraph()
            sage: G.edge_boundary([0, 1], sort=True)
            [(0, 2, None), (1, 2, None), (1, 3, None)]
            sage: G.edge_boundary([0], [0])
            []
            sage: G.edge_boundary([2], [0])
            [(0, 2, None)]
        """
        vertices1 = set(v for v in vertices1 if v in self)
        if self._directed:
            if vertices2 is not None:
                vertices2 = set(v for v in vertices2 if v in self)
                output = [e for e in self.outgoing_edge_iterator(vertices1, labels=labels)
                          if e[1] in vertices2]
            else:
                output = [e for e in self.outgoing_edge_iterator(vertices1, labels=labels)
                          if e[1] not in vertices1]
        else:
            if vertices2 is not None:
                vertices2 = set(v for v in vertices2 if v in self)
                output = [e for e in self.edges(vertices=vertices1, labels=labels, sort=False)
                          if (e[0] in vertices1 and e[1] in vertices2) or
                             (e[1] in vertices1 and e[0] in vertices2)]
            else:
                output = [e for e in self.edges(vertices=vertices1, labels=labels, sort=False)
                          if e[1] not in vertices1 or e[0] not in vertices1]
        if sort:
            output.sort()
        return output

    def edge_iterator(self, vertices=None, labels=True, ignore_direction=False, sort_vertices=True):
        r"""
        Return an iterator over edges.

        The iterator returned is over the edges incident with any vertex given
        in the parameter ``vertices``. If the graph is directed, iterates over
        edges going out only. If ``vertices`` is ``None``, then returns an
        iterator over all edges. If ``self`` is directed, returns outgoing edges
        only.

        INPUT:

        - ``vertices`` -- object (default: ``None``); a vertex, a list of
          vertices or ``None``

        - ``labels`` -- boolean (default: ``True``); if ``False``, each edge is
           a tuple `(u,v)` of vertices

        - ``ignore_direction`` -- boolean (default: ``False``); only applies to
           directed graphs. If ``True``, searches across edges in either
           direction.

        - ``sort_vertices`` -- boolean (default: ``True``); only applies to
          undirected graphs. If ``True``, sort the ends of the edges.
          Not sorting the ends is faster.

        .. NOTE::

            It is somewhat safe to modify the graph during iterating.

            ``vertices`` must be specified if modifying the vertices.

            Without multiedges, you can safely use this graph to relabel
            edges or delete some edges. If you add edges, they might later
            appear in the iterator or not
            (depending on the internal order of vertices).

            In case of multiedges, all arcs from one vertex to another are
            internally cached. So the iterator will yield them, even if you delete
            them all after seeing the first one.

        EXAMPLES::

            sage: for i in graphs.PetersenGraph().edge_iterator([0]):
            ....:  print(i)
            (0, 1, None)
            (0, 4, None)
            (0, 5, None)
            sage: D = DiGraph({0: [1, 2], 1: [0]})
            sage: for i in D.edge_iterator([0]):
            ....:  print(i)
            (0, 1, None)
            (0, 2, None)

        ::

            sage: G = graphs.TetrahedralGraph()
            sage: list(G.edge_iterator(labels=False))
            [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

        ::

            sage: G = graphs.TetrahedralGraph()
            sage: list(G.edge_iterator(labels=False, sort_vertices=False))
            [(1, 0), (2, 0), (3, 0), (2, 1), (3, 1), (3, 2)]

        ::

            sage: D = DiGraph({1: [0], 2: [0]})
            sage: list(D.edge_iterator(0))
            []
            sage: list(D.edge_iterator(0, ignore_direction=True))
            [(1, 0, None), (2, 0, None)]
        """
        if vertices is None:
            vertices = self
        elif vertices in self:
            vertices = [vertices]
        else:
            vertices = [v for v in vertices if v in self]

        if ignore_direction and self._directed:
            from itertools import chain
            return chain(self._backend.iterator_out_edges(vertices, labels),
                         self._backend.iterator_in_edges(vertices, labels))
        elif self._directed:
            return self._backend.iterator_out_edges(vertices, labels)
        elif not sort_vertices:
            return self._backend.iterator_unsorted_edges(vertices, labels)
        else:
            return self._backend.iterator_edges(vertices, labels)

    def edges_incident(self, vertices=None, labels=True, sort=False):
        r"""
        Return incident edges to some vertices.

        If ``vertices`` is a vertex, then it returns the list of edges
        incident to that vertex. If ``vertices`` is a list of vertices
        then it returns the list of all edges adjacent to those
        vertices. If ``vertices`` is ``None``, it returns a list of all edges
        in graph. For digraphs, only lists outward edges.

        INPUT:

        - ``vertices`` -- object (default: ``None``); a vertex, a list of
          vertices or ``None``

        - ``labels`` -- boolean (default: ``True``); if ``False``, each edge is
           a tuple `(u,v)` of vertices

        - ``sort`` -- boolean (default: ``False``); if ``True`` the returned
          list is sorted

        EXAMPLES::

            sage: graphs.PetersenGraph().edges_incident([0, 9], labels=False)
            [(0, 1), (0, 4), (0, 5), (4, 9), (6, 9), (7, 9)]
            sage: D = DiGraph({0: [1]})
            sage: D.edges_incident([0])
            [(0, 1, None)]
            sage: D.edges_incident([1])
            []

        TESTS::

            sage: G = Graph({0: [0]}, loops=True)  # issue 9581
            sage: G.edges_incident(0)
            [(0, 0, None)]
        """
        if vertices in self:
            vertices = [vertices]

        if sort:
            return sorted(self.edge_iterator(vertices=vertices, labels=labels))
        return list(self.edge_iterator(vertices=vertices, labels=labels))

    def edge_label(self, u, v):
        """
        Return the label of an edge.

        If the graph allows multiple edges, then the list of labels on the edges
        is returned.

        .. SEEALSO::

            - :meth:`set_edge_label`

        EXAMPLES::

            sage: G = Graph({0: {1: 'edgelabel'}})
            sage: G.edge_label(0, 1)
            'edgelabel'
            sage: D = DiGraph({1: {2: 'up'}, 2: {1: 'down'}})
            sage: D.edge_label(2, 1)
            'down'

        ::

            sage: G = Graph(multiedges=True)
            sage: [G.add_edge(0, 1, i) for i in range(1, 6)]
            [None, None, None, None, None]
            sage: sorted(G.edge_label(0, 1))
            [1, 2, 3, 4, 5]

        TESTS::

            sage: g = graphs.CycleGraph(5)
            sage: g.edge_label(2, 3) is None
            True
        """
        return self._backend.get_edge_label(u, v)

    def edge_labels(self):
        """
        Return a list of the labels of all edges in ``self``.

        The output list is not sorted.

        EXAMPLES::

            sage: G = Graph({0: {1: 'x', 2: 'z', 3: 'a'}, 2: {5: 'out'}}, sparse=True)
            sage: G.edge_labels()
            ['x', 'z', 'a', 'out']
            sage: G = DiGraph({0: {1: 'x', 2: 'z', 3: 'a'}, 2: {5: 'out'}}, sparse=True)
            sage: G.edge_labels()
            ['x', 'z', 'a', 'out']
        """
        return [l for _, _, l in self.edge_iterator()]

    def remove_multiple_edges(self):
        """
        Remove all multiple edges, retaining one edge for each.

        .. SEEALSO::

            See also :meth:`allow_multiple_edges`

        EXAMPLES::

            sage: G = Graph(multiedges=True, sparse=True)
            sage: G.add_edges([(0,1), (0,1), (0,1), (0,1), (1,2)])
            sage: G.edges(sort=True, labels=False)
            [(0, 1), (0, 1), (0, 1), (0, 1), (1, 2)]

        ::

            sage: G.remove_multiple_edges()
            sage: G.edges(sort=True, labels=False)
            [(0, 1), (1, 2)]

        ::

            sage: D = DiGraph(multiedges=True, sparse=True)
            sage: D.add_edges([(0, 1, 1), (0, 1, 2), (0, 1, 3), (0, 1, 4), (1, 2, None)])
            sage: D.edges(sort=True, labels=False)
            [(0, 1), (0, 1), (0, 1), (0, 1), (1, 2)]
            sage: D.remove_multiple_edges()
            sage: D.edges(sort=True, labels=False)
            [(0, 1), (1, 2)]
        """
        if self.allows_multiple_edges():
            if self._directed:
                for v in self:
                    for u in self.neighbor_in_iterator(v):
                        labels = self.edge_label(u, v)
                        if len(labels) > 1:
                            self.delete_edges((u, v, labels[i]) for i in range(1, len(labels)))
            else:
                for v in self:
                    for u in self.neighbor_iterator(v):
                        labels = self.edge_label(u, v)
                        if len(labels) > 1:
                            self.delete_edges((u, v, labels[i]) for i in range(1, len(labels)))

    def remove_loops(self, vertices=None):
        """
        Remove loops on vertices in ``vertices``.

        If ``vertices`` is ``None``, removes all loops.

        EXAMPLES::

            sage: G = Graph(4, loops=True)
            sage: G.add_edges([(0, 0), (1, 1), (2, 2), (3, 3), (2, 3)])
            sage: G.edges(sort=True, labels=False)
            [(0, 0), (1, 1), (2, 2), (2, 3), (3, 3)]
            sage: G.remove_loops()
            sage: G.edges(sort=True, labels=False)
            [(2, 3)]
            sage: G.allows_loops()
            True
            sage: G.has_loops()
            False

            sage: D = DiGraph(4, loops=True)
            sage: D.add_edges([(0, 0), (1, 1), (2, 2), (3, 3), (2, 3)])
            sage: D.edges(sort=True, labels=False)
            [(0, 0), (1, 1), (2, 2), (2, 3), (3, 3)]
            sage: D.remove_loops()
            sage: D.edges(sort=True, labels=False)
            [(2, 3)]
            sage: D.allows_loops()
            True
            sage: D.has_loops()
            False
        """
        if vertices is None:
            vertices = self
        for v in vertices:
            if self.has_edge(v, v):
                self.delete_multiedge(v, v)

    # Modifications

    def clear(self):
        """
        Empties the graph of vertices and edges and removes name, associated
        objects, and position information.

        EXAMPLES::

            sage: G = graphs.CycleGraph(4)
            sage: G.set_vertices({0:'vertex0'})
            sage: print(G.order(), G.size())
            4 4
            sage: G.name()
            'Cycle graph'
            sage: G.get_vertex(0)
            'vertex0'
            sage: H = G.copy(sparse=True)
            sage: H.clear()
            sage: print(H.order(), H.size())
            0 0
            sage: H.name()
            ''
            sage: H.get_vertex(0)
            sage: H = G.copy(sparse=False)
            sage: H.clear()
            sage: print(H.order(), H.size())
            0 0
            sage: H.name()
            ''
            sage: H.get_vertex(0)
        """
        self.name('')
        self.delete_vertices(self.vertex_iterator())

    # Degree functions

    def degree(self, vertices=None, labels=False):
        """
        Return the degree (in + out for digraphs) of a vertex or of vertices.

        INPUT:

        - ``vertices`` -- a vertex or an iterable container of vertices
          (default: ``None``); if ``vertices`` is a single vertex, returns the
          number of neighbors of that vertex. If ``vertices`` is an iterable
          container of vertices, returns a list of degrees. If ``vertices`` is
          ``None``, same as listing all vertices.

        - ``labels`` -- boolean (default: ``False``); when ``True``, return a
          dictionary mapping each vertex in ``vertices`` to its
          degree. Otherwise, return the degree of a single vertex or a list of
          the degrees of each vertex in ``vertices``

        OUTPUT:

        - When ``vertices`` is a single vertex and ``labels`` is ``False``,
          returns the degree of that vertex as an integer

        - When ``vertices`` is an iterable container of vertices (or ``None``)
          and ``labels`` is ``False``, returns a list of integers. The `i`-th
          value is the degree of the `i`-th vertex in the list
          ``vertices``. When ``vertices`` is ``None``, the `i`-th value is the
          degree of `i`-th vertex in the ordering ``list(self)``, which might be
          different from the ordering of the vertices given by
          ``g.vertices(sort=True)``.

        - When ``labels`` is ``True``, returns a dictionary mapping each vertex
          in ``vertices`` to its degree

        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: P.degree(5)
            3

        ::

            sage: K = graphs.CompleteGraph(9)
            sage: K.degree()
            [8, 8, 8, 8, 8, 8, 8, 8, 8]

        ::

            sage: D = DiGraph({0: [1, 2, 3], 1: [0, 2], 2: [3], 3: [4], 4: [0,5], 5: [1]})
            sage: D.degree(vertices=[0, 1, 2], labels=True)
            {0: 5, 1: 4, 2: 3}
            sage: D.degree()
            [5, 4, 3, 3, 3, 2]

        When ``vertices=None`` and ``labels=False``, the `i`-th value of the
        returned list is the degree of the `i`-th vertex in the list
        ``list(self)``::

            sage: D = digraphs.DeBruijn(4, 2)
            sage: D.delete_vertex('20')
            sage: print(D.degree())
            [7, 7, 6, 7, 8, 8, 7, 8, 8, 7, 8, 8, 8, 7, 8]
            sage: print(D.degree(vertices=list(D)))
            [7, 7, 6, 7, 8, 8, 7, 8, 8, 7, 8, 8, 8, 7, 8]
            sage: print(D.degree(vertices=D.vertices(sort=False)))
            [7, 7, 6, 7, 8, 8, 7, 8, 8, 7, 8, 8, 8, 7, 8]
        """
        if labels:
            return dict(self.degree_iterator(vertices, labels))
        elif vertices in self and not labels:
            return next(self.degree_iterator(vertices, labels))
        else:
            return list(self.degree_iterator(vertices, labels))

    def average_degree(self):
        r"""
        Return the average degree of the graph.

        The average degree of a graph `G=(V,E)` is equal to `\frac{2|E|}{|V|}`.

        EXAMPLES:

        The average degree of a regular graph is equal to the degree of any
        vertex::

            sage: g = graphs.CompleteGraph(5)
            sage: g.average_degree() == 4
            True

        The average degree of a tree is always strictly less than `2`::

           sage: tree = graphs.RandomTree(20)
           sage: tree.average_degree() < 2
           True

        For any graph, it is equal to `\frac{2|E|}{|V|}`::

            sage: g = graphs.RandomGNP(20, .4)
            sage: g.average_degree() == 2 * g.size() / g.order()
            True
        """
        return 2 * Integer(self.size()) / Integer(self.order())

    def degree_histogram(self):
        r"""
        Return a list, whose `i`-th entry is the frequency of degree `i`.

        EXAMPLES::

            sage: G = graphs.Grid2dGraph(9, 12)
            sage: G.degree_histogram()
            [0, 0, 4, 34, 70]

        ::

            sage: G = graphs.Grid2dGraph(9, 12).to_directed()
            sage: G.degree_histogram()
            [0, 0, 0, 0, 4, 0, 34, 0, 70]

        TESTS::

            sage: Graph().degree_histogram()
            []
        """
        if not self.order():
            return []
        degree_sequence = self.degree()
        dmax = max(degree_sequence) + 1
        frequency = [0] * dmax
        for d in degree_sequence:
            frequency[d] += 1
        return frequency

    def degree_iterator(self, vertices=None, labels=False):
        """
        Return an iterator over the degrees of the (di)graph.

        In the case of a digraph, the degree is defined as the sum of the
        in-degree and the out-degree, i.e. the total number of edges incident to
        a given vertex.

        INPUT:

        - ``vertices`` -- a vertex or an iterable container of vertices
          (default: ``None``); if ``vertices`` is a single vertex, the iterator
          will yield the number of neighbors of that vertex. If ``vertices`` is
          an iterable container of vertices, return an iterator over the degrees
          of these vertices. If ``vertices`` is ``None``, same as listing all
          vertices.

        - ``labels`` -- boolean (default: ``False``); whether to return an
          iterator over degrees (``labels=False``), or over tuples ``(vertex,
          degree)``

        .. NOTE::

            The returned iterator yields values in order specified by
            ``list(vertices)``. When ``vertices`` is ``None``, it yields values
            in the same order as ``list(self)``, which might be different from
            the ordering of the vertices given by ``g.vertices(sort=True)``.

        EXAMPLES::

            sage: G = graphs.Grid2dGraph(3, 4)
            sage: for i in G.degree_iterator():
            ....:     print(i)
            2
            3
            3
            ...
            3
            2
            sage: for i in G.degree_iterator(labels=True):
            ....:     print(i)
            ((0, 0), 2)
            ((0, 1), 3)
            ((0, 2), 3)
            ...
            ((2, 2), 3)
            ((2, 3), 2)

        ::

            sage: D = graphs.Grid2dGraph(2,4).to_directed()
            sage: for i in D.degree_iterator():
            ....:     print(i)
            4
            6
            ...
            6
            4
            sage: for i in D.degree_iterator(labels=True):
            ....:     print(i)
            ((0, 0), 4)
            ((0, 1), 6)
            ...
            ((1, 2), 6)
            ((1, 3), 4)

        When ``vertices=None`` yields values in the order of ``list(D)``::

            sage: V = list(D)
            sage: D = digraphs.DeBruijn(4, 2)
            sage: D.delete_vertex('20')
            sage: print(list(D.degree_iterator()))
            [7, 7, 6, 7, 8, 8, 7, 8, 8, 7, 8, 8, 8, 7, 8]
            sage: print([D.degree(v) for v in D])
            [7, 7, 6, 7, 8, 8, 7, 8, 8, 7, 8, 8, 8, 7, 8]
        """
        if vertices is None:
            vertices = self
        elif vertices in self:
            vertices = [vertices]
        else:
            vertices = [v for v in vertices if v in self]
        if labels:
            for v in vertices:
                yield (v, self._backend.degree(v, self._directed))
        else:
            for v in vertices:
                yield self._backend.degree(v, self._directed)

    def degree_sequence(self):
        r"""
        Return the degree sequence of this (di)graph.

        EXAMPLES:

        The degree sequence of an undirected graph::

            sage: g = Graph({1: [2, 5], 2: [1, 5, 3, 4], 3: [2, 5], 4: [3], 5: [2, 3]})
            sage: g.degree_sequence()
            [4, 3, 3, 2, 2]

        The degree sequence of a digraph::

            sage: g = DiGraph({1: [2, 5, 6], 2: [3, 6], 3: [4, 6], 4: [6], 5: [4, 6]})
            sage: g.degree_sequence()
            [5, 3, 3, 3, 3, 3]

        Degree sequences of some common graphs::

            sage: graphs.PetersenGraph().degree_sequence()
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
            sage: graphs.HouseGraph().degree_sequence()
            [3, 3, 2, 2, 2]
            sage: graphs.FlowerSnark().degree_sequence()
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        """
        return sorted(self.degree_iterator(), reverse=True)

    def is_regular(self, k=None):
        """
        Check whether this graph is (`k`-)regular.

        INPUT:

        - ``k`` -- integer (default: ``None``); the degree of regularity to
          check for

        EXAMPLES::

            sage: G = graphs.HoffmanSingletonGraph()
            sage: G.is_regular()
            True
            sage: G.is_regular(9)
            False

        So the Hoffman-Singleton graph is regular, but not 9-regular. In fact,
        we can now find the degree easily as follows::

            sage: next(G.degree_iterator())
            7

        The house graph is not regular::

            sage: graphs.HouseGraph().is_regular()
            False

        A graph without vertices is `k`-regular for every `k`::

            sage: Graph().is_regular()
            True
        """
        if not self.order():
            return True

        deg_it = self.degree_iterator()
        if k is None:
            k = next(deg_it)

        for d in deg_it:
            if d != k:
                return False

        return True

    # Substructures

    def subgraph(self, vertices=None, edges=None, inplace=False,
                 vertex_property=None, edge_property=None, algorithm=None,
                 immutable=None):
        r"""
        Return the subgraph containing the given vertices and edges.

        If either vertices or edges are not specified, they are assumed to be
        all vertices or edges. If edges are not specified, returns the subgraph
        induced by the vertices.

        INPUT:

        - ``inplace`` -- boolean (default: ``False``); using ``inplace=True``
          will simply delete the extra vertices and edges from the current
          graph. This will modify the graph.

        - ``vertices`` -- a single vertex or an iterable container of vertices,
          e.g. a list, set, graph, file or numeric array. If not passed (i.e.,
          ``None``), defaults to the entire graph.

        - ``edges`` -- as with ``vertices``, edges can be a single edge or an
          iterable container of edges (e.g., a list, set, file, numeric array,
          etc.). By default (``edges=None``), all edges are assumed and the
          returned graph is an induced subgraph. In the case of multiple edges,
          specifying an edge as `(u,v)` means to keep all edges `(u,v)`,
          regardless of the label.

        - ``vertex_property`` -- function (default: ``None``); a function that
          inputs a vertex and outputs a boolean value, i.e., a vertex ``v`` in
          ``vertices`` is kept if ``vertex_property(v) == True``

        - ``edge_property`` -- function (default: ``None``); a function that
          inputs an edge and outputs a boolean value, i.e., a edge ``e`` in
          ``edges`` is kept if ``edge_property(e) == True``

        - ``algorithm`` -- string (default: ``None``); one of the following:

          - If ``algorithm="delete"`` or ``inplace=True``, then the graph is
            constructed by deleting edges and vertices

          - If ``algorithm="add"``, then the graph is constructed by building a
            new graph from the appropriate vertices and edges. Implies
            ``inplace=False``.

          - If ``algorithm=None``, then the algorithm is chosen based on the
            number of vertices in the subgraph.

        - ``immutable`` -- boolean (default: ``None``); whether to create a
          mutable/immutable subgraph. ``immutable=None`` (default) means that
          the graph and its subgraph will behave the same way.

        EXAMPLES::

            sage: G = graphs.CompleteGraph(9)
            sage: H = G.subgraph([0, 1, 2]); H
            Subgraph of (Complete graph): Graph on 3 vertices
            sage: G
            Complete graph: Graph on 9 vertices
            sage: J = G.subgraph(edges=[(0, 1)])
            sage: J.edges(sort=True, labels=False)
            [(0, 1)]
            sage: set(J) == set(G)
            True
            sage: G.subgraph([0, 1, 2], inplace=True); G
            Subgraph of (Complete graph): Graph on 3 vertices
            sage: G.subgraph() == G
            True

        ::

            sage: D = digraphs.Complete(9)
            sage: H = D.subgraph([0, 1, 2]); H
            Subgraph of (Complete digraph): Digraph on 3 vertices
            sage: H = D.subgraph(edges=[(0, 1), (0, 2)])
            sage: H.edges(sort=True, labels=False)
            [(0, 1), (0, 2)]
            sage: set(H) == set(D)
            True
            sage: D
            Complete digraph: Digraph on 9 vertices
            sage: D.subgraph([0, 1, 2], inplace=True); D
            Subgraph of (Complete digraph): Digraph on 3 vertices
            sage: D.subgraph() == D
            True

        A more complicated example involving multiple edges and labels::

            sage: G = Graph(multiedges=True, sparse=True)
            sage: G.add_edges([(0, 1, 'a'), (0, 1, 'b'), (1, 0, 'c'), (0, 2, 'd'), (0, 2, 'e'), (2, 0, 'f'), (1, 2, 'g')])
            sage: G.subgraph(edges=[(0, 1), (0, 2,'d'), (0, 2, 'not in graph')]).edges(sort=True)
            [(0, 1, 'a'), (0, 1, 'b'), (0, 1, 'c'), (0, 2, 'd')]
            sage: J = G.subgraph(vertices=[0, 1], edges=[(0, 1, 'a'), (0, 2, 'c')])
            sage: J.edges(sort=True)
            [(0, 1, 'a')]
            sage: J.vertices(sort=True)
            [0, 1]
            sage: G.subgraph(vertices=G) == G
            True

        ::

            sage: D = DiGraph(multiedges=True, sparse=True)
            sage: D.add_edges([(0, 1, 'a'), (0, 1, 'b'), (1, 0, 'c'), (0, 2, 'd'), (0, 2, 'e'), (2, 0, 'f'), (1, 2, 'g')])
            sage: D.subgraph(edges=[(0, 1), (0, 2, 'd'), (0, 2, 'not in graph')]).edges(sort=True)
            [(0, 1, 'a'), (0, 1, 'b'), (0, 2, 'd')]
            sage: H = D.subgraph(vertices=[0, 1], edges=[(0, 1, 'a'), (0, 2, 'c')])
            sage: H.edges(sort=True)
            [(0, 1, 'a')]
            sage: H.vertices(sort=True)
            [0, 1]

        Using the property arguments::

            sage: P = graphs.PetersenGraph()
            sage: S = P.subgraph(vertex_property=lambda v: not (v % 2))
            sage: S.vertices(sort=True)
            [0, 2, 4, 6, 8]

        ::

            sage: C = graphs.CubeGraph(2)
            sage: S = C.subgraph(edge_property=(lambda e: e[0][0] == e[1][0]))
            sage: C.edges(sort=True)
            [('00', '01', None), ('00', '10', None), ('01', '11', None), ('10', '11', None)]
            sage: S.edges(sort=True)
            [('00', '01', None), ('10', '11', None)]


        The algorithm is not specified, then a reasonable choice is made for
        speed::

            sage: g = graphs.PathGraph(1000)
            sage: g.subgraph(list(range(10)))  # uses the 'add' algorithm
            Subgraph of (Path graph): Graph on 10 vertices

        TESTS:

        The appropriate properties are preserved::

            sage: g = graphs.PathGraph(10)
            sage: g.is_planar(set_embedding=True)
            True
            sage: g.set_vertices({v: 'v%d'%v for v in g})
            sage: h = g.subgraph([3..5])
            sage: sorted(h.get_pos().keys())
            [3, 4, 5]
            sage: h.get_vertices()
            {3: 'v3', 4: 'v4', 5: 'v5'}
        """
        if vertices is None:
            vertices = self
        elif vertices in self:
            vertices = [vertices]
        else:
            vertices = list(vertices)

        if vertex_property is not None:
            vertices = [v for v in vertices if vertex_property(v)]

        if algorithm is not None and algorithm not in ("delete", "add"):
            raise ValueError('algorithm should be None, "delete", or "add"')

        if (inplace or algorithm == "delete"):
            return self._subgraph_by_deleting(vertices=vertices, edges=edges,
                                              inplace=inplace,
                                              edge_property=edge_property,
                                              immutable=immutable)
        else:
            return self._subgraph_by_adding(vertices=vertices, edges=edges,
                                            edge_property=edge_property,
                                            immutable=immutable)

    def _subgraph_by_adding(self, vertices=None, edges=None, edge_property=None, immutable=None):
        r"""
        Return the subgraph containing the given vertices and edges.

        The edges also satisfy the ``edge_property``, if it is not ``None``.
        The subgraph is created by creating a new empty graph and adding the
        necessary vertices, edges, and other properties.

        INPUT:

        - ``vertices`` -- (default: ``None``); an iterable container of
          vertices, e.g. a list, set, graph, file or numeric array. If not
          passed (i.e., ``None``), defaults to the entire graph.

        - ``edges`` -- a single edge or an iterable container of edges (e.g., a
          list, set, file, numeric array, etc.). By default (``edges=None``),
          all edges are assumed and the returned graph is an induced
          subgraph. In the case of multiple edges, specifying an edge as `(u,v)`
          means to keep all edges `(u,v)`, regardless of the label.

        - ``edge_property`` -- function (default: ``None``); a function that
          inputs an edge and outputs a boolean value, i.e., a edge ``e`` in
          ``edges`` is kept if ``edge_property(e) == True``

        - ``immutable`` -- boolean (default: ``None``); whether to create a
          mutable/immutable subgraph. ``immutable=None`` (default) means that
          the graph and its subgraph will behave the same way.

        EXAMPLES::

            sage: G = graphs.CompleteGraph(9)
            sage: H = G._subgraph_by_adding([0, 1, 2]); H
            Subgraph of (Complete graph): Graph on 3 vertices
            sage: G
            Complete graph: Graph on 9 vertices
            sage: J = G._subgraph_by_adding(vertices=G, edges=[(0, 1)])
            sage: J.edges(sort=True, labels=False)
            [(0, 1)]
            sage: set(J) == set(G)
            True
            sage: G._subgraph_by_adding(vertices=G) == G
            True

        ::

            sage: D = digraphs.Complete(9)
            sage: H = D._subgraph_by_adding([0, 1, 2]); H
            Subgraph of (Complete digraph): Digraph on 3 vertices
            sage: H = D._subgraph_by_adding(vertices=D, edges=[(0, 1), (0, 2)])
            sage: H.edges(sort=True, labels=False)
            [(0, 1), (0, 2)]
            sage: set(H) == set(D)
            True
            sage: D
            Complete digraph: Digraph on 9 vertices
            sage: D._subgraph_by_adding(vertices=D) == D
            True

        A more complicated example involving multiple edges and labels::

            sage: G = Graph(multiedges=True, sparse=True)
            sage: G.add_edges([(0, 1, 'a'), (0, 1, 'b'), (1, 0, 'c'), (0, 2, 'd'), (0, 2, 'e'), (2, 0, 'f'), (1, 2, 'g')])
            sage: G._subgraph_by_adding(vertices=G, edges=[(0, 1), (0, 2, 'd'), (0, 2, 'not in graph')]).edges(sort=True)
            [(0, 1, 'a'), (0, 1, 'b'), (0, 1, 'c'), (0, 2, 'd')]
            sage: J = G._subgraph_by_adding(vertices=[0, 1], edges=[(0, 1, 'a'), (0, 2, 'c')])
            sage: J.edges(sort=True)
            [(0, 1, 'a')]
            sage: J.vertices(sort=True)
            [0, 1]
            sage: G._subgraph_by_adding(vertices=G) == G
            True

        ::

            sage: D = DiGraph(multiedges=True, sparse=True)
            sage: D.add_edges([(0, 1, 'a'), (0, 1, 'b'), (1, 0, 'c'), (0, 2, 'd'), (0, 2, 'e'), (2, 0, 'f'), (1, 2, 'g')])
            sage: D._subgraph_by_adding(vertices=D, edges=[(0, 1), (0, 2, 'd'), (0, 2, 'not in graph')]).edges(sort=True)
            [(0, 1, 'a'), (0, 1, 'b'), (0, 2, 'd')]
            sage: H = D._subgraph_by_adding(vertices=[0, 1], edges=[(0, 1, 'a'), (0, 2, 'c')])
            sage: H.edges(sort=True)
            [(0, 1, 'a')]
            sage: H.vertices(sort=True)
            [0, 1]

        Using the property arguments::

            sage: C = graphs.CubeGraph(2)
            sage: S = C._subgraph_by_adding(vertices=C, edge_property=(lambda e: e[0][0] == e[1][0]))
            sage: C.edges(sort=True)
            [('00', '01', None), ('00', '10', None), ('01', '11', None), ('10', '11', None)]
            sage: S.edges(sort=True)
            [('00', '01', None), ('10', '11', None)]

        TESTS:

        Properties of the graph are preserved::

            sage: g = graphs.PathGraph(10)
            sage: g.is_planar(set_embedding=True)
            True
            sage: g.set_vertices({v: 'v%d'%v for v in g})
            sage: h = g._subgraph_by_adding([3..5])
            sage: sorted(h.get_pos().keys())
            [3, 4, 5]
            sage: h.get_vertices()
            {3: 'v3', 4: 'v4', 5: 'v5'}
        """
        G = self.__class__(weighted=self._weighted, loops=self.allows_loops(),
                           multiedges=self.allows_multiple_edges())
        G.name("Subgraph of (%s)" % self.name())
        if edges is None and edge_property is None:
            self._backend.subgraph_given_vertices(G._backend, vertices)
        else:
            G.add_vertices(self if vertices is None else vertices)

            if edges is not None:
                edges_to_keep_labeled = frozenset(e for e in edges if len(e) == 3)
                edges_to_keep_unlabeled = frozenset(e for e in edges if len(e) == 2)

                edges_to_keep = []
                if self._directed:
                    for u, v, l in self.edges(vertices=vertices, sort=False):
                        if (v in G and ((u, v, l) in edges_to_keep_labeled
                                        or (u, v) in edges_to_keep_unlabeled)):
                            edges_to_keep.append((u, v, l))
                else:
                    for u, v, l in self.edges(vertices=vertices, sort=False):
                        if (u in G and v in G
                            and ((u, v, l) in edges_to_keep_labeled
                                 or (v, u, l) in edges_to_keep_labeled
                                 or (u, v) in edges_to_keep_unlabeled
                                 or (v, u) in edges_to_keep_unlabeled)):
                            edges_to_keep.append((u, v, l))
            else:
                s_vertices = set(vertices)
                edges_to_keep = [e for e in self.edges(vertices=vertices, sort=False, sort_vertices=False)
                                 if e[0] in s_vertices and e[1] in s_vertices]

            if edge_property is not None:
                edges_to_keep = [e for e in edges_to_keep if edge_property(e)]
            G.add_edges(edges_to_keep)

        # copy _assoc, _pos, _pos3d and _embedding to the subgraph
        try:
            assoc = self._assoc
        except AttributeError:
            assoc = None
        if assoc is not None:
            G._assoc = {v: assoc[v] for v in G if v in assoc}
        pos = self.get_pos()
        if pos is not None:
            G._pos = {v: pos[v] for v in G if v in pos}
        pos3d = self.get_pos(dim=3)
        if pos3d is not None:
            G._pos3d = {v: pos3d[v] for v in G if v in pos3d}
        embedding = self.get_embedding()
        if embedding is not None:
            G._embedding = {u: [v for v in embedding[u] if u in G] for u in G}

        if immutable is None:
            immutable = self.is_immutable()
        if immutable:
            G = G.copy(immutable=True)

        return G

    def _subgraph_by_deleting(self, vertices=None, edges=None, inplace=False,
                              edge_property=None, immutable=None):
        r"""
        Return the subgraph containing the given vertices and edges.

        The edges also satisfy the ``edge_property``, if it is not ``None``.
        The subgraph is created by creating deleting things that are not needed.

        INPUT:

        - ``vertices`` -- (default: ``None``); an iterable container of
          vertices, e.g. a list, set, graph, file or numeric array. If not
          passed (i.e., ``None``), defaults to the entire graph.

        - ``edges`` -- a single edge or an iterable container of edges (e.g., a
          list, set, file, numeric array, etc.). By default (``edges=None``),
          all edges are assumed and the returned graph is an induced
          subgraph. In the case of multiple edges, specifying an edge as `(u,v)`
          means to keep all edges `(u,v)`, regardless of the label.

        - ``edge_property`` -- function (default: ``None``); a function that
          inputs an edge and outputs a boolean value, i.e., a edge ``e`` in
          ``edges`` is kept if ``edge_property(e) == True``

        - ``inplace`` -- boolean (default: ``False``); using ``inplace=True``
          will simply delete the extra vertices and edges from the current
          graph. This will modify the graph.

        - ``immutable`` -- boolean (default: ``None``); whether to create a
          mutable/immutable subgraph. ``immutable=None`` (default) means that
          the graph and its subgraph will behave the same way.

        EXAMPLES::

            sage: G = graphs.CompleteGraph(9)
            sage: H = G._subgraph_by_deleting([0, 1, 2]); H
            Subgraph of (Complete graph): Graph on 3 vertices
            sage: G
            Complete graph: Graph on 9 vertices
            sage: J = G._subgraph_by_deleting(vertices=G, edges=[(0, 1)])
            sage: J.edges(sort=True, labels=False)
            [(0, 1)]
            sage: set(J) == set(G)
            True
            sage: G._subgraph_by_deleting([0, 1, 2], inplace=True); G
            Subgraph of (Complete graph): Graph on 3 vertices
            sage: G._subgraph_by_deleting(vertices=G) == G
            True

        ::

            sage: D = digraphs.Complete(9)
            sage: H = D._subgraph_by_deleting([0, 1, 2]); H
            Subgraph of (Complete digraph): Digraph on 3 vertices
            sage: H = D._subgraph_by_deleting(vertices=D, edges=[(0, 1), (0, 2)])
            sage: H.edges(sort=True, labels=False)
            [(0, 1), (0, 2)]
            sage: set(H) == set(D)
            True
            sage: D
            Complete digraph: Digraph on 9 vertices
            sage: D._subgraph_by_deleting([0, 1, 2], inplace=True); D
            Subgraph of (Complete digraph): Digraph on 3 vertices
            sage: D._subgraph_by_deleting(D) == D
            True

        A more complicated example involving multiple edges and labels::

            sage: G = Graph(multiedges=True, sparse=True)
            sage: G.add_edges([(0, 1, 'a'), (0, 1, 'b'), (1, 0, 'c'), (0, 2, 'd'), (0, 2, 'e'), (2, 0, 'f'), (1, 2, 'g')])
            sage: G._subgraph_by_deleting(vertices=G, edges=[(0, 1), (0, 2, 'd'), (0, 2, 'not in graph')]).edges(sort=True)
            [(0, 1, 'a'), (0, 1, 'b'), (0, 1, 'c'), (0, 2, 'd')]
            sage: J = G._subgraph_by_deleting(vertices=[0, 1], edges=[(0, 1, 'a'), (0, 2, 'c')])
            sage: J.edges(sort=True)
            [(0, 1, 'a')]
            sage: J.vertices(sort=True)
            [0, 1]
            sage: G._subgraph_by_deleting(vertices=G) == G
            True

        ::

            sage: D = DiGraph(multiedges=True, sparse=True)
            sage: D.add_edges([(0, 1, 'a'), (0, 1, 'b'), (1, 0, 'c'), (0, 2, 'd'), (0, 2, 'e'), (2, 0, 'f'), (1, 2, 'g')])
            sage: D._subgraph_by_deleting(vertices=D, edges=[(0, 1), (0, 2, 'd'), (0, 2, 'not in graph')]).edges(sort=True)
            [(0, 1, 'a'), (0, 1, 'b'), (0, 2, 'd')]
            sage: H = D._subgraph_by_deleting(vertices=[0, 1], edges=[(0, 1, 'a'), (0, 2, 'c')])
            sage: H.edges(sort=True)
            [(0, 1, 'a')]
            sage: H.vertices(sort=True)
            [0, 1]

        Using the property arguments::

            sage: C = graphs.CubeGraph(2)
            sage: S = C._subgraph_by_deleting(vertices=C, edge_property=(lambda e: e[0][0] == e[1][0]))
            sage: C.edges(sort=True)
            [('00', '01', None), ('00', '10', None), ('01', '11', None), ('10', '11', None)]
            sage: S.edges(sort=True)
            [('00', '01', None), ('10', '11', None)]

        TESTS:

        Properties of the graph are preserved::

            sage: g = graphs.PathGraph(10)
            sage: g.is_planar(set_embedding=True)
            True
            sage: g.set_vertices({v: 'v%d'%v for v in g})
            sage: h = g._subgraph_by_deleting([3..5])
            sage: sorted(h.get_pos().keys())
            [3, 4, 5]
            sage: h.get_vertices()
            {3: 'v3', 4: 'v4', 5: 'v5'}

        :trac:`17683`::

            sage: graphs.PetersenGraph().copy(immutable=True).subgraph([1, 2])
            Subgraph of (Petersen graph): Graph on 2 vertices
        """
        if inplace:
            G = self
            if vertices is not None:
                vertices = set(vertices)
                G.delete_vertices([v for v in G if v not in vertices])
            G.name("Subgraph of (%s)" % self.name())
        else:
            G = self._subgraph_by_adding(vertices)

        edges_to_delete = []
        if edges is not None:
            edges_to_keep_labeled = frozenset(e for e in edges if len(e) == 3)
            edges_to_keep_unlabeled = frozenset(e for e in edges if len(e) == 2)
            edges_to_delete = []
            if G._directed:
                for e in G.edge_iterator():
                    if (e not in edges_to_keep_labeled
                            and e[:2] not in edges_to_keep_unlabeled):
                        edges_to_delete.append(e)
            else:
                for u, v, l in G.edge_iterator():
                    if ((u, v, l) not in edges_to_keep_labeled
                            and (v, u, l) not in edges_to_keep_labeled
                            and (u, v) not in edges_to_keep_unlabeled
                            and (v, u) not in edges_to_keep_unlabeled):
                        edges_to_delete.append((u, v, l))
        if edge_property is not None:
            # We might get duplicate edges, but this does handle the case of
            # multiple edges.
            edges_to_delete.extend(e for e in G.edge_iterator() if not edge_property(e))

        G.delete_edges(edges_to_delete)
        if not inplace:
            if immutable is None:
                immutable = self.is_immutable()
            if immutable:
                G = G.copy(immutable=True)
            return G

    def subgraph_search(self, G, induced=False):
        r"""
        Return a copy of ``G`` in ``self``.

        INPUT:

        - ``G`` -- the (di)graph whose copy we are looking for in ``self``

        - ``induced`` -- boolean (default: ``False``); whether or not to search
          for an induced copy of ``G`` in ``self``

        OUTPUT:

        If ``induced=False``, return a copy of ``G`` in this graph.  Otherwise,
        return an induced copy of ``G`` in ``self``. If ``G`` is the empty
        graph, return the empty graph since it is a subgraph of every graph. Now
        suppose ``G`` is not the empty graph. If there is no copy (induced or
        otherwise) of ``G`` in ``self``, we return ``None``.

        .. NOTE::

            The vertex labels and the edge labels in the graph are ignored.

        .. SEEALSO::

            - :meth:`~GenericGraph.subgraph_search_count` -- counts the number
              of copies of `H` inside of `G`

            - :meth:`~GenericGraph.subgraph_search_iterator` -- iterator over
              the copies of `H` inside of `G`

        ALGORITHM:

        See the documentation of
        :class:`~sage.graphs.generic_graph_pyx.SubgraphSearch`.

        EXAMPLES:

        The Petersen graph contains the path graph `P_5`::

             sage: g = graphs.PetersenGraph()
             sage: h1 = g.subgraph_search(graphs.PathGraph(5)); h1
             Subgraph of (Petersen graph): Graph on 5 vertices
             sage: h1.vertices(sort=True); h1.edges(sort=True, labels=False)
             [0, 1, 2, 3, 4]
             [(0, 1), (1, 2), (2, 3), (3, 4)]
             sage: I1 = g.subgraph_search(graphs.PathGraph(5), induced=True); I1
             Subgraph of (Petersen graph): Graph on 5 vertices
             sage: I1.vertices(sort=True); I1.edges(sort=True, labels=False)
             [0, 1, 2, 3, 8]
             [(0, 1), (1, 2), (2, 3), (3, 8)]

        It also contains the claw `K_{1,3}`::

             sage: h2 = g.subgraph_search(graphs.ClawGraph()); h2
             Subgraph of (Petersen graph): Graph on 4 vertices
             sage: h2.vertices(sort=True); h2.edges(sort=True, labels=False)
             [0, 1, 4, 5]
             [(0, 1), (0, 4), (0, 5)]
             sage: I2 = g.subgraph_search(graphs.ClawGraph(), induced=True); I2
             Subgraph of (Petersen graph): Graph on 4 vertices
             sage: I2.vertices(sort=True); I2.edges(sort=True, labels=False)
             [0, 1, 4, 5]
             [(0, 1), (0, 4), (0, 5)]

        Of course the induced copies are isomorphic to the graphs we were
        looking for::

             sage: I1.is_isomorphic(graphs.PathGraph(5))
             True
             sage: I2.is_isomorphic(graphs.ClawGraph())
             True

        However, the Petersen graph does not contain a subgraph isomorphic to
        `K_3`::

             sage: g.subgraph_search(graphs.CompleteGraph(3)) is None
             True

        Nor does it contain a nonempty induced subgraph isomorphic to `P_6`::

             sage: g.subgraph_search(graphs.PathGraph(6), induced=True) is None
             True

        The empty graph is a subgraph of every graph::

             sage: g.subgraph_search(graphs.EmptyGraph())
             Graph on 0 vertices
             sage: g.subgraph_search(graphs.EmptyGraph(), induced=True)
             Graph on 0 vertices

        The subgraph may just have edges missing::

            sage: k3 = graphs.CompleteGraph(3); p3 = graphs.PathGraph(3)
            sage: k3.relabel(list('abc'))
            sage: s = k3.subgraph_search(p3)
            sage: s.edges(sort=True, labels=False)
            [('a', 'b'), ('b', 'c')]

        Of course, `P_3` is not an induced subgraph of `K_3`, though::

            sage: k3 = graphs.CompleteGraph(3); p3 = graphs.PathGraph(3)
            sage: k3.relabel(list('abc'))
            sage: k3.subgraph_search(p3, induced=True) is None
            True

        If the graph has labels, the labels are just ignored::

            sage: g.set_vertex(0, 'foo')
            sage: c = g.subgraph_search(graphs.PathGraph(5))
            sage: c.get_vertices()
            {0: 'foo', 1: None, 2: None, 3: None, 4: None}

        TESTS:

        Inside of a small graph (:trac:`13906`)::

            sage: Graph(5).subgraph_search(Graph(1))
            Graph on 1 vertex

        For labelled edges (:trac:`14999`)::

            sage: G = graphs.CompleteGraph(10)
            sage: C = G.subgraph_search(graphs.CycleGraph(4))
            sage: C.size()
            4
            sage: C.edges(sort=True)
            [(0, 1, None), (0, 3, None), (1, 2, None), (2, 3, None)]

            sage: for (u,v) in G.edges(sort=True, labels=False):
            ....:     G.set_edge_label(u, v, u)

            sage: C = G.subgraph_search(graphs.CycleGraph(4))
            sage: C.edges(sort=True)
            [(0, 1, 0), (0, 3, 0), (1, 2, 1), (2, 3, 2)]

        """
        # return the first graph found by method subgraph_search_iterator
        for g in self.subgraph_search_iterator(G, induced=induced, return_graphs=True):
            return g

    def subgraph_search_count(self, G, induced=False):
        r"""
        Return the number of labelled occurrences of ``G`` in ``self``.

        INPUT:

        - ``G`` -- the (di)graph whose copies we are looking for in ``self``

        - ``induced`` -- boolean (default: ``False``); whether or not to count
          induced copies of ``G`` in ``self``

        .. NOTE::

            The vertex labels and the edge labels in the graph are ignored.

        ALGORITHM:

        See the documentation of
        :class:`~sage.graphs.generic_graph_pyx.SubgraphSearch`.

        .. SEEALSO::

            - :meth:`~GenericGraph.subgraph_search` -- finds an subgraph
              isomorphic to `H` inside of a graph `G`

            - :meth:`~GenericGraph.subgraph_search_iterator` -- iterator over
              the copies of a graph `H` inside of a graph `G`

        EXAMPLES:

        Counting the number of paths `P_5` in a PetersenGraph::

            sage: g = graphs.PetersenGraph()
            sage: g.subgraph_search_count(graphs.PathGraph(5))
            240

        Requiring these subgraphs be induced::

            sage: g.subgraph_search_count(graphs.PathGraph(5), induced=True)
            120

        If we define the graph `T_k` (the transitive tournament on `k` vertices)
        as the graph on `\{0, ..., k-1\}` such that `ij \in T_k` if `i<j`, how
        many directed triangles can be found in `T_5` ? The answer is of course
        `0`::

             sage: T5 = digraphs.TransitiveTournament(5)
             sage: T5.subgraph_search_count(digraphs.Circuit(3))
             0

        If we count instead the number of `T_3` in `T_5`, we expect
        the answer to be `\binom{5}{3}`::

             sage: T3 = digraphs.TransitiveTournament(3)
             sage: T5.subgraph_search_count(T3)
             10
             sage: binomial(5,3)
             10
             sage: T3.is_isomorphic(T5.subgraph(vertices=[0, 1, 2]))
             True

        The empty graph is a subgraph of every graph::

            sage: g.subgraph_search_count(graphs.EmptyGraph())
            1

        If the graph has vertex labels or edge labels, the label is just ignored::

            sage: g.set_vertex(0, 'foo')
            sage: g.subgraph_search_count(graphs.PathGraph(5))
            240

        TESTS:

        Inside of a small graph (:trac:`13906`)::

            sage: Graph(5).subgraph_search_count(Graph(1))
            5
        """
        from sage.graphs.generic_graph_pyx import SubgraphSearch

        if not G.order():
            return 1

        if self.order() < G.order():
            return 0

        if G.order() == 1:
            return self.order()

        S = SubgraphSearch(self, G, induced=induced)

        return S.cardinality()

    def subgraph_search_iterator(self, G, induced=False, return_graphs=True):
        r"""
        Return an iterator over the labelled copies of ``G`` in ``self``.

        INPUT:

        - ``G`` -- the graph whose copies we are looking for in ``self``

        - ``induced`` -- boolean (default: ``False``); whether or not to iterate
          over the induced copies of ``G`` in ``self``

        - ``return_graphs`` -- boolean (default: ``True``); whether to return
          (di)graphs or only the list of vertices of the found (di)graphs

        .. NOTE::

            The vertex labels and the edge labels in the graph are ignored.

        ALGORITHM:

        See the documentation of
        :class:`~sage.graphs.generic_graph_pyx.SubgraphSearch`.

        OUTPUT:

        Iterator over the labelled copies of ``G`` in ``self``, as *lists* or
        *(di)graphs*. For each value `(v_1, v_2, ..., v_k)` returned, the first
        vertex of `G` is associated with `v_1`, the second with `v_2`, etc.

        .. NOTE::

            This method works on :class:`~sage.graphs.graph.Graph`,
            :class:`~sage.graphs.digraph.DiGraph` and
            :class:`~sage.graphs.bipartite_graph.BipartiteGraph`.

        .. SEEALSO::

            - :meth:`~GenericGraph.subgraph_search` -- finds an subgraph
              isomorphic to `H` inside of `G`

            - :meth:`~GenericGraph.subgraph_search_count` -- counts the number
              of copies of `H` inside of `G`

        EXAMPLES:

        Iterating through all the labelled `P_3` of `P_5`::

            sage: g = graphs.PathGraph(5)
            sage: P3 = graphs.PathGraph(3)
            sage: for p in g.subgraph_search_iterator(P3, return_graphs=False):
            ....:     print(p)
            [0, 1, 2]
            [1, 2, 3]
            [2, 1, 0]
            [2, 3, 4]
            [3, 2, 1]
            [4, 3, 2]
            sage: for p in g.subgraph_search_iterator(P3, return_graphs=True):
            ....:     print(p)
            Subgraph of (Path graph)
            Subgraph of (Path graph)
            Subgraph of (Path graph)
            Subgraph of (Path graph)
            Subgraph of (Path graph)
            Subgraph of (Path graph)
            sage: all(h.is_isomorphic(P3) for h in g.subgraph_search_iterator(P3))
            True

        If the graph has vertex labels or edge labels, the label is just ignored::

            sage: g.set_vertex(0, 'foo')
            sage: for p in g.subgraph_search_iterator(P3, return_graphs=False):
            ....:     print(p)
            [0, 1, 2]
            [1, 2, 3]
            [2, 1, 0]
            [2, 3, 4]
            [3, 2, 1]
            [4, 3, 2]

        Search for induced subgraphs::

            sage: H = graphs.HouseGraph()
            sage: P4 = graphs.PathGraph(4)
            sage: all(h.is_isomorphic(P4) for h in H.subgraph_search_iterator(P4, induced=True))
            True
            sage: sum(1 for h in H.subgraph_search_iterator(P4, induced=True))
            4
            sage: sum(1 for h in H.subgraph_search_iterator(P4, induced=False))
            20

        Search for subdigraphs::

            sage: H = digraphs.Complete(5)
            sage: P4 = digraphs.Path(4)
            sage: sum(1 for _ in H.subgraph_search_iterator(P4, induced=True))
            0
            sage: sum(1 for _ in H.subgraph_search_iterator(P4, induced=False))
            120

        This method also works for bipartite graphs::

            sage: K33 = BipartiteGraph(graphs.CompleteBipartiteGraph(3, 3))
            sage: K22 = BipartiteGraph(graphs.CompleteBipartiteGraph(2, 2))
            sage: sum(1 for _ in K33.subgraph_search_iterator(K22))
            72

        TESTS:

        Inside of a small graph (:trac:`13906`)::

            sage: list(Graph(5).subgraph_search_iterator(Graph(1)))
            [Graph on 1 vertex, Graph on 1 vertex, Graph on 1 vertex, Graph on 1 vertex, Graph on 1 vertex]

        Check that the behavior of the method is consistent (:trac:`34004`)::

            sage: g = graphs.CycleGraph(3)
            sage: for i in range(3):
            ....:     g.subgraph_search_iterator(graphs.PathGraph(i))
            <generator object GenericGraph.subgraph_search_iterator...
            <generator object GenericGraph.subgraph_search_iterator...
            <generator object GenericGraph.subgraph_search_iterator...
            sage: for i in range(3):
            ....:     g.subgraph_search_iterator(graphs.PathGraph(i), return_graphs=False)
            <generator object GenericGraph.subgraph_search_iterator...
            <generator object GenericGraph.subgraph_search_iterator...
            <generator object GenericGraph.subgraph_search_iterator...

        Corner cases::

            sage: list(Graph().subgraph_search_iterator(graphs.PathGraph(2)))
            []
            sage: list(Graph(1).subgraph_search_iterator(graphs.PathGraph(2)))
            []
            sage: list(Graph(2).subgraph_search_iterator(graphs.PathGraph(2)))
            []

        Check the type of yielded graphs::

            sage: H = graphs.HouseGraph()
            sage: P4 = graphs.PathGraph(4)
            sage: for g in H.subgraph_search_iterator(P4, return_graphs=True):
            ....:     print(type(g))
            ....:     break
            <class 'sage.graphs.graph.Graph'>
            sage: K4 = digraphs.Complete(4)
            sage: K3 = digraphs.Complete(3)
            sage: for g in K4.subgraph_search_iterator(K3, return_graphs=True):
            ....:     print(type(g))
            ....:     break
            <class 'sage.graphs.digraph.DiGraph'>
            sage: K33 = BipartiteGraph(graphs.CompleteBipartiteGraph(3, 3))
            sage: K22 = BipartiteGraph(graphs.CompleteBipartiteGraph(2, 2))
            sage: for b in K33.subgraph_search_iterator(K22, return_graphs=True):
            ....:     print(type(b))
            ....:     break
            <class 'sage.graphs.bipartite_graph.BipartiteGraph'>
            sage: P5 = graphs.PathGraph(5)
            sage: for b in K33.subgraph_search_iterator(P5, return_graphs=True):
            ....:     print(type(b))
            ....:     break
            <class 'sage.graphs.bipartite_graph.BipartiteGraph'>
            sage: for b in Graph(K33).subgraph_search_iterator(K22, return_graphs=True):
            ....:     print(type(b))
            ....:     break
            <class 'sage.graphs.graph.Graph'>
        """
        self._scream_if_not_simple()
        G._scream_if_not_simple()
        if self.is_directed() and not G.is_directed():
            raise ValueError("cannot search for a graph in a digraph")
        if not self.is_directed() and G.is_directed():
            raise ValueError("cannot search for a digraph in a graph")
        DoG = self.__class__
        if not G.order():
            yield DoG() if return_graphs else []
        elif self.order() < G.order() or self.size() < G.size():
            return
        elif G.order() == 1:
            for v in self:
                if return_graphs:
                    yield DoG([[v], []], format='vertices_and_edges')
                else:
                    yield [v]
        else:
            from sage.graphs.generic_graph_pyx import SubgraphSearch
            for g in SubgraphSearch(self, G, induced=induced):
                if not return_graphs:
                    yield g
                elif induced:
                    yield self.subgraph(g)
                else:
                    G_to_g = dict(zip(G, g))
                    yield self.subgraph(g, edges=[(G_to_g[u], G_to_g[v])
                                                  for u, v in G.edge_iterator(labels=False)])

    def random_subgraph(self, p, inplace=False):
        """
        Return a random subgraph containing each vertex with probability ``p``.

        INPUT:

        - ``p`` -- the probability of choosing a vertex

        - ``inplace`` -- boolean (default: ``False``); using ``inplace=True``
          will simply delete the extra vertices and edges from the current
          graph. This will modify the graph.

        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: P.random_subgraph(.25)
            Subgraph of (Petersen graph): Graph on ... vert...
        """
        p = float(p)
        if p < 0 or p > 1:
            raise ValueError("a probability must be in range [0..1]")
        vertices = [v for v in self if random() < p]
        return self.subgraph(vertices=vertices, inplace=inplace)

    def is_chordal(self, certificate=False, algorithm="B"):
        r"""
        Check whether the given graph is chordal.

        A Graph `G` is said to be chordal if it contains no induced hole (a
        cycle of length at least 4).

        Alternatively, chordality can be defined using a Perfect Elimination
        Order :

        A Perfect Elimination Order of a graph `G` is an ordering `v_1,...,v_n`
        of its vertex set such that for all `i`, the neighbors of `v_i` whose
        index is greater that `i` induce a complete subgraph in `G`. Hence, the
        graph `G` can be totally erased by successively removing vertices whose
        neighborhood is a clique (also called *simplicial* vertices)
        [FG1965]_.

        (It can be seen that if `G` contains an induced hole, then it cannot
        have a perfect elimination order. Indeed, if we write `h_1,...,h_k` the
        `k` vertices of such a hole, then the first of those vertices to be
        removed would have two non-adjacent neighbors in the graph.)

        A Graph is then chordal if and only if it has a Perfect Elimination
        Order.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate.

          * If ``certificate = False`` (default), returns ``True`` or ``False``
            accordingly.

          * If ``certificate = True``, returns :

            * ``(True, peo)`` when the graph is chordal, where ``peo`` is a
              perfect elimination order of its vertices.

            * ``(False, Hole)`` when the graph is not chordal, where ``Hole`` (a
              ``Graph`` object) is an induced subgraph of ``self`` isomorphic to
              a hole.

        - ``algorithm`` -- string (default: ``"B"``); the algorithm to choose
          among ``"A"`` or ``"B"`` (see next section). While they will agree on
          whether the given graph is chordal, they cannot be expected to return
          the same certificates.

        ALGORITHM:

        This algorithm works through computing a Lex BFS on the graph, then
        checking whether the order is a Perfect Elimination Order by computing
        for each vertex `v` the subgraph induces by its non-deleted neighbors,
        then testing whether this graph is complete.

        This problem can be solved in `O(m)` [RT1975]_ ( where `m` is the number
        of edges in the graph ) but this implementation is not linear because of
        the complexity of Lex BFS.

        EXAMPLES:

        The lexicographic product of a Path and a Complete Graph
        is chordal ::

            sage: g = graphs.PathGraph(5).lexicographic_product(graphs.CompleteGraph(3))
            sage: g.is_chordal()
            True

        The same goes with the product of a random lobster (which is a tree)
        and a Complete Graph ::

            sage: g = graphs.RandomLobster(10, .5, .5).lexicographic_product(graphs.CompleteGraph(3))
            sage: g.is_chordal()
            True

        The disjoint union of chordal graphs is still chordal::

            sage: (2 * g).is_chordal()
            True

        Let us check the certificate given by Sage is indeed a perfect
        elimination order::

            sage: _, peo = g.is_chordal(certificate=True)
            sage: for v in peo:
            ....:     if not g.subgraph(g.neighbors(v)).is_clique():
            ....:          raise ValueError("this should never happen")
            ....:     g.delete_vertex(v)

        Of course, the Petersen Graph is not chordal as it has girth 5::

            sage: g = graphs.PetersenGraph()
            sage: g.girth()
            5
            sage: g.is_chordal()
            False

        We can even obtain such a cycle as a certificate::

            sage: _, hole = g.is_chordal(certificate=True)
            sage: hole
            Subgraph of (Petersen graph): Graph on 5 vertices
            sage: hole.is_isomorphic(graphs.CycleGraph(5))
            True

        TESTS:

        This should not raise exceptions (:trac:`10899`)::

            sage: Graph(1).is_chordal()
            True
            sage: for g in graphs(5):
            ....:     _ = g.is_chordal()

        :trac:`11735`::

           sage: g = Graph({3: [2, 1, 4], 2: [1], 4: [1], 5: [2, 1, 4]})
           sage: _, g1 = g.is_chordal(certificate=True); g1.is_chordal()
           False
           sage: g1.is_isomorphic(graphs.CycleGraph(g1.order()))
           True
        """
        if algorithm not in ['A', 'B']:
            raise ValueError('unknown algorithm "{}"'.format(algorithm))

        self._scream_if_not_simple()

        # If the graph is not connected, we are computing the result on each
        # component
        if not self.is_connected():

            # If the user wants a certificate, we had no choice but to collect
            # the perfect elimination orders... But we return a hole immediately
            # if we find any !
            if certificate:
                peo = []
                for gg in self.connected_components_subgraphs():

                    b, certif = gg.is_chordal(certificate=True)
                    if not b:
                        return False, certif
                    else:
                        peo.extend(certif)

                return True, peo

            # One line if no certificate is requested
            else:
                return all(gg.is_chordal() for gg in self.connected_components_subgraphs())

        hole = None
        g = copy(self)

        # Algorithms
        #
        # They find the perfect elimination ordering or produce a hole

        if algorithm == "A":

            peo, t_peo = self.lex_BFS(tree=True)
            peo.reverse()

            # Iteratively removing vertices and checking everything is fine.
            for v in peo:

                if not t_peo.out_degree(v):
                    g.delete_vertex(v)
                    continue

                x = next(t_peo.neighbor_out_iterator(v))
                S = self.neighbors(x) + [x]

                if not frozenset(g.neighbor_iterator(v)).issubset(S):

                    # Do we need to return a hole ?
                    if certificate:

                        # In this case, let us take two nonadjacent neighbors of
                        # v. In order to do so, we pick a vertex y which is a
                        # neighbor of v but is not adjacent to x, which we know
                        # exists by the test written two lines above.

                        for y in g.neighbors(v):
                            if y not in S:
                                break

                        g.delete_vertices([vv for vv in g.neighbor_iterator(v) if vv != y and vv != x])
                        g.delete_vertex(v)

                        # Our hole is v + (a shortest path between x and y not
                        # containing v or any of its neighbors).

                        hole = self.subgraph(vertices=[v] + g.shortest_path(x, y))

                        # End of the algorithm
                        break
                    else:
                        return False

                g.delete_vertex(v)

        elif algorithm == "B":

            peo, t_peo = self.lex_BFS(reverse=True, tree=True)

            # Remembering the (closed) neighborhoods of each vertex
            neighbors_subsets = {v: frozenset(self.neighbors(v) + [v]) for v in g}
            pos_in_peo = dict(zip(peo, range(self.order())))

            # Iteratively removing vertices and checking everything is fine.
            for v in reversed(peo):

                if (t_peo.out_degree(v) and
                    not frozenset(v1 for v1 in g.neighbor_iterator(v) if pos_in_peo[v1] > pos_in_peo[v]).issubset(
                        neighbors_subsets[next(t_peo.neighbor_out_iterator(v))])):

                    # Do we need to return a hole ?
                    if certificate:

                        # In this case, let us take two nonadjacent neighbors of
                        # v. In order to do so, we pick a vertex y which is a
                        # neighbor of v but is not adjacent to x, which we know
                        # exists by the test written two lines above.
                        max_tup = (-1, 0)
                        nb1 = [u for u in g.neighbor_iterator(v) if pos_in_peo[u] > pos_in_peo[v]]
                        for xi in nb1:
                            for yi in nb1:
                                if yi not in neighbors_subsets[xi]:
                                    new_tup = (pos_in_peo[xi], pos_in_peo[yi])
                                    if max_tup < new_tup:
                                        max_tup = new_tup
                                        x, y = xi, yi

                        # Our hole is v + (a shortest path between x and y not
                        # containing v or any of its neighbors).

                        # g.delete_vertices([vv for vv in g.vertices() if pos_in_peo[vv] < pos_in_peo[v]])

                        g.delete_vertices([vv for vv in g.neighbor_iterator(v) if vv != y and vv != x])
                        g.delete_vertex(v)

                        hole = self.subgraph(vertices=[v] + g.shortest_path(x, y))

                        # End of the algorithm
                        break
                    else:
                        return False

        # Returning values
        # ----------------

        # 1- The graph is not chordal
        if hole is not None:
            # There was a bug there once, so it's better to check the
            # answer is valid, especially when it is so cheap ;-)

            if hole.order() <= 3 or not hole.is_regular(k=2):
                raise RuntimeError("the graph is not chordal, and something went wrong "
                                   "in the computation of the certificate. Please report "
                                   "this bug, providing the graph if possible")

            return (False, hole)

        # 2- The graph is chordal
        if certificate:
            return True, peo

        else:
            return True

    def is_circulant(self, certificate=False):
        r"""
        Check whether the graph is circulant.

        For more information, see :wikipedia:`Circulant_graph`.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return a
          certificate for yes-answers (see OUTPUT section)

        OUTPUT:

        When ``certificate`` is set to ``False`` (default) this method only
        returns ``True`` or ``False`` answers. When ``certificate`` is set to
        ``True``, the method either returns ``(False, None)`` or ``(True,
        lists_of_parameters)`` each element of ``lists_of_parameters`` can be
        used to define the graph as a circulant graph.

        See the documentation of
        :func:`~sage.graphs.graph_generators.GraphGenerators.CirculantGraph` and
        :meth:`~sage.graphs.digraph_generators.DiGraphGenerators.Circulant` for
        more information, and the examples below.

        .. SEEALSO::

            :meth:`~sage.graphs.graph_generators.GraphGenerators.CirculantGraph`
            -- a constructor for circulant graphs.

        EXAMPLES:

        The Petersen graph is not a circulant graph::

            sage: g = graphs.PetersenGraph()
            sage: g.is_circulant()
            False

        A cycle is obviously a circulant graph, but several sets of parameters
        can be used to define it::

            sage: g = graphs.CycleGraph(5)
            sage: g.is_circulant(certificate=True)
            (True, [(5, [1, 4]), (5, [2, 3])])

        The same goes for directed graphs::

            sage: g = digraphs.Circuit(5)
            sage: g.is_circulant(certificate=True)
            (True, [(5, [1]), (5, [3]), (5, [2]), (5, [4])])

        With this information, it is very easy to create (and plot) all possible
        drawings of a circulant graph::

            sage: g = graphs.CirculantGraph(13, [2, 3, 10, 11])
            sage: for param in g.is_circulant(certificate=True)[1]:
            ....:    graphs.CirculantGraph(*param)
            Circulant graph ([2, 3, 10, 11]): Graph on 13 vertices
            Circulant graph ([1, 5, 8, 12]): Graph on 13 vertices
            Circulant graph ([4, 6, 7, 9]): Graph on 13 vertices

        TESTS::

            sage: digraphs.DeBruijn(3,1).is_circulant(certificate=True)
            (True, [(3, [0, 1, 2])])
            sage: Graph(1).is_circulant(certificate=True)
            (True, (1, []))
            sage: Graph(0).is_circulant(certificate=True)
            (True, (0, []))
            sage: Graph({0: [0]}).is_circulant(certificate=True)
            (True, (1, [0]))
        """
        self._scream_if_not_simple(allow_loops=True)
        # Stupid cases
        if self.order() <= 1:
            if certificate:
                return (True, (self.order(), [0] if self.size() else []))
            else:
                return True

        certif_list = []

        # The automorphism group, the translation between the vertices of self
        # and 1..n, and the orbits.
        ag, orbits = self.automorphism_group([list(self)],
                                             order=False,
                                             return_group=True,
                                             orbits=True)

        # Not transitive ? Not a circulant graph !
        if len(orbits) != 1:
            return (False, None) if certificate else False

        # We go through all conjugacy classes of the automorphism
        # group, and only keep the cycles of length n
        for e in ag.conjugacy_classes_representatives():
            cycles = e.cycle_tuples()

            # If the automorphism is not the identity and has exactly one
            # cycle that contains all vertices.
            if not cycles or len(cycles[0]) != self.order():
                continue

            # From now on the graph is a circulant graph !

            if not certificate:
                return True

            # We build the list of integers defining the circulant graph, and
            # add it to the list.
            cycle = cycles[0]
            u = cycle[0]
            integers = [i for i, v in enumerate(cycle) if self.has_edge(u, v)]
            certif_list.append((self.order(), integers))

        if not certificate:
            return False
        else:
            if certif_list:
                return (True, certif_list)
            else:
                return (False, None)

    def is_interval(self, certificate=False):
        r"""
        Check whether the graph is an interval graph.

        An *interval graph* is one where every vertex can be seen as
        an interval on the real line so that there is an edge in the graph
        iff the corresponding intervals intersects.

        See the :wikipedia:`Interval_graph` for more information.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``);

          - When ``certificate=False``, returns ``True`` is the graph is an
            interval graph and ``False`` otherwise

          - When ``certificate=True``, returns either ``(False, None)`` or
            ``(True, d)`` where ``d`` is a dictionary whose keys are the
            vertices and values are pairs of integers.  They correspond to an
            embedding of the interval graph, each vertex being represented by an
            interval going from the first of the two values to the second.

        ALGORITHM:

        Through the use of PQ-Trees.

        AUTHOR:

        Nathann Cohen (implementation)

        EXAMPLES::

            sage: g = Graph({1: [2, 3, 4], 4: [2, 3]})
            sage: g.is_interval()
            True
            sage: g.is_interval(certificate=True)
            (True, {1: (0, 5), 2: (4, 6), 3: (1, 3), 4: (2, 7)})

        The Petersen Graph is not chordal, so it cannot be an interval graph::

            sage: g = graphs.PetersenGraph()
            sage: g.is_interval()
            False

        A chordal but still not an interval graph::

            sage: g = Graph({1: [4, 2, 3], 2: [3, 5], 3: [6]})
            sage: g.is_interval()
            False

        .. SEEALSO::

            - :mod:`Interval Graph Recognition <sage.graphs.pq_trees>`.

            - :meth:`PQ <sage.graphs.pq_trees.PQ>` -- implementation of PQ-Trees
            - :meth:`is_chordal`
            - :meth:`~sage.graphs.graph_generators.GraphGenerators.IntervalGraph`
            - :meth:`~sage.graphs.graph_generators.GraphGenerators.RandomIntervalGraph`

        TESTS::

            sage: E = Graph()
            sage: E.is_interval()
            True
            sage: E.is_interval(certificate=True)
            (True, {})

            sage: graphs.CycleGraph(4).is_interval(certificate=True)
            (False, None)

        Enumerate all small interval graphs (see :oeis:`A005975`)::

            sage: [sum(1 for g in graphs(i) if g.is_interval()) for i in range(8)]  # long time
            [1, 1, 2, 4, 10, 27, 92, 369]

        Test certificate on a larger graph by re-doing isomorphic graph::

            sage: s6 = ':S__@_@A_@AB_@AC_@ACD_@ACDE_ACDEF_ACDEFG_ACDEGH_ACDEGHI'
            sage: s6 += '_ACDEGHIJ_ACDEGIJK_ACDEGIJKL_ACDEGIJKLMaCEGIJKNaCEGIJK'
            sage: s6 += 'NaCGIJKNPaCIP'
            sage: g = Graph(s6, loops=False, multiedges=False)
            sage: d = g.is_interval(certificate=True)[1]
            sage: g2 = graphs.IntervalGraph(d.values())
            sage: g2.is_isomorphic(g)
            True
        """
        self._scream_if_not_simple()

        # An interval graph is a chordal graph. Without this, there is no
        # telling how we should find its maximal cliques, by the way :-)
        if not self.is_chordal():
            return (False, None) if certificate else False

        # First, we need to gather the list of maximal cliques, which is easy as
        # the graph is chordal
        cliques = []

        # As we will be deleting vertices ...
        g = copy(self)

        for cc in g.connected_components_subgraphs():

            # We pick a perfect elimination order for every connected
            # component. We will then iteratively take the last vertex in the
            # order (a simplicial vertex) and consider the clique it forms with
            # its neighbors. If we do not have an inclusion-wise larger clique
            # in our list, we add it !
            peo = cc.lex_BFS()

            while peo:
                v = peo.pop()
                clique = frozenset([v] + cc.neighbors(v))
                cc.delete_vertex(v)

                if not any(clique.issubset(c) for c in cliques):
                    cliques.append(clique)

        from sage.graphs.pq_trees import reorder_sets

        try:
            ordered_sets = reorder_sets(cliques)
            if not certificate:
                return True

        except ValueError:
            return (False, None) if certificate else False

        # We are now listing the maximal cliques in the given order,
        # and keeping track of the vertices appearing/disappearing

        current = set()
        beg = {}
        end = {}

        i = 0

        ordered_sets.append([])
        for S in map(set, ordered_sets):
            for v in current - S:
                end[v] = i
                i += 1

            for v in S - current:
                beg[v] = i
                i += 1

            current = S

        return (True, {v: (beg[v], end[v]) for v in self})

    def is_gallai_tree(self):
        r"""
        Return whether the current graph is a Gallai tree.

        A graph is a Gallai tree if and only if it is connected and its
        `2`-connected components are all isomorphic to complete graphs or odd
        cycles.

        A connected graph is not degree-choosable if and only if it is a Gallai
        tree [ERT1979]_.

        EXAMPLES:

        A complete graph is, or course, a Gallai Tree::

            sage: g = graphs.CompleteGraph(15)
            sage: g.is_gallai_tree()
            True

        The Petersen Graph is not::

            sage: g = graphs.PetersenGraph()
            sage: g.is_gallai_tree()
            False

        A Graph built from vertex-disjoint complete graphs linked by one edge to
        a special vertex `-1` is a ''star-shaped'' Gallai tree::

            sage: g = 8 * graphs.CompleteGraph(6)
            sage: g.add_edges([(-1, c[0]) for c in g.connected_components()])
            sage: g.is_gallai_tree()
            True

        TESTS:

        Check that :trac:`25613` is fixed::

            sage: g = graphs.CycleGraph(5)
            sage: g.add_edge(0, 5)
            sage: g.is_gallai_tree()
            True
        """
        self._scream_if_not_simple()
        if not self.is_connected():
            return False

        for c in self.blocks_and_cut_vertices()[0]:
            gg = self.subgraph(c)
            #       is it an odd cycle ?              a complete graph ?
            if not ((len(c) % 2 and gg.size() == len(c)) or gg.is_clique()):
                return False

        return True

    def is_clique(self, vertices=None, directed_clique=False, induced=True, loops=False):
        """
        Check whether a set of vertices is a clique

        A clique is a set of vertices such that there is exactly one edge
        between any two vertices.

        INPUT:

        - ``vertices`` -- a single vertex or an iterable container of vertices
          (default: ``None); when set, check whether the set of vertices is a
          clique, otherwise check whether ``self`` is a clique

        - ``directed_clique`` -- boolean (default: ``False``); if set to
          ``False``, only consider the underlying undirected graph. If set to
          ``True`` and the graph is directed, only return ``True`` if all
          possible edges in _both_ directions exist.

        - ``induced`` -- boolean (default: ``True``); if set to ``True``, check
          that the graph has exactly one edge between any two vertices. If set
          to ``False``, check that the graph has at least one edge between any
          two vertices.

        - ``loops`` -- boolean (default: ``False``); if set to ``True``, check
          that each vertex of the graph has a loop, and exactly one if
          furthermore ``induced == True``. If set to ``False``, check that the
          graph has no loop when ``induced == True``, and ignore loops
          otherwise.

        EXAMPLES::

            sage: g = graphs.CompleteGraph(4)
            sage: g.is_clique([1, 2, 3])
            True
            sage: g.is_clique()
            True
            sage: h = graphs.CycleGraph(4)
            sage: h.is_clique([1, 2])
            True
            sage: h.is_clique([1, 2, 3])
            False
            sage: h.is_clique()
            False
            sage: i = digraphs.Complete(4)
            sage: i.delete_edge([0, 1])
            sage: i.is_clique(directed_clique=False, induced=True)
            False
            sage: i.is_clique(directed_clique=False, induced=False)
            True
            sage: i.is_clique(directed_clique=True)
            False

        TESTS:

        Check that :trac:`25696` is fixed::

            sage: G = Graph([(0, 1), (0, 1), (0, 1), (0, 3), (1, 2), (2, 3)], multiedges=True)
            sage: G.is_clique()
            False

        Check cases with loops or multiple edges::

            sage: G = Graph(multiedges=True, loops=True)
            sage: G.add_clique([0, 1, 2, 3])
            sage: G.is_clique(induced=True, loops=False)
            True
            sage: G.is_clique(induced=True, loops=True)
            False
            sage: G.is_clique(induced=False, loops=False)
            True
            sage: G.is_clique(induced=False, loops=True)
            False
            sage: G.add_edges([(0, 0)] * 4)
            sage: G.is_clique(induced=True, loops=False)
            False
            sage: G.is_clique(induced=True, loops=True)
            False
            sage: G.is_clique(induced=False, loops=False)
            True
            sage: G.is_clique(induced=False, loops=True)
            False
            sage: G.add_edges([(1, 1), (2, 2), (3, 3)])
            sage: G.is_clique(induced=True, loops=False)
            False
            sage: G.is_clique(induced=True, loops=True)
            False
            sage: G.is_clique(induced=False, loops=False)
            True
            sage: G.is_clique(induced=False, loops=True)
            True
            sage: G.delete_edges([(0, 0)] * 3)
            sage: G.is_clique(induced=True, loops=False)
            False
            sage: G.is_clique(induced=True, loops=True)
            True
            sage: G.is_clique(induced=False, loops=False)
            True
            sage: G.is_clique(induced=False, loops=True)
            True

        Giving a set of vertices that is not a subset of the vertices of the
        graph::

            sage: g = Graph({1: [2]})
            sage: g.is_clique([1, 2, 3])
            False
        """
        if vertices is None:
            G = self
        elif vertices in self:
            G = self.subgraph(vertices, immutable=False)
        else:
            vertices = list(vertices)
            for u in vertices:
                if not self.has_vertex(u):
                    return False
            G = self.subgraph(vertices, immutable=False)

        N = G.order()
        if G.is_directed() and directed_clique:
            M = N*(N-1) + (N if loops else 0)
        else:
            M = N*(N-1)/2 + (N if loops else 0)

        # We check that the graph has a priori enough edges
        if G.size() < M or (induced and G.size() > M):
            return False

        if loops and not G.allows_loops():
            return False
        elif not loops and G.allows_loops():
            loop_edges = G.loop_edges(labels=False)
            if induced and loop_edges:
                return False

        if G.allows_multiple_edges() or (G.is_directed() and not directed_clique):
            # We check that we have edges between all pairs of vertices
            v_to_int = {v: i for i, v in enumerate(self)}
            if G.is_directed() and not directed_clique:
                def R(u, v):
                    return (u, v) if u <= v else (v, u)
            else:
                def R(u, v):
                    return (u, v)
            if loops:
                edges = set(R(v_to_int[u], v_to_int[v]) for u, v in G.edge_iterator(labels=False))
            else:
                edges = set(R(v_to_int[u], v_to_int[v]) for u, v in G.edge_iterator(labels=False) if u != v)

            # If induced == True, we already know that G.size() == M, so
            # we only need to check that we have the right set of edges.
            return len(edges) >= M

        else:
            # The graph is simple
            if G.allows_loops() and not induced and not loops:
                return G.size() - len(loop_edges) == M

            return G.size() == M

    def is_cycle(self, directed_cycle=True):
        r"""
        Check whether ``self`` is a (directed) cycle graph.

        We follow the definition provided in [BM2008]_ for undirected graphs. A
        cycle on three or more vertices is a simple graph whose vertices can be
        arranged in a cyclic order so that two vertices are adjacent if they are
        consecutive in the order, and not adjacent otherwise. A cycle on a
        vertex consists of a single vertex provided with a loop and a cycle with
        two vertices consists of two vertices connected by a pair of parallel
        edges. In other words, an undirected graph is a cycle if it is 2-regular
        and connected. The empty graph is not a cycle.

        For directed graphs, a directed cycle, or circuit, on two or more
        vertices is a strongly connected directed graph without loops nor
        multiple edges with has many arcs as vertices. A circuit on a vertex
        consists of a single vertex provided with a loop.

        INPUT:

        - ``directed_cycle`` -- boolean (default: ``True``); if set to ``True``
          and the graph is directed, only return ``True`` if ``self`` is a
          directed cycle graph (i.e., a circuit). If set to ``False``, we ignore
          the direction of edges and so opposite arcs become multiple (parallel)
          edges. This parameter is ignored for undirected graphs.

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: G.is_cycle()
            False
            sage: graphs.CycleGraph(5).is_cycle()
            True
            sage: Graph([(0,1 )]).is_cycle()
            False
            sage: Graph([(0, 1), (0, 1)], multiedges=True).is_cycle()
            True
            sage: Graph([(0, 1), (0, 1), (0, 1)], multiedges=True).is_cycle()
            False
            sage: Graph().is_cycle()
            False
            sage: G = Graph([(0, 0)], loops=True)
            sage: G.is_cycle()
            True
            sage: digraphs.Circuit(3).is_cycle()
            True
            sage: digraphs.Circuit(2).is_cycle()
            True
            sage: digraphs.Circuit(2).is_cycle(directed_cycle=False)
            True
            sage: D = DiGraph(graphs.CycleGraph(3))
            sage: D.is_cycle()
            False
            sage: D.is_cycle(directed_cycle=False)
            False
            sage: D.edges(sort=True, labels=False)
            [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        """
        if not self.order():
            # The empty graph is not a cycle
            return False
        elif self.order() == 1:
            # A (di)graph of order one is a cycle if it has a single loop
            return self.size() == 1

        g = self
        if g._directed:
            if directed_cycle:
                return g.order() == g.size() and g.is_strongly_connected()
            else:
                # We make a copy of self ignoring the direction of edges
                from sage.graphs.graph import Graph
                g = Graph(multiedges=True, loops=True)
                g.add_edges(self.edge_iterator(labels=False))

        return g.is_regular(k=2) and g.is_connected()

    def is_independent_set(self, vertices=None):
        """
        Check whether ``vertices`` is an independent set of ``self``.

        An independent set is a set of vertices such that there is no edge
        between any two vertices.

        INPUT:

        - ``vertices`` -- a single vertex or an iterable container of vertices
          (default: ``None); when set, check whether the given set of vertices
          is an independent set, otherwise, check whether the set of vertices of
          ``self`` is an independent set

        EXAMPLES::

            sage: graphs.CycleGraph(4).is_independent_set([1,3])
            True
            sage: graphs.CycleGraph(4).is_independent_set([1,2,3])
            False
        """
        if vertices is None:
            return not self.size()
        return not self.subgraph(vertices).size()

    def is_subgraph(self, other, induced=True, up_to_isomorphism=False):
        """
        Check whether ``self`` is a subgraph of ``other``.

        .. WARNING::

            The arguments ``induced`` and ``up_to_isomorphism`` are set
            respectively to ``True`` and ``False`` by default.

        INPUT:

        - ``other`` -- a Sage (Di)Graph

        - ``induced`` -- boolean (default: ``True``); if set to ``True`` check
          whether the graph is an *induced* subgraph of ``other`` that is if the
          vertices of the graph are also vertices of ``other``, and the edges of
          the graph are equal to the edges of ``other`` between the vertices
          contained in the graph.

          If set to ``False`` tests whether the graph is a subgraph of ``other``
          that is if all vertices of the graph are also in ``other`` and all
          edges of the graph are also in ``other``.

        - ``up_to_isomorphism`` -- boolean (default: ``False``); if set to
          ``True`` check whether ``other`` is a subgraph ignoring the labeling
          of vertices and edges. Otherwise, vertex and edge labellings must
          coincide in the copy or induced copy.

        OUTPUT:

        boolean -- ``True`` iff the graph is a (possibly induced) subgraph of
        ``other``.

        .. SEEALSO::

            For more advanced search of subgraphs isomorphic to a given graph,
            you could consider the following methods:

            - :meth:`~GenericGraph.subgraph_search` -- find a subgraph
              isomorphic to ``other`` inside of the graph

            - :meth:`~GenericGraph.subgraph_search_count` -- count the number
              of such copies

            - :meth:`~GenericGraph.subgraph_search_iterator` --
              iterator over all the copies of ``other`` contained in the graph

        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: G = P.subgraph(range(6))
            sage: G.is_subgraph(P)
            True

            sage: H = graphs.CycleGraph(5)
            sage: G = graphs.PathGraph(5)
            sage: G.is_subgraph(H)
            False
            sage: G.is_subgraph(H, induced=False)
            True
            sage: H.is_subgraph(G, induced=False)
            False

        The 4x4 grid contains a path of length 15 and an induced path of length
        11::

             sage: p11 = graphs.PathGraph(11)
             sage: p15 = graphs.PathGraph(15)
             sage: g = graphs.Grid2dGraph(4, 4)
             sage: p15.is_subgraph(g, induced=False, up_to_isomorphism=True)
             True
             sage: p15.is_subgraph(g, induced=True, up_to_isomorphism=True)
             False
             sage: p11.is_subgraph(g, induced=True, up_to_isomorphism=True)
             True

        TESTS:

        Raise an error when ``self`` and ``other`` are of different types::

            sage: Graph([(0, 1)]).is_subgraph(DiGraph([(0, 1)]))
            Traceback (most recent call last):
            ...
            ValueError: the input parameter must be a Graph
            sage: DiGraph([(0, 1)]).is_subgraph(Graph([(0, 1)]))
            Traceback (most recent call last):
            ...
            ValueError: the input parameter must be a DiGraph

        """
        from sage.graphs.graph import Graph
        from sage.graphs.digraph import DiGraph
        if isinstance(self, Graph) and not isinstance(other, Graph):
            raise ValueError('the input parameter must be a Graph')

        if isinstance(self, DiGraph) and not isinstance(other, DiGraph):
            raise ValueError('the input parameter must be a DiGraph')

        if self.num_verts() > other.num_verts() or self.num_edges() > other.num_edges():
            return False

        if up_to_isomorphism:
            return other.subgraph_search(self, induced=induced) is not None

        if not all(other.has_vertex(v) for v in self.vertex_iterator()):
            return False

        self._scream_if_not_simple()
        other._scream_if_not_simple()

        if induced:
            # Check whether ``self`` is contained in ``other``
            # and whether the induced subgraph of ``other`` is contained in ``self``.
            return (self._backend.is_subgraph(other._backend, self)
                    and other._backend.is_subgraph(self._backend, self))
        else:
            return self._backend.is_subgraph(other._backend, self)

    # Cluster

    def cluster_triangles(self, nbunch=None, implementation=None):
        r"""
        Return the number of triangles for the set `nbunch` of vertices as a
        dictionary keyed by vertex.

        See also section "Clustering" in chapter "Algorithms" of [HSS]_.

        INPUT:

        - ``nbunch`` -- a list of vertices (default: ``None); the vertices to
          inspect. If ``nbunch=None``, returns data for all vertices in the
          graph.

        - ``implementation`` -- string (default: ``None``); one of
          ``'sparse_copy'``, ``'dense_copy'``, ``'networkx'`` or ``None``
          (default). In the latter case, the best algorithm available is
          used. Note that ``'networkx'`` does not support directed graphs.

        EXAMPLES::

            sage: F = graphs.FruchtGraph()
            sage: list(F.cluster_triangles().values())
            [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0]
            sage: F.cluster_triangles()
            {0: 1, 1: 1, 2: 0, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 0, 9: 1, 10: 1, 11: 0}
            sage: F.cluster_triangles(nbunch=[0, 1, 2])
            {0: 1, 1: 1, 2: 0}

        ::

            sage: G = graphs.RandomGNP(20, .3)
            sage: d1 = G.cluster_triangles(implementation="networkx")
            sage: d2 = G.cluster_triangles(implementation="dense_copy")
            sage: d3 = G.cluster_triangles(implementation="sparse_copy")
            sage: d1 == d2 and d1 == d3
            True

        TESTS::

            sage: DiGraph().cluster_triangles(implementation="networkx")
            Traceback (most recent call last):
            ...
            ValueError: the 'networkx' implementation does not support directed graphs
            sage: Graph().cluster_triangles(implementation="welcome")
            Traceback (most recent call last):
            ...
            ValueError: the implementation can only be 'networkx', 'sparse_copy', 'dense_copy' or None
        """
        if implementation is None:
            from sage.graphs.base.dense_graph import DenseGraphBackend
            if isinstance(self._backend, DenseGraphBackend):
                implementation = 'dense_copy'
            else:
                implementation = 'sparse_copy'

        if implementation == 'networkx':
            if self.is_directed():
                raise ValueError("the 'networkx' implementation does not support directed graphs")
            import networkx
            return networkx.triangles(self.networkx_graph(), nbunch)

        elif implementation == 'sparse_copy':
            from sage.graphs.base.static_sparse_graph import triangles_count

        elif implementation == "dense_copy":
            from sage.graphs.base.static_dense_graph import triangles_count

        else:
            raise ValueError("the implementation can only be 'networkx', "
                             "'sparse_copy', 'dense_copy' or None")

        if nbunch is None:
            return triangles_count(self)
        return {v: c for v, c in triangles_count(self).items() if v in nbunch}

    def clustering_average(self, implementation=None):
        r"""
        Return the average clustering coefficient.

        The clustering coefficient of a node `i` is the fraction of existing
        triangles containing node `i` over all possible triangles containing
        `i`: `c_i = T(i) / \binom {k_i} 2` where `T(i)` is the number of
        existing triangles through `i`, and `k_i` is the degree of vertex `i`.

        A coefficient for the whole graph is the average of the `c_i`.

        See also section "Clustering" in chapter "Algorithms" of [HSS]_.

        INPUT:

        - ``implementation`` -- string (default: ``None``); one of ``'boost'``,
          ``'sparse_copy'``, ``'dense_copy'``, ``'networkx'`` or ``None``
          (default). In the latter case, the best algorithm available is
          used. Note that only ``'networkx'`` supports directed graphs.

        EXAMPLES::

            sage: (graphs.FruchtGraph()).clustering_average()
            1/4
            sage: (graphs.FruchtGraph()).clustering_average(implementation='networkx')
            0.25

        TESTS:

        Boost does not work with DiGraph::

            sage: digraphs.Circuit(10).clustering_average(implementation='boost')
            Traceback (most recent call last):
            ...
            ValueError: this value of 'implementation' is invalid for directed graphs

        The result is the same with all implementations::

            sage: G = graphs.RandomGNM(10,20)
            sage: coeffs = [G.clustering_average(implementation=impl)
            ....:           for impl in ['boost','sparse_copy','dense_copy','networkx']]
            sage: max(coeffs)-min(coeffs) # tol abs 1e-12
            0

        """
        if implementation is None:
            from sage.graphs.base.dense_graph import DenseGraphBackend
            if self.is_directed():
                implementation = 'networkx'
            elif isinstance(self._backend, DenseGraphBackend):
                implementation = 'dense_copy'
            else:
                implementation = 'sparse_copy'

        if implementation not in ['networkx', 'boost', 'dense_copy', 'sparse_copy']:
            raise ValueError("the implementation can only be 'networkx', "
                             "'boost', 'sparse_copy', 'dense_copy' or None")

        if self.is_directed() and implementation != 'networkx':
            raise ValueError("this value of 'implementation' is invalid for directed graphs")

        if implementation == 'boost':
            from sage.graphs.base.boost_graph import clustering_coeff
            return clustering_coeff(self)[0]
        elif implementation == 'networkx':
            import networkx
            return networkx.average_clustering(self.networkx_graph())
        else:
            coeffs = self.clustering_coeff(implementation=implementation)
            return sum(coeffs.values()) / len(coeffs)

    def clustering_coeff(self,
                         nodes=None,
                         weight=False,
                         implementation=None):
        r"""
        Return the clustering coefficient for each vertex in ``nodes`` as a
        dictionary keyed by vertex.

        For an unweighted graph, the clustering coefficient of a node `i` is the
        fraction of existing triangles containing node `i` over all possible
        triangles containing `i`: `c_i = T(i) / \binom {k_i} 2` where `T(i)` is
        the number of existing triangles through `i`, and `k_i` is the degree of
        vertex `i`.

        For weighted graphs the clustering is defined as the geometric average
        of the subgraph edge weights, normalized by the maximum weight in the
        network.

        The value of `c_i` is assigned `0` if `k_i < 2`.

        See also section "Clustering" in chapter "Algorithms" of [HSS]_.

        INPUT:

        - ``nodes`` -- an iterable container of vertices (default: ``None``);
          the vertices to inspect. By default, returns data on all vertices in
          graph

        - ``weight`` -- string or boolean (default: ``False``); if it is a
          string it uses the indicated edge property as weight.  ``weight =
          True`` is equivalent to ``weight = 'weight'``

        - ``implementation`` -- string (default: ``None``); one of ``'boost'``,
          ``'sparse_copy'``, ``'dense_copy'``, ``'networkx'`` or ``None``
          (default). In the latter case, the best algorithm available is
          used. Note that only ``'networkx'`` supports directed or weighted
          graphs, and that ``'sparse_copy'`` and ``'dense_copy'`` do not support
          ``node`` different from ``None``

        EXAMPLES::

            sage: graphs.FruchtGraph().clustering_coeff()
            {0: 1/3, 1: 1/3, 2: 0, 3: 1/3, 4: 1/3, 5: 1/3,
             6: 1/3, 7: 1/3, 8: 0, 9: 1/3, 10: 1/3, 11: 0}

            sage: (graphs.FruchtGraph()).clustering_coeff(weight=True)
            {0: 0.3333333333333333, 1: 0.3333333333333333, 2: 0,
            3: 0.3333333333333333, 4: 0.3333333333333333,
            5: 0.3333333333333333, 6: 0.3333333333333333,
            7: 0.3333333333333333, 8: 0, 9: 0.3333333333333333,
            10: 0.3333333333333333, 11: 0}

            sage: (graphs.FruchtGraph()).clustering_coeff(nodes=[0,1,2])
            {0: 0.3333333333333333, 1: 0.3333333333333333, 2: 0.0}

            sage: (graphs.FruchtGraph()).clustering_coeff(nodes=[0,1,2],
            ....:   weight=True)
            {0: 0.3333333333333333, 1: 0.3333333333333333, 2: 0}

            sage: (graphs.GridGraph([5,5])).clustering_coeff(nodes=[(0,0),(0,1),(2,2)])
            {(0, 0): 0.0, (0, 1): 0.0, (2, 2): 0.0}

        TESTS:

        Boost does not work with weights::

            sage: graphs.FruchtGraph().clustering_coeff(implementation='boost', weight=True)
            Traceback (most recent call last):
            ...
            ValueError: this value of 'implementation' is invalid for directed/weighted graphs

        Boost does not work with DiGraph::

            sage: digraphs.Circuit(10).clustering_coeff(implementation='boost')
            Traceback (most recent call last):
            ...
            ValueError: this value of 'implementation' is invalid for directed/weighted graphs

        Check that the result is the same with all implementations::

            sage: G = graphs.RandomGNM(10, 20)
            sage: G.relabel(list("abcdefghik"))
            sage: coeffs = [G.clustering_coeff(implementation=impl)
            ....:           for impl in ['boost', 'sparse_copy', 'dense_copy', 'networkx']]
            sage: for v in G:
            ....:     coeffs_v = [c[v] for c in coeffs]
            ....:     if max(coeffs_v) - min(coeffs_v) > 1E-12:
            ....:         raise ValueError("error for v={}, min={}, max={}".format(v, min(coeffs_v), max(coeffs_v)))

        TESTS::

            sage: graphs.EmptyGraph().clustering_coeff()
            {}
        """
        from sage.rings.integer import Integer

        if implementation is None:
            from sage.graphs.base.dense_graph import DenseGraphBackend
            if self.is_directed() or weight:
                implementation = 'networkx'
            elif nodes is not None:
                implementation = 'boost'
            elif isinstance(self._backend, DenseGraphBackend):
                implementation = 'dense_copy'
            else:
                implementation = 'sparse_copy'

        if implementation not in ['networkx', 'boost', 'dense_copy', 'sparse_copy']:
            raise ValueError("the implementation can only be 'networkx', "
                             "'boost', 'sparse_copy', 'dense_copy' or None")

        if (self.is_directed() or weight) and implementation != 'networkx':
            raise ValueError("this value of 'implementation' is invalid for directed/weighted graphs")

        if (implementation in ['sparse_copy', 'dense_copy'] and nodes is not None):
            raise ValueError("'sparse_copy','dense_copy' do not support 'nodes' different from 'None'")

        if not self.order():
            return {}

        def coeff_from_triangle_count(v, count):
            dv = self.degree(v)
            if dv < 2:
                return 0
            return 2 * count / Integer(dv * (dv - 1))

        if implementation == 'boost':
            from sage.graphs.base.boost_graph import clustering_coeff
            return clustering_coeff(self, nodes)[1]
        elif implementation == 'networkx':
            import networkx
            return networkx.clustering(self.networkx_graph(), nodes, weight=weight)
        elif implementation == 'sparse_copy':
            from sage.graphs.base.static_sparse_graph import triangles_count
            return {v: coeff_from_triangle_count(v, count)
                    for v, count in triangles_count(self).items()}
        elif implementation == "dense_copy":
            from sage.graphs.base.static_dense_graph import triangles_count
            return {v: coeff_from_triangle_count(v, count)
                    for v, count in triangles_count(self).items()}

    def cluster_transitivity(self):
        r"""
        Return the transitivity (fraction of transitive triangles) of the graph.

        Transitivity is the fraction of all existing triangles over all
        connected triples (triads),
        `T = 3\times\frac{\text{triangles}}{\text{triads}}`.

        See also section "Clustering" in chapter "Algorithms" of [HSS]_.

        EXAMPLES::

            sage: graphs.FruchtGraph().cluster_transitivity()
            0.25
        """
        import networkx
        return networkx.transitivity(self.networkx_graph())

    # Distance

    def distance(self, u, v, by_weight=False, weight_function=None, check_weight=True):
        """
        Return the (directed) distance from ``u`` to ``v`` in the (di)graph.

        The distance is the length of the shortest path from ``u`` to ``v``.

        This method simply calls :meth:`~GenericGraph.shortest_path_length`,
        with default arguments. For more information, and for more option, we
        refer to that method.

        INPUT:

        - ``by_weight`` -- boolean (default: ``False``); if ``False``, the graph
          is considered unweighted, and the distance is the number of edges in a
          shortest path. If ``True``, the distance is the sum of edge labels
          (which are assumed to be numbers).

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l``, if ``l``
          is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); whether to check that
          the ``weight_function`` outputs a number for each edge.

        EXAMPLES::

            sage: G = graphs.CycleGraph(9)
            sage: G.distance(0,1)
            1
            sage: G.distance(0,4)
            4
            sage: G.distance(0,5)
            4
            sage: G = Graph({0:[], 1:[]})
            sage: G.distance(0,1)
            +Infinity
            sage: G = Graph({ 0: {1: 1}, 1: {2: 1}, 2: {3: 1}, 3: {4: 2}, 4: {0: 2}}, sparse = True)
            sage: G.plot(edge_labels=True).show() # long time
            sage: G.distance(0, 3)
            2
            sage: G.distance(0, 3, by_weight=True)
            3
        """
        return self.shortest_path_length(u, v, by_weight=by_weight,
                                         weight_function=weight_function,
                                         check_weight=check_weight)

    def distance_all_pairs(self, by_weight=False, algorithm=None,
                           weight_function=None, check_weight=True):
        r"""
        Return the distances between all pairs of vertices.

        INPUT:

        - ``by_weight`` boolean (default: `False``); if ``True``, the edges in
          the graph are weighted; if ``False``, all edges have weight 1.

        - ``algorithm`` -- string (default: ``None``); one of the following
          algorithms:

          - ``'BFS'``: the computation is done through a BFS centered on each
            vertex successively. Works only if ``by_weight==False``.

          - ``'Floyd-Warshall-Cython'``: the Cython implementation of
            the Floyd-Warshall algorithm. Works only if ``by_weight==False``.

          - ``'Floyd-Warshall-Python'``: the Python implementation of
            the Floyd-Warshall algorithm. Works also with weighted graphs, even
            with negative weights (but no negative cycle is allowed).

          - ``'Dijkstra_NetworkX'``: the Dijkstra algorithm, implemented in
            NetworkX. It works with weighted graphs, but no negative weight is
            allowed.

          - ``'Dijkstra_Boost'``: the Dijkstra algorithm, implemented in Boost
            (works only with positive weights).

          - ``'Johnson_Boost'``: the Johnson algorithm, implemented in
            Boost (works also with negative weights, if there is no negative
            cycle).

          - ``None`` (default): Sage chooses the best algorithm: ``'BFS'`` if
            ``by_weight`` is ``False``, ``'Dijkstra_Boost'`` if all weights are
            positive, ``'Floyd-Warshall-Cython'`` otherwise.

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l``, if ``l``
          is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); whether to check that
          the ``weight_function`` outputs a number for each edge.

        OUTPUT:

        A doubly indexed dictionary

        .. NOTE::

            There is a Cython version of this method that is usually much faster
            for large graphs, as most of the time is actually spent building the
            final double dictionary. Everything on the subject is to be found in
            the :mod:`~sage.graphs.distances_all_pairs` module.

        .. NOTE::

            This algorithm simply calls
            :meth:`GenericGraph.shortest_path_all_pairs`, and we suggest to look
            at that method for more information and examples.

        EXAMPLES:

        The Petersen Graph::

            sage: g = graphs.PetersenGraph()
            sage: print(g.distance_all_pairs())
            {0: {0: 0, 1: 1, 2: 2, 3: 2, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2, 9: 2},
             1: {0: 1, 1: 0, 2: 1, 3: 2, 4: 2, 5: 2, 6: 1, 7: 2, 8: 2, 9: 2},
             2: {0: 2, 1: 1, 2: 0, 3: 1, 4: 2, 5: 2, 6: 2, 7: 1, 8: 2, 9: 2},
             3: {0: 2, 1: 2, 2: 1, 3: 0, 4: 1, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2},
             4: {0: 1, 1: 2, 2: 2, 3: 1, 4: 0, 5: 2, 6: 2, 7: 2, 8: 2, 9: 1},
             5: {0: 1, 1: 2, 2: 2, 3: 2, 4: 2, 5: 0, 6: 2, 7: 1, 8: 1, 9: 2},
             6: {0: 2, 1: 1, 2: 2, 3: 2, 4: 2, 5: 2, 6: 0, 7: 2, 8: 1, 9: 1},
             7: {0: 2, 1: 2, 2: 1, 3: 2, 4: 2, 5: 1, 6: 2, 7: 0, 8: 2, 9: 1},
             8: {0: 2, 1: 2, 2: 2, 3: 1, 4: 2, 5: 1, 6: 1, 7: 2, 8: 0, 9: 2},
             9: {0: 2, 1: 2, 2: 2, 3: 2, 4: 1, 5: 2, 6: 1, 7: 1, 8: 2, 9: 0}}

        Testing on Random Graphs::

            sage: g = graphs.RandomGNP(20,.3)
            sage: distances = g.distance_all_pairs()
            sage: all((g.distance(0,v) == Infinity and v not in distances[0]) or
            ....:     g.distance(0,v) == distances[0][v] for v in g)
            True

        .. SEEALSO::

            * :meth:`~sage.graphs.generic_graph.GenericGraph.distance_matrix`
            * :meth:`~sage.graphs.generic_graph.GenericGraph.shortest_path_all_pairs`
        """
        return self.shortest_path_all_pairs(by_weight=by_weight,
                                            algorithm=algorithm,
                                            weight_function=weight_function,
                                            check_weight=check_weight)[0]

    def girth(self, certificate=False):
        """
        Return the girth of the graph.

        The girth is the length of the shortest cycle in the graph
        (directed cycle if the graph is directed). Graphs without
        (directed) cycles have infinite girth.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); whether to return
          ``(g, c)``, where ``g`` is the girth and ``c`` is a list
          of vertices of a (directed) cycle of length ``g`` in the graph,
          thus providing a certificate that the girth is at most ``g``,
          or ``None`` if ``g``  infinite

        EXAMPLES::

            sage: graphs.TetrahedralGraph().girth()
            3
            sage: graphs.CubeGraph(3).girth()
            4
            sage: graphs.PetersenGraph().girth(certificate=True)  # random
            (5, [4, 3, 2, 1, 0])
            sage: graphs.HeawoodGraph().girth()
            6
            sage: next(graphs.trees(9)).girth()
            +Infinity

        .. SEEALSO::

            * :meth:`~GenericGraph.odd_girth` -- return the odd girth
              of the graph.

        TESTS:

        Prior to :trac:`12243`, the girth computation assumed vertices were
        integers (and failed). The example below tests the computation for
        graphs with vertices that are not integers. In this example the vertices
        are sets::

            sage: G = graphs.OddGraph(3)
            sage: type(G.vertices(sort=True)[0])
            <class 'sage.sets.set.Set_object_enumerated_with_category'>
            sage: G.girth()
            5

        Issue :trac:`12355`::

            sage: H=Graph([(0, 1), (0, 3), (0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (1, 6), (2, 5), (3, 4), (5, 6)])
            sage: H.girth()
            3

        Girth < 3 (see :trac:`12355`)::

            sage: g = graphs.PetersenGraph()
            sage: g.allow_multiple_edges(True)
            sage: g.allow_loops(True)
            sage: g.girth()
            5
            sage: g.add_edge(0,0)
            sage: g.girth()
            1
            sage: g.delete_edge(0,0)
            sage: g.add_edge(0,1)
            sage: g.girth()
            2
            sage: g.delete_edge(0,1)
            sage: g.girth()
            5
            sage: g = DiGraph(g)
            sage: g.girth()
            2

        Directed graphs (see :trac:`28142`)::

            sage: g = digraphs.Circuit(6)
            sage: g.girth()
            6
            sage: g = digraphs.RandomDirectedGNC(10)
            sage: g.girth()
            +Infinity
            sage: g = DiGraph([(0, 1), (1, 2), (1, 3), (2, 3), (3, 4), (4, 0)])
            sage: g.girth()
            4
            sage: Graph(g).girth()
            3
        """
        # Cases where girth <= 2
        if self.allows_loops():
            for u in self:
                if self.has_edge(u, u):
                    return (1, [u]) if certificate else 1
        if self.is_directed():
            for u, v in self.edge_iterator(labels=False):
                if self.has_edge(v, u):
                    return (2, [u, v]) if certificate else 2
        elif self.allows_multiple_edges():
            edges = set()
            for e in self.edge_iterator(labels=False):
                if e in edges:
                    return (2, list(e)) if certificate else 2
                edges.add(e)

        return self._girth_bfs(odd=False, certificate=certificate)

    def odd_girth(self, algorithm="bfs", certificate=False):
        r"""
        Return the odd girth of the graph.

        The odd girth is the length of the shortest cycle of odd length
        in the graph (directed cycle if the graph is directed).
        Bipartite graphs have infinite odd girth.

        INPUT:

        - ``algorithm`` -- string (default: ``"bfs"``); the algorithm to use:

          - ``"bfs"`` -- BFS-based algorithm

          - any algorithm accepted by
            :meth:`~sage.matrix.matrix_integer_dense.Matrix_integer_dense.charpoly`
            for computation from the characteristic polynomial (see
            [Har1962]_ and [Big1993]_, p. 45)

        - ``certificate`` -- boolean (default: ``False``); whether to return
          ``(g, c)``, where ``g`` is the odd girth and ``c`` is a list of
          vertices of a (directed) cycle of length ``g`` in the graph, thus
          providing a certificate that the odd girth is at most ``g``, or
          ``None`` if ``g`` is infinite. So far, this parameter is accepted only
          when ``algorithm = "bfs"``.

        EXAMPLES:

        The McGee graph has girth 7 and therefore its odd girth is 7 as well::

            sage: G = graphs.McGeeGraph()
            sage: G.girth()
            7
            sage: G.odd_girth()
            7

        Any complete (directed) graph on more than 2 vertices contains
        a (directed) triangle and has thus odd girth 3::

            sage: G = graphs.CompleteGraph(5)
            sage: G.odd_girth(certificate=True)  # random
            (3, [2, 1, 0])
            sage: G = digraphs.Complete(5)
            sage: G.odd_girth(certificate=True)  # random
            (3, [1, 2, 0])

        Bipartite graphs have no odd cycle and consequently have
        infinite odd girth::

            sage: G = graphs.RandomBipartite(6, 6, .5)
            sage: G.odd_girth()
            +Infinity
            sage: G = graphs.Grid2dGraph(3, 4)
            sage: G.odd_girth()
            +Infinity

        The odd girth of a (directed) graph with loops is 1::

            sage: G = graphs.RandomGNP(10, .5)
            sage: G.allow_loops(True)
            sage: G.add_edge(0, 0)
            sage: G.odd_girth()
            1
            sage: G = digraphs.RandomDirectedGNP(10, .5)
            sage: G.allow_loops(True)
            sage: G.add_edge(0, 0)
            sage: G.odd_girth()
            1

        .. SEEALSO::

            * :meth:`~GenericGraph.girth` -- return the girth of the graph.

        TESTS:

        Odd girth of odd cycles::

            sage: [graphs.CycleGraph(i).odd_girth() for i in range(3, 12, 2)]
            [3, 5, 7, 9, 11]

        Directed graphs (see :trac:`28142`)::

            sage: g = digraphs.Circuit(7)
            sage: g.odd_girth()
            7
            sage: g = graphs.CompleteBipartiteGraph(10, 10).random_orientation()
            sage: g.odd_girth()
            +Infinity
            sage: g = DiGraph([(0, 1), (1, 2), (1, 3), (2, 3), (3, 4), (4, 0)])
            sage: g.odd_girth()
            5
            sage: Graph(g).odd_girth()
            3

        Small cases::

            sage: [graphs.CompleteGraph(i).odd_girth() for i in range(5)]
            [+Infinity, +Infinity, +Infinity, 3, 3]
            sage: [digraphs.Complete(i).odd_girth() for i in range(5)]
            [+Infinity, +Infinity, +Infinity, 3, 3]
        """
        # Case where odd girth is 1
        if self.allows_loops():
            for u in self:
                if self.has_edge(u, u):
                    return (1, [u]) if certificate else 1

        if self.is_bipartite():
            from sage.rings.infinity import Infinity
            return (Infinity, None) if certificate else Infinity

        if algorithm == "bfs":
            return self._girth_bfs(odd=True, certificate=certificate)

        if certificate:
            raise ValueError("certificate is only supported with algorithm='bfs'")

        ch = self.am().charpoly(algorithm=algorithm).coefficients(sparse=False)

        n = self.order()
        for i in range(n-1, -1, -2):
            if ch[i]:
                return n - i

    def _girth_bfs(self, odd=False, certificate=False):
        r"""
        Return the girth of the graph using breadth-first search.

        Loops and parallel edges are ignored,
        so the returned value is at least 3.

        INPUT:

        - ``odd`` -- boolean (default: ``False``); whether to compute the odd
          girth instead of the girth

        - ``certificate`` -- boolean (default: ``False``); whether to return
          ``(g, c)``, where ``g`` is the (odd) girth and ``c`` is a list
          of vertices of a cycle of length ``g`` in the graph,
          thus providing a certificate that the (odd) girth is at most ``g``,
          or ``None`` if ``g``  infinite

        EXAMPLES:

        The 5-prism has girth 4 and odd girth 5::

            sage: G = graphs.CycleGraph(5).cartesian_product(graphs.CompleteGraph(2))
            sage: G._girth_bfs(certificate=True)  # random
            (4, [(2, 0), (1, 0), (1, 1), (2, 1)])
            sage: G._girth_bfs(odd=True)
            5

        .. SEEALSO::

            * :meth:`~GenericGraph.girth` -- return the girth of the graph.
            * :meth:`~GenericGraph.odd_girth` -- return the odd girth of the graph.
        """
        n = self.num_verts()
        best = n + 1
        seen = set()
        for w in self:
            seen.add(w)
            span = {w: None}
            depth = 1
            thisList = set([w])
            while 2 * depth <= best:
                nextList = set()
                for v in thisList:
                    for u in self.neighbor_iterator(v):
                        if u in seen:
                            continue
                        if u not in span:
                            span[u] = v
                            nextList.add(u)
                        else:
                            if u in thisList:
                                best = depth * 2 - 1
                                ends = (u, v)
                                bestSpan = span
                                break
                            if not odd and u in nextList:
                                best = depth * 2
                                ends = (u, v)
                                bestSpan = span
                    if best == 2 * depth - 1:
                        break
                if best <= 3:
                    break
                thisList = nextList
                depth += 1
        if best == n + 1:
            from sage.rings.infinity import Infinity
            return (Infinity, None) if certificate else Infinity
        if certificate:
            cycles = {}
            for x in ends:
                cycles[x] = []
                y = x
                while bestSpan[y] is not None:
                    cycles[x].append(y)
                    y = bestSpan[y]
            cycles[x].append(y)
            u, v = ends
            return (best, list(reversed(cycles[u])) + cycles[v])
        else:
            return best

    # Centrality

    def centrality_betweenness(self, k=None, normalized=True, weight=None,
                               endpoints=False, seed=None, exact=False,
                               algorithm=None):
        r"""
        Return the betweenness centrality.

        The betweenness centrality of a vertex is the fraction of number of
        shortest paths that go through each vertex. The betweenness is
        normalized by default to be in range (0,1).

        Measures of the centrality of a vertex within a graph determine the
        relative importance of that vertex to its graph. Vertices that occur on
        more shortest paths between other vertices have higher betweenness than
        vertices that occur on less.

        INPUT:

        - ``normalized`` -- boolean (default: ``True``); if set to ``False``,
          result is not normalized.

        - ``k`` -- integer (default: ``None``); if set to an integer, use ``k``
          node samples to estimate betweenness. Higher values give better
          approximations. Not available when ``algorithm="Sage"``.

        - ``weight`` -- string (default: ``None``); if set to a string, use that
          attribute of the nodes as weight. ``weight = True`` is equivalent to
          ``weight = "weight"``. Not available when ``algorithm="Sage"``.

        - ``endpoints`` -- boolean (default: ``False``); if set to ``True`` it
          includes the endpoints in the shortest paths count. Not available when
          ``algorithm="Sage"``.

        - ``exact`` -- boolean (default: ``False``); whether to compute over
          rationals or on ``double`` C variables. Not available when
          ``algorithm="NetworkX"``.

        - ``algorithm`` -- string (default: ``None``); can be either ``"Sage"``
          (see :mod:`~sage.graphs.centrality`), ``"NetworkX"`` or ``"None"``. In
          the latter case, Sage's algorithm will be used whenever possible.

        .. SEEALSO::

            - :meth:`~sage.graphs.graph.Graph.centrality_degree`
            - :meth:`~centrality_closeness`

        EXAMPLES::

            sage: g = graphs.ChvatalGraph()
            sage: g.centrality_betweenness() # abs tol 1e-10
            {0: 0.06969696969696969, 1: 0.06969696969696969,
             2: 0.0606060606060606, 3: 0.0606060606060606,
             4: 0.06969696969696969, 5: 0.06969696969696969,
             6: 0.0606060606060606, 7: 0.0606060606060606,
             8: 0.0606060606060606, 9: 0.0606060606060606,
             10: 0.0606060606060606, 11: 0.0606060606060606}
            sage: g.centrality_betweenness(normalized=False) # abs tol 1e-10
            {0: 3.833333333333333, 1: 3.833333333333333, 2: 3.333333333333333,
             3: 3.333333333333333, 4: 3.833333333333333, 5: 3.833333333333333,
             6: 3.333333333333333, 7: 3.333333333333333, 8: 3.333333333333333,
             9: 3.333333333333333, 10: 3.333333333333333,
             11: 3.333333333333333}
            sage: D = DiGraph({0:[1,2,3], 1:[2], 3:[0,1]})
            sage: D.show(figsize=[2,2])
            sage: D = D.to_undirected()
            sage: D.show(figsize=[2,2])
            sage: D.centrality_betweenness() # abs tol abs 1e-10
            {0: 0.16666666666666666, 1: 0.16666666666666666, 2: 0.0, 3: 0.0}

        TESTS::

            sage: tests = ([graphs.RandomGNP(30,.1) for i in range(10)]+
            ....:          [digraphs.RandomDirectedGNP(30,.1) for i in range(10)])
            sage: for g in tests:
            ....:     r1 = g.centrality_betweenness(algorithm="Sage",exact=0)
            ....:     r2 = g.centrality_betweenness(algorithm="Sage",exact=1)
            ....:     r3 = g.centrality_betweenness(algorithm="NetworkX")
            ....:     for x in g:
            ....:         if max([r1[x],r2[x],r3[x]])-min([r1[x],r2[x],r3[x]]) > 0.01:
            ....:             print("Error",x,[r1[x],r2[x],r3[x]])
        """
        if algorithm == "NetworkX" and exact:
            raise ValueError("'exact' is not available with the NetworkX implementation")
        if (algorithm is None and
                seed is None and
                weight is None and
                endpoints is False and
                k is None):
            algorithm = "Sage"
        elif algorithm is None:
            algorithm = "NetworkX"

        if algorithm == "Sage":
            from .centrality import centrality_betweenness
            return centrality_betweenness(self, normalize=normalized, exact=exact)
        elif algorithm == "NetworkX":
            import networkx
            return networkx.betweenness_centrality(self.networkx_graph(),
                                                   k=k,
                                                   normalized=normalized,
                                                   weight=weight,
                                                   endpoints=endpoints,
                                                   seed=seed)
        else:
            raise ValueError("'algorithm' can be \"NetworkX\", \"Sage\" or None")

    def centrality_closeness(self, vert=None, by_weight=False, algorithm=None,
                             weight_function=None, check_weight=True):
        r"""
        Return the closeness centrality of all vertices in ``vert``.

        In a (strongly) connected graph, the closeness centrality of a vertex
        `v` is equal to the inverse of the average distance between `v` and
        other vertices.  If the graph is disconnected, the closeness centrality
        of `v` is multiplied by the fraction of reachable vertices in the graph:
        this way, central vertices should also reach several other vertices in
        the graph [OLJ2014]_. In formulas,

        .. MATH::

            c(v)=\frac{r(v)-1}{\sum_{w \in R(v)} d(v,w)}\frac{r(v)-1}{n-1}

        where `R(v)` is the set of vertices reachable from `v`, and `r(v)` is
        the cardinality of `R(v)`.

        'Closeness centrality may be defined as the total graph-theoretic
        distance of a given vertex from all other vertices... Closeness is an
        inverse measure of centrality in that a larger value indicates a less
        central actor while a smaller value indicates a more central actor,'
        [Bor1995]_.

        For more information, see the :wikipedia:`Centrality`.

        INPUT:

        - ``vert`` -- the vertex or the list of vertices we want to analyze. If
          ``None`` (default), all vertices are considered.

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
          in the graph are weighted, and otherwise all edges have weight 1

        - ``algorithm`` -- string (default: ``None``); one of the following
          algorithms:

          - ``'BFS'``: performs a BFS from each vertex that has to be analyzed.
            Does not work with edge weights.

          - ``'NetworkX'``: the NetworkX algorithm (works only with positive
            weights).

          - ``'Dijkstra_Boost'``: the Dijkstra algorithm, implemented in Boost
            (works only with positive weights).

          - ``'Floyd-Warshall-Cython'``: the Cython implementation of the
            Floyd-Warshall algorithm. Works only if ``by_weight==False`` and all
            centralities are needed.

          - ``'Floyd-Warshall-Python'``: the Python implementation of the
            Floyd-Warshall algorithm. Works only if all centralities are needed,
            but it can deal with weighted graphs, even with negative weights
            (but no negative cycle is allowed).

          - ``'Johnson_Boost'``: the Johnson algorithm, implemented in Boost
            (works also with negative weights, if there is no negative cycle).

          - ``None`` (default): Sage chooses the best algorithm: ``'BFS'`` if
            ``by_weight`` is ``False``, ``'Dijkstra_Boost'`` if all weights are
            positive, ``'Johnson_Boost'`` otherwise.

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l`` as a
          weight, if ``l`` is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the ``weight_function`` outputs a number for each edge.

        OUTPUT:

        If ``vert`` is a vertex, the closeness centrality of that vertex.
        Otherwise, a dictionary associating to each vertex in ``vert`` its
        closeness centrality. If a vertex has (out)degree 0, its closeness
        centrality is not defined, and the vertex is not included in the output.

        .. SEEALSO::

            - :func:`~sage.graphs.centrality.centrality_closeness_top_k`
            - :meth:`~sage.graphs.graph.Graph.centrality_degree`
            - :meth:`~centrality_betweenness`

        EXAMPLES:

        Standard examples::

            sage: (graphs.ChvatalGraph()).centrality_closeness()
            {0: 0.61111111111111..., 1: 0.61111111111111...,
             2: 0.61111111111111..., 3: 0.61111111111111...,
             4: 0.61111111111111..., 5: 0.61111111111111...,
             6: 0.61111111111111..., 7: 0.61111111111111...,
             8: 0.61111111111111..., 9: 0.61111111111111...,
             10: 0.61111111111111..., 11: 0.61111111111111...}
            sage: D = DiGraph({0:[1,2,3], 1:[2], 3:[0,1]})
            sage: D.show(figsize=[2,2])
            sage: D.centrality_closeness(vert=[0,1])
            {0: 1.0, 1: 0.3333333333333333}
            sage: D = D.to_undirected()
            sage: D.show(figsize=[2,2])
            sage: D.centrality_closeness()
            {0: 1.0, 1: 1.0, 2: 0.75, 3: 0.75}

        In a (strongly) connected (di)graph, the closeness centrality of `v`
        is inverse of the average distance between `v` and all other vertices::

            sage: g = graphs.PathGraph(5)
            sage: g.centrality_closeness(0)
            0.4
            sage: dist = g.shortest_path_lengths(0).values()
            sage: float(len(dist)-1) / sum(dist)
            0.4
            sage: d = g.to_directed()
            sage: d.centrality_closeness(0)
            0.4
            sage: dist = d.shortest_path_lengths(0).values()
            sage: float(len(dist)-1) / sum(dist)
            0.4

        If a vertex has (out)degree 0, its closeness centrality is not defined::

            sage: g = Graph(5)
            sage: g.centrality_closeness()
            {}
            sage: print(g.centrality_closeness(0))
            None

        Weighted graphs::

            sage: D = graphs.GridGraph([2,2])
            sage: weight_function = lambda e:10
            sage: D.centrality_closeness([(0,0),(0,1)])                          # tol abs 1e-12
            {(0, 0): 0.75, (0, 1): 0.75}
            sage: D.centrality_closeness((0,0), weight_function=weight_function) # tol abs 1e-12
            0.075

        TESTS:

        The result does not depend on the algorithm::

            sage: import random
            sage: import itertools
            sage: n = random.randint(2,20)
            sage: m = random.randint(0, n*(n-1)/2)
            sage: g = graphs.RandomGNM(n,m)
            sage: c1 = g.centrality_closeness(algorithm='BFS')
            sage: c2 = g.centrality_closeness(algorithm='NetworkX')
            sage: c3 = g.centrality_closeness(algorithm='Dijkstra_Boost')
            sage: c4 = g.centrality_closeness(algorithm='Floyd-Warshall-Cython')
            sage: c5 = g.centrality_closeness(algorithm='Floyd-Warshall-Python')
            sage: c6 = g.centrality_closeness(algorithm='Johnson_Boost')
            sage: len(c1)==len(c2)==len(c3)==len(c4)==len(c5)==len(c6)
            True
            sage: c = [c1,c2,c3,c4,c5,c6]
            sage: all( sum(abs(ci[v] - cj[v]) for v in g if g.degree(v)) < 1e-12
            ....:      for ci, cj in itertools.combinations(c, 2) )
            True

        Directed graphs::

            sage: import random
            sage: import itertools
            sage: n = random.randint(2,20)
            sage: m = random.randint(0, n*(n-1)/2)
            sage: g = digraphs.RandomDirectedGNM(n,m)
            sage: c1 = g.centrality_closeness(algorithm='BFS')
            sage: c2 = g.centrality_closeness(algorithm='NetworkX')
            sage: c3 = g.centrality_closeness(algorithm='Dijkstra_Boost')
            sage: c4 = g.centrality_closeness(algorithm='Floyd-Warshall-Cython')
            sage: c5 = g.centrality_closeness(algorithm='Floyd-Warshall-Python')
            sage: c6 = g.centrality_closeness(algorithm='Johnson_Boost')
            sage: len(c1)==len(c2)==len(c3)==len(c4)==len(c5)==len(c6)
            True
            sage: c = [c1,c2,c3,c4,c5,c6]
            sage: all( sum(abs(ci[v] - cj[v]) for v in g if g.out_degree(v)) < 1e-12
            ....:      for ci, cj in itertools.combinations(c, 2) )
            True

        Weighted graphs::

            sage: import random
            sage: import itertools
            sage: n = random.randint(2,20)
            sage: m = random.randint(0, n*(n-1)/2)
            sage: g = graphs.RandomGNM(n,m)
            sage: for v,w in g.edges(sort=True, labels=False):
            ....:     g.set_edge_label(v,w,float(random.uniform(1,100)))
            sage: c1 = g.centrality_closeness(by_weight=True, algorithm='NetworkX')
            sage: c2 = g.centrality_closeness(by_weight=True, algorithm='Dijkstra_Boost')
            sage: c3 = g.centrality_closeness(by_weight=True, algorithm='Floyd-Warshall-Python')
            sage: c4 = g.centrality_closeness(by_weight=True, algorithm='Johnson_Boost')
            sage: len(c1)==len(c2)==len(c3)==len(c4)
            True
            sage: c = [c1,c2,c3,c4]
            sage: all( sum(abs(ci[v] - cj[v]) for v in g if g.degree(v)) < 1e-12
            ....:      for ci, cj in itertools.combinations(c, 2) )
            True

        """
        by_weight, weight_function = self._get_weight_function(by_weight=by_weight,
                                                               weight_function=weight_function,
                                                               check_weight=check_weight)

        onlyone = False
        if vert in self:
            v_iter = iter([vert])
            onlyone = True
        elif vert is None:
            v_iter = self.vertex_iterator()
        else:
            v_iter = iter(vert)

        if algorithm is None:
            if not by_weight:
                algorithm = 'BFS'
            elif any(float(weight_function(e)) < 0 for e in self.edge_iterator()):
                algorithm = 'Johnson_Boost'
            if algorithm is None:
                algorithm = 'Dijkstra_Boost'
        if algorithm in ['BFS', 'Floyd-Warshall-Cython']:
            if by_weight:
                raise ValueError("algorithm '{}' does not work with weights".format(algorithm))
            # We don't want the default weight function
            weight_function = None

        if algorithm == 'NetworkX':
            import networkx
            if by_weight:
                if self.is_directed():
                    G = networkx.DiGraph([(e[1], e[0], {'weight': weight_function(e)}) for e in self.edge_iterator()])
                else:
                    G = networkx.Graph([(e[0], e[1], {'weight': weight_function(e)}) for e in self.edge_iterator()])
            else:
                if self.is_directed():
                    G = self.reverse().networkx_graph()
                else:
                    G = self.networkx_graph()
            G.add_nodes_from(self)

            degree = self.out_degree if self.is_directed() else self.degree
            if vert is None:
                closeness = networkx.closeness_centrality(G, vert, distance='weight' if by_weight else None)
                return {v: c for v, c in closeness.items() if degree(v)}
            closeness = {}
            for x in v_iter:
                if degree(x):
                    closeness[x] = networkx.closeness_centrality(G, x, distance='weight' if by_weight else None)
            if onlyone:
                return closeness.get(vert, None)
            else:
                return closeness
        elif algorithm == "Johnson_Boost":
            from sage.graphs.base.boost_graph import johnson_closeness_centrality
            self.weighted(by_weight)
            closeness = johnson_closeness_centrality(self, weight_function)
            if onlyone:
                return closeness.get(vert, None)
            else:
                return {v: closeness[v] for v in v_iter if v in closeness}
        else:
            closeness = dict()
            distances = None
            if algorithm in ["Floyd-Warshall-Cython",
                             "Floyd-Warshall-Python"]:
                distances = self.shortest_path_all_pairs(algorithm=algorithm,
                                                         by_weight=by_weight,
                                                         weight_function=weight_function,
                                                         check_weight=False)[0]

            for v in v_iter:
                if distances is None:
                    distv = self.shortest_path_lengths(v, algorithm=algorithm,
                                                       by_weight=by_weight,
                                                       weight_function=weight_function,
                                                       check_weight=False)
                else:
                    distv = distances[v]
                try:
                    closeness[v] = float(len(distv) - 1) * (len(distv) - 1) / (float(sum(distv.values())) * (self.num_verts() - 1))
                except ZeroDivisionError:
                    pass
            if onlyone:
                return closeness.get(vert, None)
            else:
                return closeness

    def triangles_count(self, algorithm=None):
        r"""
        Return the number of triangles in the (di)graph.

        For digraphs, we count the number of directed circuit of length 3.

        INPUT:

        - ``algorithm`` -- string (default: ``None``); specifies the algorithm
          to use (note that only ``'iter'`` is available for directed graphs):

          - ``'sparse_copy'`` -- counts the triangles in a sparse copy of the
            graph (see :mod:`sage.graphs.base.static_sparse_graph`). Calls
            :func:`static_sparse_graph.triangles_count
            <sage.graphs.base.static_sparse_graph.triangles_count>`

          - ``'dense_copy'`` -- counts the triangles in a dense copy of the
            graph (see :mod:`sage.graphs.base.static_dense_graph`). Calls
            :func:`static_dense_graph.triangles_count
            <sage.graphs.base.static_dense_graph.triangles_count>`

          - ``'matrix'`` uses the trace of the cube of the adjacency matrix

          - ``'iter'`` iterates over the pairs of neighbors of each vertex. No
            copy of the graph is performed

          - ``None`` -- for undirected graphs, uses ``"sparse_copy"`` or
            ``"dense_copy"`` depending on whether the graph is stored as dense
            or sparse. For directed graphs, uses ``'iter'``.

        EXAMPLES:

        The Petersen graph is triangle free and thus::

            sage: G = graphs.PetersenGraph()
            sage: G.triangles_count()
            0

        Any triple of vertices in the complete graph induces a triangle so we
        have::

            sage: G = graphs.CompleteGraph(15)
            sage: G.triangles_count() == binomial(15, 3)
            True

        The 2-dimensional DeBruijn graph of 2 symbols has 2 directed `C_3`::

            sage: G = digraphs.DeBruijn(2,2)
            sage: G.triangles_count()
            2

        The directed `n`-cycle is trivially triangle free for `n > 3`::

            sage: G = digraphs.Circuit(10)
            sage: G.triangles_count()
            0

        TESTS:

        Comparison of algorithms::

            sage: G = graphs.RandomBarabasiAlbert(50,2)
            sage: results = []
            sage: results.append(G.triangles_count(algorithm='matrix'))
            sage: results.append(G.triangles_count(algorithm='iter'))
            sage: results.append(G.triangles_count(algorithm='sparse_copy'))
            sage: results.append(G.triangles_count(algorithm='dense_copy'))
            sage: any(x != results[0] for x in results)
            False

        Asking for an unknown algorithm::

            sage: G = Graph()
            sage: G.triangles_count(algorithm='tip top')
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm "tip top"
            sage: digraphs.Path(5).triangles_count(algorithm="sparse_copy")
            Traceback (most recent call last):
            ...
            ValueError: the value of algorithm(=sparse_copy) must be 'iter' or None for directed graphs
        """
        if self.is_directed():
            if algorithm is not None and algorithm != "iter":
                raise ValueError("the value of algorithm(={}) must be 'iter' "
                                 "or None for directed graphs".format(algorithm))

            self._scream_if_not_simple(allow_loops=True)
            from sage.graphs.digraph_generators import digraphs
            return self.subgraph_search_count(digraphs.Circuit(3)) // 3

        else:
            self._scream_if_not_simple()
            if algorithm is None:
                from sage.graphs.base.dense_graph import DenseGraphBackend
                algorithm = ('dense_copy' if isinstance(self._backend, DenseGraphBackend) else
                             'sparse_copy')

            if algorithm == 'iter':
                tr = 0
                for u in self:
                    Nu = set(self.neighbors(u))
                    for v in Nu:
                        tr += len(Nu.intersection(self.neighbors(v)))
                return Integer(tr // 6)
            elif algorithm == "sparse_copy":
                from sage.graphs.base.static_sparse_graph import triangles_count
                return sum(triangles_count(self).values()) // 3
            elif algorithm == "dense_copy":
                from sage.graphs.base.static_dense_graph import triangles_count
                return sum(triangles_count(self).values()) // 3
            elif algorithm == 'matrix':
                return (self.adjacency_matrix(vertices=list(self))**3).trace() // 6
            else:
                raise ValueError('unknown algorithm "{}"'.format(algorithm))

    def shortest_path(self, u, v, by_weight=False, algorithm=None,
                      weight_function=None, check_weight=True):
        r"""
        Return a list of vertices representing some shortest path from ``u`` to
        ``v``.

        If there is no path from `u` to `v`, the returned list is empty.

        For more information and more examples, see
        :meth:`~GenericGraph.shortest_paths` (the inputs are very similar).

        INPUT:

        - ``u``, ``v`` -- the start and the end vertices of the paths

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
          in the graph are weighted, otherwise all edges have weight 1

        - ``algorithm`` -- string (default: ``None``); one of the following
          algorithms:

          - ``'BFS'``: performs a BFS from ``u``. Does not work with edge
            weights.

          - ``'BFS_Bid'``: performs a BFS from ``u`` and from ``v``. Does not
            work with edge weights.

          - ``'Dijkstra_NetworkX'``: the Dijkstra algorithm, implemented in
            NetworkX. Works only with positive weights.

          - ``'Dijkstra_Bid_NetworkX'``: performs a Dijkstra visit from ``u``
            and from ``v`` (NetworkX implementation). Works only with positive
            weights.

          - ``'Dijkstra_Bid'``: a Cython implementation that performs
            a Dijkstra visit from ``u`` and from ``v``. Works only with positive
            weights.

          - ``'Bellman-Ford_Boost'``: the Bellman-Ford algorithm, implemented in
            Boost. Works also with negative weights, if there is no negative
            cycle.

          - ``None`` (default): Sage chooses the best algorithm: ``'BFS_Bid'``
            if ``by_weight`` is ``False``, ``'Dijkstra_Bid'`` otherwise.

          .. NOTE::

              If there are negative weights and algorithm is ``None``, the
              result is not reliable. This occurs because, for performance
              reasons, we cannot check whether there are edges with negative
              weights before running the algorithm. If there are, the user
              should explicitly input ``algorithm='Bellman-Ford_Boost'``.

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l``, if ``l``
          is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the weight_function outputs a number for each edge

        EXAMPLES::

            sage: D = graphs.DodecahedralGraph()
            sage: D.shortest_path(4, 9)
            [4, 17, 16, 12, 13, 9]
            sage: D.shortest_path(4, 9, algorithm='BFS')
            [4, 3, 2, 1, 8, 9]
            sage: D.shortest_path(4, 8, algorithm='Dijkstra_NetworkX')
            [4, 3, 2, 1, 8]
            sage: D.shortest_path(4, 8, algorithm='Dijkstra_Bid_NetworkX')
            [4, 3, 2, 1, 8]
            sage: D.shortest_path(4, 9, algorithm='Dijkstra_Bid')
            [4, 3, 19, 0, 10, 9]
            sage: D.shortest_path(5, 5)
            [5]
            sage: D.delete_edges(D.edges_incident(13))
            sage: D.shortest_path(13, 4)
            []
            sage: G = Graph({0: {1: 1}, 1: {2: 1}, 2: {3: 1}, 3: {4: 2}, 4: {0: 2}}, sparse = True)
            sage: G.plot(edge_labels=True).show() # long time
            sage: G.shortest_path(0, 3)
            [0, 4, 3]
            sage: G.shortest_path(0, 3, by_weight=True)
            [0, 1, 2, 3]
            sage: G.shortest_path(0, 3, by_weight=True, algorithm='Dijkstra_NetworkX')
            [0, 1, 2, 3]
            sage: G.shortest_path(0, 3, by_weight=True, algorithm='Dijkstra_Bid_NetworkX')
            [0, 1, 2, 3]

        TESTS:

        If the algorithm is not implemented::

            sage: G.shortest_path(0, 3, by_weight=True, algorithm='tip top')
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm "tip top"

        BFS on weighted graphs::

            sage: G.shortest_path(0, 3, by_weight=True, algorithm='BFS')
            Traceback (most recent call last):
            ...
            ValueError: the 'BFS' algorithm does not work on weighted graphs
            sage: G.shortest_path(0, 3, by_weight=True, algorithm='BFS_Bid')
            Traceback (most recent call last):
            ...
            ValueError: the 'BFS_Bid' algorithm does not work on weighted graphs

        If vertex is not in the graph::

            sage: G.shortest_path(0, 5)
            Traceback (most recent call last):
            ...
            ValueError: vertex '5' is not in the (di)graph
            sage: G.shortest_path(6, 5)
            Traceback (most recent call last):
            ...
            ValueError: vertex '6' is not in the (di)graph

        If no path exists from ``u`` to ``v`` (:trac:`28098`)::

            sage: G = Graph()
            sage: G.add_vertices([1, 2])
            sage: for alg in ['BFS', 'BFS_Bid', 'Dijkstra_NetworkX', 'Dijkstra_Bid_NetworkX',
            ....:             'Dijkstra_Bid', 'Bellman-Ford_Boost']:
            ....:     G.shortest_path(1, 2, algorithm=alg)
            []
            []
            []
            []
            []
            []

        .. TODO::

            Add options to return a path as a list of edges with or without edge
            labels. This can be useful in (di)graphs with multiple edges.
        """
        if not self.has_vertex(u):
            raise ValueError("vertex '{}' is not in the (di)graph".format(u))
        if not self.has_vertex(v):
            raise ValueError("vertex '{}' is not in the (di)graph".format(v))
        if u == v:
            return [u]

        by_weight, weight_function = self._get_weight_function(by_weight=by_weight,
                                                               weight_function=weight_function,
                                                               check_weight=check_weight)

        if algorithm is None:
            algorithm = 'Dijkstra_Bid' if by_weight else 'BFS_Bid'
        elif algorithm in ['BFS', 'BFS_Bid']:
            if by_weight:
                raise ValueError("the '{}' algorithm does not work on weighted graphs".format(algorithm))
            # We don't want the default weight function
            weight_function = None

        if algorithm in ['BFS', 'Dijkstra_NetworkX', 'Bellman-Ford_Boost']:
            all_paths = self.shortest_paths(u, algorithm=algorithm, by_weight=by_weight,
                                            weight_function=weight_function, check_weight=False)
            if v in all_paths:
                return all_paths[v]
            return []
        elif algorithm == "Dijkstra_Bid":
            return self._backend.bidirectional_dijkstra(u, v, weight_function)
        elif algorithm == "Dijkstra_Bid_NetworkX":
            import networkx
            if self.is_directed():
                G = networkx.DiGraph([(e[0], e[1], {'weight': weight_function(e)}) for e in self.edge_iterator()])
            else:
                G = networkx.Graph([(e[0], e[1], {'weight': weight_function(e)}) for e in self.edge_iterator()])
            G.add_nodes_from(self)
            try:
                return networkx.bidirectional_dijkstra(G, u, v)[1]
            except networkx.NetworkXNoPath:
                return []
        elif algorithm == "BFS_Bid":
            return self._backend.shortest_path(u, v)
        else:
            raise ValueError('unknown algorithm "{}"'.format(algorithm))

    def shortest_path_length(self, u, v, by_weight=False, algorithm=None,
                             weight_function=None, check_weight=True):
        r"""
        Return the minimal length of a path from ``u`` to ``v``.

        If there is no path from `u` to `v`, returns ``Infinity``.

        For more information and more examples, we refer to
        :meth:`~GenericGraph.shortest_path` and
        :meth:`~GenericGraph.shortest_paths`, which have very similar inputs.

        INPUT:

        - ``u``, ``v`` -- the start and the end vertices of the paths

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
          in the graph are weighted, otherwise all edges have weight 1

        - ``algorithm`` -- string (default: ``None``); one of the following
          algorithms:

          - ``'BFS'``: performs a BFS from ``u``. Does not work with edge
            weights.

          - ``'BFS_Bid'``: performs a BFS from ``u`` and from ``v``. Does not
            work with edge weights.

          - ``'Dijkstra_NetworkX'``: the Dijkstra algorithm, implemented in
            NetworkX. Works only with positive weights.

          - ``'Dijkstra_Bid_NetworkX'``: performs a Dijkstra visit from ``u``
            and from ``v`` (NetworkX implementation). Works only with positive
            weights.

          - ``'Dijkstra_Bid'``: a Cython implementation that performs
            a Dijkstra visit from ``u`` and from ``v``. Works only with positive
            weights.

          - ``'Bellman-Ford_Boost'``: the Bellman-Ford algorithm, implemented in
            Boost. Works also with negative weights, if there is no negative
            cycle.

          - ``None`` (default): Sage chooses the best algorithm: ``'BFS_Bid'``
            if ``by_weight`` is ``False``, ``'Dijkstra_Bid'`` otherwise.

          .. NOTE::

              If there are negative weights and algorithm is ``None``, the
              result is not reliable. This occurs because, for performance
              reasons, we cannot check whether there are edges with negative
              weights before running the algorithm. If there are, the user
              should explicitly input ``algorithm='Bellman-Ford_Boost'``.

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l``, if ``l``
          is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the weight_function outputs a number for each edge

        EXAMPLES:

        Standard examples::

            sage: D = graphs.DodecahedralGraph()
            sage: D.shortest_path_length(4, 9)
            5
            sage: D.shortest_path_length(4, 9, algorithm='BFS')
            5
            sage: D.shortest_path_length(4, 9, algorithm='Dijkstra_NetworkX')
            5
            sage: D.shortest_path_length(4, 9, algorithm='Dijkstra_Bid_NetworkX')
            5
            sage: D.shortest_path_length(4, 9, algorithm='Dijkstra_Bid')
            5
            sage: D.shortest_path_length(4, 9, algorithm='Bellman-Ford_Boost')
            5
            sage: D.shortest_path_length(5, 5)
            0
            sage: D.delete_edges(D.edges_incident(13))
            sage: D.shortest_path_length(13, 4)
            +Infinity
            sage: G = Graph({0: {1: 1}, 1: {2: 1}, 2: {3: 1}, 3: {4: 2}, 4: {0: 2}}, sparse = True)
            sage: G.plot(edge_labels=True).show() # long time
            sage: G.shortest_path_length(0, 3)
            2
            sage: G.shortest_path_length(0, 3, by_weight=True)
            3
            sage: G.shortest_path_length(0, 3, by_weight=True, algorithm='Dijkstra_NetworkX')
            3
            sage: G.shortest_path_length(0, 3, by_weight=True, algorithm='Dijkstra_Bid_NetworkX')
            3

        If Dijkstra is used with negative weights, usually it raises an error::

            sage: G = DiGraph({0: {1: 1}, 1: {2: 1}, 2: {3: 1}, 3: {4: 2}, 4: {0: -2}}, sparse = True)
            sage: G.shortest_path_length(4, 1, by_weight=True, algorithm=None)
            Traceback (most recent call last):
            ...
            ValueError: the graph contains an edge with negative weight
            sage: G.shortest_path_length(4, 1, by_weight=True, algorithm='Bellman-Ford_Boost')
            -1

        However, sometimes the result may be wrong, and no error is raised::

            sage: G = DiGraph([(0,1,1),(1,2,1),(0,3,1000),(3,4,-3000), (4,2,1000)])
            sage: G.shortest_path_length(0, 2, by_weight=True, algorithm='Bellman-Ford_Boost')
            -1000
            sage: G.shortest_path_length(0, 2, by_weight=True)
            2

        TESTS:

        If vertex is not in the graph::

            sage: G.shortest_path(0, 5)
            Traceback (most recent call last):
            ...
            ValueError: vertex '5' is not in the (di)graph
            sage: G.shortest_path(6, 5)
            Traceback (most recent call last):
            ...
            ValueError: vertex '6' is not in the (di)graph

        If no path exists from ``u`` to ``v`` (:trac:`28098`)::

            sage: G = Graph()
            sage: G.add_vertices([1, 2])
            sage: for alg in ['BFS', 'BFS_Bid', 'Dijkstra_NetworkX', 'Dijkstra_Bid_NetworkX',
            ....:             'Dijkstra_Bid', 'Bellman-Ford_Boost']:
            ....:     G.shortest_path_length(1, 2, algorithm=alg)
            +Infinity
            +Infinity
            +Infinity
            +Infinity
            +Infinity
            +Infinity
        """
        if not self.has_vertex(u):
            raise ValueError("vertex '{}' is not in the (di)graph".format(u))
        if not self.has_vertex(v):
            raise ValueError("vertex '{}' is not in the (di)graph".format(v))
        if u == v:  # to avoid a NetworkX bug
            return 0

        by_weight, weight_function = self._get_weight_function(by_weight=by_weight,
                                                               weight_function=weight_function,
                                                               check_weight=check_weight)

        if algorithm is None:
            algorithm = 'Dijkstra_Bid' if by_weight else 'BFS_Bid'
        elif algorithm in ['BFS', 'BFS_Bid']:
            if by_weight:
                raise ValueError("the '{}' algorithm does not work on weighted graphs".format(algorithm))
            # We don't want the default weight function
            weight_function = None

        if algorithm in ['BFS', 'Dijkstra_NetworkX', 'Bellman-Ford_Boost']:
            all_path_lengths = self.shortest_path_lengths(u, by_weight, algorithm, weight_function, check_weight)
            if v in all_path_lengths:
                return all_path_lengths[v]
            from sage.rings.infinity import Infinity
            return Infinity

        elif algorithm == "Dijkstra_Bid":
            return self._backend.bidirectional_dijkstra(u, v, weight_function, distance_flag=True)
        elif algorithm == "Dijkstra_Bid_NetworkX":
            import networkx
            if self.is_directed():
                G = networkx.DiGraph([(e[0], e[1], {'weight': weight_function(e)}) for e in self.edge_iterator()])
            else:
                G = networkx.Graph([(e[0], e[1], {'weight': weight_function(e)}) for e in self.edge_iterator()])
            G.add_nodes_from(self)
            try:
                return networkx.bidirectional_dijkstra(G, u, v)[0]
            except networkx.NetworkXNoPath:
                from sage.rings.infinity import Infinity
                return Infinity
        elif algorithm == "BFS_Bid":
            return self._backend.shortest_path(u, v, distance_flag=True)
        else:
            raise ValueError('unknown algorithm "{}"'.format(algorithm))

    def _check_weight_function(self, weight_function=None):
        r"""
        Check that an edge weight function outputs only numbers.

        The weight function inputs a labelled edge ``(u, v, l)`` and outputs its
        weight. Here, we check that the output is always a number (otherwise,
        several functions might have unexpected behavior). If the function fails
        the test, an exception is raised.

        INPUT:

        - ``weight_function`` -- function (default: ``None``); the weight
          function to be tested

        EXAMPLES:

        The standard weight function outputs labels::

            sage: G = Graph([(0, 1, 1), (1, 2, 3), (2, 3, 2)])
            sage: weight_function=lambda e:e[2]
            sage: G._check_weight_function(weight_function)
            sage: [weight_function(e) for e in G.edges(sort=True)]
            [1, 3, 2]

        However, it might be more complicated::

            sage: G = Graph([(0, 1, {'name':'a', 'weight':1}), (1, 2, {'name': 'b', 'weight': 3}), (2, 3, {'name': 'c', 'weight': 2})])
            sage: weight_function=lambda e:e[2]['weight']
            sage: G._check_weight_function(weight_function)
            sage: [weight_function(e) for e in G.edges(sort=True)]
            [1, 3, 2]

        A weight function that does not match labels::

            sage: G.add_edge((0, 3, {'name': 'd', 'weight': 'd'}))
            sage: G._check_weight_function(weight_function)
            Traceback (most recent call last):
            ...
            ValueError: the weight function cannot find the weight of (0, 3, {'name': 'd', 'weight': 'd'})

        Numeric string as a weight in weight_function::

            sage: G = Graph({0: {1: '123'}})
            sage: weight_function=lambda e:e[2]
            sage: G._check_weight_function(weight_function)
            Traceback (most recent call last):
            ...
            ValueError: the weight function cannot find the weight of (0, 1, '123')
        """
        for e in self.edge_iterator():
            try:
                temp = weight_function(e)
                float(temp)
                if isinstance(temp, (str, bytes)):
                    raise ValueError()
            except Exception:
                raise ValueError("the weight function cannot find the "
                                 "weight of " + str(e))

    def _get_weight_function(self, by_weight=False, weight_function=None, check_weight=True):
        r"""
        Return an edge weight function.

        An edge weight function is a function that takes as input an edge and
        outputs its weight.

        This method is a helper function for methods using the weight of edges.
        It either checks the validity of an input weight function, or returns a
        valid weight function on the edges.

        INPUT:

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
          in the graph are weighted, otherwise all edges have weight 1

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l``, if ``l``
          is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the weight_function outputs a number for each edge

        EXAMPLES:

        The default weight function outputs 1 for each edge::

            sage: G = Graph([(0, 1, 1), (1, 2, 3), (2, 3, 2)])
            sage: by_weight, weight_function = G._get_weight_function()
            sage: by_weight
            False
            sage: [weight_function(e) for e in G.edges(sort=True)]
            [1, 1, 1]

        The standard weight function outputs labels::

            sage: G = Graph([(0, 1, 1), (1, 2, 3), (2, 3, 2)])
            sage: by_weight, weight_function = G._get_weight_function(by_weight=True)
            sage: by_weight
            True
            sage: [weight_function(e) for e in G.edges(sort=True)]
            [1, 3, 2]

        However, it might be more complicated::

            sage: G = Graph([(0, 1, {'name':'a', 'weight':1}), (1, 2, {'name': 'b', 'weight': 3}), (2, 3, {'name': 'c', 'weight': 2})])
            sage: by_weight, weight_function = G._get_weight_function(weight_function=lambda e:e[2]['weight'])
            sage: by_weight
            True
            sage: [weight_function(e) for e in G.edges(sort=True)]
            [1, 3, 2]

        Numeric string as a weight in weight_function::

            sage: G = Graph({0: {1: '123'}})
            sage: by_weight, weight_function = G._get_weight_function(by_weight=True)
            Traceback (most recent call last):
            ...
            ValueError: the weight function cannot find the weight of (0, 1, '123')
        """
        if weight_function is not None:
            by_weight = True
        if by_weight:
            if weight_function is None:
                def weight_function(e):
                    return 1 if e[2] is None else e[2]
            if check_weight:
                self._check_weight_function(weight_function)
        else:
            def weight_function(e):
                return 1
        return by_weight, weight_function

    def shortest_paths(self, u, by_weight=False, algorithm=None,
                       weight_function=None, check_weight=True, cutoff=None):
        r"""
        Return a dictionary associating to each vertex ``v`` a shortest path
        from ``u`` to ``v``, if it exists.

        If `u` and `v` are not connected, vertex `v` is not present in the
        dictionary.

        INPUT:

        - ``u`` -- the starting vertex

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
          in the graph are weighted, otherwise all edges have weight 1

        - ``algorithm`` -- string (default: ``None``); one of the following
          algorithms:

          - ``'BFS'``: performs a BFS from ``u``. Does not work with edge
            weights.

          - ``'Dijkstra_NetworkX'``: the Dijkstra algorithm, implemented in
            NetworkX (works only with positive weights).

          - ``'Dijkstra_Boost'``: the Dijkstra algorithm, implemented in Boost
            (works only with positive weights).

          - ``'Bellman-Ford_Boost'``: the Bellman-Ford algorithm, implemented in
            Boost (works also with negative weights, if there is no negative
            cycle).

          - ``None`` (default): Sage chooses the best algorithm: ``'BFS'`` if
            ``by_weight`` is ``False``, ``'Dijkstra_Boost'`` if all weights are
            positive, ``'Bellman-Ford_Boost'`` otherwise.

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l``, if ``l``
          is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the weight_function outputs a number for each edge

        - ``cutoff`` -- integer (default: ``None``); integer depth to stop
          search (used only if ``algorithm=='BFS'``)

        EXAMPLES:

        Standard example::

            sage: D = graphs.DodecahedralGraph()
            sage: D.shortest_paths(0)
            {0: [0], 1: [0, 1], 2: [0, 1, 2], 3: [0, 19, 3], 4: [0, 19, 3, 4],
             5: [0, 1, 2, 6, 5], 6: [0, 1, 2, 6], 7: [0, 1, 8, 7], 8: [0, 1, 8],
             9: [0, 10, 9], 10: [0, 10], 11: [0, 10, 11], 12: [0, 10, 11, 12],
             13: [0, 10, 9, 13], 14: [0, 1, 8, 7, 14],
             15: [0, 19, 18, 17, 16, 15], 16: [0, 19, 18, 17, 16],
             17: [0, 19, 18, 17], 18: [0, 19, 18], 19: [0, 19]}

        All these paths are obviously induced graphs::

            sage: all(D.subgraph(p).is_isomorphic(graphs.PathGraph(len(p))) for p in D.shortest_paths(0).values())
            True

        ::

            sage: D.shortest_paths(0, cutoff=2)
            {0: [0], 1: [0, 1], 2: [0, 1, 2], 3: [0, 19, 3], 8: [0, 1, 8],
             9: [0, 10, 9], 10: [0, 10], 11: [0, 10, 11], 18: [0, 19, 18],
             19: [0, 19]}
            sage: G = Graph( { 0: {1: 1}, 1: {2: 1}, 2: {3: 1}, 3: {4: 2}, 4: {0: 2} }, sparse=True)
            sage: G.plot(edge_labels=True).show() # long time
            sage: G.shortest_paths(0, by_weight=True)
            {0: [0], 1: [0, 1], 2: [0, 1, 2], 3: [0, 1, 2, 3], 4: [0, 4]}

        Weighted shortest paths::

            sage: D = DiGraph([(0,1,1),(1,2,3),(0,2,5)])
            sage: D.shortest_paths(0)
            {0: [0], 1: [0, 1], 2: [0, 2]}
            sage: D.shortest_paths(0, by_weight=True)
            {0: [0], 1: [0, 1], 2: [0, 1, 2]}

        Using a weight function (this way, ``by_weight`` is set to ``True``)::

            sage: D = DiGraph([(0,1,{'weight':1}),(1,2,{'weight':3}),(0,2,{'weight':5})])
            sage: weight_function = lambda e:e[2]['weight']
            sage: D.shortest_paths(0, weight_function=weight_function)
            {0: [0], 1: [0, 1], 2: [0, 1, 2]}

        If the weight function does not match the label::

            sage: D.shortest_paths(0, weight_function=lambda e:e[2])
            Traceback (most recent call last):
            ...
            ValueError: the weight function cannot find the weight of (0, 1, {'weight': 1})

        However, if ``check_weight`` is set to ``False``, unexpected behavior
        may occur::

            sage: D.shortest_paths(0, algorithm='Dijkstra_NetworkX', weight_function=lambda e:e[2], check_weight=False)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for +: 'int' and 'dict'

        Negative weights::

            sage: D = DiGraph([(0,1,1),(1,2,-2),(0,2,4)])
            sage: D.shortest_paths(0, by_weight=True)
            {0: [0], 1: [0, 1], 2: [0, 1, 2]}

        Negative cycles::

            sage: D.add_edge(2,0,0)
            sage: D.shortest_paths(0, by_weight=True)
            Traceback (most recent call last):
            ...
            ValueError: the graph contains a negative cycle

        TESTS:

        If we ask for an unknown algorithm::

            sage: D = DiGraph([(0,1,1),(1,2,2),(0,2,4)])
            sage: D.shortest_paths(0, algorithm='tip top')
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm "tip top"

        If we ask for BFS in a weighted graph::

            sage: D.shortest_paths(0, algorithm='BFS', by_weight=True)
            Traceback (most recent call last):
            ...
            ValueError: the 'BFS' algorithm does not work on weighted graphs

        If we run Dijkstra with negative weights::

            sage: D = DiGraph([(0,1,2),(1,2,-2),(0,2,1)])
            sage: D.shortest_paths(0, algorithm='Dijkstra_Boost', by_weight=True)
            Traceback (most recent call last):
            ...
            RuntimeError: Dijkstra algorithm does not work with negative weights, use Bellman-Ford instead
            sage: D.shortest_paths(0, algorithm='Dijkstra_NetworkX', by_weight=True)
            Traceback (most recent call last):
            ...
            ValueError: ('Contradictory paths found:', 'negative weights?')
        """
        by_weight, weight_function = self._get_weight_function(by_weight=by_weight,
                                                               weight_function=weight_function,
                                                               check_weight=check_weight)

        if algorithm is None and not by_weight:
            algorithm = 'BFS'

        if algorithm == 'BFS':
            if by_weight:
                raise ValueError("the 'BFS' algorithm does not work on "
                                 "weighted graphs")
            return self._backend.shortest_path_all_vertices(u, cutoff)

        elif algorithm == 'Dijkstra_NetworkX':
            import networkx
            # If this is not present, an error might be raised by NetworkX
            if self.order() == 1 and self.has_vertex(u):
                return {u: [u]}
            if by_weight:
                if self.is_directed():
                    G = networkx.DiGraph([(e[0], e[1], {'weight': weight_function(e)}) for e in self.edge_iterator()])
                else:
                    G = networkx.Graph([(e[0], e[1], {'weight': weight_function(e)}) for e in self.edge_iterator()])
            else:
                # Needed to remove labels.
                if self.is_directed():
                    G = networkx.DiGraph(list(self.edges(labels=False, sort=False)))
                else:
                    G = networkx.Graph(list(self.edges(labels=False, sort=False)))
            G.add_nodes_from(self)
            return networkx.single_source_dijkstra_path(G, u)

        elif algorithm in ['Dijkstra_Boost', 'Bellman-Ford_Boost', None]:
            from sage.graphs.base.boost_graph import shortest_paths
            _, pred = shortest_paths(self, u, weight_function, algorithm)
            paths = {}
            for v in pred.keys():
                w = v
                path = [w]
                while w != u:
                    w = pred[w]
                    path.append(w)
                path.reverse()
                paths[v] = path
            return paths

        else:
            raise ValueError('unknown algorithm "{}"'.format(algorithm))

    def _path_length(self, path, by_weight=False, weight_function=None):
        r"""
        Return the (weighted) length of the path provided.

        If the path is empty, returns Infinity.

        .. WARNING::

            if the graph is unweighted, the algorithm does not check that the
            path exists.

        INPUT:

        - ``path`` -- an ordered list of vertices forming a path

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
          in the graph are weighted, otherwise all edges have weight 1

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l`` as a
          weight, if ``l`` is not ``None``, else ``1`` as a weight.

        EXAMPLES:

        The unweighted case::

            sage: G = graphs.CycleGraph(3)
            sage: G._path_length([0,1,2,0,1,2])
            5

        The weighted case::

            sage: G = Graph([(0,1,{'name':'a', 'weight':1}), (1,2,{'name':'b', 'weight':3}), (2,3,{'name':'c', 'weight':2})])
            sage: G._path_length([0,1,2,3])
            3
            sage: G._path_length([0,1,2,3], by_weight=True, weight_function=lambda e:e[2]['weight'])
            6

        If the path is empty::

            sage: G._path_length([0,1,2,3], by_weight=True, weight_function=lambda e:e[2]['weight'])
            6

        If we ask for a path that does not exist::

            sage: G._path_length([0,3], by_weight=False)
            1
            sage: G._path_length([0,3], by_weight=True, weight_function=lambda e:e[2]['weight'])
            Traceback (most recent call last):
            ...
            LookupError: (0, 3) is not an edge of the graph.
        """
        if not path:
            from sage.rings.infinity import Infinity
            return Infinity

        if by_weight or weight_function is not None:
            _, weight_function = self._get_weight_function(by_weight=by_weight,
                                                           weight_function=weight_function,
                                                           check_weight=False)
            return sum(weight_function((u, v, self.edge_label(u, v)))
                       for u, v in zip(path[:-1], path[1:]))
        else:
            return len(path) - 1

    def shortest_path_lengths(self, u, by_weight=False, algorithm=None,
                              weight_function=None, check_weight=True):
        r"""
        Return the length of a shortest path from ``u`` to any other vertex.

        Returns a dictionary of shortest path lengths keyed by targets,
        excluding all vertices that are not reachable from `u`.

        For more information on the input variables and more examples, we refer
        to :meth:`~GenericGraph.shortest_paths` which has the same input
        variables.

        INPUT:

        - ``u`` -- the starting vertex

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
          in the graph are weighted, otherwise all edges have weight 1

        - ``algorithm`` -- string (default: ``None``); one of the following
          algorithms:

          - ``'BFS'``: performs a BFS from ``u``. Does not work with edge
            weights.

          - ``'Dijkstra_NetworkX'``: the Dijkstra algorithm, implemented in
            NetworkX (works only with positive weights).

          - ``'Dijkstra_Boost'``: the Dijkstra algorithm, implemented in Boost
            (works only with positive weights).

          - ``'Bellman-Ford_Boost'``: the Bellman-Ford algorithm, implemented in
            Boost (works also with negative weights, if there is no negative
            cycle).

          - ``None`` (default): Sage chooses the best algorithm: ``'BFS'`` if
            ``by_weight`` is ``False``, ``'Dijkstra_Boost'`` if all weights are
            positive, ``'Bellman-Ford_Boost'`` otherwise.

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l``, if ``l``
          is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the weight_function outputs a number for each edge

        EXAMPLES:

        Unweighted case::

            sage: D = graphs.DodecahedralGraph()
            sage: D.shortest_path_lengths(0)
            {0: 0, 1: 1, 2: 2, 3: 2, 4: 3, 5: 4, 6: 3, 7: 3, 8: 2, 9: 2, 10: 1, 11: 2, 12: 3, 13: 3, 14: 4, 15: 5, 16: 4, 17: 3, 18: 2, 19: 1}

        Weighted case::

            sage: G = Graph( { 0: {1: 1}, 1: {2: 1}, 2: {3: 1}, 3: {4: 2}, 4: {0: 2} }, sparse=True)
            sage: G.plot(edge_labels=True).show() # long time
            sage: G.shortest_path_lengths(0, by_weight=True)
            {0: 0, 1: 1, 2: 2, 3: 3, 4: 2}

        Using a weight function::

            sage: D = DiGraph([(0,1,{'weight':1}),(1,2,{'weight':3}),(0,2,{'weight':5})])
            sage: weight_function = lambda e:e[2]['weight']
            sage: D.shortest_path_lengths(1, algorithm='Dijkstra_NetworkX', by_weight=False)
            {1: 0, 2: 1}
            sage: D.shortest_path_lengths(0, weight_function=weight_function)
            {0: 0, 1: 1, 2: 4}
            sage: D.shortest_path_lengths(1, weight_function=weight_function)
            {1: 0, 2: 3}

        Negative weights::

            sage: D = DiGraph([(0,1,{'weight':-1}),(1,2,{'weight':3}),(0,2,{'weight':5})])
            sage: D.shortest_path_lengths(0, weight_function=weight_function)
            {0: 0, 1: -1, 2: 2}

        Negative cycles::

            sage: D = DiGraph([(0,1,{'weight':-5}),(1,2,{'weight':3}),(2,0,{'weight':1})])
            sage: D.shortest_path_lengths(0, weight_function=weight_function)
            Traceback (most recent call last):
            ...
            ValueError: the graph contains a negative cycle

        Checking that distances are equal regardless of the algorithm used::

            sage: g = graphs.Grid2dGraph(5,5)
            sage: d1 = g.shortest_path_lengths((0,0), algorithm="BFS")
            sage: d2 = g.shortest_path_lengths((0,0), algorithm="Dijkstra_NetworkX")
            sage: d3 = g.shortest_path_lengths((0,0), algorithm="Dijkstra_Boost")
            sage: d4 = g.shortest_path_lengths((0,0), algorithm="Bellman-Ford_Boost")
            sage: d1 == d2 == d3 == d4
            True
        """
        by_weight, weight_function = self._get_weight_function(by_weight=by_weight,
                                                               weight_function=weight_function,
                                                               check_weight=check_weight)

        if algorithm is None and not by_weight:
            algorithm = 'BFS'

        if algorithm == 'BFS':
            if by_weight:
                raise ValueError("the 'BFS' algorithm does not work on weighted graphs")
            return self._backend.shortest_path_all_vertices(u, cutoff=None, distance_flag=True)

        elif algorithm == 'Dijkstra_NetworkX':
            import networkx
            # If this is not present, an error might be raised by NetworkX
            if self.num_verts() == 1 and next(self.vertex_iterator()) == u:
                return {u: [u]}
            if by_weight:
                if self.is_directed():
                    G = networkx.DiGraph([(e[0], e[1], {'weight': weight_function(e)}) for e in self.edge_iterator()])
                else:
                    G = networkx.Graph([(e[0], e[1], {'weight': weight_function(e)}) for e in self.edge_iterator()])
            else:
                # Needed to remove labels.
                if self.is_directed():
                    G = networkx.DiGraph(list(self.edges(labels=False, sort=False)))
                else:
                    G = networkx.Graph(list(self.edges(labels=False, sort=False)))
            G.add_nodes_from(self)
            return networkx.single_source_dijkstra_path_length(G, u)

        elif algorithm in ['Dijkstra_Boost', 'Bellman-Ford_Boost', None]:
            from sage.graphs.base.boost_graph import shortest_paths
            return shortest_paths(self, u, weight_function, algorithm)[0]

        else:
            raise ValueError('unknown algorithm "{}"'.format(algorithm))

    def shortest_path_all_pairs(self, by_weight=False, algorithm=None,
                                weight_function=None, check_weight=True):
        r"""
        Return a shortest path between each pair of vertices.

        INPUT:

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
          in the graph are weighted, otherwise all edges have weight 1

        - ``algorithm`` -- string (default: ``None``); one of the following
          algorithms:

          - ``'BFS'``: the computation is done through a BFS centered on each
            vertex successively. Works only if ``by_weight==False``.

          - ``'Floyd-Warshall-Cython'``: the Cython implementation of the
            Floyd-Warshall algorithm. Works only if ``by_weight==False``.

          - ``'Floyd-Warshall-Python'``: the Python implementation of the
            Floyd-Warshall algorithm. Works also with weighted graphs, even with
            negative weights (but no negative cycle is allowed).

          - ``'Floyd-Warshall_Boost'``: the Boost implementation of the
            Floyd-Warshall algorithm. Works also with weighted graphs, even with
            negative weights (but no negative cycle is allowed).

          - ``'Floyd-Warshall_SciPy'``: the SciPy implementation of the
            Floyd-Warshall algorithm. Works also with weighted graphs, even with
            negative weights (but no negative cycle is allowed).

          - ``'Dijkstra_NetworkX'``: the Dijkstra algorithm, implemented in
            NetworkX. It works with weighted graphs, but no negative weight is
            allowed.

          - ``'Dijkstra_Boost'``: the Dijkstra algorithm, implemented in Boost
            (works only with positive weights).

          - ``'Johnson_Boost'``: the Johnson algorithm, implemented in Boost
            (works also with negative weights, if there is no negative cycle).

          - ``None`` (default): Sage chooses the best algorithm: ``'BFS'`` if
            ``by_weight`` is ``False``, ``'Dijkstra_Boost'`` if all weights are
            positive, ``'Floyd-Warshall_Boost'`` otherwise.

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l``, if ``l``
          is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the weight_function outputs a number for each edge

        OUTPUT:

        A tuple ``(dist, pred)``. They are both dicts of dicts. The first
        indicates the length ``dist[u][v]`` of the shortest weighted path from
        `u` to `v`. The second is a compact representation of all the paths - it
        indicates the predecessor ``pred[u][v]`` of `v` in the shortest path
        from `u` to `v`.

        .. NOTE::

            Only reachable vertices are present in the dictionaries.

        .. NOTE::

            There is a Cython version of this method that is usually much faster
            for large graphs, as most of the time is actually spent building the
            final double dictionary. Everything on the subject is to be found in
            the :mod:`~sage.graphs.distances_all_pairs` module.

        EXAMPLES:

        Some standard examples (see :meth:`~GenericGraph.shortest_paths` for
        more examples on how to use the input variables)::

            sage: G = Graph( { 0: {1: 1}, 1: {2: 1}, 2: {3: 1}, 3: {4: 2}, 4: {0: 2} }, sparse=True)
            sage: G.plot(edge_labels=True).show() # long time
            sage: dist, pred = G.shortest_path_all_pairs(by_weight = True)
            sage: dist
            {0: {0: 0, 1: 1, 2: 2, 3: 3, 4: 2},
             1: {0: 1, 1: 0, 2: 1, 3: 2, 4: 3},
             2: {0: 2, 1: 1, 2: 0, 3: 1, 4: 3},
             3: {0: 3, 1: 2, 2: 1, 3: 0, 4: 2},
             4: {0: 2, 1: 3, 2: 3, 3: 2, 4: 0}}
            sage: pred
            {0: {0: None, 1: 0, 2: 1, 3: 2, 4: 0},
             1: {0: 1, 1: None, 2: 1, 3: 2, 4: 0},
             2: {0: 1, 1: 2, 2: None, 3: 2, 4: 3},
             3: {0: 1, 1: 2, 2: 3, 3: None, 4: 3},
             4: {0: 4, 1: 0, 2: 3, 3: 4, 4: None}}
            sage: pred[0]
            {0: None, 1: 0, 2: 1, 3: 2, 4: 0}
            sage: G = Graph( { 0: {1: {'weight':1}}, 1: {2: {'weight':1}}, 2: {3: {'weight':1}}, 3: {4: {'weight':2}}, 4: {0: {'weight':2}} }, sparse=True)
            sage: dist, pred = G.shortest_path_all_pairs(weight_function = lambda e:e[2]['weight'])
            sage: dist
            {0: {0: 0, 1: 1, 2: 2, 3: 3, 4: 2},
             1: {0: 1, 1: 0, 2: 1, 3: 2, 4: 3},
             2: {0: 2, 1: 1, 2: 0, 3: 1, 4: 3},
             3: {0: 3, 1: 2, 2: 1, 3: 0, 4: 2},
             4: {0: 2, 1: 3, 2: 3, 3: 2, 4: 0}}
            sage: pred
            {0: {0: None, 1: 0, 2: 1, 3: 2, 4: 0},
             1: {0: 1, 1: None, 2: 1, 3: 2, 4: 0},
             2: {0: 1, 1: 2, 2: None, 3: 2, 4: 3},
             3: {0: 1, 1: 2, 2: 3, 3: None, 4: 3},
             4: {0: 4, 1: 0, 2: 3, 3: 4, 4: None}}

        So for example the shortest weighted path from `0` to `3` is obtained as
        follows. The predecessor of `3` is ``pred[0][3] == 2``, the predecessor
        of `2` is ``pred[0][2] == 1``, and the predecessor of `1` is
        ``pred[0][1] == 0``.

        ::

            sage: G = Graph( { 0: {1:None}, 1: {2:None}, 2: {3: 1}, 3: {4: 2}, 4: {0: 2} }, sparse=True )
            sage: G.shortest_path_all_pairs()
            ({0: {0: 0, 1: 1, 2: 2, 3: 2, 4: 1},
            1: {0: 1, 1: 0, 2: 1, 3: 2, 4: 2},
            2: {0: 2, 1: 1, 2: 0, 3: 1, 4: 2},
            3: {0: 2, 1: 2, 2: 1, 3: 0, 4: 1},
            4: {0: 1, 1: 2, 2: 2, 3: 1, 4: 0}},
            {0: {0: None, 1: 0, 2: 1, 3: 4, 4: 0},
            1: {0: 1, 1: None, 2: 1, 3: 2, 4: 0},
            2: {0: 1, 1: 2, 2: None, 3: 2, 4: 3},
            3: {0: 4, 1: 2, 2: 3, 3: None, 4: 3},
            4: {0: 4, 1: 0, 2: 3, 3: 4, 4: None}})
            sage: G.shortest_path_all_pairs(weight_function=lambda e:(e[2] if e[2] is not None else 1))
            ({0: {0: 0, 1: 1, 2: 2, 3: 3, 4: 2},
            1: {0: 1, 1: 0, 2: 1, 3: 2, 4: 3},
            2: {0: 2, 1: 1, 2: 0, 3: 1, 4: 3},
            3: {0: 3, 1: 2, 2: 1, 3: 0, 4: 2},
            4: {0: 2, 1: 3, 2: 3, 3: 2, 4: 0}},
            {0: {0: None, 1: 0, 2: 1, 3: 2, 4: 0},
            1: {0: 1, 1: None, 2: 1, 3: 2, 4: 0},
            2: {0: 1, 1: 2, 2: None, 3: 2, 4: 3},
            3: {0: 1, 1: 2, 2: 3, 3: None, 4: 3},
            4: {0: 4, 1: 0, 2: 3, 3: 4, 4: None}})

        Checking that distances are equal regardless of the algorithm used::

            sage: g = graphs.Grid2dGraph(5,5)
            sage: d1, _ = g.shortest_path_all_pairs(algorithm="BFS")
            sage: d2, _ = g.shortest_path_all_pairs(algorithm="Floyd-Warshall-Cython")
            sage: d3, _ = g.shortest_path_all_pairs(algorithm="Floyd-Warshall-Python")
            sage: d4, _ = g.shortest_path_all_pairs(algorithm="Dijkstra_NetworkX")
            sage: d5, _ = g.shortest_path_all_pairs(algorithm="Dijkstra_Boost")
            sage: d6, _ = g.shortest_path_all_pairs(algorithm="Johnson_Boost")
            sage: d7, _ = g.shortest_path_all_pairs(algorithm="Floyd-Warshall_Boost")
            sage: d8, _ = g.shortest_path_all_pairs(algorithm="Floyd-Warshall_SciPy")
            sage: d1 == d2 == d3 == d4 == d5 == d6 == d7 == d8
            True

        Checking that distances are equal regardless of the algorithm used::

            sage: g = digraphs.RandomDirectedGNM(6,12)
            sage: d1, _ = g.shortest_path_all_pairs(algorithm="BFS")
            sage: d2, _ = g.shortest_path_all_pairs(algorithm="Floyd-Warshall-Cython")
            sage: d3, _ = g.shortest_path_all_pairs(algorithm="Floyd-Warshall-Python")
            sage: d4, _ = g.shortest_path_all_pairs(algorithm="Dijkstra_NetworkX")
            sage: d5, _ = g.shortest_path_all_pairs(algorithm="Dijkstra_Boost")
            sage: d6, _ = g.shortest_path_all_pairs(algorithm="Johnson_Boost")
            sage: d7, _ = g.shortest_path_all_pairs(algorithm="Floyd-Warshall_Boost")
            sage: d8, _ = g.shortest_path_all_pairs(algorithm="Floyd-Warshall_SciPy")
            sage: d1 == d2 == d3 == d4 == d5 == d6 == d7 == d8
            True

        Checking that weighted distances are equal regardless of the algorithm
        used::

            sage: g = graphs.CompleteGraph(5)
            sage: import random
            sage: for v, w in g.edges(labels=False, sort=False):
            ....:     g.add_edge(v, w, random.uniform(1, 10))
            sage: d1, _ = g.shortest_path_all_pairs(algorithm="Floyd-Warshall-Python")
            sage: d2, _ = g.shortest_path_all_pairs(algorithm="Dijkstra_NetworkX")
            sage: d3, _ = g.shortest_path_all_pairs(algorithm="Dijkstra_Boost")
            sage: d4, _ = g.shortest_path_all_pairs(algorithm="Johnson_Boost")
            sage: d5, _ = g.shortest_path_all_pairs(algorithm="Floyd-Warshall_Boost")
            sage: d6, _ = g.shortest_path_all_pairs(algorithm="Floyd-Warshall_SciPy")
            sage: d1 == d2 == d3 == d4 == d5 == d6
            True

        Checking a random path is valid::

            sage: dist, path = g.shortest_path_all_pairs(algorithm="BFS")
            sage: u,v = g.random_vertex(), g.random_vertex()
            sage: p = [v]
            sage: while p[0] is not None:
            ....:   p.insert(0,path[u][p[0]])
            sage: len(p) == dist[u][v] + 2
            True

        Negative weights::

            sage: g = DiGraph([(0,1,-2),(1,0,1)], weighted=True)
            sage: g.shortest_path_all_pairs(by_weight=True)
            Traceback (most recent call last):
            ...
            ValueError: the graph contains a negative cycle

        Unreachable vertices are not present in the dictionaries::

            sage: g = DiGraph([(0,1,1),(1,2,2)])
            sage: g.shortest_path_all_pairs(algorithm='BFS')
            ({0: {0: 0, 1: 1, 2: 2}, 1: {1: 0, 2: 1}, 2: {2: 0}},
             {0: {0: None, 1: 0, 2: 1}, 1: {1: None, 2: 1}, 2: {2: None}})
            sage: g.shortest_path_all_pairs(algorithm='Dijkstra_NetworkX')
            ({0: {0: 0, 1: 1, 2: 2}, 1: {1: 0, 2: 1}, 2: {2: 0}},
             {0: {0: None, 1: 1, 2: 1}, 1: {1: None, 2: 2}, 2: {2: None}})
            sage: g.shortest_path_all_pairs(algorithm='Dijkstra_Boost')
            ({0: {0: 0, 1: 1, 2: 2}, 1: {1: 0, 2: 1}, 2: {2: 0}},
             {0: {0: None, 1: 0, 2: 1}, 1: {1: None, 2: 1}, 2: {2: None}})
            sage: g.shortest_path_all_pairs(algorithm='Floyd-Warshall-Python')
            ({0: {0: 0, 1: 1, 2: 2}, 1: {1: 0, 2: 1}, 2: {2: 0}},
             {0: {0: None, 1: 0, 2: 1}, 1: {1: None, 2: 1}, 2: {2: None}})
            sage: g.shortest_path_all_pairs(algorithm='Floyd-Warshall-Cython')
            ({0: {0: 0, 1: 1, 2: 2}, 1: {1: 0, 2: 1}, 2: {2: 0}},
             {0: {0: None, 1: 0, 2: 1}, 1: {1: None, 2: 1}, 2: {2: None}})
            sage: g.shortest_path_all_pairs(algorithm='Floyd-Warshall_SciPy')
            ({0: {0: 0.0, 1: 1.0, 2: 2.0}, 1: {1: 0.0, 2: 1.0}, 2: {2: 0.0}},
             {0: {0: None, 1: 0, 2: 1}, 1: {1: None, 2: 1}, 2: {2: None}})

        In order to change the default behavior if the graph is disconnected,
        we can use default values with dictionaries::

            sage: G = 2*graphs.PathGraph(2)
            sage: d,_ = G.shortest_path_all_pairs()
            sage: import itertools
            sage: from sage.rings.infinity import Infinity
            sage: for u,v in itertools.combinations(G.vertex_iterator(), 2):
            ....:     print("dist({}, {}) = {}".format(u,v, d[u].get(v,+Infinity)))
            dist(0, 1) = 1
            dist(0, 2) = +Infinity
            dist(0, 3) = +Infinity
            dist(1, 2) = +Infinity
            dist(1, 3) = +Infinity
            dist(2, 3) = 1

        TESTS:

        Wrong name for ``algorithm``::

            sage: g.shortest_path_all_pairs(algorithm="Bob")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm "Bob"

        Algorithms that do not work with weights::

            sage: g = Graph({0: {1:1}, 1: {2:1}, 2: {3: 1}, 3: {4: 2}, 4: {0: 2}}, sparse=True )
            sage: g.shortest_path_all_pairs(algorithm="BFS", by_weight=True)
            Traceback (most recent call last):
            ...
            ValueError: algorithm 'BFS' does not work with weights
            sage: g.shortest_path_all_pairs(algorithm="Floyd-Warshall-Cython", by_weight=True)
            Traceback (most recent call last):
            ...
            ValueError: algorithm 'Floyd-Warshall-Cython' does not work with weights

        Dijkstra with negative weights::

            sage: g = Graph({0: {1:1}, 1: {2:1}, 2: {3: 1}, 3: {4: -2}, 4: {0: -2}})
            sage: g.shortest_path_all_pairs(algorithm="Dijkstra_Boost", by_weight=True)
            Traceback (most recent call last):
            ...
            RuntimeError: Dijkstra algorithm does not work with negative weights, use Bellman-Ford instead
        """
        from sage.rings.infinity import Infinity

        by_weight, weight_function = self._get_weight_function(by_weight=by_weight,
                                                               weight_function=weight_function,
                                                               check_weight=check_weight)

        if algorithm is None:
            if by_weight:
                if any(weight_function(e) < 0 for e in self.edge_iterator()):
                    algorithm = "Floyd-Warshall_Boost"
                else:
                    algorithm = "Dijkstra_Boost"
            else:
                algorithm = "BFS"

        if by_weight and algorithm in ['BFS', "Floyd-Warshall-Cython"]:
            raise ValueError("algorithm '" + algorithm + "' does not work "
                             "with weights")

        if algorithm == "BFS":
            from sage.graphs.distances_all_pairs import distances_and_predecessors_all_pairs
            return distances_and_predecessors_all_pairs(self)

        elif algorithm == "Floyd-Warshall-Cython":
            from sage.graphs.distances_all_pairs import floyd_warshall
            return floyd_warshall(self, distances=True)

        elif algorithm == "Floyd-Warshall_Boost":
            from sage.graphs.base.boost_graph import floyd_warshall_shortest_paths
            return floyd_warshall_shortest_paths(self, weight_function, distances=True, predecessors=True)

        elif algorithm == "Floyd-Warshall_SciPy":
            # Turn the graph to a n x n matrix
            n = self.order()
            int_to_vertex = list(self)
            vertex_to_int = {u: i for i, u in enumerate(int_to_vertex)}
            if by_weight:
                M = [[float('inf')]*n for _ in range(n)]
                for i in range(n):
                    M[i][i] = 0
                for e in self.edges(sort=False):
                    u = vertex_to_int[e[0]]
                    v = vertex_to_int[e[1]]
                    M[u][v] = min(M[u][v], weight_function(e))
                    if not self.is_directed():
                        M[v][u] = M[u][v]
            else:
                M = self.adjacency_matrix(vertices=int_to_vertex)

            # We call the Floyd-Warshall method from SciPy
            from numpy import array as np_array
            from scipy.sparse.csgraph import floyd_warshall
            dd, pp = floyd_warshall(np_array(M), directed=self.is_directed(),
                                    return_predecessors=True, unweighted=not by_weight)

            # and format the result
            dist = {int_to_vertex[i]: {int_to_vertex[j]: dd[i, j]
                                       for j in range(n) if dd[i, j] != +Infinity}
                    for i in range(n)}
            pred = {int_to_vertex[i]: {int_to_vertex[j]: (int_to_vertex[pp[i, j]] if i != j else None)
                                       for j in range(n) if (i == j or pp[i, j] != -9999)}
                    for i in range(n)}
            return dist, pred

        elif algorithm == "Johnson_Boost":
            from sage.graphs.base.boost_graph import johnson_shortest_paths
            return johnson_shortest_paths(self, weight_function, distances=True, predecessors=True)

        elif algorithm == "Dijkstra_Boost":
            from sage.graphs.base.boost_graph import shortest_paths
            dist = dict()
            pred = dict()
            for u in self:
                dist[u], pred[u] = shortest_paths(self, u, weight_function, algorithm)
            return dist, pred

        elif algorithm == "Dijkstra_NetworkX":
            dist = dict()
            pred = dict()
            for u in self:
                paths = self.shortest_paths(u, by_weight=by_weight,
                                            algorithm=algorithm,
                                            weight_function=weight_function)
                dist[u] = {v: self._path_length(p, by_weight=by_weight,
                                                weight_function=weight_function)
                           for v, p in paths.items()}
                pred[u] = {v: None if len(p) <= 1 else p[1]
                           for v, p in paths.items()}
            return dist, pred

        elif algorithm != "Floyd-Warshall-Python":
            raise ValueError('unknown algorithm "{}"'.format(algorithm))

        if self.is_directed():
            neighbor = self.neighbor_out_iterator
        else:
            neighbor = self.neighbor_iterator

        dist = {}
        pred = {}
        for u in self:
            du = {u: 0}
            pu = {u: None}

            for v in neighbor(u):
                if by_weight is False:
                    du[v] = 1
                else:
                    du[v] = weight_function((u, v, self.edge_label(u, v)))
                pu[v] = u

            dist[u] = du
            pred[u] = pu

        for w in self:
            dw = dist[w]
            for u in self:
                du = dist[u]
                for v in self:
                    if du.get(v, Infinity) > du.get(w, Infinity) + dw.get(v, Infinity):
                        if u == v:
                            raise ValueError("the graph contains a negative cycle")
                        du[v] = du[w] + dw[v]
                        pred[u][v] = pred[w][v]

        return dist, pred

    def wiener_index(self, by_weight=False, algorithm=None,
                     weight_function=None, check_weight=True):
        r"""
        Return the Wiener index of ``self``.

        The graph is expected to have no cycles of negative weight.

        The Wiener index of a undirected graph `G` is `W(G) = \frac{1}{2}
        \sum_{u,v\in G} d(u,v)` where `d(u,v)` denotes the distance between
        vertices `u` and `v` (see [KRG1996]_).

        The Wiener index of a directed graph `G` is defined as the sum of the
        distances between each pairs of vertices, i.e.,
        `W(G) = \sum_{u,v\in G} d(u,v)`.

        For more information on the input variables and more examples, we refer
        to :meth:`~GenericGraph.shortest_paths` and
        :meth:`~GenericGraph.shortest_path_all_pairs`, which have very similar
        input variables.

        INPUT:

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
          in the graph are weighted, otherwise all edges have weight 1

        - ``algorithm`` -- string (default: ``None``); one of the following
          algorithms:

          - For ``by_weight==False`` only:

            - ``'BFS'`` - the computation is done through a BFS centered on
              each vertex successively.

            - ``'Floyd-Warshall-Cython'`` - the Cython implementation of
              the Floyd-Warshall algorithm. Usually slower than ``'BFS'``.

          - For graphs without negative weights:

            - ``'Dijkstra_Boost'``: the Dijkstra algorithm, implemented in
              Boost.

            - ``'Dijkstra_NetworkX'``: the Dijkstra algorithm, implemented in
              NetworkX. Usually slower than ``'Dijkstra_Boost'``.

          - For graphs with negative weights:

            - ``'Bellman-Ford_Boost'``: the Bellman-Ford algorithm, implemented
              in Boost.

            - ``'Johnson_Boost'``: the Johnson algorithm, implemented in
              Boost.

            - ``'Floyd-Warshall-Python'`` - the Python implementation of
              the Floyd-Warshall algorithm. Usually slower than
              ``'Johnson_Boost'``.

          - ``None`` (default): Sage chooses the best algorithm: ``'BFS'`` for
            unweighted graphs, ``'Dijkstra_Boost'`` if all weights are
            positive, ``'Johnson_Boost'``, otherwise.

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l`` as a
          weight, if ``l`` is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the weight_function outputs a number for each edge

        .. NOTE::

            Some algorithms (e.g., Boost algorithms) use floating point numbers
            for internal computations. Whenever the solution is integral, we try
            to convert the returned value to an integer.

        EXAMPLES::

            sage: G = Graph( { 0: {1: None}, 1: {2: None}, 2: {3: 1}, 3: {4: 2}, 4: {0: 2} }, sparse=True)
            sage: G.wiener_index()
            15
            sage: G.wiener_index(weight_function=lambda e:(e[2] if e[2] is not None else 1))
            20
            sage: G.wiener_index(weight_function=lambda e:(e[2] if e[2] is not None else 200))
            820
            sage: G.wiener_index(algorithm='BFS')
            15
            sage: G.wiener_index(algorithm='Floyd-Warshall-Cython')
            15
            sage: G.wiener_index(algorithm='Floyd-Warshall-Python')
            15
            sage: G.wiener_index(algorithm='Dijkstra_Boost')
            15
            sage: G.wiener_index(algorithm='Bellman-Ford_Boost')
            15
            sage: G.wiener_index(algorithm='Johnson_Boost')
            15
            sage: G.wiener_index(algorithm='Dijkstra_NetworkX')
            15

        Wiener index of complete (di)graphs::

            sage: n = 5
            sage: g = graphs.CompleteGraph(n)
            sage: g.wiener_index() == (n * (n - 1)) / 2
            True
            sage: g = digraphs.Complete(n)
            sage: g.wiener_index() == n * (n - 1)
            True

        Wiener index of circuit digraphs::

            sage: n = 7
            sage: g = digraphs.Circuit(n)
            sage: w = lambda x: (x*x*(x-1))/2
            sage: g.wiener_index(algorithm='Dijkstra_Boost') == w(n)
            True

        Wiener index of a graph of order 1::

            sage: Graph(1).wiener_index()
            0

        The Wiener index is not defined on the empty graph::

            sage: Graph().wiener_index()
            Traceback (most recent call last):
            ...
            ValueError: Wiener index is not defined for the empty graph

        TESTS::

            sage: weight_function=lambda e:(e[2] if e[2] is not None else 200)
            sage: G.wiener_index(algorithm='BFS', weight_function=weight_function)
            Traceback (most recent call last):
            ...
            ValueError: algorithm 'BFS' does not work with weights
            sage: G.wiener_index(algorithm='Floyd-Warshall-Cython', weight_function=weight_function)
            Traceback (most recent call last):
            ...
            ValueError: algorithm 'Floyd-Warshall-Cython' does not work with weights

            sage: Graph([(0, 1, 1)]).wiener_index(algorithm="coco beach")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm "coco beach"
        """
        if not self:
            raise ValueError("Wiener index is not defined for the empty graph")
        elif self.order() == 1:
            return 0

        by_weight, weight_function = self._get_weight_function(by_weight=by_weight,
                                                               weight_function=weight_function,
                                                               check_weight=check_weight)

        if algorithm in ['BFS', 'Floyd-Warshall-Cython']:
            if by_weight:
                raise ValueError("algorithm '{}' does not work with weights".format(algorithm))
            # We don't want the default weight function
            weight_function = None

        if algorithm == 'BFS' or (algorithm is None and not by_weight):
            from .distances_all_pairs import wiener_index
            return wiener_index(self)

        if algorithm in ['Dijkstra_Boost', 'Bellman-Ford_Boost'] or (algorithm is None and by_weight):
            from .base.boost_graph import wiener_index
            WI = wiener_index(self, algorithm=algorithm,
                              weight_function=weight_function,
                              check_weight=False)

        elif (not self.is_connected()
              or (self.is_directed() and not self.is_strongly_connected())):
            from sage.rings.infinity import Infinity
            return Infinity

        elif algorithm == "Dijkstra_NetworkX":
            import networkx
            if by_weight:
                if self.is_directed():
                    G = networkx.DiGraph([(e[0], e[1], {'weight': weight_function(e)}) for e in self.edges(sort=False)])
                else:
                    G = networkx.Graph([(e[0], e[1], {'weight': weight_function(e)}) for e in self.edges(sort=False)])
            else:
                # Needed to remove labels.
                if self.is_directed():
                    G = networkx.DiGraph(list(self.edges(labels=False, sort=False)))
                else:
                    G = networkx.Graph(list(self.edges(labels=False, sort=False)))
            G.add_nodes_from(self)
            total = sum(sum(networkx.single_source_dijkstra_path_length(G, u).values())
                        for u in G)
            WI = total if self.is_directed() else (total / 2)

        else:
            distances = self.shortest_path_all_pairs(
                by_weight=by_weight, algorithm=algorithm,
                weight_function=weight_function, check_weight=False)[0]
            total = sum(sum(u.values()) for u in distances.values())
            WI = total if self.is_directed() else (total / 2)

        if WI in ZZ:
            WI = Integer(WI)

        return WI

    def average_distance(self, by_weight=False, algorithm=None,
                         weight_function=None, check_weight=True):
        r"""
        Return the average distance between vertices of the graph.

        Formally, for a graph `G` this value is equal to `\frac 1 {n(n-1)}
        \sum_{u,v\in G} d(u,v)` where `d(u,v)` denotes the distance between
        vertices `u` and `v` and `n` is the number of vertices in `G`.

        For more information on the input variables and more examples, we refer
        to :meth:`~GenericGraph.wiener_index` and
        :meth:`~GenericGraph.shortest_path_all_pairs`,
        which have very similar input variables.

        INPUT:

        - ``by_weight`` -- boolean (default: ``False``); if ``True``, the edges
          in the graph are weighted, otherwise all edges have weight 1

        - ``algorithm`` -- string (default: ``None``); one of the
          algorithms available for method :meth:`~GenericGraph.wiener_index`

        - ``weight_function`` -- function (default: ``None``); a function that
          takes as input an edge ``(u, v, l)`` and outputs its weight. If not
          ``None``, ``by_weight`` is automatically set to ``True``. If ``None``
          and ``by_weight`` is ``True``, we use the edge label ``l``, if ``l``
          is not ``None``, else ``1`` as a weight.

        - ``check_weight`` -- boolean (default: ``True``); if ``True``, we check
          that the weight_function outputs a number for each edge

        EXAMPLES:

        From [GYLL1993]_::

            sage: g=graphs.PathGraph(10)
            sage: w=lambda x: (x*(x*x -1)/6)/(x*(x-1)/2)
            sage: g.average_distance()==w(10)
            True

        Average distance of a circuit::

            sage: g = digraphs.Circuit(6)
            sage: g.average_distance()
            3

        TESTS:

        Giving an empty graph::

            sage: g = Graph()
            sage: g.average_distance()
            Traceback (most recent call last):
            ...
            ValueError: average distance is not defined for empty or one-element graph

        :trac:`22885`::

            sage: G = graphs.PetersenGraph()
            sage: G2 = Graph([(u, v, 2) for u,v in G.edge_iterator(labels=False)], weighted=True)
            sage: G2.average_distance()
            5/3
            sage: G2.average_distance(by_weight=True)
            10/3
        """
        if self.order() < 2:
            raise ValueError("average distance is not defined for empty or one-element graph")
        WI = self.wiener_index(by_weight=by_weight, algorithm=algorithm,
                               weight_function=weight_function, check_weight=check_weight)
        f = 1 if self.is_directed() else 2
        if WI in ZZ:
            return QQ((f * WI, self.order() * (self.order() - 1)))
        return f * WI / (self.order() * (self.order() - 1))

    # Searches

    def breadth_first_search(self, start, ignore_direction=False,
                             distance=None, neighbors=None,
                             report_distance=False, edges=False):
        """
        Return an iterator over the vertices in a breadth-first ordering.

        INPUT:

        - ``start`` -- vertex or list of vertices from which to start the
          traversal

        - ``ignore_direction`` -- boolean (default: ``False``); only applies to
          directed graphs. If ``True``, searches across edges in either
          direction.

        - ``distance`` -- integer (default: ``None``); the maximum distance from
          the ``start`` nodes to traverse. The ``start`` nodes are at distance
          zero from themselves.

        - ``neighbors`` -- function (default: ``None``); a function that inputs
          a vertex and return a list of vertices. For an undirected graph,
          ``neighbors`` is by default the :meth:`.neighbors` function. For a
          digraph, the ``neighbors`` function defaults to the
          :meth:`~DiGraph.neighbor_out_iterator` function of the graph.

        - ``report_distance`` -- boolean (default: ``False``); if ``True``,
          reports pairs ``(vertex, distance)`` where ``distance`` is the
          distance from the ``start`` nodes. If ``False`` only the vertices are
          reported.

        - ``edges`` -- boolean (default: ``False``); whether to return the edges
          of the BFS tree in the order of visit or the vertices (default).
          Edges are directed in root to leaf orientation of the tree.

          Note that parameters ``edges`` and ``report_distance`` cannot be
          ``True`` simultaneously.

        .. SEEALSO::

            - :meth:`breadth_first_search <sage.graphs.base.c_graph.CGraphBackend.breadth_first_search>`
              -- breadth-first search for fast compiled graphs.

            - :meth:`depth_first_search <sage.graphs.base.c_graph.CGraphBackend.depth_first_search>`
              -- depth-first search for fast compiled graphs.

            - :meth:`depth_first_search` -- depth-first search for generic graphs.

        EXAMPLES::

            sage: G = Graph({0: [1], 1: [2], 2: [3], 3: [4], 4: [0]})
            sage: list(G.breadth_first_search(0))
            [0, 1, 4, 2, 3]

        By default, the edge direction of a digraph is respected, but this
        can be overridden by the ``ignore_direction`` parameter::

            sage: D = DiGraph({0: [1, 2, 3], 1: [4, 5], 2: [5], 3: [6], 5: [7], 6: [7], 7: [0]})
            sage: list(D.breadth_first_search(0))
            [0, 1, 2, 3, 4, 5, 6, 7]
            sage: list(D.breadth_first_search(0, ignore_direction=True))
            [0, 1, 2, 3, 7, 4, 5, 6]

        You can specify a maximum distance in which to search. A distance of
        zero returns the ``start`` vertices::

            sage: D = DiGraph({0: [1, 2, 3], 1: [4, 5], 2: [5], 3: [6], 5: [7], 6: [7], 7: [0]})
            sage: list(D.breadth_first_search(0, distance=0))
            [0]
            sage: list(D.breadth_first_search(0, distance=1))
            [0, 1, 2, 3]

        Multiple starting vertices can be specified in a list::

            sage: D = DiGraph({0: [1, 2, 3], 1: [4, 5], 2: [5], 3: [6], 5: [7], 6: [7], 7: [0]})
            sage: list(D.breadth_first_search([0]))
            [0, 1, 2, 3, 4, 5, 6, 7]
            sage: list(D.breadth_first_search([0, 6]))
            [0, 6, 1, 2, 3, 7, 4, 5]
            sage: list(D.breadth_first_search([0, 6], distance=0))
            [0, 6]
            sage: list(D.breadth_first_search([0, 6], distance=1))
            [0, 6, 1, 2, 3, 7]
            sage: list(D.breadth_first_search(6, ignore_direction=True, distance=2))
            [6, 3, 7, 0, 5]

        More generally, you can specify a ``neighbors`` function. For example,
        you can traverse the graph backwards by setting ``neighbors`` to be the
        :meth:`.neighbors_in` function of the graph::

            sage: D = DiGraph({0: [1, 2, 3], 1: [4, 5], 2: [5], 3: [6], 5: [7], 6: [7], 7: [0]})
            sage: list(D.breadth_first_search(5, neighbors=D.neighbors_in, distance=2))
            [5, 1, 2, 0]
            sage: list(D.breadth_first_search(5, neighbors=D.neighbors_out, distance=2))
            [5, 7, 0]
            sage: list(D.breadth_first_search(5 ,neighbors=D.neighbors, distance=2))
            [5, 1, 2, 7, 0, 4, 6]

        It is possible (:trac:`16470`) using the keyword ``report_distance`` to
        get pairs ``(vertex, distance)`` encoding the distance from the starting
        vertices::

            sage: G = graphs.PetersenGraph()
            sage: list(G.breadth_first_search(0, report_distance=True))
            [(0, 0), (1, 1), (4, 1), (5, 1), (2, 2), (6, 2), (3, 2), (9, 2),
            (7, 2), (8, 2)]
            sage: list(G.breadth_first_search(0, report_distance=False))
            [0, 1, 4, 5, 2, 6, 3, 9, 7, 8]

            sage: D = DiGraph({0: [1, 3], 1: [0, 2], 2: [0, 3], 3: [4]})
            sage: D.show()
            sage: list(D.breadth_first_search(4, neighbors=D.neighbor_in_iterator, report_distance=True))
            [(4, 0), (3, 1), (0, 2), (2, 2), (1, 3)]

            sage: C = graphs.CycleGraph(4)
            sage: list(C.breadth_first_search([0, 1], report_distance=True))
            [(0, 0), (1, 0), (3, 1), (2, 1)]

        You can get edges of the BFS tree instead of the vertices using the
        ``edges`` parameter::

            sage: D = DiGraph({1:[2,3],2:[4],3:[4],4:[1],5:[2,6]})
            sage: list(D.breadth_first_search(1, edges=True))
            [(1, 2), (1, 3), (2, 4)]

        TESTS::

            sage: D = DiGraph({1: [0], 2: [0]})
            sage: list(D.breadth_first_search(0))
            [0]
            sage: list(D.breadth_first_search(0, ignore_direction=True))
            [0, 1, 2]
            sage: G = Graph({1:[2,3],2:[4,5],3:[5]})
            sage: list(G.breadth_first_search(1, edges=True))
            [(1, 2), (1, 3), (2, 4), (2, 5)]
            sage: D = DiGraph({1:[2,3],2:[4],3:[4],4:[1,5],5:[2,6]})
            sage: list(D.breadth_first_search(1, edges=True))
            [(1, 2), (1, 3), (2, 4), (4, 5), (5, 6)]
            sage: G = Graph([(0,1)])
            sage: list(G.breadth_first_search(1, report_distance=True, edges=True))
            Traceback (most recent call last):
            ...
            ValueError: parameters edges and report_distance cannot be True simultaneously
        """
        from sage.rings.semirings.non_negative_integer_semiring import NN
        if (distance is not None and distance not in NN):
            raise ValueError("distance must be a non-negative integer, not {0}".format(distance))

        if (report_distance and edges):
            raise ValueError("parameters edges and report_distance cannot be True simultaneously")

        # Preferably use the Cython implementation
        if (neighbors is None and not isinstance(start, list) and distance is None
                and hasattr(self._backend, "breadth_first_search")):
            yield from self._backend.breadth_first_search(
                    start, ignore_direction=ignore_direction,
                    report_distance=report_distance, edges=edges)
        else:
            if neighbors is None:
                if not self._directed or ignore_direction:
                    neighbors = self.neighbor_iterator
                else:
                    neighbors = self.neighbor_out_iterator
            seen = set()
            if isinstance(start, list):
                queue = [(v, 0) for v in start]
            else:
                queue = [(start, 0)]

            # Non-existing start vertex is detected later if distance > 0.
            if not distance:
                for v in queue:
                    if not v[0] in self:
                        raise LookupError("start vertex ({0}) is not a vertex of the graph".format(v[0]))

            for v, d in queue:
                if not edges:
                    if report_distance:
                        yield v, d
                    else:
                        yield v
                seen.add(v)

            while queue:
                v, d = queue.pop(0)
                if distance is None or d < distance:
                    for w in neighbors(v):
                        if w not in seen:
                            seen.add(w)
                            queue.append((w, d + 1))
                            if edges:
                                yield v, w
                            elif report_distance:
                                yield w, d+1
                            else:
                                yield w

    def depth_first_search(self, start, ignore_direction=False,
                           neighbors=None, edges=False):
        """
        Return an iterator over the vertices in a depth-first ordering.

        INPUT:

        - ``start`` -- vertex or list of vertices from which to start the
          traversal

        - ``ignore_direction`` -- boolean (default: ``False``); only applies to
          directed graphs. If ``True``, searches across edges in either
          direction.

        - ``neighbors`` -- function (default: ``None``); a function that inputs
          a vertex and return a list of vertices. For an undirected graph,
          ``neighbors`` is by default the :meth:`.neighbors` function. For a
          digraph, the ``neighbors`` function defaults to the
          :meth:`~DiGraph.neighbor_out_iterator` function of the graph.

        - ``edges`` -- boolean (default: ``False``); whether to return the edges
          of the DFS tree in the order of visit or the vertices (default).
          Edges are directed in root to leaf orientation of the tree.

        .. SEEALSO::

            - :meth:`breadth_first_search`

            - :meth:`breadth_first_search <sage.graphs.base.c_graph.CGraphBackend.breadth_first_search>`
              -- breadth-first search for fast compiled graphs.

            - :meth:`depth_first_search <sage.graphs.base.c_graph.CGraphBackend.depth_first_search>`
              -- depth-first search for fast compiled graphs.

        EXAMPLES::

            sage: G = Graph({0: [1], 1: [2], 2: [3], 3: [4], 4: [0]})
            sage: list(G.depth_first_search(0))
            [0, 4, 3, 2, 1]

        By default, the edge direction of a digraph is respected, but this can
        be overridden by the ``ignore_direction`` parameter::


            sage: D = DiGraph({0: [1, 2, 3], 1: [4, 5], 2: [5], 3: [6], 5: [7], 6: [7], 7: [0]})
            sage: list(D.depth_first_search(0))
            [0, 3, 6, 7, 2, 5, 1, 4]
            sage: list(D.depth_first_search(0, ignore_direction=True))
            [0, 7, 6, 3, 5, 2, 1, 4]

        Multiple starting vertices can be specified in a list::

            sage: D = DiGraph({0: [1, 2, 3], 1: [4, 5], 2: [5], 3: [6], 5: [7], 6: [7], 7: [0]})
            sage: list(D.depth_first_search([0]))
            [0, 3, 6, 7, 2, 5, 1, 4]
            sage: list(D.depth_first_search([0, 6]))
            [0, 3, 6, 7, 2, 5, 1, 4]

        More generally, you can specify a ``neighbors`` function.  For example,
        you can traverse the graph backwards by setting ``neighbors`` to be the
        :meth:`.neighbors_in` function of the graph::

            sage: D = digraphs.Path(10)
            sage: D.add_path([22, 23, 24, 5])
            sage: D.add_path([5, 33, 34, 35])
            sage: list(D.depth_first_search(5, neighbors=D.neighbors_in))
            [5, 4, 3, 2, 1, 0, 24, 23, 22]
            sage: list(D.breadth_first_search(5, neighbors=D.neighbors_in))
            [5, 24, 4, 23, 3, 22, 2, 1, 0]
            sage: list(D.depth_first_search(5, neighbors=D.neighbors_out))
            [5, 6, 7, 8, 9, 33, 34, 35]
            sage: list(D.breadth_first_search(5, neighbors=D.neighbors_out))
            [5, 33, 6, 34, 7, 35, 8, 9]

        You can get edges of the DFS tree instead of the vertices using the
        ``edges`` parameter::

            sage: D = digraphs.Path(5)
            sage: list(D.depth_first_search(2, edges=True))
            [(2, 3), (3, 4)]
            sage: list(D.depth_first_search(2, edges=True, ignore_direction=True))
            [(2, 3), (3, 4), (2, 1), (1, 0)]

        TESTS::

            sage: D = DiGraph({1: [0], 2: [0]})
            sage: list(D.depth_first_search(0))
            [0]
            sage: G = DiGraph([(0, 1), (1, 2), (3, 4), (4, 5)])
            sage: list(G.depth_first_search([0], edges=True))
            [(0, 1), (1, 2)]
            sage: list(G.depth_first_search([0, 3], edges=True))
            [(0, 1), (1, 2), (3, 4), (4, 5)]
            sage: D = DiGraph({1: [2, 3], 3: [4, 6], 4: [6], 5: [4, 7], 6: [7]})
            sage: list(D.depth_first_search(1))
            [1, 3, 6, 7, 4, 2]
            sage: list(D.depth_first_search(1, edges=True))
            [(1, 3), (3, 6), (6, 7), (3, 4), (1, 2)]
            sage: list(D.depth_first_search([1, 3], edges=True))
            [(1, 3), (3, 6), (6, 7), (3, 4), (1, 2)]
            sage: list(D.depth_first_search([], ignore_direction=True, edges=True))
            []
            sage: list(D.depth_first_search(1, ignore_direction=True))
            [1, 3, 6, 4, 5, 7, 2]
            sage: list(D.depth_first_search(1, ignore_direction=True, edges=True))
            [(1, 3), (3, 6), (6, 7), (7, 5), (5, 4), (1, 2)]

        """
        # Preferably use the Cython implementation
        if (neighbors is None and not isinstance(start, list)
                and hasattr(self._backend, "depth_first_search") and not edges):
            yield from self._backend.depth_first_search(start, ignore_direction=ignore_direction)
        else:
            if neighbors is None:
                if not self._directed or ignore_direction:
                    neighbors = self.neighbor_iterator
                else:
                    neighbors = self.neighbor_out_iterator
            seen = set()
            if isinstance(start, list):
                # Reverse the list so that the initial vertices come out in the same order
                queue = [(v, 0) for v in reversed(start)]
            else:
                queue = [(start, 0)]

            if not edges:
                while queue:
                    v, d = queue.pop()
                    if v not in seen:
                        yield v
                        seen.add(v)
                        for w in neighbors(v):
                            if w not in seen:
                                queue.append((w, d + 1))
            else:
                queue = [(None, v, d) for v, d in queue]
                while queue:
                    v, w, d = queue.pop()
                    if w not in seen:
                        if v is not None:
                            yield v, w
                        seen.add(w)
                        for x in neighbors(w):
                            if x not in seen:
                                queue.append((w, x, d + 1))

    # Constructors

    def add_clique(self, vertices, loops=False):
        """
        Add a clique to the graph with the given vertices.

        If the vertices are already present, only the edges are added.

        INPUT:

        - ``vertices`` -- an iterable container of vertices for the clique to be
          added, e.g. a list, set, graph, etc.

        - ``loops`` -- boolean (default: ``False``); whether to add edges from
          every given vertex to itself. This is allowed only if the (di)graph
          allows loops.

        EXAMPLES::

            sage: G = Graph()
            sage: G.add_clique(range(4))
            sage: G.is_isomorphic(graphs.CompleteGraph(4))
            True
            sage: D = DiGraph()
            sage: D.add_clique(range(4))
            sage: D.is_isomorphic(digraphs.Complete(4))
            True
            sage: D = DiGraph(loops=True)
            sage: D.add_clique(range(4), loops=True)
            sage: D.is_isomorphic(digraphs.Complete(4, loops=True))
            True
            sage: D = DiGraph(loops=False)
            sage: D.add_clique(range(4), loops=True)
            Traceback (most recent call last):
            ...
            ValueError: cannot add edge from 0 to 0 in graph without loops

        If the list of vertices contains repeated elements, a loop will be added
        at that vertex, even if ``loops=False``::

            sage: G = Graph(loops=True)
            sage: G.add_clique([1, 1])
            sage: G.edges(sort=True)
            [(1, 1, None)]

        This is equivalent to::

            sage: G = Graph(loops=True)
            sage: G.add_clique([1], loops=True)
            sage: G.edges(sort=True)
            [(1, 1, None)]

        TESTS:

        Using different kinds of iterable container of vertices, :trac:`22906`::

            sage: G = Graph(4)
            sage: G.add_clique(G)
            sage: G.is_clique()
            True
            sage: G = Graph()
            sage: G.add_clique(set(range(4)))
            sage: G.is_clique()
            True
            sage: G = Graph()
            sage: G.add_clique({i: (i, i + 1) for i in range(4)})
            sage: G.is_clique()
            True
            sage: G.vertices(sort=True)
            [0, 1, 2, 3]
            sage: D = DiGraph(4, loops=True)
            sage: D.add_clique(range(4), loops=True)
            sage: D.is_clique(directed_clique=True, loops=True)
            True
        """
        import itertools
        if loops:
            if self.is_directed():
                self.add_edges(itertools.product(vertices, repeat=2))
            else:
                self.add_edges(itertools.combinations_with_replacement(vertices, 2))
        else:
            if self.is_directed():
                self.add_edges(itertools.permutations(vertices, 2))
            else:
                self.add_edges(itertools.combinations(vertices, 2))

    def add_cycle(self, vertices):
        """
        Add a cycle to the graph with the given vertices.

        If the vertices are already present, only the edges are added.

        For digraphs, adds the directed cycle, whose orientation is determined
        by the list. Adds edges ``(vertices[u], vertices[u+1])`` and
        ``(vertices[-1], vertices[0])``.

        INPUT:

        - ``vertices`` -- an ordered list of the vertices of the cycle to be
          added

        EXAMPLES::

            sage: G = Graph()
            sage: G.add_vertices(range(10)); G
            Graph on 10 vertices
            sage: show(G)
            sage: G.add_cycle(list(range(10, 20)))
            sage: show(G)
            sage: G.add_cycle(list(range(10)))
            sage: show(G)

        ::

            sage: D = DiGraph()
            sage: D.add_cycle(list(range(4)))
            sage: D.edges(sort=True)
            [(0, 1, None), (1, 2, None), (2, 3, None), (3, 0, None)]

        TESTS:

        Small cases::

            sage: G = Graph()
            sage: G.add_cycle([])
            sage: G.order(), G.size()
            (0, 0)
            sage: G.add_cycle(['a'])
            sage: G.order(), G.size()
            (1, 0)
            sage: G = Graph()
            sage: G.add_cycle(['a', 'b'])
            sage: G.order(), G.size()
            (2, 1)
            sage: G = Graph()
            sage: G.add_cycle(['a', 'b', 'c'])
            sage: G.order(), G.size()
            (3, 3)
        """
        if vertices:
            self.add_path(vertices)
            if len(vertices) > 1:
                self.add_edge(vertices[-1], vertices[0])

    def add_path(self, vertices):
        """
        Add a path to the graph with the given vertices.

        If the vertices are already present, only the edges are added.

        For digraphs, adds the directed path ``vertices[0], ..., vertices[-1]``.

        INPUT:

        - ``vertices`` -- an ordered list of the vertices of the path to be
          added

        EXAMPLES::

            sage: G = Graph()
            sage: G.add_vertices(range(10)); G
            Graph on 10 vertices
            sage: show(G)
            sage: G.add_path(list(range(10, 20)))
            sage: show(G)
            sage: G.add_path(list(range(10)))
            sage: show(G)

        ::

            sage: D = DiGraph()
            sage: D.add_path(list(range(4)))
            sage: D.edges(sort=True)
            [(0, 1, None), (1, 2, None), (2, 3, None)]
        """
        if not vertices:
            return
        self.add_vertices(vertices)
        self.add_edges(zip(vertices[:-1], vertices[1:]))

    def complement(self):
        """
        Return the complement of the (di)graph.

        The complement of a graph has the same vertices, but exactly those edges
        that are not in the original graph. This is not well defined for graphs
        with multiple edges.

        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: P.plot() # long time
            Graphics object consisting of 26 graphics primitives
            sage: PC = P.complement()
            sage: PC.plot() # long time
            Graphics object consisting of 41 graphics primitives

        ::

            sage: graphs.TetrahedralGraph().complement().size()
            0
            sage: graphs.CycleGraph(4).complement().edges(sort=True)
            [(0, 2, None), (1, 3, None)]
            sage: graphs.CycleGraph(4).complement()
            complement(Cycle graph): Graph on 4 vertices
            sage: G = Graph(multiedges=True, sparse=True)
            sage: G.add_edges([(0, 1)] * 3)
            sage: G.complement()
            Traceback (most recent call last):
            ...
            ValueError: This method is not known to work on graphs with
            multiedges. Perhaps this method can be updated to handle them, but
            in the meantime if you want to use it please disallow multiedges
            using allow_multiple_edges().

        TESTS:

        We check that :trac:`15669` is fixed::

            sage: G = graphs.PathGraph(5).copy(immutable=True)
            sage: G.complement()
            complement(Path graph): Graph on 5 vertices

        The name is not updated when there was none in the first place::

            sage: g = Graph(graphs.PetersenGraph().edges(sort=False)); g
            Graph on 10 vertices
            sage: g.complement()
            Graph on 10 vertices

        """
        self._scream_if_not_simple()

        G = self.copy(data_structure='dense')
        G._backend.c_graph()[0].complement()

        if self.name():
            G.name("complement({})".format(self.name()))

        if self.is_immutable():
            return G.copy(immutable=True)
        return G

    def to_simple(self, to_undirected=True, keep_label='any', immutable=None):
        """
        Return a simple version of the ``self``.

        In particular, loops and multiple edges are removed, and the graph might
        optionally be converted to an undirected graph.

        INPUT:

        - ``to_undirected`` -- boolean (default: ``True``); if ``True``, the
          graph is also converted to an undirected graph

        - ``keep_label`` -- string (default: ``'any'``); if there are multiple
          edges with different labels, this variable defines which label should
          be kept:

          - ``'any'`` -- any label
          - ``'min'`` -- the smallest label
          - ``'max'`` -- the largest label

        .. WARNING::

            ``'min'`` and ``'max'`` only works if the labels can be compared. A
            ``TypeError`` might be raised when working with non-comparable
            objects in Python 3.

        - ``immutable`` -- boolean (default: ``Non``); whether to create a
          mutable/immutable copy. ``immutable=None`` (default) means that the
          graph and its copy will behave the same way.

        EXAMPLES::

            sage: G = DiGraph(loops=True, multiedges=True, sparse=True)
            sage: G.add_edges([(0, 0, None), (1, 1, None), (2, 2, None), (2, 3, 1), (2, 3, 2), (3, 2, None)])
            sage: G.edges(sort=True, labels=False)
            [(0, 0), (1, 1), (2, 2), (2, 3), (2, 3), (3, 2)]
            sage: H = G.to_simple()
            sage: H.edges(sort=True, labels=False)
            [(2, 3)]
            sage: H.is_directed()
            False
            sage: H.allows_loops()
            False
            sage: H.allows_multiple_edges()
            False
            sage: G.to_simple(to_undirected=False, keep_label='min').edges(sort=True)
            [(2, 3, 1), (3, 2, None)]
            sage: G.to_simple(to_undirected=False, keep_label='max').edges(sort=True)
            [(2, 3, 2), (3, 2, None)]
        """
        if to_undirected:
            from sage.graphs.graph import Graph
            g = Graph(self)
        else:
            g = copy(self)
        g.allow_loops(False)
        g.allow_multiple_edges(False, keep_label=keep_label)
        if immutable is None:
            immutable = self.is_immutable()
        if immutable:
            g = g.copy(immutable=True)
        return g

    def disjoint_union(self, other, labels="pairs", immutable=None):
        """
        Return the disjoint union of ``self`` and ``other``.

        INPUT:

        - ``labels`` -- string (default: ``'pairs'``); if set to ``'pairs'``,
          each element ``v`` in the first graph will be named ``(0, v)`` and
          each element ``u`` in ``other`` will be named ``(1, u)`` in the
          result. If set to ``'integers'``, the elements of the result will be
          relabeled with consecutive integers.

        - ``immutable`` -- boolean (default: ``None``); whether to create a
          mutable/immutable disjoint union. ``immutable=None`` (default) means
          that the graphs and their disjoint union will behave the same way.

        .. SEEALSO::

            * :meth:`~sage.graphs.generic_graph.GenericGraph.union`

            * :meth:`~Graph.join`

        EXAMPLES::

            sage: G = graphs.CycleGraph(3)
            sage: H = graphs.CycleGraph(4)
            sage: J = G.disjoint_union(H); J
            Cycle graph disjoint_union Cycle graph: Graph on 7 vertices
            sage: J.vertices(sort=True)
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (1, 3)]
            sage: J = G.disjoint_union(H, labels='integers'); J
            Cycle graph disjoint_union Cycle graph: Graph on 7 vertices
            sage: J.vertices(sort=True)
            [0, 1, 2, 3, 4, 5, 6]
            sage: (G + H).vertices(sort=True)  # '+'-operator is a shortcut
            [0, 1, 2, 3, 4, 5, 6]

        ::

            sage: G = Graph({'a': ['b']})
            sage: G.name("Custom path")
            sage: G.name()
            'Custom path'
            sage: H = graphs.CycleGraph(3)
            sage: J = G.disjoint_union(H); J
            Custom path disjoint_union Cycle graph: Graph on 5 vertices
            sage: J.vertices(sort=True)
            [(0, 'a'), (0, 'b'), (1, 0), (1, 1), (1, 2)]

        """
        if (self._directed and not other._directed) or (not self._directed and other._directed):
            raise TypeError('both arguments must be of the same class')

        if labels not in ['pairs', 'integers']:
            raise ValueError("parameter labels must be either 'pairs' or 'integers'")
        if labels == "integers":
            r_self = {v: i for i, v in enumerate(self)}
            n_self = self.order()
            r_other = {v: i + n_self for i, v in enumerate(other)}
        else:
            r_self = {v: (0, v) for v in self}
            r_other = {v: (1, v) for v in other}
        G = self.relabel(r_self, inplace=False).union(other.relabel(r_other, inplace=False), immutable=immutable)

        a = self.name()
        if not a:
            a = self._repr_()
        b = other.name()
        if not b:
            b = other._repr_()
        G._name = '{} disjoint_union {}'.format(a, b)
        return G

    def union(self, other, immutable=None):
        """
        Return the union of ``self`` and ``other``.

        If the graphs have common vertices, the common vertices will be
        identified.

        If one of the two graphs allows loops (or multiple edges), the resulting
        graph will allow loops (or multiple edges).

        If both graphs are weighted the resulting graphs is weighted.

        If both graphs are immutable, the resulting graph is immutable, unless
        requested otherwise.

        INPUT:

        - ``immutable`` -- boolean (default: ``None``); whether to create a
          mutable/immutable union. ``immutable=None`` (default) means that the
          graphs and their union will behave the same way.

        .. SEEALSO::

            * :meth:`~sage.graphs.generic_graph.GenericGraph.disjoint_union`

            * :meth:`~Graph.join`

        EXAMPLES::

            sage: G = graphs.CycleGraph(3)
            sage: H = graphs.CycleGraph(4)
            sage: J = G.union(H); J
            Graph on 4 vertices
            sage: J.vertices(sort=True)
            [0, 1, 2, 3]
            sage: J.edges(sort=True, labels=False)
            [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)]

        TESTS:

        Multiple edges and loops (:trac:`15627`)::

            sage: g = Graph(multiedges=True, loops=True)
            sage: g.add_edges(graphs.PetersenGraph().edges(sort=True))
            sage: g.add_edges(graphs.PetersenGraph().edges(sort=True))
            sage: g.add_edge(0,0)
            sage: g.add_edge(0,0,"Hey")
            sage: g.add_edge(0,9)
            sage: g.add_edge(0,9)
            sage: g.add_edge(0,9)
            sage: (2*g.size()) == (2*g).size()
            True

        Immutable input ? Immutable output (:trac:`15627`)::

            sage: g = g.copy(immutable=True)
            sage: (2*g)._backend
            <sage.graphs.base.static_sparse_backend.StaticSparseBackend object at ...>

        Check that weighted is appropriately inherited (:trac:`23843`)::

            sage: G1 = Graph(weighted=True)
            sage: G2 = Graph(weighted=False)
            sage: G1.union(G1).weighted()
            True
            sage: G1.union(G2).weighted() or G2.union(G1).weighted()
            False

            sage: D1 = DiGraph(weighted=True)
            sage: D2 = DiGraph(weighted=False)
            sage: D1.union(D1).weighted()
            True
            sage: D1.union(D2).weighted() or D2.union(D1).weighted()
            False
        """
        if (self._directed and not other._directed) or (not self._directed and other._directed):
            raise TypeError('both arguments must be of the same class')

        multiedges = self.allows_multiple_edges() or other.allows_multiple_edges()
        loops      = self.allows_loops()          or other.allows_loops()
        weighted   = self.weighted()              and other.weighted()

        if self._directed:
            from sage.graphs.digraph import DiGraph
            G = DiGraph(multiedges=multiedges, loops=loops, weighted=weighted)
        else:
            from sage.graphs.graph import Graph
            G = Graph(multiedges=multiedges, loops=loops, weighted=weighted)
        G.add_vertices(self)
        G.add_vertices(other)
        G.add_edges(self.edge_iterator())
        G.add_edges(other.edge_iterator())

        if immutable is None:
            immutable = self.is_immutable() and other.is_immutable()
        if immutable:
            G = G.copy(immutable=True)

        return G

    def cartesian_product(self, other):
        r"""
        Return the Cartesian product of ``self`` and ``other``.

        The Cartesian product of `G` and `H` is the graph `L` with vertex set
        `V(L)` equal to the Cartesian product of the vertices `V(G)` and `V(H)`,
        and `((u,v), (w,x))` is an edge iff either - `(u, w)` is an edge of self
        and `v = x`, or - `(v, x)` is an edge of other and `u = w`.

        .. SEEALSO::

            - :meth:`~sage.graphs.graph_decompositions.graph_products.is_cartesian_product`
              -- factorization of graphs according to the Cartesian product

            - :mod:`~sage.graphs.graph_decompositions.graph_products`
              -- a module on graph products

        TESTS:

        Cartesian product of graphs::

            sage: G = Graph([(0, 1), (1, 2)])
            sage: H = Graph([('a', 'b')])
            sage: C1 = G.cartesian_product(H)
            sage: C1.edges(sort=True, labels=None)
            [((0, 'a'), (0, 'b')), ((0, 'a'), (1, 'a')), ((0, 'b'), (1, 'b')),
             ((1, 'a'), (1, 'b')), ((1, 'a'), (2, 'a')), ((1, 'b'), (2, 'b')),
             ((2, 'a'), (2, 'b'))]
            sage: C2 = H.cartesian_product(G)
            sage: C1.is_isomorphic(C2)
            True

        Construction of a Toroidal grid::

            sage: A = graphs.CycleGraph(3)
            sage: B = graphs.CycleGraph(4)
            sage: T = A.cartesian_product(B)
            sage: T.is_isomorphic(graphs.ToroidalGrid2dGraph(3, 4))
            True

        Cartesian product of digraphs::

            sage: P = DiGraph([(0, 1)])
            sage: B = digraphs.DeBruijn(['a', 'b'], 2)
            sage: Q = P.cartesian_product(B)
            sage: Q.edges(sort=True, labels=None)
            [((0, 'aa'), (0, 'aa')), ((0, 'aa'), (0, 'ab')),
             ((0, 'aa'), (1, 'aa')), ((0, 'ab'), (0, 'ba')),
             ((0, 'ab'), (0, 'bb')), ((0, 'ab'), (1, 'ab')),
             ((0, 'ba'), (0, 'aa')), ((0, 'ba'), (0, 'ab')),
             ((0, 'ba'), (1, 'ba')), ((0, 'bb'), (0, 'ba')),
             ((0, 'bb'), (0, 'bb')), ((0, 'bb'), (1, 'bb')),
             ((1, 'aa'), (1, 'aa')), ((1, 'aa'), (1, 'ab')),
             ((1, 'ab'), (1, 'ba')), ((1, 'ab'), (1, 'bb')),
             ((1, 'ba'), (1, 'aa')), ((1, 'ba'), (1, 'ab')),
             ((1, 'bb'), (1, 'ba')), ((1, 'bb'), (1, 'bb'))]
            sage: Q.strongly_connected_components_digraph().num_verts()
            2
            sage: V = Q.strongly_connected_component_containing_vertex((0, 'aa'))
            sage: B.is_isomorphic(Q.subgraph(V))
            True
        """
        self._scream_if_not_simple(allow_loops=True)
        if self._directed and other._directed:
            from sage.graphs.digraph import DiGraph
            G = DiGraph(loops=(self.has_loops() or other.has_loops()))
        elif (not self._directed) and (not other._directed):
            from sage.graphs.graph import Graph
            G = Graph(loops=(self.has_loops() or other.has_loops()))
        else:
            raise TypeError('the graphs should be both directed or both undirected')

        G.add_vertices((u, v) for u in self for v in other)
        for u, w in self.edge_iterator(labels=None):
            for v in other:
                G.add_edge((u, v), (w, v))
        for v, x in other.edge_iterator(labels=None):
            for u in self:
                G.add_edge((u, v), (u, x))
        return G

    def tensor_product(self, other):
        r"""
        Return the tensor product of ``self`` and ``other``.

        The tensor product of `G` and `H` is the graph `L` with vertex set
        `V(L)` equal to the Cartesian product of the vertices `V(G)` and `V(H)`,
        and `((u,v), (w,x))` is an edge iff - `(u, w)` is an edge of self, and -
        `(v, x)` is an edge of other.

        The tensor product is also known as the categorical product and the
        Kronecker product (referring to the Kronecker matrix product). See
        the :wikipedia:`Kronecker_product`.

        EXAMPLES::

            sage: Z = graphs.CompleteGraph(2)
            sage: C = graphs.CycleGraph(5)
            sage: T = C.tensor_product(Z); T
            Graph on 10 vertices
            sage: T.size()
            10
            sage: T.plot() # long time
            Graphics object consisting of 21 graphics primitives

        ::

            sage: D = graphs.DodecahedralGraph()
            sage: P = graphs.PetersenGraph()
            sage: T = D.tensor_product(P); T
            Graph on 200 vertices
            sage: T.size()
            900
            sage: T.plot() # long time
            Graphics object consisting of 1101 graphics primitives

        TESTS:

        Tensor product of graphs::

            sage: G = Graph([(0, 1), (1, 2)])
            sage: H = Graph([('a', 'b')])
            sage: T = G.tensor_product(H)
            sage: T.edges(sort=True, labels=None)
            [((0, 'a'), (1, 'b')), ((0, 'b'), (1, 'a')), ((1, 'a'), (2, 'b')), ((1, 'b'), (2, 'a'))]
            sage: T.is_isomorphic(H.tensor_product(G))
            True

        Tensor product of digraphs::

            sage: I = DiGraph([(0, 1), (1, 2)])
            sage: J = DiGraph([('a', 'b')])
            sage: T = I.tensor_product(J)
            sage: T.edges(sort=True, labels=None)
            [((0, 'a'), (1, 'b')), ((1, 'a'), (2, 'b'))]
            sage: T.is_isomorphic(J.tensor_product(I))
            True

        The tensor product of two DeBruijn digraphs of same diameter is a DeBruijn digraph::

            sage: B1 = digraphs.DeBruijn(2, 3)
            sage: B2 = digraphs.DeBruijn(3, 3)
            sage: T = B1.tensor_product(B2)
            sage: T.is_isomorphic(digraphs.DeBruijn(2 * 3, 3))
            True
        """
        self._scream_if_not_simple(allow_loops=True)
        if self._directed and other._directed:
            from sage.graphs.digraph import DiGraph
            G = DiGraph(loops=(self.has_loops() or other.has_loops()))
        elif (not self._directed) and (not other._directed):
            from sage.graphs.graph import Graph
            G = Graph(loops=(self.has_loops() or other.has_loops()))
        else:
            raise TypeError('the graphs should be both directed or both undirected')
        G.add_vertices((u, v) for u in self for v in other)
        for u, w in self.edge_iterator(labels=None):
            for v, x in other.edge_iterator(labels=None):
                G.add_edge((u, v), (w, x))
                if not G._directed:
                    G.add_edge((u, x), (w, v))
        return G

    categorical_product = tensor_product
    kronecker_product = tensor_product

    def lexicographic_product(self, other):
        r"""
        Return the lexicographic product of ``self`` and ``other``.

        The lexicographic product of `G` and `H` is the graph `L` with vertex
        set `V(L)=V(G)\times V(H)`, and `((u,v), (w,x))` is an edge iff :

        * `(u, w)` is an edge of `G`, or
        * `u = w` and `(v, x)` is an edge of `H`.

        EXAMPLES::

            sage: Z = graphs.CompleteGraph(2)
            sage: C = graphs.CycleGraph(5)
            sage: L = C.lexicographic_product(Z); L
            Graph on 10 vertices
            sage: L.plot() # long time
            Graphics object consisting of 36 graphics primitives

        ::

            sage: D = graphs.DodecahedralGraph()
            sage: P = graphs.PetersenGraph()
            sage: L = D.lexicographic_product(P); L
            Graph on 200 vertices
            sage: L.plot() # long time
            Graphics object consisting of 3501 graphics primitives

        TESTS:

        Lexicographic product of graphs::

            sage: G = Graph([(0, 1), (1, 2)])
            sage: H = Graph([('a', 'b')])
            sage: T = G.lexicographic_product(H)
            sage: T.edges(sort=True, labels=None)
            [((0, 'a'), (0, 'b')), ((0, 'a'), (1, 'a')), ((0, 'a'), (1, 'b')),
             ((0, 'b'), (1, 'a')), ((0, 'b'), (1, 'b')), ((1, 'a'), (1, 'b')),
             ((1, 'a'), (2, 'a')), ((1, 'a'), (2, 'b')), ((1, 'b'), (2, 'a')),
             ((1, 'b'), (2, 'b')), ((2, 'a'), (2, 'b'))]
            sage: T.is_isomorphic(H.lexicographic_product(G))
            False

        Lexicographic product of digraphs::

            sage: I = DiGraph([(0, 1), (1, 2)])
            sage: J = DiGraph([('a', 'b')])
            sage: T = I.lexicographic_product(J)
            sage: T.edges(sort=True, labels=None)
            [((0, 'a'), (0, 'b')), ((0, 'a'), (1, 'a')), ((0, 'a'), (1, 'b')),
             ((0, 'b'), (1, 'a')), ((0, 'b'), (1, 'b')), ((1, 'a'), (1, 'b')),
             ((1, 'a'), (2, 'a')), ((1, 'a'), (2, 'b')), ((1, 'b'), (2, 'a')),
             ((1, 'b'), (2, 'b')), ((2, 'a'), (2, 'b'))]
            sage: T.is_isomorphic(J.lexicographic_product(I))
            False
        """
        self._scream_if_not_simple(allow_loops=True)
        if self._directed and other._directed:
            from sage.graphs.digraph import DiGraph
            G = DiGraph(loops=(self.has_loops() or other.has_loops()))
        elif (not self._directed) and (not other._directed):
            from sage.graphs.graph import Graph
            G = Graph(loops=(self.has_loops() or other.has_loops()))
        else:
            raise TypeError('the graphs should be both directed or both undirected')
        G.add_vertices((u, v) for u in self for v in other)
        for u, w in self.edge_iterator(labels=None):
            for v in other:
                for x in other:
                    G.add_edge((u, v), (w, x))
        for u in self:
            for v, x in other.edge_iterator(labels=None):
                G.add_edge((u, v), (u, x))
        return G

    def strong_product(self, other):
        r"""
        Return the strong product of ``self`` and ``other``.

        The strong product of `G` and `H` is the graph `L` with vertex set
        `V(L)=V(G)\times V(H)`, and `((u,v), (w,x))` is an edge of `L` iff
        either :

        * `(u, w)` is an edge of `G` and `v = x`, or
        * `(v, x)` is an edge of `H` and `u = w`, or
        * `(u, w)` is an edge of `G` and `(v, x)` is an edge of `H`.

        In other words, the edges of the strong product is the union of the
        edges of the tensor and Cartesian products.

        EXAMPLES::

            sage: Z = graphs.CompleteGraph(2)
            sage: C = graphs.CycleGraph(5)
            sage: S = C.strong_product(Z); S
            Graph on 10 vertices
            sage: S.plot() # long time
            Graphics object consisting of 36 graphics primitives

        ::

            sage: D = graphs.DodecahedralGraph()
            sage: P = graphs.PetersenGraph()
            sage: S = D.strong_product(P); S
            Graph on 200 vertices
            sage: S.plot() # long time
            Graphics object consisting of 1701 graphics primitives

        TESTS:

        Strong product of graphs is commutative::

            sage: G = Graph([(0, 1), (1, 2)])
            sage: H = Graph([('a', 'b')])
            sage: T = G.strong_product(H)
            sage: T.is_isomorphic(H.strong_product(G))
            True

        Strong product of digraphs is commutative::

            sage: I = DiGraph([(0, 1), (1, 2)])
            sage: J = DiGraph([('a', 'b')])
            sage: T = I.strong_product(J)
            sage: T.is_isomorphic(J.strong_product(I))
            True

        Counting the edges (see :trac:`13699`)::

            sage: g = graphs.RandomGNP(5, .5)
            sage: gn,gm = g.order(), g.size()
            sage: h = graphs.RandomGNP(5, .5)
            sage: hn,hm = h.order(), h.size()
            sage: product_size = g.strong_product(h).size()
            sage: expected = gm * hn + hm * gn + 2 * gm * hm
            sage: product_size == expected
            True
        """
        self._scream_if_not_simple(allow_loops=True)
        if self._directed and other._directed:
            from sage.graphs.digraph import DiGraph
            G = DiGraph(loops=(self.has_loops() or other.has_loops()))
        elif (not self._directed) and (not other._directed):
            from sage.graphs.graph import Graph
            G = Graph(loops=(self.has_loops() or other.has_loops()))
        else:
            raise TypeError('the graphs should be both directed or both undirected')

        G.add_vertices((u, v) for u in self for v in other)
        for u, w in self.edge_iterator(labels=None):
            for v in other:
                G.add_edge((u, v), (w, v))
            for v, x in other.edge_iterator(labels=None):
                G.add_edge((u, v), (w, x))
                if not self._directed:
                    G.add_edge((w, v), (u, x))
        for v, x in other.edge_iterator(labels=None):
            for u in self:
                G.add_edge((u, v), (u, x))
        return G

    def disjunctive_product(self, other):
        r"""
        Return the disjunctive product of ``self`` and ``other``.

        The disjunctive product of `G` and `H` is the graph `L` with vertex set
        `V(L)=V(G)\times V(H)`, and `((u,v), (w,x))` is an edge iff either :

        * `(u, w)` is an edge of `G`, or
        * `(v, x)` is an edge of `H`.

        EXAMPLES::

            sage: Z = graphs.CompleteGraph(2)
            sage: D = Z.disjunctive_product(Z); D
            Graph on 4 vertices
            sage: D.plot() # long time
            Graphics object consisting of 11 graphics primitives

        ::

            sage: C = graphs.CycleGraph(5)
            sage: D = C.disjunctive_product(Z); D
            Graph on 10 vertices
            sage: D.plot() # long time
            Graphics object consisting of 46 graphics primitives

        TESTS:

        Disjunctive product of graphs::

            sage: G = Graph([(0, 1), (1 ,2)])
            sage: H = Graph([('a', 'b')])
            sage: T = G.disjunctive_product(H)
            sage: T.edges(sort=True, labels=None)
            [((0, 'a'), (0, 'b')), ((0, 'a'), (1, 'a')), ((0, 'a'), (1, 'b')),
             ((0, 'a'), (2, 'b')), ((0, 'b'), (1, 'a')), ((0, 'b'), (1, 'b')),
             ((0, 'b'), (2, 'a')), ((1, 'a'), (1, 'b')), ((1, 'a'), (2, 'a')),
             ((1, 'a'), (2, 'b')), ((1, 'b'), (2, 'a')), ((1, 'b'), (2, 'b')),
             ((2, 'a'), (2, 'b'))]
            sage: T.is_isomorphic(H.disjunctive_product(G))
            True

        Disjunctive product of digraphs::

            sage: I = DiGraph([(0, 1), (1, 2)])
            sage: J = DiGraph([('a', 'b')])
            sage: T = I.disjunctive_product(J)
            sage: T.edges(sort=True, labels=None)
            [((0, 'a'), (0, 'b')), ((0, 'a'), (1, 'a')), ((0, 'a'), (1, 'b')),
             ((0, 'a'), (2, 'b')), ((0, 'b'), (1, 'a')), ((0, 'b'), (1, 'b')),
             ((1, 'a'), (0, 'b')), ((1, 'a'), (1, 'b')), ((1, 'a'), (2, 'a')),
             ((1, 'a'), (2, 'b')), ((1, 'b'), (2, 'a')), ((1, 'b'), (2, 'b')),
             ((2, 'a'), (0, 'b')), ((2, 'a'), (1, 'b')), ((2, 'a'), (2, 'b'))]
            sage: T.is_isomorphic(J.disjunctive_product(I))
            True
        """
        self._scream_if_not_simple(allow_loops=True)
        if self._directed and other._directed:
            from sage.graphs.digraph import DiGraph
            G = DiGraph(loops=(self.has_loops() or other.has_loops()))
        elif (not self._directed) and (not other._directed):
            from sage.graphs.graph import Graph
            G = Graph(loops=(self.has_loops() or other.has_loops()))
        else:
            raise TypeError('the graphs should be both directed or both undirected')

        G.add_vertices((u, v) for u in self for v in other)
        for u, w in self.edge_iterator(labels=None):
            for v in other:
                for x in other:
                    G.add_edge((u, v), (w, x))
        for v, x in other.edge_iterator(labels=None):
            for u in self:
                for w in self:
                    G.add_edge((u, v), (w, x))
        return G

    def transitive_closure(self, loops=True):
        r"""
        Return the transitive closure of the (di)graph.

        The transitive closure of a graph `G` has an edge `(x, y)` if and only
        if there is a path between `x` and `y` in `G`.

        The transitive closure of any (strongly) connected component of a
        (di)graph is a complete graph. The transitive closure of a directed
        acyclic graph is a directed acyclic graph representing the full partial
        order.

        .. NOTE::

            If the (di)graph allows loops, its transitive closure will by
            default have one loop edge per vertex. This can be prevented by
            disallowing loops in the (di)graph (``self.allow_loops(False)``).

        EXAMPLES::

            sage: g = graphs.PathGraph(4)
            sage: g.transitive_closure()
            Transitive closure of Path graph: Graph on 4 vertices
            sage: g.transitive_closure().is_isomorphic(graphs.CompleteGraph(4))
            True
            sage: g = DiGraph({0: [1, 2], 1: [3], 2: [4, 5]})
            sage: g.transitive_closure().edges(sort=True, labels=False)
            [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 3), (2, 4), (2, 5)]

        On an immutable digraph::

            sage: digraphs.Path(5).copy(immutable=True).transitive_closure()
            Transitive closure of Path: Digraph on 5 vertices

        The transitive closure of a (di)graph allowing loops has by default a
        loop edge per vertex. Parameter ``loops`` allows to prevent that::

            sage: G = digraphs.Circuit(3)
            sage: G.transitive_closure().loop_edges(labels=False)
            []
            sage: G.allow_loops(True)
            sage: G.transitive_closure().loop_edges(labels=False)
            [(0, 0), (1, 1), (2, 2)]

        ::

            sage: G = graphs.CycleGraph(3)
            sage: G.transitive_closure().loop_edges(labels=False)
            []
            sage: G.allow_loops(True)
            sage: G.transitive_closure().loop_edges(labels=False)
            [(0, 0), (1, 1), (2, 2)]
        """
        G = copy(self)
        G.name('Transitive closure of ' + self.name())
        G.add_edges(((u, v) for u in G for v in G.breadth_first_search(u)), loops=None)
        return G

    def transitive_reduction(self):
        r"""
        Return a transitive reduction of a graph.

        A transitive reduction `H` of `G` has a path from `x` to `y` if and only
        if there was a path from `x` to `y` in `G`. Deleting any edge of `H`
        destroys this property. A transitive reduction is not unique in
        general. A transitive reduction has the same transitive closure as the
        original graph.

        A transitive reduction of a complete graph is a tree. A transitive
        reduction of a tree is itself.

        EXAMPLES::

            sage: g = graphs.PathGraph(4)
            sage: g.transitive_reduction() == g
            True
            sage: g = graphs.CompleteGraph(5)
            sage: h = g.transitive_reduction(); h.size()
            4
            sage: g = DiGraph({0: [1, 2], 1: [2, 3, 4, 5], 2: [4, 5]})
            sage: g.transitive_reduction().size()
            5
        """
        if self.is_directed():
            if self.is_directed_acyclic():
                from sage.graphs.generic_graph_pyx import transitive_reduction_acyclic
                return transitive_reduction_acyclic(self)

            G = copy(self)
            G.allow_multiple_edges(False)
            n = G.order()
            for e in G.edges(sort=False):
                # Try deleting the edge, see if we still have a path between
                # the vertices.
                G.delete_edge(e)
                if G.distance(e[0], e[1]) > n:
                    # oops, we shouldn't have deleted it
                    G.add_edge(e)
            return G

        else:
            # The transitive reduction of each connected component of an
            # undirected graph is a spanning tree
            from sage.graphs.graph import Graph
            if self.is_connected():
                return Graph(self.min_spanning_tree(weight_function=lambda e: 1))
            else:
                G = Graph(list(self))
                for cc in self.connected_components():
                    if len(cc) > 1:
                        edges = self.subgraph(cc).min_spanning_tree(weight_function=lambda e: 1)
                        G.add_edges(edges)
                return G

    def is_transitively_reduced(self):
        r"""
        Check whether the digraph is transitively reduced.

        A digraph is transitively reduced if it is equal to its transitive
        reduction. A graph is transitively reduced if it is a forest.

        EXAMPLES::

            sage: d = DiGraph({0: [1], 1: [2], 2: [3]})
            sage: d.is_transitively_reduced()
            True

            sage: d = DiGraph({0: [1, 2], 1: [2]})
            sage: d.is_transitively_reduced()
            False

            sage: d = DiGraph({0: [1, 2], 1: [2], 2: []})
            sage: d.is_transitively_reduced()
            False
        """
        if self.is_directed():
            if self.is_directed_acyclic():
                return self == self.transitive_reduction()

            from sage.rings.infinity import Infinity
            G = copy(self)
            for e in self.edge_iterator():
                G.delete_edge(e)
                if G.distance(e[0], e[1]) == Infinity:
                    G.add_edge(e)
                else:
                    return False
            return True

        return self.is_forest()

    # Visualization

    def _color_by_label(self, format='hex', as_function=False, default_color="black"):
        """
        Coloring of the edges according to their label for plotting

        INPUT:

        - ``format`` -- "rgbtuple", "hex", ``True`` (same as "hex"), or a
          function or dictionary assigning colors to labels (default: "hex")

        - ``default_color`` -- a string (default: ``"black"``); the color of the
          labels. Setting ``default_color=None`` is the same as
          ``default_color="black"``.

        - ``as_function`` -- boolean (default: ``False``); whether to return the
          coloring as a function assigning a color to each label, or as a
          dictionary mapping colors to list of edges

        OUTPUT: A coloring of the edges of this graph.

        If ``as_function`` is ``True``, then the coloring is returned as a
        function assigning a color to each label. Otherwise (the default, for
        backward compatibility), the coloring is returned as a dictionary
        assigning to each color the list of the edges of the graph of that
        color.

        This is factored out from plot() for use in 3d plots, etc.

        If ``format`` is a function, then it is used directly as
        coloring. Otherwise, for each label a default color is chosen along a
        rainbow (see :func:`sage.plot.colors.rainbow`). If ``format`` is a
        dictionary, then the colors specified there override the default
        choices.

        EXAMPLES:

        We consider the Cayley graph of the symmetric group, whose edges are
        labelled by the numbers 1,2, and 3::

            sage: G = SymmetricGroup(4).cayley_graph()                                          # optional - sage.groups
            sage: set(G.edge_labels())                                                          # optional - sage.groups
            {1, 2, 3}

        We first request the coloring as a function::

            sage: f = G._color_by_label(as_function=True)                                       # optional - sage.groups
            sage: [f(1), f(2), f(3)]                                                            # optional - sage.groups
            ['#0000ff', '#ff0000', '#00ff00']
            sage: f = G._color_by_label({1: "blue", 2: "red", 3: "green"}, as_function=True)    # optional - sage.groups
            sage: [f(1), f(2), f(3)]                                                            # optional - sage.groups
            ['blue', 'red', 'green']
            sage: f = G._color_by_label({1: "red"}, as_function=True)                           # optional - sage.groups
            sage: [f(1), f(2), f(3)]                                                            # optional - sage.groups
            ['red', 'black', 'black']
            sage: f = G._color_by_label({1: "red"}, as_function=True, default_color='blue')     # optional - sage.groups
            sage: [f(1), f(2), f(3)]                                                            # optional - sage.groups
            ['red', 'blue', 'blue']

        The default output is a dictionary assigning edges to colors::

            sage: G._color_by_label()                                                           # optional - sage.groups
            {'#0000ff': [((), (1,2), 1), ...],
             '#00ff00': [((), (3,4), 3), ...],
             '#ff0000': [((), (2,3), 2), ...]}

            sage: G._color_by_label({1: "blue", 2: "red", 3: "green"})                          # optional - sage.groups
            {'blue': [((), (1,2), 1), ...],
             'green': [((), (3,4), 3), ...],
             'red': [((), (2,3), 2), ...]}

        TESTS:

        We check what happens when several labels have the same color::

            sage: result = G._color_by_label({1: "blue", 2: "blue", 3: "green"})                # optional - sage.groups
            sage: sorted(result)                                                                # optional - sage.groups
            ['blue', 'green']
            sage: len(result['blue'])                                                           # optional - sage.groups
            48
            sage: len(result['green'])                                                          # optional - sage.groups
            24
        """
        if format is True:
            format = "hex"
        if isinstance(format, str):
            # Find all labels; this is slower and huglier than:
            #    labels = set(edge[2] for edge in self.edge_iterator())
            # but works with non hashable edge labels, and keeps backward
            # compatibility for the label ordering.
            labels = []
            for edge in self.edge_iterator():
                label = edge[2]
                if label not in labels:
                    labels.append(label)

            from sage.plot.colors import rainbow
            colors = rainbow(len(labels), format=format)
            color_of_label = dict(zip(labels, colors))
            color_of_label = color_of_label.__getitem__
        elif isinstance(format, dict):
            def color_of_label(label):
                return format.get(label, default_color)
        else:
            # This assumes that ``format`` is already a function
            color_of_label = format

        if as_function:
            return color_of_label

        edges_by_color = {}
        for edge in self.edge_iterator():
            color = color_of_label(edge[2])
            if color in edges_by_color:
                edges_by_color[color].append(edge)
            else:
                edges_by_color[color] = [edge]
        return edges_by_color

    def latex_options(self):
        r"""
        Return an instance of :class:`~sage.graphs.graph_latex.GraphLatex` for
        the graph.

        Changes to this object will affect the LaTeX version of the graph.  For
        a full explanation of how to use LaTeX to render graphs, see the
        introduction to the :mod:`~sage.graphs.graph_latex` module.

        EXAMPLES::

            sage: g = graphs.PetersenGraph()
            sage: opts = g.latex_options()
            sage: opts
            LaTeX options for Petersen graph: {}
            sage: opts.set_option('tkz_style', 'Classic')
            sage: opts
            LaTeX options for Petersen graph: {'tkz_style': 'Classic'}
        """
        if self._latex_opts is None:
            from sage.graphs.graph_latex import GraphLatex
            self._latex_opts = GraphLatex(self)
        return self._latex_opts

    def set_latex_options(self, **kwds):
        r"""
        Set multiple options for rendering a graph with LaTeX.

        INPUT:

        - ``kwds`` -- any number of option/value pairs to set many graph latex
          options at once (a variable number, in any order). Existing values are
          overwritten, new values are added.  Existing values can be cleared by
          setting the value to ``None``.  Possible options are documented at
          :meth:`sage.graphs.graph_latex.GraphLatex.set_option`.

        This method is a convenience for setting the options of a graph directly
        on an instance of the graph.  For a full explanation of how to use LaTeX
        to render graphs, see the introduction to the
        :mod:`~sage.graphs.graph_latex` module.

        EXAMPLES::

            sage: g = graphs.PetersenGraph()
            sage: g.set_latex_options(tkz_style='Welsh')
            sage: opts = g.latex_options()
            sage: opts.get_option('tkz_style')
            'Welsh'
        """
        opts = self.latex_options()
        opts.set_options(**kwds)

    def layout(self, layout=None, pos=None, dim=2, save_pos=False, **options):
        """
        Return a layout for the vertices of this graph.

        INPUT:

        - ``layout`` -- string (default: ``None``); specifies a layout algorithm
          among ``"acyclic"``, ``"acyclic_dummy"``, ``"circular"``,
          ``"ranked"``, ``"graphviz"``, ``"planar"``, ``"spring"``,
          ``"forest"`` or ``"tree"``

        - ``pos`` -- dictionary (default: ``None``); a dictionary of positions

        - ``dim`` -- integer (default: ``2``); the number of dimensions of the
          layout, 2 or 3

        - ``save_pos`` -- boolean (default: ``False``); whether to save the
          positions

        - ``**options`` -- layout options (see below)

        If ``layout`` is set, the specified algorithm is used to compute the
        positions.

        Otherwise, if ``pos`` is specified, use the given positions.

        Otherwise, try to fetch previously computed and saved positions.

        Otherwise use the default layout (usually the spring layout).

        If ``save_pos = True``, the layout is saved for later use.

        EXAMPLES::

            sage: g = digraphs.ButterflyGraph(1)
            sage: D2 = g.layout(); D2  # random
            {('0', 0): [2.69..., 0.43...],
             ('0', 1): [1.35..., 0.86...],
             ('1', 0): [0.89..., -0.42...],
             ('1', 1): [2.26..., -0.87...]}

            sage: g.layout(layout="acyclic_dummy", save_pos=True)
            {('0', 0): [0.3..., 0],
             ('0', 1): [0.3..., 1],
             ('1', 0): [0.6..., 0],
             ('1', 1): [0.6..., 1]}
            sage: g.get_pos()
            {('0', 0): [0.3..., 0],
             ('0', 1): [0.3..., 1],
             ('1', 0): [0.6..., 0],
             ('1', 1): [0.6..., 1]}

            sage: D3 = g.layout(dim=3); D3  # random
            {('0', 0): [0.68..., 0.50..., -0.24...],
             ('0', 1): [1.02..., -0.02..., 0.93...],
             ('1', 0): [2.06..., -0.49..., 0.23...],
             ('1', 1): [1.74..., 0.01..., -0.92...]}

        Some safety tests::

            sage: sorted(D2.keys()) == sorted(D3.keys()) == sorted(g)
            True
            sage: isinstance(D2, dict) and isinstance(D3, dict)
            True
            sage: [c in RDF for c in D2[('0', 0)]]
            [True, True]
            sage: [c in RDF for c in D3[('0', 0)]]
            [True, True, True]

        Here is the list of all the available layout options (``**options``)::

            sage: from sage.graphs.graph_plot import layout_options
            sage: for key, value in sorted(layout_options.items()):
            ....:     print("option {} : {}".format(key, value))
            option by_component : Whether to do the spring layout by connected component -- a boolean.
            option dim : The dimension of the layout -- 2 or 3.
            option forest_roots : An iterable specifying which vertices to use as roots for the ``layout='forest'`` option. If no root is specified for a tree, then one is chosen close to the center of the tree. Ignored unless ``layout='forest'``.
            option heights : A dictionary mapping heights to the list of vertices at this height.
            option iterations : The number of times to execute the spring layout algorithm.
            option layout : A layout algorithm -- one of : "acyclic", "circular" (plots the graph with vertices evenly distributed on a circle), "ranked", "graphviz", "planar", "spring" (traditional spring layout, using the graph's current positions as initial positions), or "tree" (the tree will be plotted in levels, depending on minimum distance for the root).
            option prog : Which graphviz layout program to use -- one of "circo", "dot", "fdp", "neato", or "twopi".
            option save_pos : Whether or not to save the computed position for the graph.
            option spring : Use spring layout to finalize the current layout.
            option tree_orientation : The direction of tree branches -- 'up', 'down', 'left' or 'right'.
            option tree_root : A vertex designation for drawing trees. A vertex of the tree to be used as the root for the ``layout='tree'`` option. If no root is specified, then one is chosen close to the center of the tree. Ignored unless ``layout='tree'``.

        Some of them only apply to certain layout algorithms. For details, see
        :meth:`.layout_acyclic`, :meth:`.layout_planar`,
        :meth:`.layout_circular`, :meth:`.layout_spring`, ...

        .. WARNING:: unknown optional arguments are silently ignored

        .. WARNING::

            ``graphviz`` and ``dot2tex`` are currently required to obtain a nice
            ``'acyclic'`` layout. See :meth:`.layout_graphviz` for installation
            instructions.

        A subclass may implement another layout algorithm ``"blah"``, by
        implementing a method ``.layout_blah``. It may override the default
        layout by overriding :meth:`.layout_default`, and similarly override the
        predefined layouts.

        .. TODO::

            use this feature for all the predefined graphs classes (like for the
            Petersen graph, ...), rather than systematically building the layout
            at construction time.

        TESTS::

            sage: for style in ('spring', 'planar', 'circular', 'forest'):
            ....:     for G in [Graph([(1, 2)]), Graph([(1, 2), (2, 3), (3, 4)])]:
            ....:         pos = G.layout(style, save_pos=True)
            ....:         assert G._pos is not None
        """
        if layout is None:
            if pos is None:
                pos = self.get_pos(dim=dim)
            if pos is None:
                layout = 'default'

        if hasattr(self, "layout_%s" % layout):
            pos = getattr(self, "layout_%s" % layout)(dim=dim, **options)
        elif layout is not None:
            raise ValueError("unknown layout algorithm: %s" % layout)

        if len(pos) < self.order():
            pos = self.layout_extend_randomly(pos, dim=dim)

        if save_pos:
            self.set_pos(pos, dim=dim)
        return pos

    def layout_spring(self, by_component=True, **options):
        """
        Return a spring layout for this graph.

        INPUT:

         - ``by_components`` -- boolean (default: ``True``);

         - ``**options`` -- options for method
           :meth:`~sage.graphs.generic_graph_pyx.spring_layout_fast`

        OUTPUT: a dictionary mapping vertices to positions

        EXAMPLES::

            sage: g = graphs.LadderGraph(3) #TODO!!!!
            sage: g.layout_spring()  # random
            {0: [1.0, -0.29...],
            1: [1.64..., 0.30...],
            2: [2.34..., 0.89...],
            3: [1.49..., -0.83...],
            4: [2.14..., -0.30...],
            5: [2.80..., 0.22...]}
            sage: g = graphs.LadderGraph(7)
            sage: g.plot(layout="spring")
            Graphics object consisting of 34 graphics primitives
        """
        return spring_layout_fast(self, by_component=by_component, **options)

    layout_default = layout_spring

    def layout_ranked(self, heights=None, dim=2, spring=False, **options):
        """
        Return a ranked layout for this graph

        INPUT:

        - ``heights`` -- dictionary (default: ``None``); a dictionary mapping
          heights to the list of vertices at this height

        - ``dim`` -- integer (default: ``2``); the number of dimensions of the
          layout, 2 or 3

        - ``spring`` -- boolean (default: ``False``);

        - ``**options`` -- options for method
          :meth:`~sage.graphs.generic_graph_pyx.spring_layout_fast`

        OUTPUT: a dictionary mapping vertices to positions

        Returns a layout computed by randomly arranging the vertices
        along the given heights

        EXAMPLES::

            sage: g = graphs.LadderGraph(3)
            sage: g.layout_ranked(heights={i: (i, i+3) for i in range(3)})  # random
            {0: [0.668..., 0],
             1: [0.667..., 1],
             2: [0.677..., 2],
             3: [1.34..., 0],
             4: [1.33..., 1],
             5: [1.33..., 2]}
            sage: g = graphs.LadderGraph(7)
            sage: g.plot(layout="ranked", heights={i: (i, i+7) for i in range(7)})
            Graphics object consisting of 34 graphics primitives
        """
        assert heights is not None

        from sage.misc.randstate import current_randstate
        random = current_randstate().python_random().random

        if not self.order():
            return {}

        pos = {}
        mmax = max(len(ccc) for ccc in heights.values())
        ymin = min(heights.keys())
        ymax = max(heights.keys())
        dist = (max(ymax - ymin, 1)) / (mmax + 1.0)
        for height in heights:
            num_xs = len(heights[height])
            if not num_xs:
                continue
            j = (mmax - num_xs) / 2.0
            for k in range(num_xs):
                pos[heights[height][k]] = [dist * (j + k + 1) + random() * (dist * 0.03) for i in range(dim - 1)] + [height]
        if spring:
            # This does not work that well in 2d, since the vertices on the same
            # level are unlikely to cross. It is also hard to set a good
            # equilibrium distance (parameter k in run_spring).
            # - If k < 1, the layout gets squished horizontally.
            # - If k > 1, then two adjacent vertices in consecutive levels tend
            #   to be further away than desired.
            newpos = spring_layout_fast(self,
                                        vpos=pos,
                                        dim=dim,
                                        height=True,
                                        **options)
            # spring_layout_fast actually *does* touch the last coordinates
            # (conversion to floats + translation)
            # We restore back the original height.
            for x in self:
                newpos[x][dim - 1] = pos[x][dim - 1]
            pos = newpos
        return pos

    def layout_extend_randomly(self, pos, dim=2):
        """
        Extend randomly a partial layout

        INPUT:

        - ``pos`` -- a dictionary mapping vertices to positions

        - ``dim`` -- integer (default: ``2``); the number of dimensions of the
          layout, 2 or 3

        OUTPUT: a dictionary mapping vertices to positions

        The vertices not referenced in ``pos`` are assigned random positions
        within the box delimited by the other vertices.

        EXAMPLES::

            sage: H = digraphs.ButterflyGraph(1)
            sage: pos = {('0', 0): (0, 0), ('1', 1): (1, 1)}
            sage: H.layout_extend_randomly(pos)  # random
            {('0', 0): (0, 0),
             ('0', 1): [0.0446..., 0.332...],
             ('1', 0): [0.1114..., 0.514...],
             ('1', 1): (1, 1)}
            sage: xmin, xmax, ymin, ymax = H._layout_bounding_box(pos)
            sage: (xmin, ymin) == (0, 0) and (xmax, ymax) == (1, 1)
            True
        """
        assert dim == 2  # 3d not yet implemented
        from sage.misc.randstate import current_randstate
        random = current_randstate().python_random().random

        xmin, xmax, ymin, ymax = self._layout_bounding_box(pos)

        dx = xmax - xmin
        dy = ymax - ymin
        # Check each vertex position is in pos, add position randomly within the
        # plot range if none is defined
        for v in self:
            if v not in pos:
                pos[v] = [xmin + dx * random(), ymin + dy * random()]
        return pos

    def layout_circular(self, dim=2, center=(0, 0), radius=1, shift=0, angle=0, **options):
        r"""
        Return a circular layout for this graph

        INPUT:

        - ``dim`` -- integer (default: ``2``); the number of dimensions of the
          layout, 2 or 3

        - ``center`` -- tuple (default: ``(0, 0)``); position of the center of
          the circle

        - ``radius`` -- (default: 1); the radius of the circle

        - ``shift`` -- (default: 0); rotation of the circle. A value of
          ``shift=1`` will replace in the drawing the `i`-th element of the list
          by the `(i-1)`-th. Non-integer values are admissible, and a value of
          `\alpha` corresponds to a rotation of the circle by an angle of
          `\alpha 2\pi/n` (where `n` is the number of vertices set on the
          circle).

        - ``angle`` -- (default: 0); rotate the embedding of all vertices. For
          instance, when ``angle == 0``, the first vertex get position
          ``(center[0] + radius, center[1])``. With a value of `\pi/2`, the
          first vertex get position ``(center[0], center[1] + radius)``.

        - ``**options`` -- other parameters not used here

        OUTPUT: a dictionary mapping vertices to positions

        EXAMPLES::

            sage: G = graphs.CirculantGraph(7, [1, 3])
            sage: G.layout_circular()
            {0: (0.0, 1.0),
             1: (-0.78...,  0.62...),
             2: (-0.97..., -0.22...),
             3: (-0.43..., -0.90...),
             4: (0.43...,  -0.90...),
             5: (0.97...,  -0.22...),
             6: (0.78...,   0.62...)}
            sage: G.plot(layout="circular")
            Graphics object consisting of 22 graphics primitives
        """
        assert dim == 2, "3D circular layout not implemented"
        from math import pi
        return self._circle_embedding(self.vertices(sort=True), center=(0, 0),
                                      radius=1, shift=0, angle=pi/2,
                                      return_dict=True)

    def layout_forest(self, tree_orientation="down", forest_roots=None,
                      **options):
        """
        Return an ordered forest layout for this graph.

        The function relies on :meth:`~GenericGraph.layout_tree` to deal with
        each connected component.

        INPUT:

        - ``forest_roots`` -- an iterable of vertices (default: ``None``);
          the root vertices of the trees in the forest; a vertex is chosen
          close to the center of each component for which no root is specified
          in ``forest_roots`` or if ``forest_roots`` is ``None``

        - ``tree_orientation`` -- string (default: ``'down'``); the direction in
          which the tree is growing, can be ``'up'``, ``'down'``, ``'left'`` or
          ``'right'``

        - ``**options`` -- other parameters ignored here

        EXAMPLES::

            sage: G = graphs.RandomTree(4) + graphs.RandomTree(5) + graphs.RandomTree(6)
            sage: p = G.layout_forest()
            sage: G.plot(pos=p) # random
            Graphics object consisting of 28 graphics primitives

            sage: H = graphs.PathGraph(5) + graphs.PathGraph(5) + graphs.BalancedTree(2,2)
            sage: p = H.layout_forest(forest_roots=[14,3])
            sage: H.plot(pos=p)
            Graphics object consisting of 32 graphics primitives

        TESTS::

            sage: G = Graph(0)
            sage: G.plot(layout='forest')
            Graphics object consisting of 0 graphics primitives

        Works for forests that are trees::

            sage: g = graphs.StarGraph(4)
            sage: p = g.layout_forest(forest_roots=[1])
            sage: sorted(p.items())
            [(0, [2.0, -1]), (1, [2.0, 0]), (2, [3.0, -2]), (3, [2.0, -2]), (4, [1.0, -2])]

        The parameter ``forest_roots`` should be an iterable (or ``None``)::

            sage: H = graphs.PathGraph(5)
            sage: p = H.layout_forest(forest_roots=3)
            Traceback (most recent call last):
            ...
            TypeError: forest_roots should be an iterable of vertices
        """
        if not self:
            return dict()
        else:
            # Compute the layout component by component
            return layout_split(self.__class__.layout_tree,
                                self,
                                tree_orientation=tree_orientation,
                                forest_roots=forest_roots,
                                **options)

    def layout_tree(self, tree_orientation="down", tree_root=None,
                    dim=2, **options):
        r"""
        Return an ordered tree layout for this graph.

        The graph must be a tree (no non-oriented cycles). In case of doubt
        whether the graph is connected or not, prefer
        :meth:`~GenericGraph.layout_forest`.

        INPUT:

        - ``tree_root`` -- a vertex (default: ``None``); the root vertex of the
          tree. By default (``None``) a vertex is chosen close to the center of
          the tree.

        - ``tree_orientation`` -- string (default: ``'down'``); the direction in
          which the tree is growing, can be ``'up'``, ``'down'``, ``'left'`` or
          ``'right'``

        - ``dim`` -- integer (default: ``2``); the number of dimensions of the
          layout, 2 or 3

        - ``**options`` -- other parameters not used here

        If the tree has been given a planar embedding (fixed circular order on
        the set of neighbors of every vertex) using ``set_embedding``, the
        algorithm will create a layout that respects this embedding.

        OUTPUT: a dictionary mapping vertices to positions

        EXAMPLES::

            sage: G = graphs.RandomTree(80)
            sage: G.plot(layout="tree", tree_orientation="right")
            Graphics object consisting of 160 graphics primitives

            sage: T = graphs.RandomLobster(25, 0.3, 0.3)
            sage: T.show(layout='tree', tree_orientation='up')

            sage: G = graphs.HoffmanSingletonGraph()
            sage: T = Graph()
            sage: T.add_edges(G.min_spanning_tree(starting_vertex=0))
            sage: T.show(layout='tree', tree_root=0)

            sage: G = graphs.BalancedTree(2, 2)
            sage: G.layout_tree(tree_root=0)
            {0: [1.5, 0],
             1: [2.5, -1],
             2: [0.5, -1],
             3: [3.0, -2],
             4: [2.0, -2],
             5: [1.0, -2],
             6: [0.0, -2]}

            sage: G = graphs.BalancedTree(2, 4)
            sage: G.plot(layout="tree", tree_root=0, tree_orientation="up")
            Graphics object consisting of 62 graphics primitives

        Using the embedding when it exists::

            sage: T = Graph([(0, 1), (0, 6), (0, 3), (1, 2), (1, 5), (3, 4), (3, 7), (3, 8)])
            sage: T.set_embedding({0: [1, 6, 3], 1: [2, 5, 0], 2: [1], 3: [4, 7, 8, 0],
            ....:     4: [3], 5: [1], 6: [0], 7: [3], 8: [3]})
            sage: T.layout_tree()
            {0: [2.166..., 0],
             1: [3.5, -1],
             2: [4.0, -2],
             3: [1.0, -1],
             4: [2.0, -2],
             5: [3.0, -2],
             6: [2.0, -1],
             7: [1.0, -2],
             8: [0.0, -2]}
            sage: T.plot(layout="tree", tree_root=3)
            Graphics object consisting of 18 graphics primitives

        TESTS::

            sage: G = graphs.BalancedTree(2, 2)
            sage: G.layout_tree(tree_root=0, tree_orientation='left')
            {0: [0, 1.5],
             1: [-1, 2.5],
             2: [-1, 0.5],
             3: [-2, 3.0],
             4: [-2, 2.0],
             5: [-2, 1.0],
             6: [-2, 0.0]}

            sage: G = graphs.CycleGraph(3)
            sage: G.plot(layout='tree')
            Traceback (most recent call last):
            ...
            RuntimeError: cannot use tree layout on this graph: self.is_tree() returns False
            sage: G = Graph(0)
            sage: G.plot(layout='tree')
            Graphics object consisting of 0 graphics primitives
        """
        if dim != 2:
            raise ValueError('only implemented in 2D')

        if not self:
            return dict()

        from sage.graphs.graph import Graph
        if not Graph(self).is_tree():
            raise RuntimeError("cannot use tree layout on this graph: "
                               "self.is_tree() returns False")

        emb = self.get_embedding()

        if tree_root is None:
            root = self.center()[0]
        else:
            root = tree_root

        pos = {}

        # The children and parent of each vertex
        if emb is None:
            children = {root: self.neighbors(root)}
        else:
            children = {root: emb[root]}
        parent = {u: root for u in children[root]}

        # stack[i] is the list of children of stick[i] which have not been given
        # a position yet.
        stack = [list(children[root])]
        stick = [root]

        # obstruction[y] is the smallest value of x to which a vertex at height
        # y can be assigned. All vertices at height y which have already been
        # assigned are on the left of (x-1,y).
        obstruction = [0.0] * self.num_verts()

        if tree_orientation in ['down', 'left']:
            o = -1
        elif tree_orientation in ['up', 'right']:
            o = 1
        else:
            raise ValueError('orientation should be "up", "down", "left" or "right"')

        def slide(v, dx):
            """
            shift the vertex ``v`` and its descendants to the right by ``dx``

            Precondition: ``v`` and its descendants have already had their
            positions computed.
            """
            level = [v]
            while level:
                nextlevel = []
                for u in level:
                    x, y = pos[u]
                    x += dx
                    obstruction[y] = max(x + 1, obstruction[y])
                    pos[u] = [x, y]
                    nextlevel += children[u]

                level = nextlevel

        while stack:
            C = stack[-1]

            # If all the children of stack[-1] have been given a position
            if not C:
                p = stick.pop()
                stack.pop()
                cp = children[p]
                y = o * len(stack)

                if not cp:
                    # If p has no children, we draw it at the leftmost position
                    # which has not been forbidden
                    x = obstruction[y]
                    pos[p] = [x, y]
                else:
                    # If p has children, we put v on a vertical line going
                    # through the barycenter of its children
                    x = sum(pos[c][0] for c in cp) / len(cp)
                    pos[p] = [x, y]
                    ox = obstruction[y]
                    if x < ox:
                        slide(p, ox - x)
                        x = ox

                # If the vertex to the right of p has not children, we want it
                # at distance 1 from p
                obstruction[y] = x + 1

            # Otherwise, we take one of the children and add it to the
            # stack. Note that this vertex is removed from the list C.
            else:
                t = C.pop()

                pt = parent[t]

                if emb is None:
                    ct = [u for u in self.neighbor_iterator(t) if u != pt]
                else:
                    ct = emb[t]
                    idx = ct.index(pt)
                    ct = ct[idx + 1:] + ct[:idx]

                children[t] = ct
                for c in ct:
                    parent[c] = t

                stack.append(list(ct))
                stick.append(t)

        if tree_orientation in ['right', 'left']:
            return {p: [py, px] for p, [px, py] in pos.items()}

        return pos

    def layout_graphviz(self, dim=2, prog='dot', **options):
        """
        Call ``graphviz`` to compute a layout of the vertices of this graph.

        INPUT:

        - ``dim`` -- integer (default: ``2``); the number of dimensions of the
          layout, 2 or 3

        - ``prog`` -- one of "dot", "neato", "twopi", "circo", or "fdp"

        - ``**options`` -- other parameters used by method
          :meth:`~GenericGraph.graphviz_string`

        EXAMPLES::

            sage: g = digraphs.ButterflyGraph(2)
            sage: g.layout_graphviz()  # optional - dot2tex graphviz
            {('...', ...): [...,...],
             ('...', ...): [...,...],
             ('...', ...): [...,...],
             ('...', ...): [...,...],
             ('...', ...): [...,...],
             ('...', ...): [...,...],
             ('...', ...): [...,...],
             ('...', ...): [...,...],
             ('...', ...): [...,...],
             ('...', ...): [...,...],
             ('...', ...): [...,...],
             ('...', ...): [...,...]}
            sage: g.plot(layout="graphviz")  # optional - dot2tex graphviz
            Graphics object consisting of 29 graphics primitives

        Note: the actual coordinates are not deterministic

        By default, an acyclic layout is computed using ``graphviz``'s ``dot``
        layout program. One may specify an alternative layout program::

            sage: g.plot(layout = "graphviz", prog = "dot")   # optional - dot2tex graphviz
            Graphics object consisting of 29 graphics primitives
            sage: g.plot(layout = "graphviz", prog = "neato") # optional - dot2tex graphviz
            Graphics object consisting of 29 graphics primitives
            sage: g.plot(layout = "graphviz", prog = "twopi") # optional - dot2tex graphviz
            Graphics object consisting of 29 graphics primitives
            sage: g.plot(layout = "graphviz", prog = "fdp")   # optional - dot2tex graphviz
            Graphics object consisting of 29 graphics primitives
            sage: g = graphs.BalancedTree(5,2)
            sage: g.plot(layout = "graphviz", prog = "circo")  # optional - dot2tex graphviz
            Graphics object consisting of 62 graphics primitives

        .. TODO::

            Put here some cool examples showcasing graphviz features.

        This requires ``graphviz`` and the ``dot2tex`` spkg. Here are some
        installation tips:

        - Install ``graphviz`` >= 2.14 so that the programs ``dot``, ``neato``,
          etc.  are in your path. The graphviz suite can be download from
          http://graphviz.org.

        - Install ``dot2tex`` with ``sage -i dot2tex``

        .. TODO::

            Use the graphviz functionality of Networkx 1.0 once it
            will be merged into Sage.

        TESTS:

        Make sure that :trac:`12364` is fixed::

            sage: m = WordMorphism('a->abb,b->ba')
            sage: w = m.fixed_point('a')
            sage: prefix = Word(list(w[:100]))
            sage: pals = prefix.palindromes()
            sage: poset = Poset((pals, lambda x,y: x.is_factor(y)))
            sage: H = poset.hasse_diagram()
            sage: d = H.layout_graphviz()     # optional - dot2tex graphviz
        """
        assert_have_dot2tex()
        assert dim == 2, "3D graphviz layout not implemented"

        key = self._keys_for_vertices()
        key_to_vertex = {key(v): v for v in self}

        import dot2tex
        positions = dot2tex.dot2tex(self.graphviz_string(**options), format="positions", prog=prog)

        return {key_to_vertex[key]: pos for key, pos in positions.items()}

    def _layout_bounding_box(self, pos):
        """
        Return a bounding box around the specified positions.

        INPUT:

        - ``pos`` -- a dictionary of positions

        EXAMPLES::

            sage: Graph()._layout_bounding_box({})
            [-1, 1, -1, 1]
            sage: Graph()._layout_bounding_box({0: (3, 5), 1: (2, 7), 2: (-4, 2)})
            [-4, 3, 2, 7]
            sage: Graph()._layout_bounding_box({0: (3, 5), 1: (3.00000000001, 4.999999999999999)})
            [2, 4.00000000001000, 4.00000000000000, 6]
        """
        xs = [pos[v][0] for v in pos]
        ys = [pos[v][1] for v in pos]
        if not xs:
            xmin = -1
            xmax = 1
            ymin = -1
            ymax = 1
        else:
            xmin = min(xs)
            xmax = max(xs)
            ymin = min(ys)
            ymax = max(ys)

        if xmax - xmin < 0.00000001:
            xmax += 1
            xmin -= 1

        if ymax - ymin < 0.00000001:
            ymax += 1
            ymin -= 1

        return [xmin, xmax, ymin, ymax]

    def _circle_embedding(self, vertices, center=(0, 0), radius=1, shift=0, angle=0, return_dict=False):
        r"""
        Set some vertices on a circle in the embedding of a this graph.

        By default, this method modifies the graph's embedding so that the
        vertices listed in ``vertices`` appear in this ordering on a circle of
        given radius and center.

        INPUT:

        - ``vertices`` -- an iterable container of vertices (list, set, dict,
          etc.). The order of the vertices in the circle embedding is given by
          ``list(vertices)``.

        - ``center`` -- tuple (default: `(0, 0)`); position of the center of the
          circle.

        - ``radius`` -- (default: 1); the radius of the circle.

        - ``shift`` -- (default: 0); rotation of the circle. A value of
          ``shift=1`` will replace in the drawing the `i`-th element of the list
          by the `(i-1)`-th. Non-integer values are admissible, and a value of
          `\alpha` corresponds to a rotation of the circle by an angle of
          `\alpha 2\pi/n` (where `n` is the number of vertices set on the
          circle).

        - ``angle`` -- (default: 0); rotate the embedding of all vertices. For
          instance, when ``angle == 0``, the first vertex get position
          ``(center[0] + radius, center[1])``. With a value of `\pi/2`, the
          first vertex get position ``(center[0], center[1] + radius)``.

        - ``return_dict`` -- boolean (default: ``False``); by default the
          computed positions of the specified vertices are stored in the
          position dictionary of the graph. When ``return_dict == True``, a
          dictionary containing only the position of the specified vertices is
          returned.

        EXAMPLES::

            sage: g = graphs.CycleGraph(5)
            sage: g._circle_embedding([0, 2, 4, 1, 3], radius=2, shift=.5)
            sage: g.show()

            sage: g._circle_embedding(g.vertices(sort=True), angle=0)
            sage: g._pos[0]
            (1.0, 0.0)
            sage: from math import pi
            sage: g._circle_embedding(g.vertices(sort=True), angle=pi/2)
            sage: g._pos[0]
            (0.0, 1.0)

            sage: g = graphs.CycleGraph(4)
            sage: pos = g._circle_embedding(g.vertex_iterator(), return_dict=True)
            sage: pos[0]
            (1.0, 0.0)

        TESTS:

        The rounding error raised in :trac:`22050` is fixed::

            sage: G = Graph(4)
            sage: G._circle_embedding(G.vertices(sort=True))
            sage: G._pos
            {0: (1.0, 0.0), 1: (0.0, 1.0), 2: (-1.0, 0.0), 3: (0.0, -1.0)}
        """
        c_x, c_y = center
        vertices = list(vertices)
        n = len(vertices)

        if return_dict:
            pos = {}
        else:
            pos = None
            try:
                pos = self._pos
            except AttributeError:
                pass
            if pos is None:
                pos = self._pos = {}

        from math import sin, cos, pi
        for i, v in enumerate(vertices):
            i += shift
            # We round cos and sin to avoid results like 1.2246467991473532e-16
            # when asking for sin(pi)
            v_x = c_x + radius * round(cos(angle + 2*i*pi / n), 10)
            v_y = c_y + radius * round(sin(angle + 2*i*pi / n), 10)
            pos[v] = (v_x, v_y)

        if return_dict:
            return pos

    def _line_embedding(self, vertices, first=(0, 0), last=(0, 1), return_dict=False):
        r"""
        Set some vertices on a line in the embedding of this graph.

        By default, this method modifies the graph's embedding so that the
        vertices of ``vertices`` appear on a line, where the position of
        ``vertices[0]`` is the pair ``first`` and the position of
        ``vertices[-1]`` is ``last``. The vertices are evenly spaced.

        INPUT:

        - ``vertices`` -- an iterable container of vertices (list, set, dict,
          etc.). The order of the vertices in the line embedding is given by
          ``list(vertices)``.

        - ``first`` -- tuple (default: `(0, 0)`); first coordinate of the line.

        - ``last`` -- tuple (default: `(0, 1)`); last coordinate of the line.

        - ``return_dict`` -- boolean (default: ``False``); by default the
          computed positions of the specified vertices are stored in the
          position dictionary of the graph. When ``return_dict == True``, a
          dictionary containing only the position of the specified vertices is
          returned.

        EXAMPLES::

            sage: g = graphs.PathGraph(5)
            sage: g._line_embedding([0, 2, 4, 1, 3], first=(-1, -1), last=(1, 1))
            sage: g.show()

            sage: pos = g._line_embedding([4, 2, 0, 1, 3], first=(-1, -1), last=(1, 1), return_dict=True)
            sage: pos[0]
            (0.0, 0.0)
            sage: g.get_pos()[0]
            (-1, -1)

        TESTS::

            sage: g = Graph(1)
            sage: g._line_embedding([0], first=(-1, -1), last=(1, 1))
            sage: g.get_pos()
            {0: (0, 0)}
            sage: g = Graph()
            sage: g._line_embedding(g.vertices(sort=False), first=(-1, -1), last=(1, 1))
            sage: g.get_pos()
            {}
        """
        vertices = list(vertices)

        if return_dict:
            pos = {}
        else:
            pos = None
            try:
                pos = self._pos
            except AttributeError:
                pass
            if pos is None:
                pos = self._pos = {}

        n = len(vertices) - 1.

        if n:
            fx, fy = first
            dx = (last[0] - first[0]) / n
            dy = (last[1] - first[1]) / n
        else:
            fx, fy = (first[0] + last[0]) / 2, (first[1] + last[1]) / 2
            dx = dy = 0

        for v in vertices:
            pos[v] = (fx, fy)
            fx += dx
            fy += dy

        if return_dict:
            return pos

    def graphplot(self, **options):
        """
        Return a :class:`~sage.graphs.graph_plot.GraphPlot` object.

        See :class:`~sage.graphs.graph_plot.GraphPlot` for more details.

        INPUT:

        - ``**options`` -- parameters for the
          :class:`~sage.graphs.graph_plot.GraphPlot` constructor

        EXAMPLES:

        Creating a :class:`~sage.graphs.graph_plot.GraphPlot` object uses the
        same options as :meth:`~GenericGraph.plot`::

            sage: g = Graph({}, loops=True, multiedges=True, sparse=True)
            sage: g.add_edges([(0,0,'a'),(0,0,'b'),(0,1,'c'),(0,1,'d'),
            ....:     (0,1,'e'),(0,1,'f'),(0,1,'f'),(2,1,'g'),(2,2,'h')])
            sage: GP = g.graphplot(edge_labels=True, color_by_label=True, edge_style='dashed')
            sage: GP.plot()
            Graphics object consisting of 22 graphics primitives

        We can modify the :class:`~sage.graphs.graph_plot.GraphPlot` object.
        Notice that the changes are cumulative::

            sage: GP.set_edges(edge_style='solid')
            sage: GP.plot()
            Graphics object consisting of 22 graphics primitives
            sage: GP.set_vertices(talk=True)
            sage: GP.plot()
            Graphics object consisting of 22 graphics primitives
        """
        from sage.graphs.graph_plot import GraphPlot
        return GraphPlot(graph=self, options=options)

    def _rich_repr_(self, display_manager, **kwds):
        """
        Rich Output Magic Method

        See :mod:`sage.repl.rich_output` for details.

        EXAMPLES::

            sage: from sage.repl.rich_output import get_display_manager
            sage: dm = get_display_manager()
            sage: Graph()._rich_repr_(dm, edge_labels=True)
            OutputPlainText container

        The ``supplemental_plot`` preference lets us control whether
        this object is shown as text or picture+text::

            sage: dm.preferences.supplemental_plot
            'never'
            sage: del dm.preferences.supplemental_plot
            sage: graphs.RandomGNP(20,0.0)
            RandomGNP(20,0.000000000000000): Graph on 20 vertices (use the .plot() method to plot)
            sage: dm.preferences.supplemental_plot = 'never'
        """
        prefs = display_manager.preferences
        is_small = (0 < self.num_verts() < 20)
        can_plot = (prefs.supplemental_plot != 'never')
        plot_graph = can_plot and (prefs.supplemental_plot == 'always' or is_small)
        # Under certain circumstances we display the plot as graphics
        if plot_graph:
            plot_kwds = dict(kwds)
            plot_kwds.setdefault('title', repr(self))
            output = self.plot(**plot_kwds)._rich_repr_(display_manager)
            if output is not None:
                return output
        # create text for non-graphical output
        if can_plot:
            text = '{0} (use the .plot() method to plot)'.format(repr(self))
        else:
            text = repr(self)
        # latex() produces huge tikz environment, override
        tp = display_manager.types
        if (prefs.text == 'latex' and tp.OutputLatex in display_manager.supported_output()):
            return tp.OutputLatex(r'\text{{{0}}}'.format(text))
        return tp.OutputPlainText(text)

    @options()
    def plot(self, **options):
        r"""
        Return a :class:`~sage.plot.graphics.Graphics` object representing the
        (di)graph.

        INPUT:

        - ``pos`` -- an optional positioning dictionary

        - ``layout`` -- string (default: ``None``); specifies a kind of layout
          to use, takes precedence over pos

          - ``'circular'`` -- plots the graph with vertices evenly distributed
            on a circle

          - ``'spring'`` -- uses the traditional spring layout, using the
            graph's current positions as initial positions

          - ``'tree'`` -- the (di)graph must be a tree. One can specify the root
            of the tree using the keyword tree_root, otherwise a root will be
            selected at random. Then the tree will be plotted in levels,
            depending on minimum distance for the root.

        - ``vertex_labels`` -- boolean (default: ``True``); whether to print
          vertex labels

        - ``edge_labels`` -- boolean (default: ``False``); whether to print edge
          labels. If ``True``, the result of ``str(l)`` is printed on the edge
          for each label `l`. Labels equal to ``None`` are not printed (to set
          edge labels, see :meth:`set_edge_label`).

        - ``edge_labels_background`` -- the color of the edge labels
          background. The default is "white". To achieve a transparent
          background use "transparent".

        - ``vertex_size`` -- size of vertices displayed

        - ``vertex_shape`` -- the shape to draw the vertices, for example
          ``"o"`` for circle or ``"s"`` for square. Whole list is available at
          https://matplotlib.org/api/markers_api.html.
          (Not available for multiedge digraphs.)

        - ``graph_border`` -- boolean (default: ``False``); whether to include a
          box around the graph

        - ``vertex_colors`` -- dictionary (default: ``None``); optional
          dictionary to specify vertex colors: each key is a color recognizable
          by matplotlib, and each corresponding entry is a list of vertices. If
          a vertex is not listed, it looks invisible on the resulting plot (it
          doesn't get drawn).

        - ``edge_colors`` -- dictionary (default: ``None``); a dictionary
          specifying edge colors: each key is a color recognized by matplotlib,
          and each entry is a list of edges.

        - ``partition`` -- a partition of the vertex set (default: ``None``); if
          specified, plot will show each cell in a different color.
          ``vertex_colors`` takes precedence.

        - ``talk`` -- boolean (default: ``False``); if ``True``, prints large
          vertices with white backgrounds so that labels are legible on slides

        - ``iterations`` -- integer; how many iterations of the spring layout
          algorithm to go through, if applicable

        - ``color_by_label`` -- a boolean or dictionary or function (default:
          ``False``); whether to color each edge with a different color
          according to its label; the colors are chosen along a rainbow, unless
          they are specified by a function or dictionary mapping labels to
          colors; this option is incompatible with ``edge_color`` and
          ``edge_colors``.

        - ``heights`` -- dictionary (default: ``None``); if specified, this is a
          dictionary from a set of floating point heights to a set of vertices

        - ``edge_style`` -- keyword arguments passed into the edge-drawing
          routine.  This currently only works for directed graphs, since we pass
          off the undirected graph to networkx

        - ``tree_root`` -- a vertex (default: ``None``); if specified, this
          vertex is used as the root for the ``layout="tree"`` option.
          Otherwise, then one is chosen at random. Ignored unless
          ``layout='tree'``.

        - ``tree_orientation`` -- string (default: ``"down"``); one of "up" or
          "down".  If "up" (resp., "down"), then the root of the tree will
          appear on the bottom (resp., top) and the tree will grow upwards
          (resp. downwards). Ignored unless ``layout='tree'``.

        - ``save_pos`` -- boolean (default: ``False``); save position computed
          during plotting

        .. NOTE::

            - This method supports any parameter accepted by
              :meth:`sage.plot.graphics.Graphics.show`.

            - See the documentation of the :mod:`sage.graphs.graph_plot` module
              for information and examples of how to define parameters that will
              be applied to **all** graph plots.

            - Default parameters for this method *and a specific graph* can also
              be set through the :class:`~sage.misc.decorators.options`
              mechanism. For more information on this different way to set
              default parameters, see the help of the :class:`options decorator
              <sage.misc.decorators.options>`.

            - See also the :mod:`sage.graphs.graph_latex` module for ways to use
              LaTeX to produce an image of a graph.

        EXAMPLES::

            sage: from sage.graphs.graph_plot import graphplot_options
            sage: sorted(graphplot_options.items())
            [...]

            sage: from math import sin, cos, pi
            sage: P = graphs.PetersenGraph()
            sage: d = {'#FF0000': [0, 5], '#FF9900': [1, 6], '#FFFF00': [2, 7], '#00FF00': [3, 8], '#0000FF': [4, 9]}
            sage: pos_dict = {}
            sage: for i in range(5):
            ....:  x = float(cos(pi/2 + ((2*pi)/5)*i))
            ....:  y = float(sin(pi/2 + ((2*pi)/5)*i))
            ....:  pos_dict[i] = [x,y]
            sage: for i in range(5, 10):
            ....:  x = float(0.5*cos(pi/2 + ((2*pi)/5)*i))
            ....:  y = float(0.5*sin(pi/2 + ((2*pi)/5)*i))
            ....:  pos_dict[i] = [x,y]
            sage: pl = P.plot(pos=pos_dict, vertex_colors=d)
            sage: pl.show()

        ::

            sage: C = graphs.CubeGraph(8)
            sage: P = C.plot(vertex_labels=False, vertex_size=0, graph_border=True)
            sage: P.show()

        ::

            sage: G = graphs.HeawoodGraph()
            sage: for u, v, l in G.edges(sort=False):
            ....:     G.set_edge_label(u, v, '(' + str(u) + ',' + str(v) + ')')
            sage: G.plot(edge_labels=True).show()

        ::

            sage: D = DiGraph({0: [1, 10, 19], 1: [8, 2], 2: [3, 6], 3: [19, 4],
            ....:              4: [17, 5], 5: [6, 15], 6: [7], 7: [8, 14],
            ....:              8: [9], 9: [10, 13], 10: [11], 11: [12, 18],
            ....:              12: [16, 13], 13: [14], 14: [15], 15: [16],
            ....:              16: [17], 17: [18], 18: [19]}, sparse=True)
            sage: for u,v,l in D.edges(sort=False):
            ....:     D.set_edge_label(u, v, '(' + str(u) + ',' + str(v) + ')')
            sage: D.plot(edge_labels=True, layout='circular').show()

        ::

            sage: from sage.plot.colors import rainbow
            sage: C = graphs.CubeGraph(5)
            sage: R = rainbow(5)
            sage: edge_colors = {R[i]: [] for i in range(5)}
            sage: for u, v, l in C.edges(sort=False):
            ....:  for i in range(5):
            ....:      if u[i] != v[i]:
            ....:          edge_colors[R[i]].append((u, v, l))
            sage: C.plot(vertex_labels=False, vertex_size=0, edge_colors=edge_colors).show()

        ::

            sage: D = graphs.DodecahedralGraph()
            sage: Pi = [[6,5,15,14,7], [16,13,8,2,4], [12,17,9,3,1], [0,19,18,10,11]]
            sage: D.show(partition=Pi)

        ::

            sage: G = graphs.PetersenGraph()
            sage: G.allow_loops(True)
            sage: G.add_edge(0, 0)
            sage: G.show()

        ::

            sage: D = DiGraph({0: [0, 1], 1: [2], 2: [3]}, loops=True)
            sage: D.show()
            sage: D.show(edge_colors={(0, 1, 0): [(0, 1, None), (1, 2, None)], (0, 0, 0): [(2, 3, None)]})

        ::

            sage: pos = {0: [0.0, 1.5], 1: [-0.8, 0.3], 2: [-0.6, -0.8], 3: [0.6, -0.8], 4: [0.8, 0.3]}
            sage: g = Graph({0: [1], 1: [2], 2: [3], 3: [4], 4: [0]})
            sage: g.plot(pos=pos, layout='spring', iterations=0)
            Graphics object consisting of 11 graphics primitives

        ::

            sage: G = Graph()
            sage: P = G.plot()
            sage: P.axes()
            False
            sage: G = DiGraph()
            sage: P = G.plot()
            sage: P.axes()
            False

        ::

            sage: G = graphs.PetersenGraph()
            sage: G.get_pos()
            {0: (0.0..., 1.0...),
             1: (-0.95..., 0.30...),
             2: (-0.58..., -0.80...),
             3: (0.58..., -0.80...),
             4: (0.95..., 0.30...),
             5: (0.0..., 0.5...),
             6: (-0.47..., 0.15...),
             7: (-0.29..., -0.40...),
             8: (0.29..., -0.40...),
             9: (0.47..., 0.15...)}
            sage: P = G.plot(save_pos=True, layout='spring')

            The following illustrates the format of a position dictionary.

            sage: G.get_pos() # currently random across platforms, see #9593
            {0: [1.17..., -0.855...],
             1: [1.81..., -0.0990...],
             2: [1.35..., 0.184...],
             3: [1.51..., 0.644...],
             4: [2.00..., -0.507...],
             5: [0.597..., -0.236...],
             6: [2.04..., 0.687...],
             7: [1.46..., -0.473...],
             8: [0.902..., 0.773...],
             9: [2.48..., -0.119...]}

        ::

            sage: T = list(graphs.trees(7))
            sage: t = T[3]
            sage: t.plot(heights={0: [0], 1: [4, 5, 1], 2: [2], 3: [3, 6]})
            Graphics object consisting of 14 graphics primitives

        ::

            sage: T = list(graphs.trees(7))
            sage: t = T[3]
            sage: t.plot(heights={0: [0], 1: [4, 5, 1], 2: [2], 3: [3, 6]})
            Graphics object consisting of 14 graphics primitives
            sage: t.set_edge_label(0, 1, -7)
            sage: t.set_edge_label(0, 5, 3)
            sage: t.set_edge_label(0, 5, 99)
            sage: t.set_edge_label(1, 2, 1000)
            sage: t.set_edge_label(3, 2, 'spam')
            sage: t.set_edge_label(2, 6, 3/2)
            sage: t.set_edge_label(0, 4, 66)
            sage: t.plot(heights={0: [0], 1: [4, 5, 1], 2: [2], 3: [3, 6]}, edge_labels=True)
            Graphics object consisting of 20 graphics primitives

        ::

            sage: T = list(graphs.trees(7))
            sage: t = T[3]
            sage: t.plot(layout='tree')
            Graphics object consisting of 14 graphics primitives

        ::

            sage: t = DiGraph('JCC???@A??GO??CO??GO??')
            sage: t.plot(layout='tree', tree_root=0, tree_orientation="up")
            Graphics object consisting of 22 graphics primitives
            sage: D = DiGraph({0: [1, 2, 3], 2: [1, 4], 3: [0]})
            sage: D.plot()
            Graphics object consisting of 16 graphics primitives

            sage: D = DiGraph(multiedges=True,sparse=True)
            sage: for i in range(5):
            ....:   D.add_edge((i, i + 1, 'a'))
            ....:   D.add_edge((i, i - 1, 'b'))
            sage: D.plot(edge_labels=True, edge_colors=D._color_by_label())
            Graphics object consisting of 34 graphics primitives
            sage: D.plot(edge_labels=True, color_by_label={'a': 'blue', 'b': 'red'}, edge_style='dashed')
            Graphics object consisting of 34 graphics primitives

            sage: g = Graph({}, loops=True, multiedges=True, sparse=True)
            sage: g.add_edges([(0, 0, 'a'), (0, 0, 'b'), (0, 1, 'c'), (0, 1, 'd'),
            ....:   (0, 1, 'e'), (0, 1, 'f'), (0, 1, 'f'), (2, 1, 'g'), (2, 2, 'h')])
            sage: g.plot(edge_labels=True, color_by_label=True, edge_style='dashed')
            Graphics object consisting of 22 graphics primitives

        ::

            sage: S = SupersingularModule(389)
            sage: H = S.hecke_matrix(2)
            sage: D = DiGraph(H,sparse=True)
            sage: P = D.plot()

        ::

            sage: G=Graph({'a':['a','b','b','b','e'],'b':['c','d','e'],'c':['c','d','d','d'],'d':['e']}, sparse=True)
            sage: G.show(pos={'a':[0,1],'b':[1,1],'c':[2,0],'d':[1,0],'e':[0,0]})

        TESTS::

            sage: G = DiGraph({0: {1: 'a', 2: 'a'}, 1: {0: 'b'}, 2: {0: 'c'}})
            sage: p = G.plot(edge_labels=True, color_by_label={'a': 'yellow', 'b': 'purple'}); p
            Graphics object consisting of 14 graphics primitives
            sage: sorted([x.options()['rgbcolor'] for x in p if isinstance(x, sage.plot.arrow.CurveArrow)])
            ['black', 'purple', 'yellow', 'yellow']
        """
        return self.graphplot(**options).plot()

    def show(self, method="matplotlib", **kwds):
        """
        Show the (di)graph.

        INPUT:

        - ``method`` -- string (default: ``"matplotlib"``); method to use to
          display the graph, either ``"matplotlib"``, or ``"js"`` to visualize
          it in a browser using `d3.js <http://d3js.org/>`_.

        - Any other argument supported by the drawing functions:

          - ``"matplotlib"`` -- see :meth:`GenericGraph.plot
            <sage.graphs.generic_graph.GenericGraph.plot>` and
            :meth:`sage.plot.graphics.Graphics.show`

          - ``"js"`` -- see :meth:`~sage.graphs.graph_plot_js.gen_html_code`

        EXAMPLES::

            sage: C = graphs.CubeGraph(8)
            sage: P = C.plot(vertex_labels=False, vertex_size=0, graph_border=True)
            sage: P.show()  # long time (3s on sage.math, 2011)

        """
        if method == "js":
            from sage.graphs.graph_plot_js import gen_html_code
            from sage.doctest import DOCTEST_MODE
            filename = gen_html_code(self, **kwds)

            if DOCTEST_MODE:
                return
            from sage.misc.viewer import browser
            import os
            os.system('%s %s 2>/dev/null 1>/dev/null &' % (browser(), filename))
            return

        from .graph_plot import graphplot_options
        # This dictionary only contains the options that graphplot
        # understands. These options are removed from kwds at the same
        # time.
        plot_kwds = {k: kwds.pop(k) for k in graphplot_options if k in kwds}

        return self.graphplot(**plot_kwds).show(**kwds)

    def plot3d(self, bgcolor=(1, 1, 1),
               vertex_colors=None, vertex_size=0.06, vertex_labels=False,
               edge_colors=None, edge_size=0.02, edge_size2=0.0325,
               pos3d=None, color_by_label=False,
               engine='threejs', **kwds):
        r"""
        Plot a graph in three dimensions.

        See also the :mod:`sage.graphs.graph_latex` module for ways to use LaTeX
        to produce an image of a graph.

        INPUT:

        - ``bgcolor`` -- rgb tuple (default: ``(1,1,1)``)

        - ``vertex_size`` -- float (default: ``0.06``)

        - ``vertex_labels`` -- a boolean (default: ``False``); whether to
          display vertices using text labels instead of spheres

        - ``vertex_colors`` -- dictionary (default: ``None``); optional
          dictionary to specify vertex colors: each key is a color recognizable
          by :mod:`~sage.plot.plot3d.tachyon` (rgb tuple (default: ``(1,0,0)``)),
          and each corresponding entry is a list of vertices. If a vertex is not
          listed, it looks invisible on the resulting plot (it does not get
          drawn).

        - ``edge_colors`` -- dictionary (default: ``None``); a dictionary
          specifying edge colors: each key is a color recognized by
          :mod:`~sage.plot.plot3d.tachyon` (default: ``(0,0,0)``), and each entry
          is a list of edges.

        - ``color_by_label`` -- a boolean or dictionary or function (default:
          ``False``) whether to color each edge with a different color according
          to its label; the colors are chosen along a rainbow, unless they are
          specified by a function or dictionary mapping labels to colors; this
          option is incompatible with ``edge_color`` and ``edge_colors``.

        - ``edge_size`` -- float (default: ``0.02``)

        - ``edge_size2`` -- float (default: ``0.0325``); used for
          :class:`~sage.plot.plot3d.tachyon.Tachyon` sleeves

        - ``pos3d`` -- a position dictionary for the vertices

        - ``layout``, ``iterations``, ... -- layout options; see :meth:`layout`

        - ``engine`` -- string (default: ``'threejs'``); the renderer to use among:

           * ``'threejs'``: interactive web-based 3D viewer using JavaScript
             and a WebGL renderer

           * ``'jmol'``: interactive 3D viewer using Java

           * ``'tachyon'``: ray tracer generating a static PNG image

        - ``xres`` -- resolution

        - ``yres`` -- resolution

        - ``**kwds`` -- passed on to the rendering engine

        EXAMPLES::

            sage: G = graphs.CubeGraph(5)
            sage: G.plot3d(iterations=500, edge_size=None, vertex_size=0.04) # long time
            Graphics3d Object

        We plot a fairly complicated Cayley graph::

            sage: A5 = AlternatingGroup(5); A5
            Alternating group of order 5!/2 as a permutation group
            sage: G = A5.cayley_graph()
            sage: G.plot3d(vertex_size=0.03, edge_size=0.01, vertex_colors={(1,1,1): list(G)}, bgcolor=(0,0,0), color_by_label=True, iterations=200) # long time
            Graphics3d Object

        Some :class:`~sage.plot.plot3d.tachyon.Tachyon` examples::

            sage: D = graphs.DodecahedralGraph()
            sage: P3D = D.plot3d(engine='tachyon')
            sage: P3D.show() # long time

        ::

            sage: G = graphs.PetersenGraph()
            sage: G.plot3d(engine='tachyon', vertex_colors={(0,0,1): list(G)}).show() # long time

        ::

            sage: C = graphs.CubeGraph(4)
            sage: C.plot3d(engine='tachyon', edge_colors={(0,1,0): C.edges(sort=False)}, vertex_colors={(1,1,1): list(C)}, bgcolor=(0,0,0)).show() # long time

        ::

            sage: K = graphs.CompleteGraph(3)
            sage: K.plot3d(engine='tachyon', edge_colors={(1,0,0): [(0,1,None)], (0,1,0): [(0,2,None)], (0,0,1): [(1,2,None)]}).show() # long time

        A directed version of the dodecahedron

        ::

            sage: D = DiGraph({0: [1, 10, 19], 1: [8, 2], 2: [3, 6], 3: [19, 4],
            ....:              4: [17, 5], 5: [6, 15], 6: [7], 7: [8, 14],
            ....:              8: [9], 9: [10, 13], 10: [11], 11: [12, 18],
            ....:              12: [16, 13], 13: [14], 14: [15], 15: [16], 16: [17],
            ....:              17: [18], 18: [19], 19: []})
            sage: D.plot3d().show() # long time

        ::

            sage: P = graphs.PetersenGraph().to_directed()
            sage: from sage.plot.colors import rainbow
            sage: R = rainbow(P.size(), 'rgbtuple')
            sage: edge_colors = {R[i]: [e] for i, e in enumerate(P.edge_iterator())}
            sage: P.plot3d(engine='tachyon', edge_colors=edge_colors).show() # long time


        ::

            sage: G=Graph({'a':['a','b','b','b','e'],'b':['c','d','e'],'c':['c','d','d','d'],'d':['e']},sparse=True)
            sage: G.show3d()
            Traceback (most recent call last):
            ...
            NotImplementedError: 3D plotting of multiple edges or loops not implemented

        Using the ``partition`` keyword::

            sage: G = graphs.WheelGraph(7)
            sage: G.plot3d(partition=[[0], [1, 2, 3, 4, 5, 6]])
            Graphics3d Object

        TESTS::

            sage: G = DiGraph({0: {1: 'a', 2: 'a'}, 1: {0: 'b'}, 2: {0: 'c'}})
            sage: p = G.plot3d(edge_labels=True, color_by_label={'a': 'yellow', 'b': 'cyan'})
            sage: s = p.x3d_str()

        This 3D plot contains four yellow objects (two cylinders and
        two cones), two black objects and 2 cyan objects::

            sage: s.count("Material diffuseColor='1.0 1.0 0.0'")
            4
            sage: s.count("Material diffuseColor='0.0 0.0 0.0'")
            2
            sage: s.count("Material diffuseColor='0.0 1.0 1.0'")
            2

        .. SEEALSO::

            - :meth:`plot`
            - :meth:`graphviz_string`
        """
        from . import graph_plot
        layout_options = {key: kwds[key] for key in kwds.keys() if key in graph_plot.layout_options}
        kwds           = {key: kwds[key] for key in kwds.keys() if key not in graph_plot.layout_options}
        if pos3d is None:
            pos3d = self.layout(dim=3, **layout_options)

        if self.has_multiple_edges() or self.has_loops():
            raise NotImplementedError("3D plotting of multiple edges or loops not implemented")
        if engine in ['threejs', 'jmol']:
            from sage.plot.plot3d.all import sphere, line3d, arrow3d, text3d
            from sage.plot.plot3d.texture import Texture
            kwds.setdefault('aspect_ratio', [1, 1, 1])

            if vertex_colors is None:
                if 'partition' in kwds:
                    from sage.plot.colors import rainbow
                    partition = kwds['partition']
                    l = len(partition)
                    R = rainbow(l)
                    vertex_colors = {R[i]: partition[i] for i in range(l)}
                else:
                    vertex_colors = {(1, 0, 0) : list(self)}

            if color_by_label:
                if edge_colors is  None:
                    # do the coloring
                    edge_colors = self._color_by_label(format=color_by_label)
            elif edge_colors is None:
                edge_colors = {(0, 0, 0) : self.edges(sort=False)}

            # by default turn off the frame
            if 'frame' not in kwds:
                kwds['frame'] = False
            # by default make the background given by bgcolor
            if 'background' not in kwds:
                kwds['background'] = bgcolor
            try:
                graphic = 0
                for color in vertex_colors:
                    texture = Texture(color=color, ambient=0.1, diffuse=0.9, specular=0.03)
                    for v in vertex_colors[color]:
                        if vertex_labels:
                            graphic += text3d(repr(v), pos3d[v])
                        else:
                            graphic += sphere(center=pos3d[v], size=vertex_size, texture=texture, **kwds)
                if self._directed:
                    for color in edge_colors:
                        for u, v, l in edge_colors[color]:
                            graphic += arrow3d(pos3d[u], pos3d[v], radius=edge_size, color=color, closed=False, **kwds)

                else:
                    for color in edge_colors:
                        texture = Texture(color=color, ambient=0.1, diffuse=0.9, specular=0.03)
                        for u, v, l in edge_colors[color]:
                            graphic += line3d([pos3d[u], pos3d[v]], radius=edge_size, texture=texture, closed=False, **kwds)

                return graphic

            except KeyError:
                raise KeyError("you have not specified positions for all the vertices")

        elif engine == 'tachyon':
            TT, pos3d = tachyon_vertex_plot(self, bgcolor=bgcolor, vertex_colors=vertex_colors,
                                            vertex_size=vertex_size, pos3d=pos3d, **kwds)

            if color_by_label:
                if edge_colors is  None:
                    # do the coloring
                    edge_colors = self._color_by_label(format=color_by_label)

            if edge_colors is None:
                edge_colors = {(0, 0, 0) : self.edges(sort=False)}

            i = 0

            for color in edge_colors:
                i += 1
                TT.texture('edge_color_%d' % i, ambient=0.1, diffuse=0.9,
                           specular=0.03, opacity=1.0, color=color)
                if self._directed:
                    for u,v,l in edge_colors[color]:
                        TT.fcylinder((pos3d[u][0], pos3d[u][1], pos3d[u][2]),
                                     (pos3d[v][0], pos3d[v][1], pos3d[v][2]),
                                     edge_size, 'edge_color_%d' % i)
                        TT.fcylinder((0.25 * pos3d[u][0] + 0.75 * pos3d[v][0],
                                      0.25 * pos3d[u][1] + 0.75 * pos3d[v][1],
                                      0.25 * pos3d[u][2] + 0.75 * pos3d[v][2]),
                                     (pos3d[v][0], pos3d[v][1], pos3d[v][2]),
                                     edge_size2, 'edge_color_%d' % i)
                else:
                    for u, v, l in edge_colors[color]:
                        TT.fcylinder((pos3d[u][0], pos3d[u][1], pos3d[u][2]),
                                     (pos3d[v][0], pos3d[v][1], pos3d[v][2]),
                                     edge_size, 'edge_color_%d' % i)

            return TT

        else:
            raise TypeError("rendering engine (%s) not implemented" % engine)

    def show3d(self, bgcolor=(1, 1, 1), vertex_colors=None, vertex_size=0.06,
               edge_colors=None, edge_size=0.02, edge_size2=0.0325,
               pos3d=None, color_by_label=False,
               engine='threejs', **kwds):
        """
        Plot the graph and show the resulting plot.

        INPUT:

        - ``bgcolor`` -- rgb tuple (default: ``(1,1,1)``)

        - ``vertex_size`` -- float (default: ``0.06``)

        - ``vertex_labels`` -- a boolean (default: ``False``); whether to
          display vertices using text labels instead of spheres

        - ``vertex_colors`` -- dictionary (default: ``None``); optional
          dictionary to specify vertex colors: each key is a color recognizable
          by :mod:`~sage.plot.plot3d.tachyon` (rgb tuple (default:
          ``(1,0,0)``)), and each corresponding entry is a list of vertices. If
          a vertex is not listed, it looks invisible on the resulting plot (it
          doesn't get drawn).

        - ``edge_colors`` -- dictionary (default: ``None``); a dictionary
          specifying edge colors: each key is a color recognized by
          :mod:`~sage.plot.plot3d.tachyon` (default: ``(0,0,0)``), and each
          entry is a list of edges.

        - ``color_by_label`` -- a boolean or dictionary or function (default:
          ``False``) whether to color each edge with a different color according
          to its label; the colors are chosen along a rainbow, unless they are
          specified by a function or dictionary mapping labels to colors; this
          option is incompatible with ``edge_color`` and ``edge_colors``.

        - ``edge_size`` -- float (default: ``0.02``)

        - ``edge_size2`` -- float (default: ``0.0325``); used for
          :class:`~sage.plot.plot3d.tachyon.Tachyon` sleeves

        - ``pos3d`` -- a position dictionary for the vertices

        - ``layout``, ``iterations``, ... -- layout options; see :meth:`layout`

        - ``engine`` -- string (default: ``'threejs'``); the renderer to use among:

           * ``'threejs'``: interactive web-based 3D viewer using JavaScript
             and a WebGL renderer

           * ``'jmol'``: interactive 3D viewer using Java

           * ``'tachyon'``: ray tracer generating a static PNG image

        - ``xres`` -- resolution

        - ``yres`` -- resolution

        - ``**kwds`` -- passed on to the rendering engine

        EXAMPLES::

            sage: G = graphs.CubeGraph(5)
            sage: G.show3d(iterations=500, edge_size=None, vertex_size=0.04) # long time

        We plot a fairly complicated Cayley graph::

            sage: A5 = AlternatingGroup(5); A5
            Alternating group of order 5!/2 as a permutation group
            sage: G = A5.cayley_graph()
            sage: G.show3d(vertex_size=0.03, edge_size=0.01, edge_size2=0.02,
            ....:          vertex_colors={(1,1,1): list(G)}, bgcolor=(0,0,0),
            ....:          color_by_label=True, iterations=200)  # long time

        Some :class:`~sage.plot.plot3d.tachyon.Tachyon` examples::

            sage: D = graphs.DodecahedralGraph()
            sage: D.show3d(engine='tachyon') # long time

        ::

            sage: G = graphs.PetersenGraph()
            sage: G.show3d(engine='tachyon', vertex_colors={(0,0,1): list(G)}) # long time

        ::

            sage: C = graphs.CubeGraph(4)
            sage: C.show3d(engine='tachyon', edge_colors={(0,1,0): C.edges(sort=False)}, vertex_colors={(1,1,1): list(C)}, bgcolor=(0,0,0)) # long time

        ::

            sage: K = graphs.CompleteGraph(3)
            sage: K.show3d(engine='tachyon', edge_colors={(1,0,0): [(0, 1, None)], (0, 1, 0): [(0, 2, None)], (0, 0, 1): [(1, 2, None)]}) # long time
        """
        self.plot3d(bgcolor=bgcolor, vertex_colors=vertex_colors,
                    edge_colors=edge_colors, vertex_size=vertex_size, engine=engine,
                    edge_size=edge_size, edge_size2=edge_size2, pos3d=pos3d,
                    color_by_label=color_by_label, **kwds).show()

    def _keys_for_vertices(self):
        """
        Return a function mapping each vertex to a unique identifier.

        The identifier is stable iff all vertex labels are unique. It is a
        string not starting with a number, as required by ``dot2tex``.

        EXAMPLES::

            sage: g = graphs.Grid2dGraph(5, 5)
            sage: g._keys_for_vertices()
            <function ...get_label at ...>

        TESTS:

        We check that :trac:`21916` is fixed::

            sage: g = graphs.PetersenGraph()
            sage: key = g._keys_for_vertices()
            sage: g.add_vertex("a")
            sage: s = g.graphviz_string()
        """
        label = {v: 'node_{0}'.format(i) for i, v in enumerate(self)}

        def get_label(vertex):
            return label[vertex]
        return get_label

    # String representation to be used by other programs
    @options(labels="string",
             vertex_labels=True, edge_labels=False,
             edge_color=None, edge_colors=None,
             edge_options=(),
             color_by_label=False,
             rankdir='down',
             subgraph_clusters=[])
    def graphviz_string(self, **options):
        r"""
        Return a representation in the ``dot`` language.

        The ``dot`` language is a text based format for graphs. It is used by
        the software suite ``graphviz``. The specifications of the language are
        available on the web (see the reference [dotspec]_).

        INPUT:

        - ``labels`` -- string (default: ``"string"``); either ``"string"`` or
          ``"latex"``. If labels is ``"string"``, latex commands are not
          interpreted. This option stands for both vertex labels and edge
          labels.

        - ``vertex_labels`` -- boolean (default: ``True``); whether to add the
          labels on vertices

        - ``edge_labels`` -- boolean (default: ``False``); whether to add the
          labels on edges

        - ``edge_color`` -- (default: ``None``); specify a default color for the
          edges. The color could be one of

          - a name given as a string such as ``"blue"`` or ``"orchid"``

          - a HSV sequence in a string such as ``".52,.386,.22"``

          - an hexadecimal code such as ``"#DA3305"``

          - a 3-tuple of floating point (to be interpreted as RGB tuple). In
            this case the 3-tuple is converted in hexadecimal code.

        - ``edge_colors`` -- dictionary (default: ``None``); a dictionary whose
          keys are colors and values are list of edges. The list of edges need
          not to be complete in which case the default color is used. See the
          option ``edge_color`` for a description of valid color formats.

        - ``color_by_label`` -- a boolean or dictionary or function (default:
          ``False``); whether to color each edge with a different color
          according to its label; the colors are chosen along a rainbow, unless
          they are specified by a function or dictionary mapping labels to
          colors; this option is incompatible with ``edge_color`` and
          ``edge_colors``.  See the option ``edge_color`` for a description of
          valid color formats.

        - ``edge_options`` -- a function (or tuple thereof) mapping edges to a
          dictionary of options for this edge

        - ``rankdir`` -- ``'left'``, ``'right'``, ``'up'``, or ``'down'``
          (default: ``'down'``, for consistency with ``graphviz``): the
          preferred ranking direction for acyclic layouts; see the ``rankdir``
          option of ``graphviz``.

        - ``subgraph_clusters`` -- a list of lists of vertices (default:
          ``[]``); From [dotspec]_: "If supported, the layout engine will do the
          layout so that the nodes belonging to the cluster are drawn together,
          with the entire drawing of the cluster contained within a bounding
          rectangle. Note that, for good and bad, cluster subgraphs are not part
          of the ``dot`` language, but solely a syntactic convention adhered to
          by certain of the layout engines."

        EXAMPLES::

            sage: G = Graph({0: {1: None, 2: None}, 1: {0: None, 2: None}, 2: {0: None, 1: None, 3: 'foo'}, 3: {2: 'foo'}}, sparse=True)
            sage: print(G.graphviz_string(edge_labels=True))
            graph {
              node_0  [label="0"];
              node_1  [label="1"];
              node_2  [label="2"];
              node_3  [label="3"];
            <BLANKLINE>
              node_0 -- node_1;
              node_0 -- node_2;
              node_1 -- node_2;
              node_2 -- node_3 [label="foo"];
            }

        A variant, with the labels in latex, for post-processing with
        ``dot2tex``::

            sage: print(G.graphviz_string(edge_labels=True, labels="latex"))
            graph {
              node [shape="plaintext"];
              node_0  [label=" ", texlbl="$0$"];
              node_1  [label=" ", texlbl="$1$"];
              node_2  [label=" ", texlbl="$2$"];
              node_3  [label=" ", texlbl="$3$"];
            <BLANKLINE>
              node_0 -- node_1;
              node_0 -- node_2;
              node_1 -- node_2;
              node_2 -- node_3 [label=" ", texlbl="$\text{\texttt{foo}}$"];
            }

        Same, with a digraph and a color for edges::

            sage: G = DiGraph({0: {1: None, 2: None}, 1: {2: None}, 2: {3: 'foo'}, 3: {}}, sparse=True)
            sage: print(G.graphviz_string(edge_color="red"))
            digraph {
              node_0  [label="0"];
              node_1  [label="1"];
              node_2  [label="2"];
              node_3  [label="3"];
            <BLANKLINE>
            edge [color="red"];
              node_0 -> node_1;
              node_0 -> node_2;
              node_1 -> node_2;
              node_2 -> node_3;
            }

        A digraph using latex labels for vertices and edges::

            sage: f(x) = -1 / x                                                             # optional - sage.symbolic
            sage: g(x) = 1 / (x + 1)                                                        # optional - sage.symbolic
            sage: G = DiGraph()                                                             # optional - sage.symbolic
            sage: G.add_edges((i, f(i), f) for i in (1, 2, 1/2, 1/4))                       # optional - sage.symbolic
            sage: G.add_edges((i, g(i), g) for i in (1, 2, 1/2, 1/4))                       # optional - sage.symbolic
            sage: print(G.graphviz_string(labels="latex", edge_labels=True))  # random      # optional - sage.symbolic
            digraph {
              node [shape="plaintext"];
              node_10  [label=" ", texlbl="$1$"];
              node_11  [label=" ", texlbl="$2$"];
              node_3  [label=" ", texlbl="$-\frac{1}{2}$"];
              node_6  [label=" ", texlbl="$\frac{1}{2}$"];
              node_7  [label=" ", texlbl="$\frac{1}{2}$"];
              node_5  [label=" ", texlbl="$\frac{1}{3}$"];
              node_8  [label=" ", texlbl="$\frac{2}{3}$"];
              node_4  [label=" ", texlbl="$\frac{1}{4}$"];
              node_1  [label=" ", texlbl="$-2$"];
              node_9  [label=" ", texlbl="$\frac{4}{5}$"];
              node_0  [label=" ", texlbl="$-4$"];
              node_2  [label=" ", texlbl="$-1$"];
            <BLANKLINE>
              node_10 -> node_2 [label=" ", texlbl="$x \ {\mapsto}\ -\frac{1}{x}$"];
              node_10 -> node_6 [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x + 1}$"];
              node_11 -> node_3 [label=" ", texlbl="$x \ {\mapsto}\ -\frac{1}{x}$"];
              node_11 -> node_5 [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x + 1}$"];
              node_7 -> node_1 [label=" ", texlbl="$x \ {\mapsto}\ -\frac{1}{x}$"];
              node_7 -> node_8 [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x + 1}$"];
              node_4 -> node_0 [label=" ", texlbl="$x \ {\mapsto}\ -\frac{1}{x}$"];
              node_4 -> node_9 [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x + 1}$"];
            }

            sage: print(G.graphviz_string(labels="latex", color_by_label=True))  # random   # optional - sage.symbolic
            digraph {
              node [shape="plaintext"];
              node_10  [label=" ", texlbl="$1$"];
              node_11  [label=" ", texlbl="$2$"];
              node_3  [label=" ", texlbl="$-\frac{1}{2}$"];
              node_6  [label=" ", texlbl="$\frac{1}{2}$"];
              node_7  [label=" ", texlbl="$\frac{1}{2}$"];
              node_5  [label=" ", texlbl="$\frac{1}{3}$"];
              node_8  [label=" ", texlbl="$\frac{2}{3}$"];
              node_4  [label=" ", texlbl="$\frac{1}{4}$"];
              node_1  [label=" ", texlbl="$-2$"];
              node_9  [label=" ", texlbl="$\frac{4}{5}$"];
              node_0  [label=" ", texlbl="$-4$"];
              node_2  [label=" ", texlbl="$-1$"];
            <BLANKLINE>
              node_10 -> node_2 [color = "#ff0000"];
              node_10 -> node_6 [color = "#00ffff"];
              node_11 -> node_3 [color = "#ff0000"];
              node_11 -> node_5 [color = "#00ffff"];
              node_7 -> node_1 [color = "#ff0000"];
              node_7 -> node_8 [color = "#00ffff"];
              node_4 -> node_0 [color = "#ff0000"];
              node_4 -> node_9 [color = "#00ffff"];
            }

            sage: print(G.graphviz_string(labels="latex", color_by_label={f: "red", g: "blue"}))  # random  # optional - sage.symbolic
            digraph {
              node [shape="plaintext"];
              node_10  [label=" ", texlbl="$1$"];
              node_11  [label=" ", texlbl="$2$"];
              node_3  [label=" ", texlbl="$-\frac{1}{2}$"];
              node_6  [label=" ", texlbl="$\frac{1}{2}$"];
              node_7  [label=" ", texlbl="$\frac{1}{2}$"];
              node_5  [label=" ", texlbl="$\frac{1}{3}$"];
              node_8  [label=" ", texlbl="$\frac{2}{3}$"];
              node_4  [label=" ", texlbl="$\frac{1}{4}$"];
              node_1  [label=" ", texlbl="$-2$"];
              node_9  [label=" ", texlbl="$\frac{4}{5}$"];
              node_0  [label=" ", texlbl="$-4$"];
              node_2  [label=" ", texlbl="$-1$"];
            <BLANKLINE>
              node_10 -> node_2 [color = "red"];
              node_10 -> node_6 [color = "blue"];
              node_11 -> node_3 [color = "red"];
              node_11 -> node_5 [color = "blue"];
              node_7 -> node_1 [color = "red"];
              node_7 -> node_8 [color = "blue"];
              node_4 -> node_0 [color = "red"];
              node_4 -> node_9 [color = "blue"];
            }

        By default ``graphviz`` renders digraphs using a hierarchical layout,
        ranking the vertices down from top to bottom. Here we specify
        alternative ranking directions for this layout::

            sage: D = DiGraph([(1, 2)])
            sage: print(D.graphviz_string(rankdir="up"))
            digraph {
              rankdir=BT
              node_0  [label="1"];
              node_1  [label="2"];
            <BLANKLINE>
              node_0 -> node_1;
            }
            sage: print(D.graphviz_string(rankdir="down"))
            digraph {
              node_0  [label="1"];
              node_1  [label="2"];
            <BLANKLINE>
              node_0 -> node_1;
            }
            sage: print(D.graphviz_string(rankdir="left"))
            digraph {
              rankdir=RL
              node_0  [label="1"];
              node_1  [label="2"];
            <BLANKLINE>
              node_0 -> node_1;
            }
            sage: print(D.graphviz_string(rankdir="right"))
            digraph {
              rankdir=LR
              node_0  [label="1"];
              node_1  [label="2"];
            <BLANKLINE>
              node_0 -> node_1;
            }

        Edge-specific options can also be specified by providing a function (or
        tuple thereof) which maps each edge to a dictionary of options. Valid
        options are

        - ``"color"``
        - ``"dot"`` (a string containing a sequence of options in ``dot`` format)
        - ``"label"`` (a string)
        - ``"label_style"`` (``"string"`` or ``"latex"``)
        - ``"edge_string"`` (``"--"`` or ``"->"``)
        - ``"dir"`` (``"forward"``, ``"back"``, ``"both"`` or ``"none"``)
        - ``"backward"`` (boolean), instead of defining the edge in the
          graphviz string as ``u -> v`` it draws it as ``v -> u
          [dir=back]`` and instead of ``u -> v [dir=back]`` it draws it as
          ``v -> u``, this changes the way it is drawn by Graphviz's dot
          program: vertex ``v`` will be *above* vertex ``u`` instead of
          below.

        Here we state that the graph should be laid out so that edges
        starting from ``1`` are going backward (e.g. going up instead of
        down)::

            sage: def edge_options(data):
            ....:     u, v, label = data
            ....:     return {"dir":"back"} if u == 1 else {}
            sage: print(G.graphviz_string(edge_options=edge_options))  # random             # optional - sage.symbolic
            digraph {
              node_0  [label="-1"];
              node_1  [label="-1/2"];
              node_2  [label="1/2"];
              node_3  [label="-2"];
              node_4  [label="1/4"];
              node_5  [label="-4"];
              node_6  [label="1/3"];
              node_7  [label="2/3"];
              node_8  [label="4/5"];
              node_9  [label="1"];
              node_10  [label="2"];
            <BLANKLINE>
              node_2 -> node_3;
              node_2 -> node_7;
              node_4 -> node_5;
              node_4 -> node_8;
              node_9 -> node_0 [dir=back];
              node_9 -> node_2 [dir=back];
              node_10 -> node_1;
              node_10 -> node_6;
            }

        We now test all options::

            sage: def edge_options(data):
            ....:     u, v, label = data
            ....:     options = {"color": {f: "red", g: "blue"}[label]}
            ....:     if (u,v) == (1/2, -2): options["label"]       = "coucou"; options["label_style"] = "string"
            ....:     if (u,v) == (1/2,2/3): options["dot"]         = "x=1,y=2"
            ....:     if (u,v) == (1,   -1): options["label_style"] = "latex"
            ....:     if (u,v) == (1,  1/2): options["dir"]         = "back"
            ....:     return options
            sage: print(G.graphviz_string(edge_options=edge_options))  # random             # optional - sage.symbolic
            digraph {
              node_0  [label="-1"];
              node_1  [label="-1/2"];
              node_2  [label="1/2"];
              node_3  [label="-2"];
              node_4  [label="1/4"];
              node_5  [label="-4"];
              node_6  [label="1/3"];
              node_7  [label="2/3"];
              node_8  [label="4/5"];
              node_9  [label="1"];
              node_10  [label="2"];
            <BLANKLINE>
              node_2 -> node_3 [label="coucou", color = "red"];
              node_2 -> node_7 [x=1,y=2, color = "blue"];
              node_4 -> node_5 [color = "red"];
              node_4 -> node_8 [color = "blue"];
              node_9 -> node_0 [label=" ", texlbl="$x \ {\mapsto}\ -\frac{1}{x}$", color = "red"];
              node_9 -> node_2 [color = "blue", dir=back];
              node_10 -> node_1 [color = "red"];
              node_10 -> node_6 [color = "blue"];
            }

        We test the possible values of the ``'dir'`` edge option::

            sage: edges = [(0,1,'a'), (1,2,'b'), (2,3,'c'), (3,4,'d')]
            sage: G = DiGraph(edges)
            sage: def edge_options(data):
            ....:     u,v,label = data
            ....:     if label == 'a': return {'dir':'forward'}
            ....:     if label == 'b': return {'dir':'back'}
            ....:     if label == 'c': return {'dir':'none'}
            ....:     if label == 'd': return {'dir':'both'}
            sage: print(G.graphviz_string(edge_options=edge_options))
            digraph {
              node_0  [label="0"];
              node_1  [label="1"];
              node_2  [label="2"];
              node_3  [label="3"];
              node_4  [label="4"];
            <BLANKLINE>
              node_0 -> node_1;
              node_1 -> node_2 [dir=back];
              node_2 -> node_3 [dir=none];
              node_3 -> node_4 [dir=both];
            }

        We test the same graph and ``'dir'`` edge options but with
        ``backward=True``, which reverses the natural direction
        each edge wants to be pointing for the layout::

            sage: def edge_options(data):
            ....:     u,v,label = data
            ....:     if label == 'a': return {'dir':'forward', 'backward':True}
            ....:     if label == 'b': return {'dir':'back', 'backward':True}
            ....:     if label == 'c': return {'dir':'none', 'backward':True}
            ....:     if label == 'd': return {'dir':'both', 'backward':True}
            sage: print(G.graphviz_string(edge_options=edge_options))
            digraph {
              node_0  [label="0"];
              node_1  [label="1"];
              node_2  [label="2"];
              node_3  [label="3"];
              node_4  [label="4"];
            <BLANKLINE>
              node_1 -> node_0 [dir=back];
              node_2 -> node_1;
              node_3 -> node_2 [dir=none];
              node_4 -> node_3 [dir=both];
            }

        TESTS:

        The following digraph has tuples as vertices::

            sage: print(DiGraph(graphs.Grid2dGraph(2,2)).graphviz_string())
            digraph {
              node_0  [label="(0, 0)"];
              node_1  [label="(0, 1)"];
              node_2  [label="(1, 0)"];
              node_3  [label="(1, 1)"];
            <BLANKLINE>
              node_0 -> node_1;
              node_0 -> node_2;
              node_1 -> node_0;
              node_1 -> node_3;
              node_2 -> node_0;
              node_2 -> node_3;
              node_3 -> node_1;
              node_3 -> node_2;
            }

        The following digraph has vertices with newlines in their string
        representations::

            sage: m1 = matrix(3, 3)
            sage: m2 = matrix(3, 3, 1)
            sage: m1.set_immutable()
            sage: m2.set_immutable()
            sage: g = DiGraph({m1: [m2]})
            sage: print(g.graphviz_string())
            digraph {
              node_0  [label="[0 0 0]\n\
            [0 0 0]\n\
            [0 0 0]"];
              node_1  [label="[1 0 0]\n\
            [0 1 0]\n\
            [0 0 1]"];
            <BLANKLINE>
              node_0 -> node_1;
            }

        Using cluster subgraphs::

            sage: d = {i: [i + 1] for i in range(5)}
            sage: G = Graph(d)
            sage: print(G.graphviz_string(subgraph_clusters=[[0, 2, 4], [1, 3, 5]]))
            graph {
              node_0  [label="0"];
              node_1  [label="1"];
              node_2  [label="2"];
              node_3  [label="3"];
              node_4  [label="4"];
              node_5  [label="5"];
            <BLANKLINE>
            subgraph cluster_0{style=filled;
            color=black;
            fillcolor=azure;
              node_0;
              node_2;
              node_4;
            }
            <BLANKLINE>
            subgraph cluster_1{style=filled;
            color=black;
            fillcolor=azure;
              node_1;
              node_3;
              node_5;
            }
            <BLANKLINE>
              node_0 -- node_1;
              node_1 -- node_2;
              node_2 -- node_3;
              node_3 -- node_4;
              node_4 -- node_5;
            }

        Check that :trac:`22950` is fixed::

            sage: D = DiGraph({1: [2]})
            sage: D.graphviz_string(edge_colors={'blue': [(1, 2)]})
            'digraph {\n  node_0  [label="1"];\n  node_1  [label="2"];\n\n
              node_0 -> node_1 [color = "blue"];\n}'

        Check that :trac:`25121` is fixed::

            sage: G = Graph([(0, 1)])
            sage: G.graphviz_string(edge_colors={(0.25, 0.5, 1.0): [(0, 1)]})
            'graph {\n  node_0  [label="0"];\n  node_1  [label="1"];\n\n  node_0 -- node_1 [color = "#4080ff"];\n}'

            sage: G = Graph([(0, 1)])
            sage: G.set_latex_options(edge_colors={(0, 1): (0.25, 0.5, 1.0)})
            sage: print(G.latex_options().dot2tex_picture()) # optional - dot2tex graphviz
            \begin{tikzpicture}[>=latex,line join=bevel,]
            ...
              \definecolor{strokecolor}{rgb}{0.25,0.5,1.0};
              \draw [strokecolor,] (node_0) ... (node_1);
            ...
            \end{tikzpicture}

        An error is raised if the value of the edge option ``dir`` is
        misspelled (:trac:`31381`)::

            sage: edges = [(0,1,'a'), (1,2,'b'), (2,3,'c'), (3,4,'d')]
            sage: G = DiGraph(edges)
            sage: def edge_options(data):
            ....:     u,v,label = data
            ....:     return {'dir':'forwward'} if label == 'a' else {}
            sage: _ = G.graphviz_string(edge_options=edge_options)
            Traceback (most recent call last):
            ...
            ValueError: dir(='forwward') in edge_options dict for the edge
            (0, 1) should be 'forward', 'back', 'both', or 'none'

        An error is raised if the value of the edge option ``edge_string``
        is invalid (:trac:`31381`)::

            sage: edges = [(0,1,'a'), (1,2,'b'), (2,3,'c'), (3,4,'d')]
            sage: G = DiGraph(edges)
            sage: def edge_options(data):
            ....:     u,v,label = data
            ....:     return {'edge_string':'<-'} if label == 'a' else {}
            sage: _ = G.graphviz_string(edge_options=edge_options)
            Traceback (most recent call last):
            ...
            ValueError: edge_string(='<-') in edge_options dict for the edge
            (0, 1) should be '--' or '->'
        """
        from sage.graphs.dot2tex_utils import quoted_latex, quoted_str

        if self.is_directed():
            graph_string = "digraph"
            default_edge_string = "->"
            default_edge_dir = "forward"
        else:
            graph_string = "graph"
            default_edge_string = "--"
            default_edge_dir = "none"

        edge_option_functions = options['edge_options']
        if not isinstance(edge_option_functions, (tuple, list)):
            edge_option_functions = [edge_option_functions]
        else:
            edge_option_functions = list(edge_option_functions)

        if options['edge_color'] is not None:
            default_color = options['edge_color']
        else:
            default_color = None

        if options['color_by_label'] is not False:
            color_by_label = self._color_by_label(format=options['color_by_label'], as_function=True, default_color=default_color)
            edge_option_functions.append(lambda u_v_label: {"color": color_by_label(u_v_label[2])})
        elif options['edge_colors'] is not None:
            if not isinstance(options['edge_colors'], dict):
                raise ValueError("incorrect format for edge_colors")
            color_by_edge = {}
            for color in options['edge_colors'].keys():
                for edge in options['edge_colors'][color]:
                    assert isinstance(edge, (list, tuple)) and len(edge) >= 2 and len(edge) <= 3,\
                        "%s is not a valid format for edge" % (edge)
                    u = edge[0]
                    v = edge[1]
                    assert self.has_edge(*edge), "%s is not an edge" % (edge)
                    if len(edge) == 2:
                        if self.has_multiple_edges():
                            for label in self.edge_label(u, v):
                                color_by_edge[(u, v, label)] = color
                        else:
                            label = self.edge_label(u, v)
                            color_by_edge[(u, v, label)] = color
                    elif len(edge) == 3:
                        color_by_edge[edge] = color

            edge_option_functions.append(lambda edge: {"color": color_by_edge[edge]} if edge in color_by_edge else {})

        key = self._keys_for_vertices()

        s = '%s {\n' % graph_string
        if options['rankdir'] != "down":
            directions = {'up': 'BT', 'down': 'TB', 'left': 'RL', 'right': 'LR'}
            if options['rankdir'] not in directions:
                raise ValueError("rankdir should be one of %s" % directions.keys())
            s += '  rankdir=%s\n' % (directions[options['rankdir']])
        if (options['vertex_labels'] and
                options['labels'] == "latex"):  # not a perfect option name
            # TODO: why do we set this only for latex labels?
            s += '  node [shape="plaintext"];\n'

        # vertices for loop
        for v in self:
            if not options['vertex_labels']:
                node_options = ""
            elif options['labels'] == "latex":
                node_options = " [label=\" \", texlbl=\"$%s$\"]" % quoted_latex(v)
            else:
                node_options = " [label=\"%s\"]" % quoted_str(v)

            s += '  %s %s;\n' % (key(v), node_options)
        s += "\n"

        # subgraphs clusters for loop
        subgraph_clusters = options['subgraph_clusters']
        for i, cluster in enumerate(subgraph_clusters):
            s += 'subgraph cluster_%s{style=filled;\n' % i
            s += 'color=black;\n'
            s += 'fillcolor=azure;\n'
            for v in cluster:
                s += '  %s;\n' % key(v)
            s += '}\n\n'

        if default_color is not None:
            s += 'edge [color="%s"];\n' % default_color

        # edges for loop
        for u, v, label in self.edge_iterator():
            edge_options = {
                'dir': default_edge_dir,
                'backward': False,
                'dot': None,
                'edge_string': default_edge_string,
                'color' : default_color,
                'label' : label,
                'label_style': options['labels'] if options['edge_labels'] else None
                }
            for f in edge_option_functions:
                edge_options.update(f((u, v, label)))

            if not edge_options['edge_string'] in ['--', '->']:
                raise ValueError("edge_string(='{}') in edge_options dict for "
                                 "the edge ({}, {}) should be '--' or '->'"
                                 .format(edge_options['edge_string'], u, v))

            dot_options = []

            if edge_options['dot'] is not None:
                assert isinstance(edge_options['dot'], str)
                dot_options.append(edge_options['dot'])

            label = edge_options['label']
            if label is not None and edge_options['label_style'] is not None:
                if edge_options['label_style'] == 'latex':
                    dot_options.append('label=" ", texlbl="$%s$"' % quoted_latex(label))
                else:
                    dot_options.append('label="%s"' % label)

            if edge_options['color'] != default_color:
                col = edge_options['color']
                if isinstance(col, (tuple, list)):
                    # convert RGB triples in hexadecimal
                    col = str(to_hex(col, keep_alpha=False))

                dot_options.append('color = "%s"' % col)

            if edge_options['backward']:
                u, v = v, u
                if edge_options['dir'] == 'forward':
                    edge_options['dir'] = 'back'
                elif edge_options['dir'] == 'back':
                    edge_options['dir'] = 'forward'

            if edge_options['dir'] == default_edge_dir:
                pass
            elif edge_options['dir'] in ['forward', 'back', 'both', 'none']:
                dot_options.append('dir={}'.format(edge_options['dir']))
            else:
                raise ValueError("dir(='{}') in edge_options dict for the"
                                 " edge ({}, {}) should be 'forward', 'back',"
                                 " 'both', or 'none'"
                                 .format(edge_options['dir'], u, v))

            s += '  %s %s %s' % (key(u), edge_options['edge_string'], key(v))
            if dot_options:
                s += " [" + ", ".join(dot_options)+"]"
            s += ";\n"
        s += "}"

        return s

    def graphviz_to_file_named(self, filename, **options):
        r"""
        Write a representation in the ``dot`` language in a file.

        The ``dot`` language is a plaintext format for graph structures. See the
        documentation of :meth:`.graphviz_string` for available options.

        INPUT:

        - ``filename`` -- the name of the file to write in

        - ``**options`` -- options for the graphviz string

        EXAMPLES::

            sage: G = Graph({0: {1: None, 2: None}, 1: {0: None, 2: None}, 2: {0: None, 1: None, 3: 'foo'}, 3: {2: 'foo'}}, sparse=True)
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile(mode="a+t") as f:
            ....:     G.graphviz_to_file_named(f.name, edge_labels=True)
            ....:     print(f.read())
            graph {
              node_0  [label="0"];
              node_1  [label="1"];
              node_2  [label="2"];
              node_3  [label="3"];
            <BLANKLINE>
              node_0 -- node_1;
              node_0 -- node_2;
              node_1 -- node_2;
              node_2 -- node_3 [label="foo"];
            }
        """
        with open(filename, 'wt') as file:
            file.write(self.graphviz_string(**options))

    # Spectrum

    def spectrum(self, laplacian=False):
        r"""
        Return a list of the eigenvalues of the adjacency matrix.

        INPUT:

        - ``laplacian`` -- boolean (default: ``False``); if ``True``, use the
          Laplacian matrix (see :meth:`kirchhoff_matrix`)

        OUTPUT:

        A list of the eigenvalues, including multiplicities, sorted with the
        largest eigenvalue first.

        .. SEEALSO::

            The method :meth:`spectral_radius` returns floating point
            approximation of the maximum eigenvalue.

        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: P.spectrum()
            [3, 1, 1, 1, 1, 1, -2, -2, -2, -2]
            sage: P.spectrum(laplacian=True)
            [5, 5, 5, 5, 2, 2, 2, 2, 2, 0]
            sage: D = P.to_directed()
            sage: D.delete_edge(7, 9)
            sage: D.spectrum()
            [2.9032119259..., 1, 1, 1, 1, 0.8060634335..., -1.7092753594..., -2, -2, -2]

        ::

            sage: C = graphs.CycleGraph(8)
            sage: C.spectrum()
            [2, 1.4142135623..., 1.4142135623..., 0, 0, -1.4142135623..., -1.4142135623..., -2]

        A digraph may have complex eigenvalues. Previously, the complex parts of
        graph eigenvalues were being dropped. For a 3-cycle, we have::

            sage: T = DiGraph({0: [1], 1: [2], 2: [0]})
            sage: T.spectrum()
            [1, -0.5000000000... + 0.8660254037...*I, -0.5000000000... - 0.8660254037...*I]

        TESTS:

        The Laplacian matrix of a graph is the negative of the adjacency matrix
        with the degree of each vertex on the diagonal.  So for a regular graph,
        if `\delta` is an eigenvalue of a regular graph of degree `r`, then
        `r-\delta` will be an eigenvalue of the Laplacian.  The
        Hoffman-Singleton graph is regular of degree 7, so the following will
        test both the Laplacian construction and the computation of
        eigenvalues. ::

            sage: H = graphs.HoffmanSingletonGraph()
            sage: evals = H.spectrum()
            sage: lap = [7 - x for x in evals]
            sage: lap.sort(reverse=True)
            sage: lap == H.spectrum(laplacian=True)
            True
        """
        # Ideally the spectrum should return something like a Factorization object
        # containing each eigenvalue once, along with its multiplicity.
        # This function, returning a list. could then just be renamed "eigenvalues"
        vertices = list(self)
        if laplacian:
            M = self.kirchhoff_matrix(vertices=vertices)
        else:
            M = self.adjacency_matrix(vertices=vertices)
        evals = M.eigenvalues()
        evals.sort(reverse=True)
        return evals

    def characteristic_polynomial(self, var='x', laplacian=False):
        r"""
        Return the characteristic polynomial of the adjacency matrix of the
        (di)graph.

        Let `G` be a (simple) graph with adjacency matrix `A`. Let `I` be the
        identity matrix of dimensions the same as `A`. The characteristic
        polynomial of `G` is defined as the determinant `\det(xI - A)`.

        .. NOTE::

            ``characteristic_polynomial`` and ``charpoly`` are aliases and thus
            provide exactly the same method.

        INPUT:

        - ``x`` -- (default: ``'x'``); the variable of the characteristic
          polynomial

        - ``laplacian`` -- boolean (default: ``False``); if ``True``, use the
          Laplacian matrix

        .. SEEALSO::

            - :meth:`kirchhoff_matrix`

            - :meth:`laplacian_matrix`

        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: P.characteristic_polynomial()
            x^10 - 15*x^8 + 75*x^6 - 24*x^5 - 165*x^4 + 120*x^3 + 120*x^2 - 160*x + 48
            sage: P.charpoly()
            x^10 - 15*x^8 + 75*x^6 - 24*x^5 - 165*x^4 + 120*x^3 + 120*x^2 - 160*x + 48
            sage: P.characteristic_polynomial(laplacian=True)
            x^10 - 30*x^9 + 390*x^8 - 2880*x^7 + 13305*x^6 -
            39882*x^5 + 77640*x^4 - 94800*x^3 + 66000*x^2 - 20000*x
        """
        if laplacian:
            return self.kirchhoff_matrix(vertices=list(self)).charpoly(var=var)
        else:
            return self.adjacency_matrix(vertices=list(self)).charpoly(var=var)

    # alias, consistent with linear algebra code
    charpoly = characteristic_polynomial

    def eigenvectors(self, laplacian=False):
        r"""
        Return the *right* eigenvectors of the adjacency matrix of the graph.

        INPUT:

        - ``laplacian`` -- boolean (default: ``False``); if ``True``, use the
          Laplacian matrix (see :meth:`kirchhoff_matrix`)

        OUTPUT:

        A list of triples.  Each triple begins with an eigenvalue of the
        adjacency matrix of the graph.  This is followed by a list of
        eigenvectors for the eigenvalue, when the eigenvectors are placed on the
        right side of the matrix.  Together, the eigenvectors form a basis for
        the eigenspace.  The triple concludes with the algebraic multiplicity of
        the eigenvalue.

        For some graphs, the exact eigenspaces provided by :meth:`eigenspaces`
        provide additional insight into the structure of the eigenspaces.

        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: P.eigenvectors()
            [(3, [
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
            ], 1), (-2, [
            (1, 0, 0, 0, -1, -1, -1, 0, 1, 1),
            (0, 1, 0, 0, -1, 0, -2, -1, 1, 2),
            (0, 0, 1, 0, -1, 1, -1, -2, 0, 2),
            (0, 0, 0, 1, -1, 1, 0, -1, -1, 1)
            ], 4), (1, [
            (1, 0, 0, 0, 0, 1, -1, 0, 0, -1),
            (0, 1, 0, 0, 0, -1, 1, -1, 0, 0),
            (0, 0, 1, 0, 0, 0, -1, 1, -1, 0),
            (0, 0, 0, 1, 0, 0, 0, -1, 1, -1),
            (0, 0, 0, 0, 1, -1, 0, 0, -1, 1)
            ], 5)]

        Eigenspaces for the Laplacian should be identical since the Petersen
        graph is regular.  However, since the output also contains the
        eigenvalues, the two outputs are slightly different::

            sage: P.eigenvectors(laplacian=True)
            [(0, [
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
            ], 1), (5, [
            (1, 0, 0, 0, -1, -1, -1, 0, 1, 1),
            (0, 1, 0, 0, -1, 0, -2, -1, 1, 2),
            (0, 0, 1, 0, -1, 1, -1, -2, 0, 2),
            (0, 0, 0, 1, -1, 1, 0, -1, -1, 1)
            ], 4), (2, [
            (1, 0, 0, 0, 0, 1, -1, 0, 0, -1),
            (0, 1, 0, 0, 0, -1, 1, -1, 0, 0),
            (0, 0, 1, 0, 0, 0, -1, 1, -1, 0),
            (0, 0, 0, 1, 0, 0, 0, -1, 1, -1),
            (0, 0, 0, 0, 1, -1, 0, 0, -1, 1)
            ], 5)]

        ::

            sage: C = graphs.CycleGraph(8)
            sage: C.eigenvectors()
            [(2,
              [
              (1, 1, 1, 1, 1, 1, 1, 1)
              ],
              1),
             (-2,
              [
              (1, -1, 1, -1, 1, -1, 1, -1)
              ],
              1),
             (0,
              [
              (1, 0, -1, 0, 1, 0, -1, 0),
              (0, 1, 0, -1, 0, 1, 0, -1)
              ],
              2),
             (-1.4142135623...,
              [(1, 0, -1, 1.4142135623..., -1, 0, 1, -1.4142135623...),
               (0, 1, -1.4142135623..., 1, 0, -1, 1.4142135623..., -1)],
              2),
             (1.4142135623...,
              [(1, 0, -1, -1.4142135623..., -1, 0, 1, 1.4142135623...),
               (0, 1, 1.4142135623..., 1, 0, -1, -1.4142135623..., -1)],
              2)]

        A digraph may have complex eigenvalues. Previously, the complex parts of
        graph eigenvalues were being dropped. For a 3-cycle, we have::

            sage: T = DiGraph({0:[1], 1:[2], 2:[0]})
            sage: T.eigenvectors()
            [(1,
              [
              (1, 1, 1)
              ],
              1),
             (-0.5000000000... - 0.8660254037...*I,
              [(1, -0.5000000000... - 0.8660254037...*I, -0.5000000000... + 0.8660254037...*I)],
              1),
             (-0.5000000000... + 0.8660254037...*I,
              [(1, -0.5000000000... + 0.8660254037...*I, -0.5000000000... - 0.8660254037...*I)],
              1)]
        """
        if laplacian:
            M = self.kirchhoff_matrix(vertices=list(self))
        else:
            M = self.adjacency_matrix(vertices=list(self))
        return M.right_eigenvectors()

    def eigenspaces(self, laplacian=False):
        r"""
        Return the *right* eigenspaces of the adjacency matrix of the graph.

        INPUT:

        - ``laplacian`` -- boolean (default: ``False``); if ``True``, use the
           Laplacian matrix (see :meth:`kirchhoff_matrix`)

        OUTPUT:

        A list of pairs.  Each pair is an eigenvalue of the adjacency matrix of
        the graph, followed by the vector space that is the eigenspace for that
        eigenvalue, when the eigenvectors are placed on the right of the matrix.

        For some graphs, some of the eigenspaces are described exactly by vector
        spaces over a :func:`~sage.rings.number_field.number_field.NumberField`.
        For numerical eigenvectors use :meth:`eigenvectors`.

        EXAMPLES::

            sage: P = graphs.PetersenGraph()
            sage: P.eigenspaces()
            [
            (3, Vector space of degree 10 and dimension 1 over Rational Field
            User basis matrix:
            [1 1 1 1 1 1 1 1 1 1]),
            (-2, Vector space of degree 10 and dimension 4 over Rational Field
            User basis matrix:
            [ 1  0  0  0 -1 -1 -1  0  1  1]
            [ 0  1  0  0 -1  0 -2 -1  1  2]
            [ 0  0  1  0 -1  1 -1 -2  0  2]
            [ 0  0  0  1 -1  1  0 -1 -1  1]),
            (1, Vector space of degree 10 and dimension 5 over Rational Field
            User basis matrix:
            [ 1  0  0  0  0  1 -1  0  0 -1]
            [ 0  1  0  0  0 -1  1 -1  0  0]
            [ 0  0  1  0  0  0 -1  1 -1  0]
            [ 0  0  0  1  0  0  0 -1  1 -1]
            [ 0  0  0  0  1 -1  0  0 -1  1])
            ]

        Eigenspaces for the Laplacian should be identical since the Petersen
        graph is regular.  However, since the output also contains the
        eigenvalues, the two outputs are slightly different::

            sage: P.eigenspaces(laplacian=True)
            [
            (0, Vector space of degree 10 and dimension 1 over Rational Field
            User basis matrix:
            [1 1 1 1 1 1 1 1 1 1]),
            (5, Vector space of degree 10 and dimension 4 over Rational Field
            User basis matrix:
            [ 1  0  0  0 -1 -1 -1  0  1  1]
            [ 0  1  0  0 -1  0 -2 -1  1  2]
            [ 0  0  1  0 -1  1 -1 -2  0  2]
            [ 0  0  0  1 -1  1  0 -1 -1  1]),
            (2, Vector space of degree 10 and dimension 5 over Rational Field
            User basis matrix:
            [ 1  0  0  0  0  1 -1  0  0 -1]
            [ 0  1  0  0  0 -1  1 -1  0  0]
            [ 0  0  1  0  0  0 -1  1 -1  0]
            [ 0  0  0  1  0  0  0 -1  1 -1]
            [ 0  0  0  0  1 -1  0  0 -1  1])
            ]

        Notice how one eigenspace below is described with a square root of 2.
        For the two possible values (positive and negative) there is a
        corresponding eigenspace::

            sage: C = graphs.CycleGraph(8)
            sage: C.eigenspaces()
            [
            (2, Vector space of degree 8 and dimension 1 over Rational Field
            User basis matrix:
            [1 1 1 1 1 1 1 1]),
            (-2, Vector space of degree 8 and dimension 1 over Rational Field
            User basis matrix:
            [ 1 -1  1 -1  1 -1  1 -1]),
            (0, Vector space of degree 8 and dimension 2 over Rational Field
            User basis matrix:
            [ 1  0 -1  0  1  0 -1  0]
            [ 0  1  0 -1  0  1  0 -1]),
            (a3, Vector space of degree 8 and dimension 2 over Number Field in a3 with defining polynomial x^2 - 2
            User basis matrix:
            [  1   0  -1 -a3  -1   0   1  a3]
            [  0   1  a3   1   0  -1 -a3  -1])
            ]

        A digraph may have complex eigenvalues and eigenvectors. For a 3-cycle,
        we have::

            sage: T = DiGraph({0: [1], 1: [2], 2: [0]})
            sage: T.eigenspaces()
            [
            (1, Vector space of degree 3 and dimension 1 over Rational Field
            User basis matrix:
            [1 1 1]),
            (a1, Vector space of degree 3 and dimension 1 over Number Field in a1 with defining polynomial x^2 + x + 1
            User basis matrix:
            [      1      a1 -a1 - 1])
            ]
        """
        if laplacian:
            M = self.kirchhoff_matrix(vertices=list(self))
        else:
            M = self.adjacency_matrix(vertices=list(self))
        # could pass format='all' to get QQbar eigenvalues and eigenspaces
        # which would be a change in default behavior
        return M.right_eigenspaces(format='galois', algebraic_multiplicity=False)

    # Automorphism and isomorphism

    def relabel(self, perm=None, inplace=True, return_map=False, check_input=True, complete_partial_function=True, immutable=None):
        r"""
        Relabels the vertices of ``self``

        INPUT:

         - ``perm`` -- a function, dictionary, iterable, permutation, or
           ``None`` (default: ``None``)

         - ``inplace`` -- a boolean (default: ``True``)

         - ``return_map`` -- a boolean (default: ``False``)

         - ``check_input`` (boolean) -- whether to test input for
           correctness. *This can potentially be very time-consuming !*.

         - ``complete_partial_function`` (boolean) -- whether to automatically
           complete the permutation if some elements of the graph are not
           associated with any new name. In this case, those elements are not
           relabeled *This can potentially be very time-consuming !*.

         - ``immutable`` (boolean) -- with ``inplace=False``, whether to create
           a mutable/immutable relabelled copy. ``immutable=None`` (default)
           means that the graph and its copy will behave the same way.

        If ``perm`` is a function ``f``, then each vertex ``v`` is
        relabeled to ``f(v)``.

        If ``perm`` is a dictionary ``d``, then each vertex ``v`` (which should
        be a key of ``d``) is relabeled to ``d[v]``.

        If ``perm`` is a list (or more generally, any iterable) of
        length ``n``, then the first vertex returned by
        ``G.vertices(sort=True)``
        is relabeled to ``l[0]``, the second to ``l[1]``, ...

        If ``perm`` is a permutation, then each vertex ``v`` is
        relabeled to ``perm(v)``. Caveat: this assumes that the
        vertices are labelled `\{0,1,...,n-1\}`; since permutations
        act by default on the set `\{1,2,...,n\}`, this is achieved by
        identifying `n` and `0`.

        If ``perm`` is ``None``, the graph is relabeled to be on the
        vertices `\{0,1,...,n-1\}`. This is *not* any kind of canonical
        labeling, but it is consistent (relabeling twice will give the
        same result).

        If ``inplace`` is ``True``, the graph is modified in place and
        ``None`` is returned. Otherwise a relabeled copy of the graph
        is returned.

        If ``return_map`` is ``True`` a dictionary representing the
        relabelling map is returned (incompatible with ``inplace==False``).

        EXAMPLES::

            sage: G = graphs.PathGraph(3)
            sage: G.am()
            [0 1 0]
            [1 0 1]
            [0 1 0]

        Relabeling using a dictionary. Note that the dictionary does not define
        the new label of vertex `0`::

            sage: G.relabel({1:2,2:1}, inplace=False).am()
            [0 0 1]
            [0 0 1]
            [1 1 0]

        This is because the method automatically "extends" the relabeling to the
        missing vertices (whose label will not change). Checking that all
        vertices have an image can require some time, and this feature can be
        disabled (at your own risk)::

            sage: G.relabel({1:2,2:1}, inplace=False, complete_partial_function = False).am()
            Traceback (most recent call last):
            ...
            KeyError: 0

        Relabeling using a list::

            sage: G.relabel([0,2,1], inplace=False).am()
            [0 0 1]
            [0 0 1]
            [1 1 0]

        Relabeling using an iterable::

            sage: G.relabel(iter((0,2,1)), inplace=False).am()
            [0 0 1]
            [0 0 1]
            [1 1 0]

        Relabeling using a Sage permutation::

            sage: G = graphs.PathGraph(3)
            sage: from sage.groups.perm_gps.permgroup_named import SymmetricGroup               # optional - sage.groups
            sage: S = SymmetricGroup(3)                                                         # optional - sage.groups
            sage: gamma = S('(1,2)')                                                            # optional - sage.groups
            sage: G.relabel(gamma, inplace=False).am()                                          # optional - sage.groups
            [0 0 1]
            [0 0 1]
            [1 1 0]

        A way to get a random relabeling::

            sage: set_random_seed(0)  # Results are reproducible
            sage: D = DiGraph({1: [2], 3: [4]})
            sage: D.relabel(Permutations(D.vertices(sort=True)).random_element())
            sage: D.sources()
            [1, 4]

        Relabeling using an injective function::

            sage: G.edges(sort=True)
            [(0, 1, None), (1, 2, None)]
            sage: H = G.relabel(lambda i: i+10, inplace=False)
            sage: H.vertices(sort=True)
            [10, 11, 12]
            sage: H.edges(sort=True)
            [(10, 11, None), (11, 12, None)]

        Relabeling using a non injective function has no meaning::

            sage: G.edges(sort=True)
            [(0, 1, None), (1, 2, None)]
            sage: G.relabel(lambda i: 0, inplace=False)
            Traceback (most recent call last):
            ...
            NotImplementedError: Non injective relabeling

        But this test can be disabled, which can lead to ... problems::

            sage: G.edges(sort=True)
            [(0, 1, None), (1, 2, None)]
            sage: G.relabel(lambda i: 0, check_input = False)
            sage: G.edges(sort=True)
            []

        Recovering the relabeling with ``return_map``::

            sage: G = graphs.CubeGraph(3)
            sage: G.relabel(range(8), return_map=True)
            {'000': 0,
             '001': 1,
             '010': 2,
             '011': 3,
             '100': 4,
             '101': 5,
             '110': 6,
             '111': 7}

        When no permutation is given, the relabeling is done to integers
        from 0 to N-1 but in an arbitrary order::

            sage: G = graphs.CubeGraph(3)
            sage: G.vertices(sort=True)
            ['000', '001', '010', '011', '100', '101', '110', '111']
            sage: G.relabel()
            sage: G.vertices(sort=True)
            [0, 1, 2, 3, 4, 5, 6, 7]

        In the above case, the mapping is arbitrary but consistent::

            sage: map1 = G.relabel(inplace=False, return_map=True)
            sage: map2 = G.relabel(inplace=False, return_map=True)
            sage: map1 == map2
            True

        ::

            sage: G = graphs.PathGraph(3)
            sage: G.relabel(lambda i: i+10, return_map=True)
            {0: 10, 1: 11, 2: 12}

        TESTS::

            sage: P = Graph(graphs.PetersenGraph())
            sage: P.delete_edge([0,1])
            sage: P.add_edge((4,5))
            sage: P.add_edge((2,6))
            sage: P.delete_vertices([0,1])
            sage: P.relabel()

        The attributes are properly updated too::

            sage: G = graphs.PathGraph(5)
            sage: G.set_vertices({0: 'before', 1: 'delete', 2: 'after'})
            sage: G.delete_vertex(1)
            sage: G.relabel()
            sage: G.get_vertices()
            {0: 'before', 1: 'after', 2: None, 3: None}
            sage: G.get_pos()
            {0: (0, 0), 1: (2, 0), 2: (3, 0), 3: (4, 0)}

        Check that :trac:`12477` is fixed::

            sage: g = Graph({1:[2,3]})
            sage: rel = {1:'a', 2:'b'}
            sage: g.relabel(rel)
            sage: set(g) == {3, 'a', 'b'}
            True
            sage: rel
            {1: 'a', 2: 'b'}

        Immutable graphs cannot be relabeled::

            sage: Graph(graphs.PetersenGraph(), immutable=True).relabel({})
            Traceback (most recent call last):
            ...
            ValueError: To relabel an immutable graph use inplace=False

        :trac:`16257`::

            sage: G = graphs.PetersenGraph()
            sage: G.relabel( [ i+1 for i in range(G.order()) ], inplace=True )
            sage: G.relabel( [ i+1 for i in range(G.order()) ], inplace=True )
        """
        from sage.groups.perm_gps.permgroup_element import PermutationGroupElement

        if not inplace:
            G = copy(self)
            perm2 = G.relabel(perm,
                              return_map=return_map,
                              check_input=check_input,
                              complete_partial_function=complete_partial_function)

            if immutable is None:
                immutable = self.is_immutable()
            if immutable:
                G = self.__class__(G, immutable=True)

            if return_map:
                return G, perm2
            else:
                return G

        if immutable:
            raise ValueError("To make an immutable copy use inplace=False")

        if self.is_immutable():
            raise ValueError("To relabel an immutable graph use inplace=False")

        # If perm is not a dictionary, we build one !

        if perm is None:
            # enumerate(self) guarantees a consistent but otherwise
            # arbitrary relabeling
            perm = {v: i for i, v in enumerate(self)}
            complete_partial_function = False
            check_input = False

        elif isinstance(perm, dict):
            # If all vertices do not have a new label, the code will touch the
            # dictionary. Let us keep the one we received from the user clean !
            perm = dict(perm)

        elif isinstance(perm, PermutationGroupElement):
            n = self.order()
            ddict = {}
            for i in range(1, n):
                ddict[i] = perm(i) % n
            if n > 0:
                ddict[0] = perm(n) % n
            perm = ddict

        else:
            # Check for generic iterable/callable
            try:
                it = iter(perm)
            except TypeError:
                if not callable(perm):
                    raise
                # callable
                perm = {v: perm(v) for v in self}
                complete_partial_function = False
            else:
                # iterable
                perm = dict(zip(self.vertices(sort=True), it))

        # Whether to complete the relabeling function if some vertices do not
        # appear in the permutation.
        if complete_partial_function:
            for v in self:
                if v not in perm:
                    perm[v] = v

        # Whether to check input
        if check_input:
            if len(set(perm.values())) < len(perm):
                raise NotImplementedError("Non injective relabeling")

            # Check hashability of values
            for t in perm.values():
                hash(t)

        embedding = self.get_embedding()
        if embedding is not None:
            self._embedding = {perm[u]: [perm[v] for v in neighbors] for u, neighbors in embedding.items()}
        pos = self.get_pos()
        if pos is not None:
            self._pos = {perm[u]: x for u, x in pos.items()}
        pos3d = self.get_pos(dim=3)
        if pos3d is not None:
            self._pos3d = {perm[u]: x for u, x in pos3d.items()}
        try:
            assoc = self._assoc
        except AttributeError:
            assoc = None
        if assoc is not None:
            self._assoc = {perm[v]: value for v, value in assoc.items()}

        self._backend.relabel(perm, self._directed)

        if return_map:
            return perm

    def degree_to_cell(self, vertex, cell):
        """
        Returns the number of edges from vertex to an edge in cell. In the
        case of a digraph, returns a tuple (in_degree, out_degree).

        EXAMPLES::

            sage: G = graphs.CubeGraph(3)
            sage: cell = G.vertices(sort=True)[:3]
            sage: G.degree_to_cell('011', cell)
            2
            sage: G.degree_to_cell('111', cell)
            0

        ::

            sage: D = DiGraph({ 0:[1,2,3], 1:[3,4], 3:[4,5]})
            sage: cell = [0,1,2]
            sage: D.degree_to_cell(5, cell)
            (0, 0)
            sage: D.degree_to_cell(3, cell)
            (2, 0)
            sage: D.degree_to_cell(0, cell)
            (0, 2)
        """
        if self._directed:
            in_neighbors_in_cell = set([a for a, _, _ in self.incoming_edges(vertex)]) & set(cell)
            out_neighbors_in_cell = set([a for _, a, _ in self.outgoing_edges(vertex)]) & set(cell)
            return (len(in_neighbors_in_cell), len(out_neighbors_in_cell))
        else:
            neighbors_in_cell = set(self.neighbors(vertex)) & set(cell)
            return len(neighbors_in_cell)

    def is_equitable(self, partition, quotient_matrix=False):
        """
        Checks whether the given partition is equitable with respect to
        self.

        A partition is equitable with respect to a graph if for every pair
        of cells C1, C2 of the partition, the number of edges from a vertex
        of C1 to C2 is the same, over all vertices in C1.

        INPUT:


        -  ``partition`` - a list of lists

        -  ``quotient_matrix`` - (default False) if True, and
           the partition is equitable, returns a matrix over the integers
           whose rows and columns represent cells of the partition, and whose
           i,j entry is the number of vertices in cell j adjacent to each
           vertex in cell i (since the partition is equitable, this is well
           defined)


        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: G.is_equitable([[0,4],[1,3,5,9],[2,6,8],[7]])
            False
            sage: G.is_equitable([[0,4],[1,3,5,9],[2,6,8,7]])
            True
            sage: G.is_equitable([[0,4],[1,3,5,9],[2,6,8,7]], quotient_matrix=True)
            [1 2 0]
            [1 0 2]
            [0 2 1]

        ::

            sage: ss = (graphs.WheelGraph(6)).line_graph(labels=False)
            sage: prt = [[(0, 1)], [(0, 2), (0, 3), (0, 4), (1, 2), (1, 4)], [(2, 3), (3, 4)]]

        ::

            sage: ss.is_equitable(prt)
            Traceback (most recent call last):
            ...
            TypeError: Partition ([[(0, 1)], [(0, 2), (0, 3), (0, 4), (1, 2), (1, 4)], [(2, 3), (3, 4)]]) is not valid for this graph: vertices are incorrect.

        ::

            sage: ss = (graphs.WheelGraph(5)).line_graph(labels=False)
            sage: ss.is_equitable(prt)
            False
        """
        from sage.misc.flatten import flatten
        if sorted(flatten(partition, max_level=1)) != self.vertices(sort=True):
            raise TypeError("Partition (%s) is not valid for this graph: vertices are incorrect." % partition)
        if any(not cell for cell in partition):
            raise TypeError("Partition (%s) is not valid for this graph: there is a cell of length 0." % partition)
        if quotient_matrix:
            from sage.matrix.constructor import Matrix
            from sage.rings.integer_ring import IntegerRing
            n = len(partition)
            M = Matrix(IntegerRing(), n)
            for i in range(n):
                for j in range(n):
                    cell_i = partition[i]
                    cell_j = partition[j]
                    degrees = [self.degree_to_cell(u, cell_j) for u in cell_i]
                    if len(set(degrees)) > 1:
                        return False
                    if self._directed:
                        M[i, j] = degrees[0][0]
                    else:
                        M[i, j] = degrees[0]
            return M
        else:
            for cell1 in partition:
                for cell2 in partition:
                    degrees = [self.degree_to_cell(u, cell2) for u in cell1]
                    if len(set(degrees)) > 1:
                        return False
            return True

    def coarsest_equitable_refinement(self, partition, sparse=True):
        r"""
        Return the coarsest partition which is finer than the input
        partition, and equitable with respect to self.

        A partition is equitable with respect to a graph if for every pair of
        cells `C_1`, `C_2` of the partition, the number of edges from a vertex
        of `C_1` to `C_2` is the same, over all vertices in `C_1`.

        A partition `P_1` is finer than `P_2` (`P_2` is coarser than `P_1`) if
        every cell of `P_1` is a subset of a cell of `P_2`.

        INPUT:

        -  ``partition`` -- a list of lists

        - ``sparse`` -- boolean (default: ``False``); whether to use sparse or
           dense representation - for small graphs, use dense for speed

        EXAMPLES::

            sage: G = graphs.PetersenGraph()
            sage: G.coarsest_equitable_refinement([[0],list(range(1,10))])
            [[0], [2, 3, 6, 7, 8, 9], [1, 4, 5]]
            sage: G = graphs.CubeGraph(3)
            sage: verts = G.vertices(sort=True)
            sage: Pi = [verts[:1], verts[1:]]
            sage: Pi
            [['000'], ['001', '010', '011', '100', '101', '110', '111']]
            sage: [sorted(cell) for cell in G.coarsest_equitable_refinement(Pi)]
            [['000'], ['011', '101', '110'], ['111'], ['001', '010', '100']]

        Note that given an equitable partition, this function returns that
        partition::

            sage: P = graphs.PetersenGraph()
            sage: prt = [[0], [1, 4, 5], [2, 3, 6, 7, 8, 9]]
            sage: P.coarsest_equitable_refinement(prt)
            [[0], [1, 4, 5], [2, 3, 6, 7, 8, 9]]

        ::

            sage: ss = (graphs.WheelGraph(6)).line_graph(labels=False)
            sage: prt = [[(0, 1)], [(0, 2), (0, 3), (0, 4), (1, 2), (1, 4)], [(2, 3), (3, 4)]]
            sage: ss.coarsest_equitable_refinement(prt)
            Traceback (most recent call last):
            ...
            TypeError: partition ([[(0, 1)], [(0, 2), (0, 3), (0, 4), (1, 2), (1, 4)], [(2, 3), (3, 4)]]) is not valid for this graph: vertices are incorrect

        ::

            sage: ss = (graphs.WheelGraph(5)).line_graph(labels=False)
            sage: ss.coarsest_equitable_refinement(prt)
            [[(0, 1)], [(1, 2), (1, 4)], [(0, 3)], [(0, 4), (0, 2)], [(2, 3), (3, 4)]]

        ALGORITHM: Brendan D. McKay's Master's Thesis, University of
        Melbourne, 1976.
        """
        from sage.misc.flatten import flatten
        if set(flatten(partition, max_level=1)) != set(self):
            raise TypeError("partition (%s) is not valid for this graph: vertices are incorrect" % partition)
        if any(len(cell) == 0 for cell in partition):
            raise TypeError("partition (%s) is not valid for this graph: there is a cell of length 0" % partition)
        if self.has_multiple_edges():
            raise TypeError("refinement function does not support multiple edges")
        G = copy(self)
        perm_from = list(G)
        perm_to = {v: i for i, v in enumerate(perm_from)}
        G.relabel(perm=perm_to)
        partition = [[perm_to[b] for b in cell] for cell in partition]
        n = G.order()
        if sparse:
            from sage.graphs.base.sparse_graph import SparseGraph
            CG = SparseGraph(n)
        else:
            from sage.graphs.base.dense_graph import DenseGraph
            CG = DenseGraph(n)
        if G.is_directed():
            for i, j in G.edge_iterator(labels=False):
                CG.add_arc(i, j)
        else:
            for i, j in G.edge_iterator(labels=False):
                CG.add_arc(i, j)
                CG.add_arc(j, i)

        from sage.groups.perm_gps.partn_ref.refinement_graphs import coarsest_equitable_refinement
        result = coarsest_equitable_refinement(CG, partition, G._directed)
        return [[perm_from[b] for b in cell] for cell in result]

    def automorphism_group(self, partition=None, verbosity=0,
                           edge_labels=False, order=False,
                           return_group=True, orbits=False, algorithm=None):
        """
        Return the automorphism group of the graph.

        With ``partition`` this can also return the largest subgroup
        of the automorphism group of the (di)graph whose orbit
        partition is finer than the partition given.

        INPUT:

        -  ``partition`` - default is the unit partition,
           otherwise computes the subgroup of the full automorphism group
           respecting the partition.

        -  ``edge_labels`` - default False, otherwise allows
           only permutations respecting edge labels.

        -  ``order`` - (default False) if True, compute the
           order of the automorphism group

        -  ``return_group`` - default True

        -  ``orbits`` - returns the orbits of the group acting
           on the vertices of the graph

        - ``algorithm`` - If ``algorithm = "bliss"`` the automorphism group is
          computed using the optional package bliss
          (http://www.tcs.tkk.fi/Software/bliss/index.html).  Setting it to
          "sage" uses Sage's implementation. If set to ``None`` (default), bliss
          is used when available.

        OUTPUT: The order of the output is group, order, orbits. However, there
        are options to turn each of these on or off.

        EXAMPLES:

        Graphs::

            sage: graphs_query = GraphQuery(display_cols=['graph6'],num_vertices=4)
            sage: L = graphs_query.get_graphs_list()
            sage: graphs_list.show_graphs(L)
            sage: for g in L:
            ....:     G = g.automorphism_group()
            ....:     G.order(), G.gens()
            (24, ((2,3), (1,2), (0,1)))
            (4, ((2,3), (0,1)))
            (2, ((1,2),))
            (6, ((1,2), (0,1)))
            (6, ((2,3), (1,2)))
            (8, ((1,2), (0,1)(2,3)))
            (2, ((0,1)(2,3),))
            (2, ((1,2),))
            (8, ((2,3), (0,1), (0,2)(1,3)))
            (4, ((2,3), (0,1)))
            (24, ((2,3), (1,2), (0,1)))
            sage: C = graphs.CubeGraph(4)
            sage: G = C.automorphism_group()
            sage: M = G.character_table() # random order of rows, thus abs() below
            sage: QQ(M.determinant()).abs()
            712483534798848
            sage: G.order()
            384

        ::

            sage: D = graphs.DodecahedralGraph()
            sage: G = D.automorphism_group()
            sage: A5 = AlternatingGroup(5)
            sage: Z2 = CyclicPermutationGroup(2)
            sage: H = A5.direct_product(Z2)[0] #see documentation for direct_product to explain the [0]
            sage: G.is_isomorphic(H)
            True

        Multigraphs::

            sage: G = Graph(multiedges=True,sparse=True)
            sage: G.add_edge(('a', 'b'))
            sage: G.add_edge(('a', 'b'))
            sage: G.add_edge(('a', 'b'))
            sage: G.automorphism_group()
            Permutation Group with generators [('a','b')]

        Digraphs::

            sage: D = DiGraph( { 0:[1], 1:[2], 2:[3], 3:[4], 4:[0] } )
            sage: D.automorphism_group()
            Permutation Group with generators [(0,1,2,3,4)]

        Edge labeled graphs::

            sage: G = Graph(sparse=True)
            sage: G.add_edges( [(0,1,'a'),(1,2,'b'),(2,3,'c'),(3,4,'b'),(4,0,'a')] )
            sage: G.automorphism_group(edge_labels=True)
            Permutation Group with generators [(1,4)(2,3)]

            sage: G.automorphism_group(edge_labels=True, algorithm="bliss") # optional - bliss
            Permutation Group with generators [(1,4)(2,3)]

            sage: G.automorphism_group(edge_labels=True, algorithm="sage")
            Permutation Group with generators [(1,4)(2,3)]

        ::

            sage: G = Graph({0 : {1 : 7}})
            sage: G.automorphism_group(edge_labels=True)
            Permutation Group with generators [(0,1)]

            sage: foo = Graph(sparse=True)
            sage: bar = Graph(sparse=True)
            sage: foo.add_edges([(0,1,1),(1,2,2), (2,3,3)])
            sage: bar.add_edges([(0,1,1),(1,2,2), (2,3,3)])
            sage: foo.automorphism_group(edge_labels=True)
            Permutation Group with generators [()]
            sage: foo.automorphism_group()
            Permutation Group with generators [(0,3)(1,2)]
            sage: bar.automorphism_group(edge_labels=True)
            Permutation Group with generators [()]

        You can also ask for just the order of the group::

            sage: G = graphs.PetersenGraph()
            sage: G.automorphism_group(return_group=False, order=True)
            120

        Or, just the orbits (note that each graph here is vertex transitive)

        ::

            sage: G = graphs.PetersenGraph()
            sage: G.automorphism_group(return_group=False, orbits=True,algorithm='sage')
            [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
            sage: orb = G.automorphism_group(partition=[[0],list(range(1,10))],
            ....:                            return_group=False, orbits=True,algorithm='sage')
            sage: sorted([sorted(o) for o in orb], key=len)
            [[0], [1, 4, 5], [2, 3, 6, 7, 8, 9]]
            sage: C = graphs.CubeGraph(3)
            sage: orb = C.automorphism_group(orbits=True, return_group=False,algorithm='sage')
            sage: [sorted(o) for o in orb]
            [['000', '001', '010', '011', '100', '101', '110', '111']]

        One can also use the faster algorithm for computing the automorphism
        group of the graph - bliss::

            sage: G = graphs.HallJankoGraph()                   # optional - bliss
            sage: A1 = G.automorphism_group()                   # optional - bliss
            sage: A2 = G.automorphism_group(algorithm='bliss')  # optional - bliss
            sage: A1.is_isomorphic(A2)                          # optional - bliss
            True

        TESTS:

        We get a KeyError when given an invalid partition (:trac:`6087`)::

            sage: g=graphs.CubeGraph(3)
            sage: g.relabel()
            sage: g.automorphism_group(partition=[[0,1,2],[3,4,5]],algorithm='sage')
            Traceback (most recent call last):
            ...
            KeyError: ...

        Labeled automorphism group::

            sage: d = digraphs.DeBruijn(3,2)
            sage: A = d.automorphism_group(algorithm='sage')
            sage: A_target = PermutationGroup(["('02','10','21')('00','11','22')('01','12','20')",
            ....:                              "('02','01')('10','20')('21','12')('22','11')"])
            sage: A.is_isomorphic(A_target)
            True
            sage: d.allow_multiple_edges(True)
            sage: d.add_edge(('00', '00', '0'))
            sage: A = d.automorphism_group(algorithm='sage')
            sage: A_target = PermutationGroup(["('01','02')('10','20')('11','22')('12','21')"])
            sage: A.is_isomorphic(A_target)
            True

        The labeling is correct::

            sage: g = graphs.PetersenGraph()
            sage: ag = g.automorphism_group()
            sage: all(len(ag.orbit(e, action="OnPairs")) == 30
            ....:       for e in g.edge_iterator(labels=False))
            True

        Empty group, correct domain::

            sage: ag = Graph({'a':['a'], 'b':[]}).automorphism_group()
            sage: ag
            Permutation Group with generators [()]
            sage: sorted(ag.domain())
            ['a', 'b']

        We can check that the subgroups are labelled correctly
        (:trac:`15656`)::

            sage: G1 = Graph(':H`ECw@HGXGAGUG`e')
            sage: G = G1.automorphism_group()
            sage: G.subgroups()
            [Subgroup generated by [()] of (Permutation Group with generators [(0,7)(1,4)(2,3)(6,8)]),
             Subgroup generated by [(0,7)(1,4)(2,3)(6,8)] of (Permutation Group with generators [(0,7)(1,4)(2,3)(6,8)])]

        We check that the representations of the groups returned with ``'sage'``
        and ``'bliss'`` are the same (:trac:`27571`)::

            sage: G = graphs.PaleyGraph(9)
            sage: a1 = G.automorphism_group(algorithm='sage')
            sage: V = sorted(G, reverse=True)
            sage: a2 = G.automorphism_group(algorithm='sage', partition=[V])
            sage: a1.is_isomorphic(a2)
            True
            sage: str(a1) == str(a2)
            False
            sage: b1 = G.automorphism_group(algorithm='bliss')  # optional - bliss
            sage: str(a1) == str(b1)                            # optional - bliss
            True
            sage: b2 = G.automorphism_group(algorithm='bliss', partition=[V])  # optional - bliss
            sage: str(a2) == str(b2)                                           # optional - bliss
            True
        """
        from sage.features.bliss import Bliss
        have_bliss = Bliss().is_present()

        # See trac #21704
        if self.has_multiple_edges():
            if algorithm == 'bliss':
                raise NotImplementedError("algorithm 'bliss' cannot be used for graph with multiedges")
            have_bliss = False

        if (algorithm == 'bliss' or  # explicit choice from the user; or
            (algorithm is None and   # by default
             have_bliss)):

            Bliss().require()

            from sage.graphs.bliss import automorphism_group
            A = automorphism_group(self, partition, use_edge_labels=edge_labels)

            # If the user only wants the automorphism group, lets return it
            # without much hassle
            if return_group and not (orbits or order):
                return A

            ret = []
            if return_group:
                ret.append(A)
            if order:
                ret.append(A.order())
            if orbits:
                ret.append(A.orbits())

            if return_group + order + orbits == 1:
                return ret[0]
            return ret

        if algorithm is not None and algorithm != "sage":
            raise ValueError("'algorithm' must be equal to 'bliss', 'sage', or None")

        from sage.groups.perm_gps.partn_ref.refinement_graphs import search_tree
        from sage.groups.perm_gps.permgroup import PermutationGroup
        from sage.graphs.graph import Graph
        from sage.graphs.digraph import DiGraph
        from itertools import chain
        dig = (self._directed or self.has_loops())

        if partition is None:
            partition = [list(self)]

        if edge_labels or self.has_multiple_edges():
            ret = graph_isom_equivalent_non_edge_labeled_graph(self, partition,
                                                               return_relabeling=True,
                                                               ignore_edge_labels=(not edge_labels))
            G, partition, relabeling = ret
            G_vertices = list(chain(*partition))
            G_to = {u: i for i, u in enumerate(G_vertices)}
            DoDG = DiGraph if self._directed else Graph
            H = DoDG(len(G_vertices), loops=G.allows_loops())
            HB = H._backend
            for u, v in G.edge_iterator(labels=False):
                HB.add_edge(G_to[u], G_to[v], None, G._directed)
            GC = HB.c_graph()[0]
            partition = [[G_to[vv] for vv in cell] for cell in partition]
            A = search_tree(GC, partition, lab=False, dict_rep=True, dig=dig, verbosity=verbosity, order=order)
            if order:
                a, b, c = A
            else:
                a, b = A
            b_new = {v: b[G_to[v]] for v in G_to}
            b = b_new
            # b is a translation of the labellings
            acting_vertices = {}
            translation_d = {}
            m = G.order()
            for v in self:
                if b[relabeling[v]] == m:
                    translation_d[v] = self.order()
                    acting_vertices[v] = 0
                else:
                    translation_d[v] = b[relabeling[v]]
                    acting_vertices[v] = b[relabeling[v]]
            real_aut_gp = []
            n = self.order()
            for gen in a:
                gen_restr = [0] * n
                for v in self:
                    gen_restr[acting_vertices[v]] = gen[acting_vertices[v]]
                if gen_restr not in real_aut_gp:
                    real_aut_gp.append(gen_restr)
            id = list(range(n))
            if id in real_aut_gp:
                real_aut_gp.remove(id)
            a = real_aut_gp
            b = translation_d
        else:
            G_vertices = list(chain(*partition))
            G_to = {u: i for i, u in enumerate(G_vertices)}
            DoDG = DiGraph if self._directed else Graph
            H = DoDG(len(G_vertices), loops=self.allows_loops())
            HB = H._backend
            for u, v in self.edge_iterator(labels=False):
                HB.add_edge(G_to[u], G_to[v], None, self._directed)
            GC = HB.c_graph()[0]
            partition = [[G_to[vv] for vv in cell] for cell in partition]

            if return_group:
                A = search_tree(GC, partition, dict_rep=True, lab=False, dig=dig, verbosity=verbosity, order=order)
                if order:
                    a, b, c = A
                else:
                    a, b = A
                b_new = {v: b[G_to[v]] for v in G_to}
                b = b_new
            else:
                a = search_tree(GC, partition, dict_rep=False, lab=False, dig=dig, verbosity=verbosity, order=order)
                if order:
                    a, c = a

        output = []
        if return_group:
            if a:
                # We translate the integer permutations into a collection of
                # cycles.
                from sage.combinat.permutation import Permutation
                gens = [Permutation(x+1 for x in aa).to_cycles() for aa in a]

                # We relabel the cycles using the vertices' names instead of integers
                n = self.order()
                int_to_vertex = {((i + 1) if i != n else 1): v for v, i in b.items()}
                gens = [[tuple(int_to_vertex[i] for i in cycle) for cycle in gen] for gen in gens]
                output.append(PermutationGroup(gens=gens, domain=int_to_vertex.values()))
            else:
                output.append(PermutationGroup([[]], domain=list(self)))
        if order:
            output.append(c)
        if orbits:
            G_from = {G_to[v]: v for v in G_to}
            from sage.groups.perm_gps.partn_ref.refinement_graphs import get_orbits
            output.append([[G_from[v] for v in W] for W in get_orbits(a, self.num_verts())])

        if len(output) == 1:
            return output[0]
        elif len(output) > 1:
            return tuple(output)
        return None

    def is_vertex_transitive(self, partition=None, verbosity=0,
                             edge_labels=False, order=False,
                             return_group=True, orbits=False):
        """
        Returns whether the automorphism group of self is transitive within
        the partition provided, by default the unit partition of the
        vertices of self (thus by default tests for vertex transitivity in
        the usual sense).

        EXAMPLES::

            sage: G = Graph({0:[1],1:[2]})
            sage: G.is_vertex_transitive()
            False
            sage: P = graphs.PetersenGraph()
            sage: P.is_vertex_transitive()
            True
            sage: D = graphs.DodecahedralGraph()
            sage: D.is_vertex_transitive()
            True
            sage: R = graphs.RandomGNP(2000, .01)
            sage: R.is_vertex_transitive()
            False
        """
        if partition is None:
            partition = [self.vertices(sort=False)]

        for p in partition:
            if not p:
                continue
            d = self.degree(p[0])
            if not all(self.degree(x) == d for x in p):
                return False

        new_partition = self.automorphism_group(partition,
                          verbosity=verbosity, edge_labels=edge_labels,
                          order=False, return_group=False, orbits=True)

        return (len(partition) == len(new_partition))

    def is_hamiltonian(self, solver=None, constraint_generation=None,
                       verbose=0, verbose_constraints=False,
                       *, integrality_tolerance=1e-3):
        r"""
        Test whether the current graph is Hamiltonian.

        A graph (resp. digraph) is said to be Hamiltonian if it contains as a
        subgraph a cycle (resp. a circuit) going through all the vertices.

        Testing for Hamiltonicity being NP-Complete, this algorithm could run
        for some time depending on the instance.

        ALGORITHM:

        See :meth:`~GenericGraph.traveling_salesman_problem`.

        INPUT:

        - ``solver`` -- string (default: ``None``); specify a Mixed Integer
          Linear Programming (MILP) solver to be used. If set to ``None``, the
          default one is used. For more information on MILP solvers and which
          default solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``constraint_generation`` (boolean) -- whether to use constraint
          generation when solving the Mixed Integer Linear Program.  When
          ``constraint_generation = None``, constraint generation is used
          whenever the graph has a density larger than 70%.

        - ``verbose`` -- integer (default: ``0``); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``verbose_constraints`` -- boolean (default: ``False``); whether to
          display which constraints are being generated

        - ``integrality_tolerance`` -- float; parameter for use with MILP
          solvers over an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        OUTPUT:

        Returns ``True`` if a Hamiltonian cycle/circuit exists, and ``False``
        otherwise.

        NOTE:

        This function, as ``hamiltonian_cycle`` and
        ``traveling_salesman_problem``, computes a Hamiltonian cycle if it
        exists: the user should *NOT* test for Hamiltonicity using
        ``is_hamiltonian`` before calling ``hamiltonian_cycle`` or
        ``traveling_salesman_problem`` as it would result in computing it twice.

        EXAMPLES:

        The Heawood Graph is known to be Hamiltonian ::

            sage: g = graphs.HeawoodGraph()
            sage: g.is_hamiltonian()
            True

        The Petergraph, though, is not ::

            sage: g = graphs.PetersenGraph()
            sage: g.is_hamiltonian()
            False

        TESTS::

            sage: g = graphs.ChvatalGraph()
            sage: g.is_hamiltonian()
            True

        :trac:`16210`::

            sage: g = graphs.CycleGraph(10)
            sage: g.allow_loops(True)
            sage: g.add_edge(0,0)
            sage: g.is_hamiltonian()
            True
        """
        from sage.categories.sets_cat import EmptySetError
        try:
            self.traveling_salesman_problem(use_edge_labels=False, solver=solver,
                                            constraint_generation=constraint_generation,
                                            verbose=verbose, verbose_constraints=verbose_constraints,
                                            integrality_tolerance=integrality_tolerance)
            return True
        except EmptySetError:
            return False

    def is_isomorphic(self, other, certificate=False, verbosity=0, edge_labels=False):
        r"""
        Tests for isomorphism between self and other.

        INPUT:

        - ``certificate`` -- if True, then output is `(a, b)`, where `a`
          is a boolean and `b` is either a map or ``None``

        - ``edge_labels`` -- boolean (default: ``False``); if ``True`` allows
          only permutations respecting edge labels

        OUTPUT:

        - either a boolean or, if ``certificate`` is ``True``, a tuple consisting
          of a boolean and a map or ``None``

        EXAMPLES:

        Graphs::

            sage: from sage.groups.perm_gps.permgroup_named import SymmetricGroup       # optional - sage.groups
            sage: D = graphs.DodecahedralGraph()
            sage: E = copy(D)
            sage: gamma = SymmetricGroup(20).random_element()                           # optional - sage.groups
            sage: E.relabel(gamma)                                                      # optional - sage.groups
            sage: D.is_isomorphic(E)
            True

        ::

            sage: D = graphs.DodecahedralGraph()
            sage: S = SymmetricGroup(20)                                                # optional - sage.groups
            sage: gamma = S.random_element()                                            # optional - sage.groups
            sage: E = copy(D)                                                           # optional - sage.groups
            sage: E.relabel(gamma)                                                      # optional - sage.groups
            sage: a,b = D.is_isomorphic(E, certificate=True); a
            True
            sage: from sage.graphs.generic_graph_pyx import spring_layout_fast
            sage: position_D = spring_layout_fast(D)
            sage: position_E = {}
            sage: for vert in position_D:
            ....:  position_E[b[vert]] = position_D[vert]
            sage: graphics_array([D.plot(pos=position_D), E.plot(pos=position_E)]).show() # long time

        ::

            sage: g=graphs.HeawoodGraph()
            sage: g.is_isomorphic(g)
            True

        Multigraphs::

            sage: G = Graph(multiedges=True,sparse=True)
            sage: G.add_edge((0,1,1))
            sage: G.add_edge((0,1,2))
            sage: G.add_edge((0,1,3))
            sage: G.add_edge((0,1,4))
            sage: H = Graph(multiedges=True,sparse=True)
            sage: H.add_edge((3,4))
            sage: H.add_edge((3,4))
            sage: H.add_edge((3,4))
            sage: H.add_edge((3,4))
            sage: G.is_isomorphic(H)
            True

        Digraphs::

            sage: A = DiGraph( { 0 : [1,2] } )
            sage: B = DiGraph( { 1 : [0,2] } )
            sage: A.is_isomorphic(B, certificate=True)
            (True, {0: 1, 1: 0, 2: 2})

        Edge labeled graphs::

            sage: G = Graph(sparse=True)
            sage: G.add_edges( [(0,1,'a'),(1,2,'b'),(2,3,'c'),(3,4,'b'),(4,0,'a')] )
            sage: H = G.relabel([1,2,3,4,0], inplace=False)
            sage: G.is_isomorphic(H, edge_labels=True)
            True

        Edge labeled digraphs::

            sage: G = DiGraph()
            sage: G.add_edges( [(0,1,'a'),(1,2,'b'),(2,3,'c'),(3,4,'b'),(4,0,'a')] )
            sage: H = G.relabel([1,2,3,4,0], inplace=False)
            sage: G.is_isomorphic(H, edge_labels=True)
            True
            sage: G.is_isomorphic(H, edge_labels=True, certificate=True)
            (True, {0: 1, 1: 2, 2: 3, 3: 4, 4: 0})

        TESTS::

            sage: g1 = '~?A[~~{ACbCwV_~__OOcCW_fAA{CF{CCAAAC__bCCCwOOV___~___'+\
            ....: '_OOOOcCCCW___fAAAA{CCCF{CCCCAAAAAC____bCCCCCwOOOOV_____~_O'+\
            ....: '@ACG_@ACGOo@ACG?{?`A?GV_GO@AC}@?_OGCC?_OI@?K?I@?_OM?_OGD?F'+\
            ....: '_A@OGC@{A@?_OG?O@?gCA?@_GCA@O?B_@OGCA?BoA@?gC?@{A?GO`???_G'+\
            ....: 'O@AC??E?O`?CG??[?O`A?G??{?GO`A???|A?_GOC`AC@_OCGACEAGS?HA?'+\
            ....: '_SA`aO@G?cOC_NG_C@AOP?GnO@_GACOE?g?`OGACCOGaGOc?HA?`GORCG_'+\
            ....: 'AO@B?K@[`A?OCI@A@By?_K@?SCABA?H?SA?a@GC`CH?Q?C_c?cGRC@G_AO'+\
            ....: 'COa@Ax?QC?_GOo_CNg@A?oC@CaCGO@CGA_O`?GSGPAGOC_@OO_aCHaG?cO'+\
            ....: '@CB?_`Ax?GQC?_cAOCG^OGAC@_D?IGO`?D?O_I?HAOO`AGOHA?cC?oAO`A'+\
            ....: 'W_Q?HCACACGO`[_OCHA?_cCACG^O_@CAGO`A?GCOGc@?I?OQOC?IGC_o@C'+\
            ....: 'AGCCE?A@DBG_OA@C_CP?OG_VA_COG@D?_OA_DFgA@CO?aH?Ga@?a?_I?S@'+\
            ....: 'A@@Oa@?@P@GCO_AACO_a_?`K_GCQ@?cAOG_OGAwQ@?K?cCGH?I?ABy@C?G'+\
            ....: '_S@@GCA@C`?OI?_D?OP@G?IGGP@O_AGCP?aG?GCPAX?cA?OGSGCGCAGCJ`'+\
            ....: '?oAGCCHAA?A_CG^O@CAG_GCSCAGCCGOCG@OA_`?`?g_OACG_`CAGOAO_H?'+\
            ....: 'a_?`AXA?OGcAAOP?a@?CGVACOG@_AGG`OA_?O`|?Ga?COKAAGCA@O`A?a?'+\
            ....: 'S@?HCG`?_?gO`AGGaC?PCAOGI?A@GO`K_CQ@?GO_`OGCAACGVAG@_COOCQ'+\
            ....: '?g?I?O`ByC?G_P?O`A?H@G?_P?`OAGC?gD?_C@_GCAGDG_OA@CCPC?AOQ?'+\
            ....: '?g_R@_AGCO____OCC_@OAbaOC?g@C_H?AOOC@?a`y?PC?G`@OOH??cOG_O'+\
            ....: 'OAG@_COAP?WA?_KAGC@C_CQ@?HAACH??c@P?_AWGaC?P?gA_C_GAD?I?Aw'+\
            ....: 'a?S@?K?`C_GAOGCS?@|?COGaA@CAAOQ?AGCAGOACOG@_G_aC@_G@CA@@AH'+\
            ....: 'A?OGc?WAAH@G?P?_?cH_`CAGOGACc@@GA?S?CGVCG@OA_CICAOOC?PO?OG'+\
            ....: '^OG_@CAC_cC?AOP?_OICG@?oAGCO_GO_GB@?_OG`AH?cA?OH?`P??cC_O?'+\
            ....: 'SCGR@O_AGCAI?Q?_GGS?D?O`[OI?_D@@CCA?cCA_?_O`By?_PC?IGAGOQ?'+\
            ....: '@A@?aO`A?Q@?K?__`_E?_GCA@CGO`C_GCQ@A?gAOQ?@C?DCACGR@GCO_AG'+\
            ....: 'PA@@GAA?A_CO`Aw_I?S@?SCB@?OC_?_P@ACNgOC@A?aCGOCAGCA@CA?H@G'+\
            ....: 'G_C@AOGa?OOG_O?g_OA?oDC_AO@GOCc?@P?_A@D??cC``O?cGAOGD?@OA_'+\
            ....: 'CAGCA?_cwKA?`?OWGG?_PO?I?S?H@?^OGAC@_Aa@CAGC?a@?_Q?@H?_OCH'+\
            ....: 'A?OQA_P?_G_O?WA?_IG_Q?HC@A@ADCA?AI?AC_?QAWOHA?cAGG_I?S?G_O'+\
            ....: 'G@GA?`[D?O_IA?`GGCS?OA_?c@?Q?^OAC@_G_Ca@CA@?OGCOH@G@A@?GQC'+\
            ....: '?_Q@GP?_OG?IGGB?OCGaG?cO@A__QGC?E?A@CH@G?GRAGOC_@GGOW@O?O_'+\
            ....: 'OGa?_c?GV@CGA_OOaC?a_?a?A_CcC@?CNgA?oC@GGE@?_OH?a@?_?QA`A@'+\
            ....: '?QC?_KGGO_OGCAa@?A?_KCGPC@G_AOAGPGC?D@?a_A?@GGO`KH?Q?C_QGA'+\
            ....: 'A_?gOG_OA?_GG`AwH?SA?`?cAI?A@D?I?@?QA?`By?K@?O`GGACA@CGCA@'+\
            ....: 'CC_?WO`?`A?OCH?`OCA@COG?I?oC@ACGPCG_AO@_aAA?Aa?g?GD@G?CO`A'+\
            ....: 'WOc?HA?OcG_?g@OGCAAAOC@ACJ_`OGACAGCS?CAGI?A`@?OCACG^'
            sage: g2 = '~?A[??osR?WARSETCJ_QWASehOXQg`QwChK?qSeFQ_sTIaWIV?XIR'+\
            ....: '?KAC?B?`?COCG?o?O_@_?`??B?`?o@_O_WCOCHC@_?`W?E?AD_O?WCCeO?'+\
            ....: 'WCSEGAGAIaA@_?aw?OK?ER?`?@_HQXA?B@Q_pA?a@Qg_`?o?h[?GOK@IR?'+\
            ....: '@A?BEQcoCG?K\\IB?GOCWiTC?GOKWIV??CGEKdH_H_?CB?`?DC??_WCG?S'+\
            ....: 'O?AP?O_?g_?D_?`?C__?D_?`?CCo??@_O_XDC???WCGEGg_??a?`G_aa??'+\
            ....: 'E?AD_@cC??K?CJ?@@K?O?WCCe?aa?G?KAIB?Gg_A?a?ag_@DC?OK?CV??E'+\
            ....: 'OO@?o?XK??GH`A?B?Qco?Gg`A?B@Q_o?CSO`?P?hSO?@DCGOK?IV???K_`'+\
            ....: 'A@_HQWC??_cCG?KXIRG?@D?GO?WySEG?@D?GOCWiTCC??a_CGEKDJ_@??K'+\
            ....: '_@A@bHQWAW?@@K??_WCG?g_?CSO?A@_O_@P??Gg_?Ca?`?@P??Gg_?D_?`'+\
            ....: '?C__?EOO?Ao?O_AAW?@@K???WCGEPP??Gg_??B?`?pDC??aa??AGACaAIG'+\
            ....: '?@DC??K?CJ?BGG?@cC??K?CJ?@@K??_e?G?KAAR?PP??Gg_A?B?a_oAIG?'+\
            ....: '@DC?OCOCTC?Gg_?CSO@?o?P[??X@??K__A@_?qW??OR??GH`A?B?Qco?Gg'+\
            ....: '_?CSO`?@_hOW?AIG?@DCGOCOITC??PP??Gg`A@_@Qw??@cC??qACGE?dH_'+\
            ....: 'O?AAW?@@GGO?WqSeO?AIG?@D?GO?WySEG?@DC??a_CGAKTIaA??PP??Gg@'+\
            ....: 'A@b@Qw?O?BGG?@c?GOKXIR?KAC?H_?CCo?A@_O_?WCG@P??Gg_?CB?`?CO'+\
            ....: 'CG@P??Gg_?Ca?`?E?AC?g_?CSO?Ao?O_@_?`@GG?@cC??k?CG??WCGOR??'+\
            ....: 'GH_??B?`?o@_O`DC??aa???KACB?a?`AIG?@DC??COCHC@_?`AIG?@DC??'+\
            ....: 'K?CJ??o?O`cC??qA??E?AD_O?WC?OR??GH_A?B?_cq?B?_AIG?@DC?O?WC'+\
            ....: 'SEGAGA?Gg_?CSO@?P?PSOOK?C?PP??Gg_A@_?aw?OK?C?X@??K__A@_?qW'+\
            ....: 'CG?K??GH_?CCo`?@_HQXA?B??AIG?@DCGO?WISEGOCO??PP??Gg`A?a@Qg'+\
            ....: '_`?o??@DC??aaCGE?DJ_@A@_??BGG?@cCGOK@IR?@A?BO?AAW?@@GGO?Wq'+\
            ....: 'Se?`?@g?@DC??a_CG?K\\IB?GOCQ??PP??Gg@A?bDQg_@A@_O?AIG?@D?G'+\
            ....: 'OKWIV??CGE@??K__?EO?`?pchK?_SA_OI@OGD?gCA_SA@OI?c@H?Q?c_H?'+\
            ....: 'QOC_HGAOCc?QOC_HGAOCc@GAQ?c@H?QD?gCA_SA@OI@?gD?_SA_OKA_SA@'+\
            ....: 'OI@?gD?_SA_OI@OHI?c_H?QOC_HGAOCc@GAQ?eC_H?QOC_HGAOCc@GAQ?c'+\
            ....: '@XD?_SA_OI@OGD?gCA_SA@PKGO`A@ACGSGO`?`ACICGO_?ACGOcGO`?O`A'+\
            ....: 'C`ACHACGO???^?????}Bw????Fo^???????Fo?}?????Bw?^?Bw?????GO'+\
            ....: '`AO`AC`ACGACGOcGO`??aCGO_O`ADACGOGO`A@ACGOA???@{?N_@{?????'+\
            ....: 'Fo?}????OFo????N_}????@{????Bw?OACGOgO`A@ACGSGO`?`ACG?OaCG'+\
            ....: 'O_GO`AO`AC`ACGACGO_@G???Fo^?????}Bw????Fo??AC@{?????Fo?}?F'+\
            ....: 'o?????^??AOGO`AO`AC@ACGQCGO_GO`A?HAACGOgO`A@ACGOGO`A`ACG?G'+\
            ....: 'Q??^?Bw?????N_@{?????Fo?QC??Fo^?????}????@{Fo???CHACGO_O`A'+\
            ....: 'CACGOgO`A@ACGO@AOcGO`?O`AC`ACGACGOcGO`?@GQFo????N_????^@{?'+\
            ....: '???Bw??`GRw?????N_@{?????Fo?}???HAO_OI@OGD?gCA_SA@OI@?gDK_'+\
            ....: '??C@GAQ?c@H?Q?c_H?QOC_HEW????????????????????????~~~~~'
            sage: G1 = Graph(g1)
            sage: G2 = Graph(g2)
            sage: G1.is_isomorphic(G2)
            True

        Ensure that isomorphic looped graphs with non-range vertex labels report
        correctly (:trac:`10814`, fixed by :trac:`8395`)::

            sage: G1 = Graph({1:[0,1]})
            sage: G2 = Graph({2:[0,2]})
            sage: G1.is_isomorphic(G2)
            True
            sage: G = Graph(multiedges = True, loops = True)
            sage: H = Graph(multiedges = True, loops = True)
            sage: G.add_edges([(0,1,0),(1,0,1),(1,1,2),(0,0,3)])
            sage: H.add_edges([(0,1,3),(1,0,2),(1,1,1),(0,0,0)])
            sage: G.is_isomorphic(H, certificate=True)
            (True, {0: 0, 1: 1})
            sage: set_random_seed(0)
            sage: D = digraphs.RandomDirectedGNP(6, .2)
            sage: D.is_isomorphic(D, certificate=True)
            (True, {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5})
            sage: D.is_isomorphic(D,edge_labels=True, certificate=True)
            (True, {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5})

        Ensure that :trac:`11620` is fixed::

            sage: G1 = DiGraph([(0, 0, 'c'), (0, 4, 'b'), (0, 5, 'c'),
            ....: (0, 5, 't'), (1, 1, 'c'), (1, 3,'c'), (1, 3, 't'), (1, 5, 'b'),
            ....: (2, 2, 'c'), (2, 3, 'b'), (2, 4, 'c'),(2, 4, 't'), (3, 1, 't'),
            ....: (3, 2, 'b'), (3, 2, 'c'), (3, 4, 'c'), (4, 0,'b'), (4, 0, 'c'),
            ....: (4, 2, 't'), (4, 5, 'c'), (5, 0, 't'), (5, 1, 'b'), (5, 1, 'c'),
            ....: (5, 3, 'c')], loops=True, multiedges=True)
            sage: G2 = G1.relabel({0:4, 1:5, 2:3, 3:2, 4:1,5:0}, inplace=False)
            sage: G1.canonical_label(edge_labels=True) == G2.canonical_label(edge_labels=True)
            True
            sage: G1.is_isomorphic(G2,edge_labels=True)
            True

        Ensure that :trac:`13114` is fixed ::


            sage: g = Graph([(0, 0, 0), (0, 2, 0), (1, 1, 0), (1, 2, 0), (1, 2, 1), (2, 2, 0)], multiedges=True, loops=True)
            sage: gg = Graph([(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 2, 0), (2, 2, 0), (2, 2, 1)], multiedges=True, loops=True)
            sage: g.is_isomorphic(gg)
            False

        Ensure that :trac:`14777` is fixed ::

            sage: g = Graph()
            sage: h = Graph()
            sage: g.is_isomorphic(h)
            True

        as well as :trac:`18613`::

            sage: g.is_isomorphic(h, certificate=True)
            (True, None)

        Ensure that :trac:`24964` is fixed ::

            sage: A = DiGraph([(6,7,'a'), (6,7,'b')], multiedges=True)
            sage: B = DiGraph([('x','y','u'), ('x','y','v')], multiedges=True)
            sage: A.is_isomorphic(B, certificate=True)
            (True, {6: 'x', 7: 'y'})
            sage: A.is_isomorphic(B, certificate=True, edge_labels=True)
            (False, None)

        """
        if not self.order() and not other.order():
            return (True, None) if certificate else True

        if (self.is_directed() != other.is_directed() or
                self.order() != other.order() or
                self.size() != other.size() or
                self.degree_sequence() != other.degree_sequence()):
            if certificate:
                return False, None
            else:
                return False

        from sage.groups.perm_gps.partn_ref.refinement_graphs import isomorphic

        self_vertices = list(self)
        other_vertices = list(other)
        if edge_labels or self.has_multiple_edges():
            if edge_labels and sorted(self.edge_labels(), key=str) != sorted(other.edge_labels(), key=str):
                return (False, None) if certificate else False
            else:
                ret = graph_isom_equivalent_non_edge_labeled_graph(self, return_relabeling=True,
                                                                   ignore_edge_labels=(not edge_labels),
                                                                   return_edge_labels=True)
                G, partition, relabeling, G_edge_labels = ret
                self_vertices = sum(partition, [])
                ret = graph_isom_equivalent_non_edge_labeled_graph(other, return_relabeling=True,
                                                                   ignore_edge_labels=(not edge_labels),
                                                                   return_edge_labels=True)
                G2, partition2, relabeling2, G2_edge_labels = ret

                if [len(_) for _ in partition] != [len(_) for _ in partition2]:
                    return (False, None) if certificate else False

                if edge_labels:
                    def multilabel(e):
                        return e
                else:
                    def multilabel(e):
                        return [[None, el[1]] for el in e]

                if [multilabel(_) for _ in G_edge_labels] != [multilabel(_) for _ in G2_edge_labels]:
                    return (False, None) if certificate else False
                partition2 = sum(partition2, [])
                other_vertices = partition2
        else:
            G = self
            partition = [self_vertices]
            G2 = other
            partition2 = other_vertices
        G_to = {u: i for i, u in enumerate(self_vertices)}
        if self._directed:
            from sage.graphs.digraph import DiGraph
            DoDG = DiGraph
        else:
            from sage.graphs.graph import Graph
            DoDG = Graph
        H = DoDG(len(self_vertices), loops=G.allows_loops())
        HB = H._backend
        for u, v in G.edge_iterator(labels=False):
            HB.add_edge(G_to[u], G_to[v], None, G._directed)
        G = HB.c_graph()[0]
        partition = [[G_to[vv] for vv in cell] for cell in partition]
        GC = G
        G2_to = {u: i for i, u in enumerate(other_vertices)}
        H2 = DoDG(len(other_vertices), loops=G2.allows_loops())
        H2B = H2._backend
        for u, v in G2.edge_iterator(labels=False):
            H2B.add_edge(G2_to[u], G2_to[v], None, G2._directed)
        G2 = H2B.c_graph()[0]
        partition2 = [G2_to[vv] for vv in partition2]
        GC2 = G2
        isom = isomorphic(GC, GC2, partition, partition2, (self._directed or self.has_loops()), 1)

        if not isom and certificate:
            return False, None
        elif not isom:
            return False
        elif not certificate:
            return True
        else:
            isom_trans = {}
            if edge_labels or self.has_multiple_edges():
                relabeling2_inv = {}
                for x in relabeling2:
                    relabeling2_inv[relabeling2[x]] = x
                for v in self:
                    isom_trans[v] = relabeling2_inv[other_vertices[isom[G_to[relabeling[v]]]]]
            else:
                for v in self:
                    isom_trans[v] = other_vertices[isom[G_to[v]]]
            return True, isom_trans

    def canonical_label(self, partition=None, certificate=False,
                        edge_labels=False, algorithm=None, return_graph=True):
        r"""
        Return the canonical graph.

        A canonical graph is the representative graph of an isomorphism
        class by some canonization function `c`. If `G` and `H` are graphs,
        then `G \cong c(G)`, and `c(G) == c(H)` if and only if `G \cong H`.

        See the :wikipedia:`Graph_canonization` for more information.

        INPUT:

        - ``partition`` -- if given, the canonical label with respect
          to this set partition will be computed. The default is the unit
          set partition.

        - ``certificate`` -- boolean (default: ``False``). When set to
          ``True``, a dictionary mapping from the vertices of the (di)graph
          to its canonical label will also be returned.

        - ``edge_labels`` -- boolean (default: ``False``). When set to
          ``True``, allows only permutations respecting edge labels.

        - ``algorithm`` -- a string (default: ``None``). The algorithm to use;
          currently available:

          * ``'bliss'``: use the optional package bliss
            (http://www.tcs.tkk.fi/Software/bliss/index.html);
          * ``'sage'``: always use Sage's implementation.
          * ``None`` (default): use bliss when available and possible

            .. NOTE::

                Make sure you always compare canonical forms obtained by the
                same algorithm.

        - ``return_graph`` -- boolean (default: ``True``). When set to
          ``False``, returns the list of edges of the canonical graph
          instead of the canonical graph; only available when ``'bliss'``
          is explicitly set as algorithm.

        EXAMPLES:

        Canonization changes isomorphism to equality::

            sage: g1 = graphs.GridGraph([2,3])
            sage: g2 = Graph({1: [2, 4], 3: [2, 6], 5: [4, 2, 6]})
            sage: g1 == g2
            False
            sage: g1.is_isomorphic(g2)
            True
            sage: g1.canonical_label() == g2.canonical_label()
            True

        We can get the relabeling used for canonization::

            sage: g, c = g1.canonical_label(algorithm='sage', certificate=True)
            sage: g
            Grid Graph for [2, 3]: Graph on 6 vertices
            sage: c
            {(0, 0): 3, (0, 1): 4, (0, 2): 2, (1, 0): 0, (1, 1): 5, (1, 2): 1}

        Multigraphs and directed graphs work too::

            sage: G = Graph(multiedges=True,sparse=True)
            sage: G.add_edge((0,1))
            sage: G.add_edge((0,1))
            sage: G.add_edge((0,1))
            sage: G.canonical_label()
            Multi-graph on 2 vertices
            sage: Graph('A?').canonical_label()
            Graph on 2 vertices

            sage: P = graphs.PetersenGraph()
            sage: DP = P.to_directed()
            sage: DP.canonical_label(algorithm='sage').adjacency_matrix()
            [0 0 0 0 0 0 0 1 1 1]
            [0 0 0 0 1 0 1 0 0 1]
            [0 0 0 1 0 0 1 0 1 0]
            [0 0 1 0 0 1 0 0 0 1]
            [0 1 0 0 0 1 0 0 1 0]
            [0 0 0 1 1 0 0 1 0 0]
            [0 1 1 0 0 0 0 1 0 0]
            [1 0 0 0 0 1 1 0 0 0]
            [1 0 1 0 1 0 0 0 0 0]
            [1 1 0 1 0 0 0 0 0 0]

        Edge labeled graphs::

            sage: G = Graph(sparse=True)
            sage: G.add_edges( [(0,1,'a'),(1,2,'b'),(2,3,'c'),(3,4,'b'),(4,0,'a')] )
            sage: G.canonical_label(edge_labels=True)
            Graph on 5 vertices
            sage: G.canonical_label(edge_labels=True, algorithm="bliss", certificate=True) # optional - bliss
            (Graph on 5 vertices, {0: 4, 1: 3, 2: 1, 3: 0, 4: 2})

            sage: G.canonical_label(edge_labels=True, algorithm="sage", certificate=True)
            (Graph on 5 vertices, {0: 4, 1: 3, 2: 0, 3: 1, 4: 2})

        Another example where different canonization algorithms give
        different graphs::

            sage: g = Graph({'a': ['b'], 'c': ['d']})
            sage: g_sage = g.canonical_label(algorithm='sage')
            sage: g_bliss = g.canonical_label(algorithm='bliss')  # optional - bliss
            sage: g_sage.edges(sort=True, labels=False)
            [(0, 3), (1, 2)]
            sage: g_bliss.edges(sort=True, labels=False)  # optional - bliss
            [(0, 1), (2, 3)]

        TESTS::

            sage: G = Graph([['a', 'b'], [('a', 'b')]])
            sage: G.canonical_label(algorithm='sage', certificate=True)
            (Graph on 2 vertices, {'a': 0, 'b': 1})
            sage: G.canonical_label(algorithm='bliss', certificate=True)  # optional - bliss
            (Graph on 2 vertices, {'a': 1, 'b': 0})

        Check for immutable graphs (:trac:`16602`)::

            sage: G = Graph([[1, 2], [2, 3]], immutable=True)
            sage: C = G.canonical_label(); C
            Graph on 3 vertices
            sage: C.vertices(sort=True)
            [0, 1, 2]

        Corner cases::

            sage: g = Graph()
            sage: g.canonical_label(algorithm='sage')
            Graph on 0 vertices
            sage: g.canonical_label(algorithm='bliss')  # optional - bliss
            Graph on 0 vertices
            sage: g = Graph({'x': []})
            sage: g.canonical_label(algorithm='sage').vertices(sort=False)
            [0]
            sage: g.canonical_label(algorithm='bliss').vertices(sort=False)  # optional - bliss
            [0]

        Check that the name is preserved with both algorithms::

            sage: g = graphs.PathGraph(1)
            sage: g.canonical_label(algorithm='sage')
            Path graph: Graph on 1 vertex
            sage: g.canonical_label(algorithm='bliss')  # optional - bliss
            Path graph: Graph on 1 vertex

        Check that :trac:`28531` is fixed::

            sage: from itertools import product, permutations
            sage: edges_list = [[(0,1), (2,3)],
            ....:               [(0,1), (1,2), (2,3)],
            ....:               [(0,1), (0,2), (1,2)],
            ....:               [(0,1), (0,2), (0,3)]]
            sage: algos = ['sage']
            sage: algos.append('bliss')     # optional - bliss
            sage: S = Set([0,1,2])
            sage: for (algo, edges) in product(algos, edges_list):
            ....:     L = cartesian_product([S] * len(edges))
            ....:     O = OrderedSetPartitions([0,1,2,3])
            ....:     P = Permutations([0,1,2,3])
            ....:     for _ in range(10):
            ....:         part = O.random_element()
            ....:         labels = L.random_element()
            ....:         g = Graph(4)
            ....:         g.add_edges([(u,v,lab) for ((u,v),lab) in zip(edges, labels)])
            ....:         gcan0 = g.canonical_label(partition=part, edge_labels=True, return_graph=True, algorithm=algo)
            ....:         for _ in range(5):
            ....:             perm = P.random_element()
            ....:             gg = Graph(4)
            ....:             gg.add_edges([(perm[u], perm[v], lab) for u,v,lab in g.edges(sort=True)])
            ....:             pp = [[perm[i] for i in s] for s in part]
            ....:             gcan1 = gg.canonical_label(partition=pp, edge_labels=True, algorithm=algo)
            ....:             gcan2, _ = gg.canonical_label(partition=pp, edge_labels=True, certificate=True, algorithm=algo)
            ....:             assert gcan0 == gcan1, (edges, labels, part, pp)
            ....:             assert gcan0 == gcan2, (edges, labels, part, pp)
        """
        # Check parameter combinations
        if algorithm not in [None, 'sage', 'bliss']:
            raise ValueError("'algorithm' must be equal to 'bliss', 'sage', or None")
        if algorithm != 'bliss' and not return_graph:
            raise ValueError("return_graph=False can only be used with algorithm='bliss'")
        has_multiedges = self.has_multiple_edges()
        if has_multiedges and algorithm == 'bliss':  # See trac #21704
            raise NotImplementedError("algorithm 'bliss' cannot be used for graph with multiedges")

        # Check bliss if explicitly requested, raise if not found.
        if algorithm == 'bliss':
            from sage.graphs.bliss import canonical_form

        # By default use bliss when possible
        elif algorithm is None:
            algorithm = 'sage'
            if not has_multiedges:
                try:
                    from sage.graphs.bliss import canonical_form
                    algorithm = 'bliss'
                except ImportError:
                    pass

        if algorithm == 'bliss':
            if return_graph:
                vert_dict = canonical_form(self, partition, False, edge_labels, True)[1]
                if not certificate:
                    return self.relabel(vert_dict, inplace=False)
                return (self.relabel(vert_dict, inplace=False), vert_dict)
            return canonical_form(self, partition, return_graph, edge_labels, certificate)

        # algorithm == 'sage':
        from sage.groups.perm_gps.partn_ref.refinement_graphs import search_tree
        from sage.graphs.graph import Graph
        from sage.graphs.digraph import DiGraph
        from itertools import chain

        dig = (self.has_loops() or self._directed)
        if partition is None:
            partition = [list(self)]
        if edge_labels or self.has_multiple_edges():
            G, partition, relabeling = graph_isom_equivalent_non_edge_labeled_graph(self, partition, return_relabeling=True)
            G_vertices = list(chain(*partition))
            G_to = {u: i for i, u in enumerate(G_vertices)}
            DoDG = DiGraph if self._directed else Graph
            H = DoDG(len(G_vertices), loops=G.allows_loops())
            HB = H._backend
            for u, v in G.edge_iterator(labels=False):
                HB.add_edge(G_to[u], G_to[v], None, G._directed)
            GC = HB.c_graph()[0]
            partition = [[G_to[vv] for vv in cell] for cell in partition]
            a, b, c = search_tree(GC, partition, certificate=True, dig=dig)
            # c is a permutation to the canonical label of G, which depends only on isomorphism class of self.
            H = copy(self)
            c_new = {v: c[G_to[relabeling[v]]] for v in self}
        else:
            G_vertices = list(chain(*partition))
            G_to = {u: i for i, u in enumerate(G_vertices)}
            DoDG = DiGraph if self._directed else Graph
            H = DoDG(len(G_vertices), loops=self.allows_loops())
            HB = H._backend
            for u, v in self.edge_iterator(labels=False):
                HB.add_edge(G_to[u], G_to[v], None, self._directed)
            GC = HB.c_graph()[0]
            partition = [[G_to[vv] for vv in cell] for cell in partition]
            a, b, c = search_tree(GC, partition, certificate=True, dig=dig)
            H = copy(self)
            c_new = {v: c[G_to[v]] for v in G_to}
        H.relabel(c_new)
        if certificate:
            return H, c_new
        else:
            return H

    def is_cayley(self, return_group=False, mapping=False,
                  generators=False, allow_disconnected=False):
        r"""
        Check whether the graph is a Cayley graph.

        If none of the parameters are ``True``, return a boolean indicating
        whether the graph is a Cayley graph. Otherwise, return a tuple
        containing said boolean and the requested data. If the graph is not
        a Cayley graph, each of the data will be ``None``.

        The empty graph is defined to be not a Cayley graph.

        .. NOTE::

            For this routine to work on all graphs, the optional package
            ``gap_packages`` needs to be installed: to do
            so, it is enough to run ``sage -i gap_packages``.

        INPUT:

        - ``return_group`` (boolean; ``False``) -- If True, return a group for
          which the graph is a Cayley graph.

        - ``mapping`` (boolean; ``False``) -- If True, return a mapping from
          vertices to group elements.

        - ``generators`` (boolean; ``False``) -- If True, return the generating
          set of the Cayley graph.

        - ``allow_disconnected`` (boolean; ``False``) -- If True, disconnected
          graphs are considered Cayley if they can be obtained from the Cayley
          construction with a generating set that does not generate the group.

        ALGORITHM:

        For connected graphs, find a regular subgroup of the automorphism
        group. For disconnected graphs, check that the graph is
        vertex-transitive and perform the check on one of its connected
        components. If a simple graph has density over 1/2, perform the check
        on its complement as its disconnectedness may increase performance.

        EXAMPLES:

        A Petersen Graph is not a Cayley graph::

            sage: g = graphs.PetersenGraph()
            sage: g.is_cayley()
            False

        A Cayley digraph is a Cayley graph::

            sage: C7 = groups.permutation.Cyclic(7)
            sage: S = [(1,2,3,4,5,6,7), (1,3,5,7,2,4,6), (1,5,2,6,3,7,4)]
            sage: d = C7.cayley_graph(generators=S)
            sage: d.is_cayley()
            True

        Graphs with loops and multiedges will have identity and repeated
        elements, respectively, among the generators::

            sage: g = Graph(graphs.PaleyGraph(9), loops=True, multiedges=True)
            sage: g.add_edges([(u, u) for u in g])
            sage: g.add_edges([(u, u+1) for u in g])
            sage: _, S = g.is_cayley(generators=True)
            sage: S # random
            [(),
             (0,2,1)(a,a + 2,a + 1)(2*a,2*a + 2,2*a + 1),
             (0,2,1)(a,a + 2,a + 1)(2*a,2*a + 2,2*a + 1),
             (0,1,2)(a,a + 1,a + 2)(2*a,2*a + 1,2*a + 2),
             (0,1,2)(a,a + 1,a + 2)(2*a,2*a + 1,2*a + 2),
             (0,2*a + 2,a + 1)(1,2*a,a + 2)(2,2*a + 1,a),
             (0,a + 1,2*a + 2)(1,a + 2,2*a)(2,a,2*a + 1)]

        TESTS:

        Cayley graphs can be reconstructed from the group and generating set::

            sage: g = graphs.PaleyGraph(9)
            sage: _, G, S = g.is_cayley(return_group=True, generators=True)
            sage: Graph(G.cayley_graph(generators=S)).is_isomorphic(g)
            True

        A disconnected graphs may also be a Cayley graph::

            sage: g = graphs.PaleyGraph(9)
            sage: h = g.disjoint_union(g)
            sage: h = h.disjoint_union(h)
            sage: h = h.disjoint_union(g)
            sage: _, G, d, S = h.is_cayley(return_group=True, mapping=True, generators=True, allow_disconnected=True)
            sage: all(set(d[u] for u in h.neighbors(v)) == set(d[v]*x for x in S) for v in h)
            True

        The method also works efficiently with dense simple graphs::

            sage: graphs.CompleteBipartiteGraph(50, 50).is_cayley()
            True

        TESTS::

            sage: graphs.EmptyGraph().is_cayley()
            False
            sage: graphs.EmptyGraph().is_cayley(return_group = True,
            ....:                               mapping = False,
            ....:                               generators = True)
            (False, False, False)
        """
        if not self:
            n = return_group + mapping + generators
            if not n:
                return False
            return tuple([False] * (n + 1))

        compute_map = mapping or generators
        certificate = return_group or compute_map
        c, G, map, genset = False, None, None, None
        if not self.is_connected():
            if allow_disconnected and self.is_vertex_transitive():
                C = self.connected_components_subgraphs()
                if certificate:
                    c, CG = C[0].is_cayley(return_group=True)
                    if c:
                        from sage.groups.perm_gps.permgroup import PermutationGroup
                        I = [C[0].is_isomorphic(g, certificate=True)[1] for g in C]
                        # gens generate the direct product of CG and a cyclic group
                        gens = [sum([[tuple([M[x] for x in p])
                                for p in h.cycle_tuples()] for M in I], [])
                                for h in CG.gens()] + \
                               [[tuple([M[v] for M in I])
                                 for v in C[0].vertices(sort=False)]]
                        G = PermutationGroup(gens, domain=self.vertices(sort=False))
                else:
                    c = C[0].is_cayley(return_group=False)
        elif (not self.allows_loops() and not self.allows_multiple_edges() and
              self.density() > Rational(1)/Rational(2)):
            if certificate:
                c, G = self.complement().is_cayley(return_group=True,
                                                   allow_disconnected=True)
            else:
                c = self.complement().is_cayley(return_group=False,
                                                allow_disconnected=True)
        else:
            A = self.automorphism_group()
            if certificate:
                G = A.has_regular_subgroup(return_group=True)
                c = G is not None
            else:
                c = A.has_regular_subgroup(return_group=False)
        if c and compute_map:
            v = next(self.vertex_iterator())
            map = {(f**-1)(v): f for f in G}
            if generators:
                # self.(out_)neighbors ignores multiedges,
                # so we use edge_iterator instead
                adj = [y if v == x else x
                       for x, y, z in self.edges(vertices=v, sort=False)]
                genset = [map[u] for u in adj]
        if certificate:
            out = [c]
            if return_group:
                out.append(G)
            if mapping:
                out.append(map)
            if generators:
                out.append(genset)
            return tuple(out)
        else:
            return c

    def is_self_complementary(self):
        r"""
        Check whether the graph is self-complementary.

        A (di)graph is self-complementary if it is isomorphic to its (di)graph
        complement. For instance, the path graph `P_4` and the cycle graph `C_5`
        are self-complementary.

        .. SEEALSO::

            - :wikipedia:`Self-complementary_graph`
            - :oeis:`A000171` for the numbers of self-complementary graphs of order `n`
            - :oeis:`A003086` for the numbers of self-complementary digraphs of order `n`.

        EXAMPLES:

        The only self-complementary path graph is `P_4`::

            sage: graphs.PathGraph(4).is_self_complementary()
            True
            sage: graphs.PathGraph(5).is_self_complementary()
            False

        The only self-complementary directed path is `P_2`::

            sage: digraphs.Path(2).is_self_complementary()
            True
            sage: digraphs.Path(3).is_self_complementary()
            False

        Every Paley graph is self-complementary::

            sage: G = graphs.PaleyGraph(9)
            sage: G.is_self_complementary()
            True

        TESTS:

        Trivial graphs and digraphs::

            sage: Graph(0).is_self_complementary()
            True
            sage: Graph(1).is_self_complementary()
            True
            sage: DiGraph(0).is_self_complementary()
            True
            sage: DiGraph(1).is_self_complementary()
            True

        Graph with the right number of edges that is not self-complementary::

            sage: G = graphs.CompleteGraph(6)
            sage: G.add_path([0, 6, 7, 8])
            sage: G.size() == G.order() * (G.order() - 1) // 4
            True
            sage: G.is_self_complementary()
            False

        The (di)graph must be simple::

            sage: Graph(loops=True, multiedges=True).is_self_complementary()
            Traceback (most recent call last):
            ...
            ValueError: This method is not known to work on graphs with
            multiedges/loops. Perhaps this method can be updated to handle them,
            but in the meantime if you want to use it please disallow
            multiedges/loops using allow_multiple_edges() and allow_loops().
            sage: DiGraph(loops=True, multiedges=True).is_self_complementary()
            Traceback (most recent call last):
            ...
            ValueError: This method is not known to work on graphs with
            multiedges/loops. Perhaps this method can be updated to handle them,
            but in the meantime if you want to use it please disallow
            multiedges/loops using allow_multiple_edges() and allow_loops().
        """
        self._scream_if_not_simple()

        if self.order() < 2:
            return True

        # A self-complementary graph has half the number of possible edges
        b = self.order() * (self.order() - 1) / (1 if self.is_directed() else 2)
        if b % 2 or b != 2 * self.size():
            return False

        # A self-complementary (di)graph must be connected
        if not self.is_connected():
            return False

        # A self-complementary graph of order >= 4 has diameter 2 or 3
        if not self.is_directed() and self.diameter() > 3:
            return False

        return self.is_isomorphic(self.complement())

    # Aliases to functions defined in other modules
    from sage.graphs.distances_all_pairs import distances_distribution
    from sage.graphs.base.boost_graph import dominator_tree
    from sage.graphs.base.static_sparse_graph import spectral_radius
    from sage.graphs.line_graph import line_graph
    from sage.graphs.connectivity import is_connected
    from sage.graphs.connectivity import connected_components
    from sage.graphs.connectivity import connected_components_number
    from sage.graphs.connectivity import connected_components_subgraphs
    from sage.graphs.connectivity import connected_component_containing_vertex
    from sage.graphs.connectivity import connected_components_sizes
    from sage.graphs.connectivity import blocks_and_cut_vertices
    from sage.graphs.connectivity import blocks_and_cuts_tree
    from sage.graphs.connectivity import is_cut_edge
    from sage.graphs.connectivity import is_cut_vertex
    from sage.graphs.connectivity import edge_connectivity
    from sage.graphs.connectivity import vertex_connectivity
    from sage.graphs.distances_all_pairs import szeged_index
    from sage.graphs.domination import dominating_set
    from sage.graphs.domination import greedy_dominating_set
    from sage.graphs.base.static_dense_graph import connected_subgraph_iterator
    from sage.graphs.path_enumeration import shortest_simple_paths
    from sage.graphs.path_enumeration import all_paths
    from sage.graphs.traversals import lex_BFS
    from sage.graphs.traversals import lex_UP
    from sage.graphs.traversals import lex_DFS
    from sage.graphs.traversals import lex_DOWN

    def katz_matrix(self, alpha, nonedgesonly=False, vertices=None):
        r"""
        Return the Katz matrix of the graph.

        Katz centrality of a node is a measure of centrality in a graph
        network. Katz centrality computes the relative influence of a node
        within a network. Connections made with distant neighbors are, however
        penalized by an attenuation factor `\alpha`.

        Adding the values in the Katz matrix of all columns in a particular row
        gives the Katz centrality measure of the vertex represented by that
        particular row.  Katz centrality measures influence by taking into
        account the total number of walks between a pair of nodes.

        See the :wikipedia:`Katz_centrality` for more information.

        INPUT:

        - ``alpha`` -- a nonnegative real number, must be less than the
          reciprocal of the spectral radius of the graph (the maximum
          absolute eigenvalue of the adjacency matrix)

        - ``nonedgesonly`` -- boolean (default: ``True``); if ``True``, value
          for each edge present in the graph is set to zero.

        - ``vertices`` -- list (default: ``None``); the ordering of the
          vertices defining how they should appear in the matrix. By default,
          the ordering given by :meth:`GenericGraph.vertices` is used.

        OUTPUT: the Katz matrix of the graph with parameter alpha

        EXAMPLES:

        We find the Katz matrix of an undirected 4-cycle.  ::

            sage: G = graphs.CycleGraph(4)
            sage: G.katz_matrix(1/20)
            [1/198  5/99 1/198  5/99]
            [ 5/99 1/198  5/99 1/198]
            [1/198  5/99 1/198  5/99]
            [ 5/99 1/198  5/99 1/198]

        We find the Katz matrix of an undirected 4-cycle with all entries
        other than those which correspond to non-edges zeroed out.  ::

            sage: G.katz_matrix(1/20, True)
            [    0     0 1/198     0]
            [    0     0     0 1/198]
            [1/198     0     0     0]
            [    0     1/198 0     0]

        This will give an error if alpha<=0 or alpha>=1/spectral_radius = 1/max
        (A.eigenvalues()).

        We find the Katz matrix in a fan on 6 vertices. ::

            sage: H = Graph([(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,2),(2,3),(3,4),(4,5)])
            sage: H.katz_matrix(1/10)
            [   169/2256    545/4512      25/188    605/4512      25/188    545/4512    485/4512]
            [   545/4512 7081/297792  4355/37224    229/9024   595/37224 4073/297792    109/9024]
            [     25/188  4355/37224    172/4653      45/376    125/4653   595/37224       5/376]
            [   605/4512    229/9024      45/376    337/9024      45/376    229/9024    121/9024]
            [     25/188   595/37224    125/4653      45/376    172/4653  4355/37224       5/376]
            [   545/4512 4073/297792   595/37224    229/9024  4355/37224 7081/297792    109/9024]
            [   485/4512    109/9024       5/376    121/9024       5/376    109/9024     97/9024]

        .. SEEALSO::

            * :meth:`~katz_centrality`
            * :wikipedia:`Katz_centrality`

        TESTS::

            sage: (graphs.CompleteGraph(4)).katz_matrix(1/4)
            [3/5 4/5 4/5 4/5]
            [4/5 3/5 4/5 4/5]
            [4/5 4/5 3/5 4/5]
            [4/5 4/5 4/5 3/5]
            sage: (graphs.CompleteGraph(4)).katz_matrix(1/4, nonedgesonly=True)
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            sage: (graphs.PathGraph(4)).katz_matrix(1/4, nonedgesonly=False)
            [15/209 60/209 16/209  4/209]
            [60/209 31/209 64/209 16/209]
            [16/209 64/209 31/209 60/209]
            [ 4/209 16/209 60/209 15/209]
            sage: (graphs.PathGraph(4)).katz_matrix(1/4, nonedgesonly=True)
            [     0      0 16/209  4/209]
            [     0      0      0 16/209]
            [16/209      0      0      0]
            [ 4/209 16/209      0      0]
        """
        if alpha <= 0:
            raise ValueError('the parameter alpha must be strictly positive')

        n = self.order()
        if not n:
            raise ValueError('graph is empty')
        if vertices is None:
            vertices = self.vertices(sort=True)
        elif (len(vertices) != n or
              set(vertices) != set(self)):
            raise ValueError("``vertices`` must be a permutation of the vertices")

        A = self.adjacency_matrix(vertices=vertices)

        spectral_radius = max([abs(eigen) for eigen in A.eigenvalues()])

        if spectral_radius == 0:
            raise ValueError('the spectral radius of the graph must not be zero')
        if alpha >= 1/spectral_radius:
            raise ValueError('the parameter alpha must be less than the reciprocal of the spectral radius of the graph')

        In = matrix.identity(n)
        K = (In - alpha * A.transpose()).inverse() - In
        if nonedgesonly:
            onesmat = matrix(QQ, n, n, lambda i, j: 1)
            Missing = onesmat - A - In
            return K.elementwise_product(Missing)
        else:
            return K

    def katz_centrality(self, alpha, u=None):
        r"""
        Return the Katz centrality of vertex `u`.

        Katz centrality of a node is a measure of centrality in a graph
        network. Katz centrality computes the relative influence of a node
        within a network. Connections made with distant neighbors are, however
        penalized by an attenuation factor `\alpha`.

        See the :wikipedia:`Katz_centrality` for more information.

        INPUT:

        - ``alpha`` -- a nonnegative real number, must be less than the
          reciprocal of the spectral radius of the graph (the maximum absolute
          eigenvalue of the adjacency matrix).

        - ``u`` -- the vertex whose Katz centrality needs to be measured
          (default: ``None``)

        OUTPUT: a list containing the Katz centrality of each vertex if u=None
        otherwise Katz centrality of the vertex u.

        EXAMPLES:

        We compute the Katz centrality of a 4-cycle (note that by symmetry,
        all 4 vertices have the same centrality) ::

            sage: G = graphs.CycleGraph(4)
            sage: G.katz_centrality(1/20)
            {0: 1/9, 1: 1/9, 2: 1/9, 3: 1/9}

        Note that in the below example the nodes having indegree `0` also have
        the Katz centrality value as `0`, as these nodes are not influenced by
        other nodes. ::

            sage: G = DiGraph({1: [10], 2:[10,11], 3:[10,11], 4:[], 5:[11, 4], 6:[11], 7:[10,11], 8:[10,11], 9:[10], 10:[11, 5, 8], 11:[6]})
            sage: G.katz_centrality(.85) # rel tol 1e-14
            {1: 0.000000000000000,
             2: 0.000000000000000,
             3: 0.000000000000000,
             4: 16.7319819819820,
             5: 18.6846846846847,
             6: 173.212076941807,
             7: 0.000000000000000,
             8: 18.6846846846847,
             9: 0.000000000000000,
             10: 20.9819819819820,
             11: 202.778914049184}


        .. SEEALSO::

            * :meth:`~katz_matrix`
            * :wikipedia:`Katz_centrality`

        TESTS::

            sage: graphs.PathGraph(3).katz_centrality(1/20)
            {0: 11/199, 1: 21/199, 2: 11/199}
            sage: graphs.PathGraph(4).katz_centrality(1/20)
            {0: 21/379, 1: 41/379, 2: 41/379, 3: 21/379}
            sage: graphs.PathGraph(3).katz_centrality(1/20,2)
            11/199
            sage: graphs.PathGraph(4).katz_centrality(1/20,3)
            21/379
            sage: (graphs.PathGraph(3) + graphs.PathGraph(4)).katz_centrality(1/20)
            {0: 11/199, 1: 21/199, 2: 11/199, 3: 21/379, 4: 41/379, 5: 41/379, 6: 21/379}

        """
        n = self.order()
        if n == 0:
            raise ValueError('graph is empty')

        if u and u not in self:
            raise ValueError("vertex ({0}) is not a vertex of the graph".format(repr(u)))

        if u:
            if self.is_connected():
                G = self
            else:
                G = self.subgraph(self.connected_component_containing_vertex(u, sort=False))
            verts = list(G)
            M = G.katz_matrix(alpha, nonedgesonly=False, vertices=verts)
            return sum(M[verts.index(u)])

        if self.is_connected():
            verts = list(self)
            M = self.katz_matrix(alpha, nonedgesonly=False, vertices=verts)
            return {u: sum(M[i]) for i, u in enumerate(verts)}
        else:
            K = {}
            for g in self.connected_components_subgraphs():
                verts = list(g)
                M = g.katz_matrix(alpha, nonedgesonly=False, vertices=verts)
                K.update({u: sum(M[i]) for i, u in enumerate(verts)})
            return K

    def edge_polytope(self, backend=None):
        r"""
        Return the edge polytope of ``self``.

        The edge polytope (EP) of a Graph on `n` vertices
        is the polytope in `\ZZ^{n}` defined as the convex hull of
        `e_i + e_j` for each edge `(i, j)`.
        Here `e_1, \dots, e_n` denotes the standard basis.

        INPUT:

        - ``backend`` -- string or ``None`` (default); the backend to use;
          see :meth:`sage.geometry.polyhedron.constructor.Polyhedron`

        EXAMPLES:

        The EP of a `4`-cycle is a square::

            sage: G = graphs.CycleGraph(4)
            sage: P = G.edge_polytope(); P
            A 2-dimensional polyhedron in ZZ^4 defined as the convex hull of 4 vertices

        The EP of a complete graph on `4` vertices is cross polytope::

            sage: G = graphs.CompleteGraph(4)
            sage: P = G.edge_polytope(); P
            A 3-dimensional polyhedron in ZZ^4 defined as the convex hull of 6 vertices
            sage: P.is_combinatorially_isomorphic(polytopes.cross_polytope(3))
            True

        The EP of a graph is isomorphic to the subdirect sum of
        its connected components EPs::

            sage: n = randint(3, 6)
            sage: G1 = graphs.RandomGNP(n, 0.2)
            sage: n = randint(3, 6)
            sage: G2 = graphs.RandomGNP(n, 0.2)
            sage: G = G1.disjoint_union(G2)
            sage: P = G.edge_polytope()
            sage: P1 = G1.edge_polytope()
            sage: P2 = G2.edge_polytope()
            sage: P.is_combinatorially_isomorphic(P1.subdirect_sum(P2))
            True

        All trees on `n` vertices have isomorphic EPs::

            sage: n = randint(4, 10)
            sage: G1 = graphs.RandomTree(n)
            sage: G2 = graphs.RandomTree(n)
            sage: P1 = G1.edge_polytope()
            sage: P2 = G2.edge_polytope()
            sage: P1.is_combinatorially_isomorphic(P2)
            True

        However, there are still many different EPs::

            sage: len(list(graphs(5)))
            34
            sage: polys = []
            sage: for G in graphs(5):
            ....:     P = G.edge_polytope()
            ....:     for P1 in polys:
            ....:         if P.is_combinatorially_isomorphic(P1):
            ....:             break
            ....:     else:
            ....:         polys.append(P)
            sage: len(polys)
            19

        TESTS:

        Obtain the EP with unsortable vertices::

            sage: G = Graph([[1, (1, 2)]])
            sage: G.edge_polytope()
            A 0-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex
        """
        from sage.matrix.special import identity_matrix
        from sage.geometry.polyhedron.parent import Polyhedra
        dim = self.num_verts()
        e = identity_matrix(dim).rows()
        dic = {v: e[i] for i, v in enumerate(self)}
        vertices = ((dic[i] + dic[j]) for i, j in self.edge_iterator(sort_vertices=False, labels=False))
        parent = Polyhedra(ZZ, dim, backend=backend)
        return parent([vertices, [], []], None)

    def symmetric_edge_polytope(self, backend=None):
        r"""
        Return the symmetric edge polytope of ``self``.

        The symmetric edge polytope (SEP) of a Graph on `n` vertices
        is the polytope in `\ZZ^{n}` defined as the convex hull of
        `e_i - e_j` and `e_j - e_i` for each edge `(i, j)`.
        Here `e_1, \dots, e_n` denotes the standard basis.

        INPUT:

        - ``backend`` -- string or ``None`` (default); the backend to use;
          see :meth:`sage.geometry.polyhedron.constructor.Polyhedron`

        EXAMPLES:

        The SEP of a `4`-cycle is a cube::

            sage: G = graphs.CycleGraph(4)
            sage: P = G.symmetric_edge_polytope(); P
            A 3-dimensional polyhedron in ZZ^4 defined as the convex hull of 8 vertices
            sage: P.is_combinatorially_isomorphic(polytopes.cube())
            True

        The SEP of a complete graph on `4` vertices is a cuboctahedron::

            sage: G = graphs.CompleteGraph(4)
            sage: P = G.symmetric_edge_polytope(); P
            A 3-dimensional polyhedron in ZZ^4 defined as the convex hull of 12 vertices
            sage: P.is_combinatorially_isomorphic(polytopes.cuboctahedron())
            True

        The SEP of a graph with edges on `n` vertices has dimension `n`
        minus the number of connected components::

            sage: n = randint(5, 12)
            sage: G = Graph()
            sage: while not G.num_edges():
            ....:     G = graphs.RandomGNP(n, 0.2)
            sage: P = G.symmetric_edge_polytope()
            sage: P.ambient_dim() == n
            True
            sage: P.dim() == n - G.connected_components_number()
            True

        The SEP of a graph is isomorphic to the subdirect sum of
        its connected components SEP's::

            sage: n = randint(3, 6)
            sage: G1 = graphs.RandomGNP(n, 0.2)
            sage: n = randint(3, 6)
            sage: G2 = graphs.RandomGNP(n, 0.2)
            sage: G = G1.disjoint_union(G2)
            sage: P = G.symmetric_edge_polytope()
            sage: P1 = G1.symmetric_edge_polytope()
            sage: P2 = G2.symmetric_edge_polytope()
            sage: P.is_combinatorially_isomorphic(P1.subdirect_sum(P2))
            True

        All trees on `n` vertices have isomorphic SEPs::

            sage: n = randint(4, 10)
            sage: G1 = graphs.RandomTree(n)
            sage: G2 = graphs.RandomTree(n)
            sage: P1 = G1.symmetric_edge_polytope()
            sage: P2 = G2.symmetric_edge_polytope()
            sage: P1.is_combinatorially_isomorphic(P2)
            True

        However, there are still many different SEPs::

            sage: len(list(graphs(5)))
            34
            sage: polys = []
            sage: for G in graphs(5):
            ....:     P = G.symmetric_edge_polytope()
            ....:     for P1 in polys:
            ....:         if P.is_combinatorially_isomorphic(P1):
            ....:             break
            ....:     else:
            ....:         polys.append(P)
            sage: len(polys)
            25

        A non-trivial example of two graphs with isomorphic SEPs::

            sage: G1 = graphs.CycleGraph(4)
            sage: G1.add_edges([[0, 5], [5, 2], [1, 6], [6, 2]])
            sage: G2 = copy(G1)
            sage: G1.add_edges([[2, 7], [7, 3]])
            sage: G2.add_edges([[0, 7], [7, 3]])
            sage: G1.is_isomorphic(G2)
            False
            sage: P1 = G1.symmetric_edge_polytope()
            sage: P2 = G2.symmetric_edge_polytope()
            sage: P1.is_combinatorially_isomorphic(P2)
            True

        Apparently, glueing two graphs together on a vertex
        gives isomorphic SEPs::

            sage: n = randint(3, 7)
            sage: g1 = graphs.RandomGNP(n, 0.2)
            sage: g2 = graphs.RandomGNP(n, 0.2)
            sage: G = g1.disjoint_union(g2)
            sage: H = copy(G)
            sage: G.merge_vertices(((0, randrange(n)), (1, randrange(n))))
            sage: H.merge_vertices(((0, randrange(n)), (1, randrange(n))))
            sage: PG = G.symmetric_edge_polytope()
            sage: PH = H.symmetric_edge_polytope()
            sage: PG.is_combinatorially_isomorphic(PH)
            True

        TESTS:

        Obtain the SEP with unsortable vertices::

            sage: G = Graph([[1, (1, 2)]])
            sage: G.symmetric_edge_polytope()
            A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
        """
        from itertools import chain
        from sage.matrix.special import identity_matrix
        from sage.geometry.polyhedron.parent import Polyhedra
        dim = self.num_verts()
        e = identity_matrix(dim).rows()
        dic = {v: e[i] for i, v in enumerate(self)}
        vertices = chain(((dic[i] - dic[j]) for i, j in self.edge_iterator(sort_vertices=False, labels=False)),
                         ((dic[j] - dic[i]) for i, j in self.edge_iterator(sort_vertices=False, labels=False)))
        parent = Polyhedra(ZZ, dim, backend=backend)
        return parent([vertices, [], []], None)


def tachyon_vertex_plot(g, bgcolor=(1, 1, 1),
                        vertex_colors=None,
                        vertex_size=0.06,
                        pos3d=None,
                        **kwds):
    """
    Helper function for plotting graphs in 3d with
    :class:`~sage.plot.plot3d.tachyon.Tachyon`.

    Returns a plot containing only the vertices, as well as the 3d position
    dictionary used for the plot.

    INPUT:
     - ``pos3d`` -- a 3D layout of the vertices

     - various rendering options

    EXAMPLES::

        sage: G = graphs.TetrahedralGraph()
        sage: from sage.graphs.generic_graph import tachyon_vertex_plot
        sage: T,p = tachyon_vertex_plot(G, pos3d=G.layout(dim=3))
        sage: type(T)
        <class 'sage.plot.plot3d.tachyon.Tachyon'>
        sage: type(p)
        <... 'dict'>
    """
    assert pos3d is not None
    from math import sqrt
    from sage.plot.plot3d.tachyon import Tachyon

    c = [0, 0, 0]
    r = []
    verts = list(g)

    if vertex_colors is None:
        vertex_colors = {(1, 0, 0): verts}
    try:
        for v in verts:
            c[0] += pos3d[v][0]
            c[1] += pos3d[v][1]
            c[2] += pos3d[v][2]
    except KeyError:
        raise KeyError("you have not specified positions for all the vertices")

    order = g.order()
    c[0] /= order
    c[1] /= order
    c[2] /= order
    for v in verts:
        pos3d[v][0] -= c[0]
        pos3d[v][1] -= c[1]
        pos3d[v][2] -= c[2]
        r.append(abs(sqrt((pos3d[v][0])**2 + (pos3d[v][1])**2 + (pos3d[v][2])**2)))
    r = max(r)
    if not r:
        r = 1
    for v in verts:
        pos3d[v][0] /= r
        pos3d[v][1] /= r
        pos3d[v][2] /= r
    TT = Tachyon(camera_center=(1.4, 1.4, 1.4), antialiasing=13, **kwds)
    TT.light((4, 3, 2), 0.02, (1, 1, 1))
    TT.texture('bg', ambient=1, diffuse=1, specular=0, opacity=1.0, color=bgcolor)
    TT.plane((-1.6, -1.6, -1.6), (1.6, 1.6, 1.6), 'bg')

    i = 0
    for color in vertex_colors:
        i += 1
        TT.texture('node_color_%d' % i, ambient=0.1, diffuse=0.9,
                   specular=0.03, opacity=1.0, color=color)
        for v in vertex_colors[color]:
            TT.sphere((pos3d[v][0], pos3d[v][1], pos3d[v][2]), vertex_size, 'node_color_%d' % i)

    return TT, pos3d


def graph_isom_equivalent_non_edge_labeled_graph(g, partition=None, standard_label=None,
                                                 return_relabeling=False, return_edge_labels=False,
                                                 inplace=False, ignore_edge_labels=False):
    r"""
    Helper function for canonical labeling of edge labeled (di)graphs.

    Translates to a bipartite incidence-structure type graph appropriate for
    computing canonical labels of edge labeled and/or multi-edge graphs.
    Note that this is actually computationally equivalent to implementing a
    change on an inner loop of the main algorithm -- namely making the
    refinement procedure sort for each label.

    If the graph is a multigraph, it is translated to a non-multigraph,
    where each instance of multiple edges is converted to a single
    edge labeled with a list ``[[label1, multiplicity], [label2,
    multiplicity], ...]`` describing how many edges of each label were
    originally there. Then in either case we are working on a graph
    without multiple edges. At this point, we create another
    (partially bipartite) graph, whose left vertices are the original
    vertices of the graph, and whose right vertices represent the
    labeled edges. Any unlabeled edges in the original graph are also
    present in the new graph, and -- this is the bipartite aspect --
    for every labeled edge `e` from `v` to `w` in the original graph,
    there is an edge between the right vertex corresponding to `e` and
    each of the left vertices corresponding to `v` and `w`. We
    partition the left vertices as they were originally, and the right
    vertices by common labels: only automorphisms taking edges to
    like-labeled edges are allowed, and this additional partition
    information enforces this on the new graph.

    INPUT:

    - ``g`` -- Graph or DiGraph

    - ``partition`` -- list (default: ``None``); a partition of the
      vertices as a list of lists of vertices. If given, the partition
      of the vertices is as well relabeled

    - ``standard_label`` -- (default: ``None``); edges in ``g`` with
      this label are preserved in the new graph

    - ``return_relabeling`` -- boolean (default: ``False``); whether
      to return a dictionary containing the relabeling

    - ``return_edge_labels`` -- boolean (default: ``False``); whether
      the different ``edge_labels`` are returned (useful if inplace is
      ``True``)

    - ``inplace`` -- boolean (default: ``False``); whether the input
      (di)graph ``g`` is modified or the return a new (di)graph. Note
      that attributes of ``g`` are *not* copied for speed issues, only
      edges and vertices.

    - ``ignore_edge_labels`` -- boolean (default: ``False``): if
      ``True``, ignore edge labels, so when constructing the new
      graph, only multiple edges are replaced with vertices. Labels on
      multiple edges are ignored -- only the multiplicity is relevant,
      so multiple edges with the same multiplicity in the original
      graph correspond to right vertices in the same partition in the
      new graph.

    OUTPUT:

    - if ``inplace`` is ``False``: the unlabeled graph without
      multiple edges
    - the partition of the vertices
    - if ``return_relabeling`` is ``True``: a dictionary containing
      the relabeling
    - if ``return_edge_labels`` is ``True``: the list of (former) edge
      labels is returned

    EXAMPLES::

        sage: from sage.graphs.generic_graph import graph_isom_equivalent_non_edge_labeled_graph

        sage: G = Graph(multiedges=True,sparse=True)
        sage: G.add_edges((0, 1, i) for i in range(10))
        sage: G.add_edge(1,2,'string')
        sage: G.add_edge(2,123)
        sage: graph_isom_equivalent_non_edge_labeled_graph(G, partition=[[0,123],[1,2]])
        [Graph on 6 vertices, [[1, 0], [2, 3], [5], [4]]]

        sage: g, part = graph_isom_equivalent_non_edge_labeled_graph(G)
        sage: g, sorted(part)
        (Graph on 6 vertices, [[0, 1, 2, 3], [4], [5]])
        sage: g.edges(sort=True)
        [(0, 3, None), (1, 4, None), (2, 4, None), (2, 5, None), (3, 5, None)]

        sage: g = graph_isom_equivalent_non_edge_labeled_graph(G,standard_label='string',return_edge_labels=True)
        sage: g[0]
        Graph on 6 vertices
        sage: g[0].edges(sort=True)
        [(0, 5, None), (1, 4, None), (2, 3, None), (2, 4, None), (3, 5, None)]
        sage: g[1]
        [[0, 1, 2, 3], [4], [5]]
        sage: g[2]
        [[['string', 1]], [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]], [[None, 1]]]

        sage: graph_isom_equivalent_non_edge_labeled_graph(G, inplace=True)
        [[[0, 1, 2, 3], [5], [4]]]
        sage: G.edges(sort=True)
        [(0, 3, None), (1, 4, None), (2, 4, None), (2, 5, None), (3, 5, None)]

        sage: G = Graph(multiedges=True,sparse=True)
        sage: G.add_edges((0, 1) for i in range(10))
        sage: G.add_edge(1, 2, 'a')
        sage: G.add_edge(1, 3, 'b')
        sage: G.add_edge(2, 3, 'b')
        sage: graph_isom_equivalent_non_edge_labeled_graph(G)[0]
        Graph on 8 vertices
        sage: graph_isom_equivalent_non_edge_labeled_graph(G, ignore_edge_labels=True)[0]
        Graph on 5 vertices

        sage: G = Graph(multiedges=True,sparse=True)
        sage: G.add_edges((0, 1, i) for i in range(5))
        sage: G.add_edges((0, 2, i+10) for i in range(5))
        sage: G.add_edges((0, 3) for i in range(4))
        sage: g0 = graph_isom_equivalent_non_edge_labeled_graph(G)
        sage: g1 = graph_isom_equivalent_non_edge_labeled_graph(G, ignore_edge_labels=True)
        sage: g0
        [Graph on 7 vertices, [[0, 1, 2, 3], [4], [5], [6]]]
        sage: g1
        [Graph on 7 vertices, [[0, 1, 2, 3], [6], [4, 5]]]

    TESTS:

    Ensure that :trac:`14108` is fixed::

        sage: G=DiGraph({0:[0,0,0],1:[1,1,1]})
        sage: H=DiGraph({0:[0,0,0,0],1:[1,1]})
        sage: G.is_isomorphic(H)
        False
        sage: H=DiGraph({0:[0,0,0,0],1:[1,1]})
        sage: HH=DiGraph({0:[0,0,0],1:[1,1,1]})
        sage: H.is_isomorphic(HH)
        False
        sage: H.is_isomorphic(HH, edge_labels=True)
        False

    Note that the new graph need not be bipartite::

        sage: G = Graph(multiedges=True,sparse=True)
        sage: G.add_edges((0, 1) for i in range(10))
        sage: G.add_edge(1,2)
        sage: G.add_edge(1,3)
        sage: G.add_edge(2,3)
        sage: g = graph_isom_equivalent_non_edge_labeled_graph(G)
        sage: g[0].is_bipartite()
        False
    """
    from sage.graphs.graph import Graph
    from sage.graphs.digraph import DiGraph
    from itertools import chain

    g_has_multiple_edges = g.has_multiple_edges()

    if g_has_multiple_edges:
        # We build a **simple** (Di)Graph G where the label of edge uv is a list
        # [[label, multiplicity], [label, multiplicity], ...] encoding the
        # number of edges uv in g with same label
        if g._directed:
            G = DiGraph(loops=g.allows_loops(), sparse=True)
            edge_iter = g._backend.iterator_in_edges(g, False)
        else:
            G = Graph(loops=g.allows_loops(), sparse=True)
            edge_iter = g._backend.iterator_edges(g, False)

        for u, v in edge_iter:
            if G.has_edge(u, v):
                continue
            # We count the number of occurrences of each distinct label
            if ignore_edge_labels:
                G.add_edge(u, v, [[None, len(g.edge_label(u, v))]])
            else:
                label_list = []
                for l in g.edge_label(u, v):
                    seen_label = False
                    for elt in label_list:
                        if elt[0] == l:
                            elt[1] += 1
                            seen_label = True
                            break
                    if not seen_label:
                        label_list.append([l, 1])

                # We sort label_list to enable equality check.
                # The use of key=str should be enough...
                label_list = sorted(label_list, key=str)

                # We add edge u,v to G, labeled with label_list
                G.add_edge(u, v, label_list)

        if G.order() < g.order():
            G.add_vertices(g)
        if inplace:
            g._backend = G._backend
    elif not inplace:
        G = copy(g)
    else:
        G = g

    G_order = G.order()
    # Do not relabel if the set of vertices is equal to the set range(n).
    # This helps to ensure that *equal* graphs on range(n) yield *equal* (not
    # just isomorphic) canonical labelings. This is just a convenience, there is
    # no mathematical meaning.
    if set(G) != set(range(G_order)):
        relabel_dict = G.relabel(return_map=True, inplace=True)
    else:
        # Do not relabel but ensure that labels are Python ints
        relabel_dict = {i: int(i) for i in G}

    if partition is None:
        partition = [list(G)]
    else:
        # We relabel as well the vertices of the partition
        partition = [[relabel_dict[i] for i in part] for part in partition]

    # We build the list of distinct edge labels
    edge_labels = []
    for _, _, label in G.edge_iterator():
        if label != standard_label and label not in edge_labels:
            edge_labels.append(label)

    edge_labels = sorted(edge_labels, key=str)

    # We now add to G, for each edge (u, v, l), a new vertex i in [n..n + m] and
    # arcs (u, i, None) and (i, v, None). We record for each distinct label l
    # the list of added vertices.

    edge_partition = [(el, []) for el in edge_labels]

    if g_has_multiple_edges:
        standard_label = [[standard_label, 1]]

    if G._directed:
        edges = list(G._backend.iterator_in_edges(G, True))
    else:
        edges = list(G._backend.iterator_edges(G, True))

    i = G_order
    for u, v, l in edges:
        if l != standard_label:
            for el, part in edge_partition:
                if el == l:
                    part.append(i)
                    break

            G._backend.add_edge(u, i, None, True)
            G._backend.add_edge(i, v, None, True)
            G.delete_edge(u, v)
            i += 1

        elif standard_label is not None:
            G._backend.set_edge_label(u, v, None, True)

    # Should we pay attention to edge labels ?
    if ignore_edge_labels:

        if g_has_multiple_edges:
            # An edge between u and v with label l and multiplicity k being
            # encoded as an uv edge with label [l,k], we must not assume that an
            # edge with multiplicity 2 is equivalent to a simple edge !
            # Hence, we still distinguish edges with different multiplicity

            # Gather the partitions of edges with same multiplicity
            tmp = {}
            for el, part in edge_partition:
                # The multiplicity of a label is the number of edges from u to v
                # it represents
                m = sum((y[1] for y in el))
                if m in tmp:
                    tmp[m].append(part)
                else:
                    tmp[m] = part

            # Flatten edge_partition to [list of edges, list of edges, ...]
            # The groups are ordered by increasing multiplicity
            edge_partition = [tmp[mu] for mu in sorted(tmp.keys())]

            # Now the edges are partitionned according to the multiplicity they
            # represent, and edge labels are forgotten.

        else:
            # If there are no multiple edges, we can just say that all edges are
            # equivalent to each other without any further consideration.
            edge_partition = [el[1] for el in edge_partition]
            edge_partition = [list(chain(*edge_partition))]

    else:
        # Flatten edge_partition to [list of edges, list of edges, ...]
        edge_partition = [part for _, part in edge_partition]

    new_partition = [part for part in chain(partition, edge_partition) if part]

    return_data = []
    if not inplace:
        return_data.append(G)
    return_data.append(new_partition)
    if return_relabeling:
        return_data.append(relabel_dict)
    if return_edge_labels:
        return_data.append(edge_labels)
    return return_data
