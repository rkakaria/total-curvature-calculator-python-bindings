#append the build folder, which contains the shared object, to the search path
import sys
import os
import igl
sys.path.append(os.path.join(sys.path[0], 'build'))

#import polyscope for visualization
import polyscope as ps

#import the shared object 
import TotalCurvatureBindings

# Total Curvature Mesh
V, F = igl.read_triangle_mesh("./total-curvature-estimation/example_data/cow.ply")

N = igl.per_vertex_normals(V, F, igl.PER_VERTEX_NORMALS_WEIGHTING_TYPE_AREA)

# calculate curvature
K = (TotalCurvatureBindings.mesh(V, F, N))

# scale curvature values for better visualization
K_vis = K**0.0425

ps.init()
ps_mesh = ps.register_surface_mesh("cow", V, F)
ps_mesh.add_scalar_quantity("curvature", K_vis, enabled=True, cmap = "jet")
ps.show()