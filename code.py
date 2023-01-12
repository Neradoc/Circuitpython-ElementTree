# SPDX-FileCopyrightText: Copyright (c) 2022 Neradoc
# SPDX-License-Identifier: Unlicense

import sys
from ElementTree import parse

with open("some-demo.xml", "r") as fp:
    tree = parse(fp)

print(tree)

def print_sub_tree(node, depth=0):
    if node.text is not None:
        text = '"' + node.text + '"'
    else:
        text = ""
    print(" "*depth, "-", node.tag, text)
    for key, value in node.attrib.items():
        print(" "*depth, "|", key, ":", value)
    for subnode in node:
        print_sub_tree(subnode, depth+2)

print_sub_tree(tree.getroot())
