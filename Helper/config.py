import numpy as np
from stl import mesh

# 1. Base Helix & Tube Parameters
radius_helix = 5.0
pitch = 2.0
turns = 4.0
tube_radius = 0.5       # Thickness of the solid tube
num_path_pts = 300      # Resolution along the helix length
num_circle_pts = 16     # Resolution of the tube cross-section

# 2. Generate Helix Backbone and Tangent Vectors
c = pitch / (2 * np.pi)
t = np.linspace(0, turns * 2 * np.pi, num_path_pts)

# Position vectors r(t)
x = radius_helix * np.cos(t)
y = radius_helix * np.sin(t)
z = c * t
path = np.vstack((x, y, z)).T

# Tangent vectors r'(t)
tx = -radius_helix * np.sin(t)
ty = radius_helix * np.cos(t)
tz = np.ones_like(t) * c
tangents = np.vstack((tx, ty, tz)).T
tangents /= np.linalg.norm(tangents, axis=1)[:, np.newaxis]

# 3. Build Mesh Coordinate Vertices
vertices = []
faces = []

for i in range(num_path_pts):
    # Create normal and binormal vectors for a coordinate frame
    up = np.array([0.0, 0.0, 1.0]) if abs(tangents[i, 2]) < 0.9 else np.array([1.0, 0.0, 0.0])
    normal = np.cross(tangents[i], up)
    normal /= np.linalg.norm(normal)
    binormal = np.cross(tangents[i], normal)
    
    # Generate circle vertices perpendicular to the curve path
    for j in range(num_circle_pts):
        angle = 2 * np.pi * j / num_circle_pts
        pt = path[i] + tube_radius * (np.cos(angle) * normal + np.sin(angle) * binormal)
        vertices.append(pt)

# 4. Generate Triangulated Index Faces
for i in range(num_path_pts - 1):
    for j in range(num_circle_pts):
        next_j = (j + 1) % num_circle_pts
        v1 = i * num_circle_pts + j
        v2 = i * num_circle_pts + next_j
        v3 = (i + 1) * num_circle_pts + j
        v4 = (i + 1) * num_circle_pts + next_j
        
        faces.append([v1, v2, v4])
        faces.append([v1, v4, v3])

# 5. Compile into standard STL mesh structure
vertices = np.array(vertices)
faces = np.array(faces)

helix_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        helix_mesh.vectors[i][j] = vertices[f[j]]

# Save output to your computer
helix_mesh.save('parametric_helix_tube.stl')
print("Successfully exported 'parametric_helix_tube.stl'")
