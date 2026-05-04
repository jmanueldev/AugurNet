import networkx as nx

class CausalGraphBuilder:
    def __init__(self):
        self.graph = nx.DiGraph()

    def reset(self):
        self.graph.clear()

    def add_hypothesis(self, events, scores):
        for i, src in enumerate(events):
            for j, dst in enumerate(events):
                if i != j:
                    weight = scores[i] * scores[j]
                    self.graph.add_edge(src, dst, weight=weight)

    def rank_root_causes(self):
        return sorted(
            self.graph.nodes,
            key=lambda n: self.graph.out_degree(n, weight="weight"),
            reverse=True
        )