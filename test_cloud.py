import polyscope as ps
import igl

#append the build folder, which contains the shared object, to the search path
import sys
import os
sys.path.append(os.path.join(sys.path[0], 'build'))

#import the shared object 
import TotalCurvatureBindings

# set V, F, and N using test data
V, F = igl.read_triangle_mesh("./total-curvature-estimation/example_data/cow_points.ply")

N, F = igl.read_triangle_mesh("./total-curvature-estimation/example_data/cow_normals.ply")

# calculate curvature
K = TotalCurvatureBindings.cloud(V, N)

# scale curvature values for better visualization
K_vis = K**0.0625

# visualize
ps.init()
ps_mesh = ps.register_point_cloud("cow cloud", V)
ps_mesh.add_scalar_quantity("curvature", K_vis, enabled=True, cmap = "jet")
ps.show()