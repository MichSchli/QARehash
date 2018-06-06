import json

file = '/home/michael/Projects/QuestionAnswering/GCNQA3/data/webquestions/en-bilty-bist-webquestions.test.deplambda.json'
outfile = open('/home/michael/Projects/QuestionAnswering/GCNQA3/data/webquestions/shitty_oracle_test.txt', 'w')

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

        gold = json_line["targetValue"][7:-2]
        gold = gold.split(") (")
        gold = [g[12:].replace("\"", "") for g in gold]

        for entity in seen.values():
            entity = "http://rdf.freebase.com/ns/" + entity["entity"]
            left_relation = relations[0]["relationLeft"]
            right_relation = relations[0]["relationRight"]
            print("\t".join([entity, left_relation, right_relation, "||".join(gold)]), file=outfile)

        print("", file=outfile)