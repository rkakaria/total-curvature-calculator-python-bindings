# total-curvature-calculator-python-bindings

## Description
This is a Python binding library for the [total curvature estimation calculator](https://github.com/HeCraneChen/total-curvature-estimation) by [Professor Crane Chen](https://github.com/HeCraneChen) written in C++. The total curvature estimation calculator is a fast and robust total curvature estimation method that works for both triangle meshes and point clouds. 

## Dependencies
- [pybind11](https://github.com/pybind/pybind11) for binding Python to C++
- [STL](https://www.geeksforgeeks.org/the-c-standard-template-library-stl/) 
- [eigen](https://eigen.tuxfamily.org/index.php?title=Main_Page) for matrix data structures 
- [openmp](https://www.openmp.org) for parallelization 
- [libigl](https://libigl.github.io) for mesh data structures and geometry processing tools 
- [polyscope](http://polyscope.run) for 3D visualizations and rendering 

## OS
This binding was developed on MacOS 14.7. Please refer to the original [C++ library](https://github.com/HeCraneChen/total-curvature-estimation) for Ubuntu and Windows documentation.
