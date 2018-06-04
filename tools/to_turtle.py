import argparse

parser = argparse.ArgumentParser(description='Indexes a graph')
parser.add_argument('--graph', type=str, help='The location of the graph')
args = parser.parse_args()

for line in open(args.graph):
    line = line.strip()
    line_parts = line.split("\t")

    output = []

    for line_part in line_parts:
        if line_part.endswith("@en"):
            parts = line_part.split("@en")
            output.append("\"" + parts[0] + "\"@en")
        elif "^^" in line_part:
            parts = line_part.split("^^")
            output.append("\"" + parts[0] + "\"^^" + parts[1])
        elif line_part.startswith("http"):
            output.append("<" + line_part + ">")

    if len(output) == 3:
        print("\t".join(output))
    else:
        print(line_parts)
        exit()
