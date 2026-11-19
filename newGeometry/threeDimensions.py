import trimesh
import numpy as np
from shape_viewer import create_shape, show_plotly

def create_shape(shape_type, measurements):
    if shape_type == 'cube':
        size =  measurements.get('size', 1)
        return trimesh.creation.box(extents=[size, size, size])
    elif shape_type == 'sphere':
        radius = measurements.get('radius', 1)
        return trimesh.creation.icosphere(radius=radius)
    elif shape_type == 'cylinder':
        radius = measurements.get('radius', 1)
        height = measurements.get('height', 2)
        return trimesh.creation.cylinder(radius=radius, height=height)
    elif shape_type == 'cone':
        radius = measurements.get('radius', 1)
        height =measurements.get('height', 2)
        return trimesh.creation.cone(radius=radius, height=height)
    else:
        raise ValueError("Unsupported shape type")

shape = create_shape('cylinder', {'radius': 1, 'height': 3})
show_plotly(shape)
