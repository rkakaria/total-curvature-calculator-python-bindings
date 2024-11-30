# total-curvature-calculator-python-bindings

## Description
This is a Python binding library for the [total curvature estimation calculator](https://github.com/HeCraneChen/total-curvature-estimation) by [Professor Crane Chen](https://github.com/HeCraneChen) written in C++. The total curvature estimation calculator is a fast and robust total curvature estimation method that works for both triangle meshes and point clouds. 

## Dependencies
- [STL](https://www.geeksforgeeks.org/the-c-standard-template-library-stl/) 
- [pybind11](https://github.com/pybind/pybind11) for binding Python to C++
- [gmp](https://gmplib.org) for arbitrary-precision arithmetic
- [eigen](https://eigen.tuxfamily.org/index.php?title=Main_Page) for matrix data structures 
- [openmp](https://www.openmp.org) for parallelization 
- [libigl](https://libigl.github.io) for mesh data structures and geometry processing tools 
- [polyscope](http://polyscope.run) for 3D visualizations and rendering
- [mpfr](https://www.mpfr.org/) for arbitrary-precision binary floating-point computation 

While some of these dependencies have been added as submodules to this repository, others must be installed using [homebrew](https://brew.sh/) or [pip](https://pypi.org/project/pip/).

## OS and Python Version
This library was developed on MacOS 14.7. Please refer to the original [C++ library](https://github.com/HeCraneChen/total-curvature-estimation) for Ubuntu and Windows documentation. 

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
If your machine uses M1/M2/M3 and your compiler cannot locate openmp, use the following before issuing the compilation commands: 
```
sudo mkdir -p /usr/local/lib /usr/local/include 
sudo ln -s $(brew --prefix libomp)/lib/libomp.dylib /usr/local/lib/libomp.dylib 
sudo ln -s $(brew --prefix libomp)/include/* /usr/local/include/ 
cmake ..
```
### Run
Exit the build folder and run the test files from the total-curvature-calculator-python-bindings folder. Polyscope is used to visualize the returned curvature values, which are stored in the variable K.
#### Triangle Mesh
```
cd .. 
python3 test_mesh.py
```
This program allows you to toggle the smoothness between 3 options:
##### Flat
<img width="1532" alt="Cow_Sagittal_Flat" src="https://github.com/user-attachments/assets/d4521cbb-b1ef-42c7-a194-3607452077f1">

##### Smooth
<img width="1532" alt="Cow_Sagittal_Smooth" src="https://github.com/user-attachments/assets/41c9b00b-51d8-4368-927d-88ed94211a34">

##### Tri Flat
<img width="1532" alt="Cow_Sagittal_Tri_Flat" src="https://github.com/user-attachments/assets/d51e09e4-7cf3-426d-b060-cc86cc6c28a5">

#### Point Cloud
```
cd ..
python3 test_cloud.py
```
<img width="1532" alt="Cow_Sagittal_Point_Cloud" src="https://github.com/user-attachments/assets/bc57d602-4d0c-44f3-af96-659eb44d098a">

## Documentation
```
Parameters 
---------- 
V : numpy double array (n, 3)
    Matrix of vertex coordinates 
F : numpy int array, optional (default None) (n, 3)
    Matrix of triangle indices 
N : numpy double array (n, 3)
    Matrix of normalized vectors at a vertex
 
Returns 
------- 
K : vector
    Per-vertex scalar field representing curvature values at each vertex

K_vis: vector
    Scaled curvature values for better visualization
```
