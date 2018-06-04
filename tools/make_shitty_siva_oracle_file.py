import json

file = '/home/michael/Projects/QuestionAnswering/GCNQA3/data/webquestions/en-bilty-bist-webquestions.test.deplambda.json'

f1s = 0.0
count = 0

graphlet_dict = {}

with open(file, "r") as data_file:
    for line in data_file:
        json_line = json.loads(line)
        key = json_line["original"].replace(" ", "")
        pairs = []

        count += 1

        if "goldRelations" not in json_line:
            continue

        relations = json_line["goldRelations"]
        seen = {}
        for f in json_line["forest"]:
            entities = f["entities"]
            for entity in entities:
                if entity["entity"] in seen:
                    continue

                seen[entity["entity"]] = entity

        greedy_entity = "http://rdf.freebase.com/ns/" + entities[0]["entity"]

        greedy_relation = relations[0]

        print(greedy_entity)
        print((list(seen.values()), relations))
        exit()

print(f1s/count)