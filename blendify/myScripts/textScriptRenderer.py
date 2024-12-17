import bpy

from blendify import scene
from blendify.materials import PrincipledBSDFMaterial
from blendify.colors import UniformColors
from blendify.renderables.primitives import MeshPrimitive

# Set up lighting and camera
scene.lights.add_point(strength=1000, translation=(4, -2, 4))
scene.set_perspective_camera((512, 512), fov_x=0.7, rotation=(0.82, 0.42, 0.18, 0.34), translation=(10, -10, 10))

# Create material and color for the text
material_text = PrincipledBSDFMaterial()
color_text = UniformColors((0.8, 0.1, 0.2))

scene.renderables.add_text_mesh(
    text="Hello World",
    size=1,
    material=material_text,
    colors=color_text,
    tag="text1",
    translation=(-0.5, -2, 0),
    rotation=(90, 90, 30, 35)
)

# Adjustment of the extrusion of text
#text_object = bpy.data.objects["text1"]
#text_object.data.extrude = 0.2

scene.render(filepath="blendify/myScripts/text1.png")
