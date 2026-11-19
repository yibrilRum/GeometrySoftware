from shapely.geometry import Polygon

room = Polygon([(0, 0), (0, 5), (7, 5), (7, 0)])
table = Polygon([(2, 2), (2, 3), (4, 3), (4, 2)])

print(f"Room area: {room.area} sqm")
print(f"Table area: {table.area} sqm")

print("Is table in the room?", room.contains(table))