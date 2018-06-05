from indexes.element_cache import ElementCache
from indexes.element_index import ElementIndex
import numpy as np

inf = '/home/michael/Projects/QuestionAnswering/GCNQA3/data/toy-125/shitty_oracle.txt'

entity_cache = ElementCache("/home/michael/Projects/QuestionAnswering/GCNQA3/data/toy-125/cache/graph_cache.entities")
event_cache = ElementCache("/home/michael/Projects/QuestionAnswering/GCNQA3/data/toy-125/cache/graph_cache.events")
vertex_index = ElementIndex("/home/michael/Projects/QuestionAnswering/GCNQA3/data/toy-125/cache/vertex_index")
relation_index = ElementIndex("/home/michael/Projects/QuestionAnswering/GCNQA3/data/toy-125/cache/relation_index")

def f1(predicted_labels, true_labels):
    true_positives = np.isin(predicted_labels, true_labels)
    false_positives = np.logical_not(true_positives)
    false_negatives = np.isin(true_labels, predicted_labels, invert=True)

    if np.sum(true_positives) + np.sum(false_positives) == 0:
        inner_precision = 1.0
    else:
        inner_precision = np.sum(true_positives) / (np.sum(true_positives) + np.sum(false_positives))

    if np.sum(true_positives) + np.sum(false_negatives) == 0:
        inner_recall = 1.0
    else:
        inner_recall = np.sum(true_positives) / (np.sum(true_positives) + np.sum(false_negatives))

    if inner_precision + inner_recall > 0:
        inner_f1 = 2 * (inner_precision * inner_recall) / (inner_precision + inner_recall)
    else:
        inner_f1 = 0

    return inner_f1

total_f1 = 0
count = 0

for line in open(inf):
    line = line.strip()
    if line:
        count += 1
        parts = line.split("\t")
        entity_index = vertex_index.to_index(parts[0])
        graphlet = entity_cache.get(entity_index)

        left_relation = parts[1]
        right_relation = parts[2]

        if left_relation.endswith(".1") and right_relation.endswith(".2"):
            idx = relation_index.to_index(left_relation[:-2])
            target = graphlet.entities[idx]
        elif left_relation.endswith(".2") and right_relation.endswith(".1"):
            idx = relation_index.to_index(left_relation[:-2])
            target = graphlet.entity_inverses[idx]
        else:
            if left_relation.endswith(".inverse"):
                idx = relation_index.to_index(left_relation[:-8])
                events = graphlet.event_inverses[idx]
            else:
                idx = relation_index.to_index(left_relation)
                events = graphlet.events[idx]

            event_graphlets = [event_cache.get(event) for event in events]
            target = []

            for event_graphlet in event_graphlets:
                if right_relation.endswith(".inverse"):
                    idx = relation_index.to_index(right_relation[:-8])
                    new_targets = event_graphlet.entity_inverses[idx] if idx in event_graphlet.entity_inverses else []
                else:
                    idx = relation_index.to_index(right_relation)
                    new_targets = event_graphlet.entities[idx] if idx in event_graphlet.entities else []

                target.extend(new_targets)

        target_texts = [vertex_index.from_index(t) for t in target]
        gold = parts[-1].split(",")

        print(target_texts)
        print(gold)

        f1_h = f1(target_texts, gold)
        print(f1_h)

        total_f1 += f1_h

print(total_f1/count)