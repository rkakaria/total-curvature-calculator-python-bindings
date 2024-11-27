#append the build folder, which contains the shared object, to the search path
import sys
import os
sys.path.append(os.path.join(sys.path[0], 'build'))

# print(sys.argv)

#import the shared object module
import TotalCurvatureBindings

# open("example_data/cow.ply")
# TotalCurvatureBindings.curvature(['test.py', '--in', '/Users/revakakaria/Documents/NEU/total-curvature-calculator-python-bindings_copy/total-curvature-calculator/example_data/cow.ply', '--out', '/Users/revakakaria/Documents/NEU/total-curvature-calculator-python-bindings_copy/total-curvature-calculator/results/cow_mesh.txt', '--format', 'mesh'])

# TotalCurvatureBindings.curvature(['test.py', '--in', '/Users/revakakaria/Documents/NEU/total-curvature-estimation-python-bindings/example_data/cow_points.ply', '/Users/revakakaria/Documents/NEU/total-curvature-estimation-python-bindings/example_data/cow_normals.ply', '--out', '/Users/revakakaria/Documents/NEU/total-curvature-estimation-python-bindings/results/cow_cloud.txt', '--format', 'point_cloud'])

# --in /Users/revakakaria/Documents/NEU/total-curvature-calculator-python-bindings_copy/total-curvature-calculator/example_data/cow.ply --out /Users/revakakaria/Documents/NEU/total-curvature-calculator-python-bindings_copy/total-curvature-calculator/results/cow_mesh.txt --format mesh

TotalCurvatureBindings.curvature(sys.argv)



#is it better to keep this as command line arguments? or parameterize it within the Python script?