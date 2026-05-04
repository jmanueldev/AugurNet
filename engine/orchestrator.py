import torch
import numpy as np

from models.encoder import CrossModalEncoder
from models.polysemantic import PolysemanticLatent
from ghe.engine_transformer import HypothesisEngine
from ghe.engine_heuristic import HeuristicEngine
from engine.iteration import IterativeInterpreter
from causal.graph_builder import CausalGraphBuilder
from ingestion.log_parser import DrainParser
from models.bert_encoder import BertLogEncoder
from feature_store.redis_store import RedisFeatureStore
from engine.ghe_client import call_ghes
from causal.neo4j_graph import Neo4jGraph

parser = DrainParser()
bert = BertLogEncoder()
store = RedisFeatureStore()
graph = Neo4jGraph("bolt://localhost:7687", "neo4j", "password")


encoder = CrossModalEncoder()
latent_model = PolysemanticLatent()
ghe1 = HypothesisEngine()
ghe2 = HeuristicEngine()
interpreter = IterativeInterpreter()
graph_builder = CausalGraphBuilder()


def tokenize(texts):
    # dummy tokenizer
    return torch.randint(0, 999, (len(texts), 5))


def metrics_to_vec(metrics_list):
    vec = []
    for m in metrics_list:
        arr = list(m.values())[:8]
        arr += [0] * (8 - len(arr))
        vec.append(arr)
    return torch.tensor(vec).float()


def run_pipeline(events):
    logs = [parser.parse(e["message"]) for e in events]

    embeddings = bert.encode(logs)

    store.set_feature("latest_embeddings", embeddings.tolist())

    ghe_results = call_ghes(embeddings)

    for i, src in enumerate(logs):
        for j, dst in enumerate(logs):
            if i != j:
                graph.add_edge(src, dst, 0.5)

    return graph.get_root_causes()