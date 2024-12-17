import requests
import trimesh
import numpy as np
import io

from blendify import scene
from blendify.colors import VertexColors
from blendify.materials import PrincipledBSDFMaterial

#Load object
bunny_url = "https://graphics.stanford.edu/~mdfisher/Data/Meshes/bunny.obj"
bunny_data = requests.get("https://graphics.stanford.edu/~mdfisher/Data/Meshes/bunny.obj").content
bunny = trimesh.load(io.BytesIO(bunny_data), file_type="obj")

# Create metallic material
material = PrincipledBSDFMaterial(metallic=0.3)
# Create per-vertex colors
colors = VertexColors(np.abs(bunny.vertex_normals))
# Add mesh
scene.renderables.add_mesh(vertices=bunny.vertices * 100, faces=bunny.faces, material=material, colors=colors)
# Set the camera
scene.set_perspective_camera(
    resolution=(600, 600),
    fov_y=np.pi / 3,
    translation=(-3, 10, 20)
)
# Create light
scene.lights.add_sun(strength=7)
# Render
scene.render(filepath="blendify/myScripts/bunny.png")