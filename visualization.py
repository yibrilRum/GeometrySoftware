from shapely.geometry import Polygon
import matplotlib.pyplot as plt

def plotPolygon(polygon, color="blue"):
    x, y = polygon.exterior.xy
    plt.fill(x, y, alpha=0.5, fc=color, ec="black")

room = Polygon([(0, 0), (0, 5), (7, 5), (7, 0)])
table = Polygon([(2, 2), (2, 3), (4, 3), (4, 2)])

plt.figure(figsize=(8, 6))
plotPolygon(room, color="lightgrey")
plotPolygon(table, color="brown")

plt.xlim(-1, 8)
plt.ylim(-1, 6)
plt.gca().set_aspect("equal")
plt.show()
