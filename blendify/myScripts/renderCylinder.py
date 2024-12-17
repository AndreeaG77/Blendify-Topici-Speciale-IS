# Script to render cylinders
from blendify import scene
from blendify.materials import PrincipledBSDFMaterial, MetalMaterial, PlasticMaterial, GlossyBSDFMaterial
from blendify.colors import UniformColors
# Add light
scene.lights.add_point(strength=1000, translation=(4, -2, 4))
# Add camera
scene.set_perspective_camera((512, 512), fov_x=0.7, rotation=(0.82, 0.42, 0.18, 0.34), translation=(5, -5, 5))
# Create material
material1 = PrincipledBSDFMaterial()
material2 = MetalMaterial()
material3 = PlasticMaterial()
material4 = GlossyBSDFMaterial()
# Create color
color1 = UniformColors((0.0, 1.0, 0.0))
color2 = UniformColors((1.0, 0.0, 0.0))
color3 = UniformColors((0.0, 0.0, 1.0))
color4 = UniformColors((1.0, 0.85, 0.9))
# Add cylinder mesh
scene.renderables.add_cylinder_mesh(0.5, 1.0, material1, color1, translation=(-0.5, -2.5, 0.0))
scene.renderables.add_cylinder_mesh(0.5, 2.0, material2, color2, translation=(0.0, -1.2, 0.0))
scene.renderables.add_cylinder_mesh(0.5, 3.0, material3, color3, translation=(0.7, 0.0, 0.0))
scene.renderables.add_cylinder_mesh(0.5, 4.0, material4, color4, translation=(1.5, 1.2, 0.0))
# Render scene
scene.render(filepath="blendify/myScripts/cylinder.png")