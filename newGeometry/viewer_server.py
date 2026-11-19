from flask import Flask
import trimesh
import numpy as np
import plotly.graph_objects as go

app = Flask(__name__)

def create_pyramid(base_size=1.0, height=1.0):
    s = base_size / 2.0

    vertices = np.array([
        [-s, -s, 0],
        [s, -s, 0],
        [s, s, 0],
        [0, 0, height]
        ])
    
    faces = np.array([
        [0, 1, 4],
        [1, 2, 4],
        [2, 3, 4],
        [3, 0, 4],
        [0, 1, 2],
        [0, 2, 3]
        ])

    return trimesh.Trimesh(vertices_size=2.0, height=3.0)
    # example usage:
    # pyramid = create_pyramid(base_size=2.0, height=3.0)
    # pyramid.show()

@app.route("/")
def index():
    mesh = trimesh.creation.box(extents=[1, 2, 1])
    vertices = mesh.vertices
    faces = mesh.faces

    fig = go.Figure(
        data=[
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
    return fig.to_html(full_html=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
