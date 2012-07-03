from pygraph.classes.digraph import digraph
from pygraph.algorithms import minmax
import euler

data = euler.readGraph("83.txt")

# data = [[131, 673, 234, 103, 18],
#  [201, 96, 342, 965, 150],
#   [630, 803, 746, 422, 111],
#    [537, 699, 497, 121, 956],
#     [805, 732, 524, 37, 331]]

gr = digraph()
leny = len(data)
lenx = len(data[0])

for y in range(leny):
    for x in range(lenx):
        gr.add_node((y, x))

gr.add_node("start")
gr.add_node("end")

gr.add_edge(("start", (0, 0)), wt=data[0][0])
gr.add_edge(((leny - 1, lenx - 1), "end"), wt=0)

for y in range(leny):
    for x in range(lenx):
        if y != leny - 1:
            gr.add_edge(((y, x), (y + 1, x)), wt=data[y + 1][x])
        if x != lenx - 1:
            gr.add_edge(((y, x), (y, x + 1)), wt=data[y][x + 1])
        if y != 0:
            gr.add_edge(((y, x), (y - 1, x)), wt=data[y - 1][x])
        if x != 0:
            gr.add_edge(((y, x), (y, x - 1)), wt=data[y][x - 1])

print minmax.shortest_path(gr, "start")[1]["end"]
