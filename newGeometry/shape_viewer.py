import trimesh
import numpy as np
import plotly.graph_objects as go

def create_shape(shape_type, measurements):
    if shape_type == 'box':
        size = measurements.get('size', [1, 1, 1])
        return trimesh.creation.box(extents=size)
    elif shape_type == 'cylinder':
        radius = measurements.get('radius', 1)
        height = measurements.get('height', 2)
        return trimesh.creation.cylinder(radius=radius, height=height)
    elif shape_type == 'sphere':
        radius = measurements.get('radius', 1)
        return trimesh.creation.sphere(radius=radius)
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")

def show_plotly(mesh):
    vertices = mesh.vertices
    faces = mesh.faces

    fig = go.Figure(
        data =[
            go.Mesh3d(
                x=vertices[:, 0],
                y=vertices[:, 1],
                z=vertices[:, 2],
                i=faces[:, 0],
                j=faces[:, 1],
                k=faces[:, 2],
                color='lightblue',
                opacity=0.5
                )
            ]
        )
    fig.update_layout(title='3D Shape', scene_aspectmode='data')
    fig.show()
