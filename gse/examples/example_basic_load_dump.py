from gse.gol import *
from gse.objgraph import ObjGraph

text = """Item1
    SubItem1 # this is a sub item
    SubItem2
        SubSubItem1
            SubSubSubItem1
    SubItem3

Item2
    SubItem3"""

text = """Project
    Planning
        Milestone1
    #some comment
            Task1 # this is a task
            Task2
        Milestone2#some other comment#and another comment
            Task3
    Development
        Phase1
            Task4
            Task5
        Phase2
            Task6
Documentation
    Draft
        Section1
    Subs
            """

text2 = """Documentation1
    Draft
        Section1
      Section2Misplaced
      Section3
       Section33
 Draft2Mislpaced
   Section22
  Section23
   Section234
    Section2344


Documentation2          
 Draft3Mislpaced
Subs
            """

text3 = """a
    a1
b
            """

text4 = """Documentation1
 Draft2Mislpaced
  Section22
 Draft3Mislpaced
Subs
            """

textb = """
root 
        aligned
    misplaced
"""
# This should be correct:
textg = """
root 
        aligned
well_placed
"""

textc = """
public void fn(n):
    n = n+1
    return n

"""

import pprint as pp
gr = ObjGraph()
gol = Gol(gr, output_root_only = True)
lines = text.splitlines()

items = list(gol.load_gen(lines))
for ctx, root in items:
    print(root)
    print(root.dumps())
    #print(gol.dumps(root))

#print("gol.loads:")
#roots = gol.loads(text)

#for root in roots:
#    print(gol.dumps(root))

"""
(None, <Project: <Planning: <Milestone1: <Task1>, <Task2>>, <Milestone2: <Task3>>>, <Development: <Phase1: <Task4>, <Task5>>, <Phase2: <Task6>>>>)
(None, <Documentation: <Draft: <Section1>>, <Subs>>)
"""