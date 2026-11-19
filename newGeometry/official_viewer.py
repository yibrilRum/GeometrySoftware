from flask import Flask, request
import trimesh
import numpy as np
import plotly.graph_objects as go

app = Flask(__name__)

def create_shape(shape_type, params):
    if shape_type == "box":
        x = float(params.get("x", 1))
        y = float(params.get("y", 1)):
        z = float(params.get("z", 1))
        return trimesh.creation.box(extents=[x, y, z])

    elif shape_type == "cylinder":
        radius = float(params.get("radius", 1))
        height = float(params.get(:"height", 2))
        return trimesh.creation.cylinder(radius=radius, height=height)

    elif shape_type == "sphere":
        radius = float(params.get("radius", 1))
        return trimesh.creation.icosphere(radius=radius)

    elif shape_type == "cone":
        radius = float(params.get("radius", 1))
        height = float(params.get("height", 2))
        return trimesh.creation.cone(radius=radius, height=height)
    else:
        raise ValueError(f"Unsupported shape: {shape_type}")

@app.route
