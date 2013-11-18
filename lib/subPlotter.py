from lib.similarity import Similarity
import networkx as nx
import matplotlib.pyplot as plt
import config
class SubPlotter():

    def __init__(self,plot,input_feed,output_feed):
        self.plot=plot
        self.node_color=[]
        self.node_size=[]

        self.input_feeds=input_feed.split(",")
        self.output_feeds=output_feed.split(",")
        self.input_seeds=self.get_seed_nodes(self.input_feeds,True)
        self.output_seeds=self.get_seed_nodes(self.output_feeds,False)
        self.visited=self.input_seeds[:]
        self.K=self.input_seeds[:]
        self.subgraph=self.get_sub_graph()
        self.H=self.plot.G.subgraph(self.subgraph)

    def show(self):
        for v in self.H:
            self.node_size.append(500)
            if v in self.plot.operation_nodes:
                self.node_color.append(1.0)
            elif v in self.plot.input_nodes:
                self.node_color.append(2.0)
            else:
                self.node_color.append(3.0)

        nx.draw(self.H,node_color=self.node_color,node_size=self.node_size,alpha=0.3,edge_color='b',font_size=8)
        plt.savefig("joker.png")
        plt.show()

    def get_sub_graph(self):
        while len(self.K)>0:
            for n in self.K[:]:
                self.K.remove(n)
                self.visited.append(n)

                if self.is_complete():
                    return self.get_graph_nodes()

                # expand
                for node in self.nodes_from_node(n):
                    # if or node
                    if node in self.plot.input_nodes or node in self.plot.output_nodes:
                        if not node in self.visited:
                            self.K.append(node)
                    # and node
                    else:
                        # see if all parents are visited
                        is_all_parents_visited=True
                        for parent in self.nodes_to_node(node):
                            if parent not in self.visited:
                                is_all_parents_visited=False

                        if is_all_parents_visited:
                            if not node in self.visited:
                                self.K.append(node)

        return []

    def get_graph_nodes(self):
        leaf=[]
        graph_nodes=[]
        print  self.visited
        for feed in self.output_feeds:
            for node in self.output_seeds:
                if node in self.visited and Similarity(feed,self.name_from_node(node)).value > config.threshold:
                    leaf.append(node)
        print leaf
        for node in leaf:
            graph_nodes.append(node)
            self.add_parents(node,graph_nodes)
        print graph_nodes
        return graph_nodes

    def add_parents(self,src,graph_nodes):
        if src in self.input_seeds:
            return
        for node in self.nodes_to_node(src):
            if node in self.visited:
                print node
                graph_nodes.append(node)
                self.add_parents(node,graph_nodes)

    def is_complete(self):
        visited_feeds=set()
        for feed in self.output_feeds:
            for visited in set(self.visited):
                #if self.name_from_node(visited)==feed:
                if Similarity(feed,self.name_from_node(visited)).value > config.threshold and visited in self.plot.output_nodes:
                    visited_feeds.add(feed)
        #print Similarity("book",self.name_from_node("_BOOK 19"))
        print  len(visited_feeds),len(self.output_feeds)
        return len(visited_feeds) == len(self.output_feeds)

    def get_seed_nodes(self,feeds,isInput):
        result = []
        if isInput:
            nodes=self.plot.input_nodes
        else:
            nodes=self.plot.output_nodes

        for feed in feeds:
            for node in nodes:
                #print node,Similarity("university","researcherAddress").value
                #print self.name_from_node(node),feed,Similarity(self.name_from_node(node),feed).value
                if Similarity(self.name_from_node(node),feed).value >config.threshold:
                    result.append(node)
        return result

    def nodes_to_node(self,node):
        nodes = []
        for edge in self.plot.G.edges():
            if edge[1] == node:
                nodes.append(edge[0])
        return nodes

    def nodes_from_node(self,node):
        nodes = []
        for edge in self.plot.G.edges():
            if edge[0] == node:
                nodes.append(edge[1])
        return nodes

    def name_from_node(self,node):
        return " ".join(node.split(" ")[:1])

    def nodes_from_name(self):
        pass
