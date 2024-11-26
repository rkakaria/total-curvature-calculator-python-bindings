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
This binding was developed on MacOS 14.7. Please refer to the original [C++ library](https://github.com/HeCraneChen/total-curvature-estimation) for Ubuntu and Windows documentation. There may be computer architecture discrepancies on the Intel chip vs M1/M2/M3. 

### Compile in MacOS
```
cd total-curvature-estimation 
mkdir build 
cd build 
cmake .. 
make
```
If your machine uses M1/M2/M3 and your compiler cannot locate openmp, use the following before issuing the compilation commands: 
```
sudo mkdir -p /usr/local/lib /usr/local/include 
sudo ln -s $(brew --prefix libomp)/lib/libomp.dylib /usr/local/lib/libomp.dylib 
sudo ln -s $(brew --prefix libomp)/include/* /usr/local/include/ 
cmake ..
```
