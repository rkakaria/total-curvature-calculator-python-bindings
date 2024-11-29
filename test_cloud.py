#append the build folder, which contains the shared object, to the search path
import sys
import os
import igl
sys.path.append(os.path.join(sys.path[0], 'build'))

#import polyscope for visualization
import polyscope as ps

#import the shared object 
import TotalCurvatureBindings

# Total Curvature Point Cloud
V, F = igl.read_triangle_mesh("./total-curvature-calculator/example_data/cow_points.ply")

N, F = igl.read_triangle_mesh("./total-curvature-calculator/example_data/cow_normals.ply")

# calculate curvature
K = TotalCurvatureBindings.cloud(V, N)

# scale curvature values for better visualization
K_vis = K**0.0625

ps.init()
ps_mesh = ps.register_point_cloud("cow cloud", V)
ps_mesh.add_scalar_quantity("curvature", K_vis, enabled=True, cmap = "jet")
ps.show()