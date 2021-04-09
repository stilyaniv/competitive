import os
from queue import SimpleQueue

import regex
from graphviz import Digraph

INPUT_FILE_PATH = "inputs/day_7_input.txt"


def parse_rule(rule_description, include_weights=False):
    if include_weights:
        pattern = regex.compile(r"([1-9])? ?([a-zA-Z]+ [a-zA-Z]+) bag")
    else:
        pattern = regex.compile(r"([a-zA-Z]+ [a-zA-Z]+) bag")
        
    return pattern.findall(rule_description)


def get_bag_parents_rules(input_file_name):
    rules = {}
    with open(input_file_name) as file:
        for line in file:
            outer_bag, *contents = parse_rule(line.strip())
            for bag in contents:
                try:
                    rules[bag].append(outer_bag)
                except KeyError:
                    rules[bag] = [outer_bag]
    return rules

def get_bag_contents_rules(input_file_name):
    rules = {}
    with open(input_file_name) as file:
        for line in file:
            outer_bag, *inner_bags = parse_rule(line.strip(), include_weights=True)
            outer_bag = outer_bag[1]
            if inner_bags == [('', 'no other')]:
                rules[outer_bag] = []
            else:
                for inner_bag in inner_bags:
                    inner_bag_type_weight = inner_bag[1], int(inner_bag[0])
                    try:
                        rules[outer_bag].append(inner_bag_type_weight)
                    except KeyError:
                        rules[outer_bag] = [inner_bag_type_weight]
    return rules


def count_ouetermost_bag_options(input_file_name, bag):
    rules = get_bag_parents_rules(input_file_name)

    queue = SimpleQueue()
    queue.put(bag)
    count = 0
    visited_nodes = set()
    while not queue.empty():
        current_node = queue.get()
        visited_nodes.add(current_node)
        count += 1
        for child in rules.get(current_node, []):
            queue.put(child)

    return len(visited_nodes) - 1


def traverse_weighted_rules(rules, current_node):
    if rules[current_node] == []:
        return 0

    bag_count = 0
    for child, weight in rules[current_node]:
        bag_count += weight + weight * traverse_weighted_rules(rules, child)

    return bag_count


def count_inner_bags(input_file_name, bag):
    rules = get_bag_contents_rules(input_file_name)
    return traverse_weighted_rules(rules, bag)


def visualise_rules(input_file_name):
    os.environ["PATH"] += (
        os.pathsep + r"C:\Users\Me\Downloads\graphviz-2.44.1-win32\Graphviz\bin"
    )

    g = Digraph("rules")
    g.attr("node", style="filled", fillcolor="grey")
    g.node("shiny gold")
    g.attr("node", style="", fillcolor="")
    g.attr(rankdir="LR")

    rules = get_bag_contents_rules(input_file_name)
    for bag, inner_bags in rules.items():
        for inner_bag in inner_bags:
            g.edge(bag, inner_bag[0], label=str(inner_bag[1]))

    g.render(filename=input_file_name + ".gv", view=True)


if __name__ == "__main__":
    # visualise_rules("day_7_example_input.txt")
    print(count_ouetermost_bag_options(INPUT_FILE_PATH, 'shiny gold'))
    print(count_inner_bags(INPUT_FILE_PATH, 'shiny gold'))
