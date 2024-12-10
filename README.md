# curvcalc: a Python binding of the C++ total curvature calculator
<p align="center">
    <img src="https://github.com/user-attachments/assets/73a276da-eab3-4961-a43f-8d332730ae50" />
</p>

## Description
This is a Python binding library for the [total curvature estimation calculator](https://github.com/HeCraneChen/total-curvature-estimation) written in C++. The total curvature estimation calculator is a fast and robust total curvature estimation method that works for both triangle meshes and point clouds. 

## Dependencies

For building in cmake:

- [STL](https://www.geeksforgeeks.org/the-c-standard-template-library-stl/) 
- [pybind11](https://github.com/pybind/pybind11) for binding Python to C++
- [gmp](https://gmplib.org) for arbitrary-precision arithmetic
- [eigen](https://eigen.tuxfamily.org/index.php?title=Main_Page) for matrix data structures 
- [openmp](https://www.openmp.org) for parallelization 
- [libigl](https://libigl.github.io) for mesh data structures and geometry processing tools 
- [polyscope](http://polyscope.run) for 3D visualizations and rendering
- [mpfr](https://www.mpfr.org/) for arbitrary-precision binary floating-point computation 

While some of these dependencies have been added as submodules to this repository, others may be installed using [homebrew](https://brew.sh/) or other methods.

For testing in python:
- [libigl Python installation](https://github.com/libigl/libigl-python-bindings)
- [polyscope Python installation](https://github.com/nmwsharp/polyscope)

## OS and Python Version
This library was developed on MacOS 15.0.1. Please refer to the original [C++ library](https://github.com/HeCraneChen/total-curvature-estimation) for Ubuntu and Windows documentation. 

The bindings were developed and tested using the macOS 64-bit universal2 build of [Python 3.9](https://www.python.org/downloads/release/python-3913/). Please note that using other distributions of Python, i.e. from anaconda, may result in errors building and using the bindings if they are not universal2 binary builds of Python, which run on both Apple Silicon and Intel chip architectures. 

## Compiling and Running

### Compile in MacOS
Clone the repository with dependencies:
```
git clone --recurse-submodules https://github.com/rkakaria/total-curvature-calculator-python-bindings.git
```
Compile using cmake:
```
cd total-curvature-calculator-python-bindings 
mkdir build 
cd build 
cmake .. 
make
```
Please visit the original C++ library readme for issues locating openmp on Apple Silicon machines. 

### Run
Exit the build folder and run the test files from the total-curvature-calculator-python-bindings folder. Libigl is used to read 3D model files and polyscope to visualize the models and returned curvature values, which are stored in the variable K.
#### Triangle Mesh
```
cd .. 
python3 test_mesh.py
```
<img width="1532" alt="Cow_Sagittal_Smooth" src="https://github.com/user-attachments/assets/41c9b00b-51d8-4368-927d-88ed94211a34">

#### Point Cloud
```
cd ..
python3 test_cloud.py
```
<img width="1532" alt="Cow_Sagittal_Point_Cloud" src="https://github.com/user-attachments/assets/bc57d602-4d0c-44f3-af96-659eb44d098a">

The Smithsonian's [3D content collection](https://3d.si.edu/) is an excellent place to find open source models to play around with!
![Mammoth](https://github.com/user-attachments/assets/5ea80d2f-6308-44a2-859c-5056aa620772)

## Documentation

Parameters 
---------- 
```
V : numpy double array (n, 3)
    Matrix of vertex coordinates 
F : numpy int array, optional (default None) (n, 3)
    Matrix of triangle indices 
N : numpy double array (n, 3)
    Matrix of normalized vectors at a vertex
```
Returns 
------- 
```
K : vector
    Per-vertex scalar field representing curvature values at each vertex

K_vis: vector
    Scaled curvature values for better visualization
```

## References
```
@inproceedings{10.1145/3587421.3595439,
author = {Chen, Crane He},
title = {Estimating Discrete Total Curvature with Per Triangle Normal Variation},
year = {2023},
isbn = {9798400701436},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3587421.3595439},
doi = {10.1145/3587421.3595439},
booktitle = {ACM SIGGRAPH 2023 Talks},
articleno = {56},
numpages = {2},
location = {Los Angeles, CA, USA},
series = {SIGGRAPH '23}
}
```
