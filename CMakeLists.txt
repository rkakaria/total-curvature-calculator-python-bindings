cmake_minimum_required(VERSION 3.16)
project(curvcalc)

list(PREPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake)

# Eigen
if(WIN32)
    # On Windows, include Eigen from the local source directory
    include_directories(${CMAKE_CURRENT_SOURCE_DIR}/eigen)
else()
    # On other operating systems, use find_package
    find_package(Eigen3 REQUIRED)
    include_directories(${EIGEN3_INCLUDE_DIR})
endif()

# Libigl
include(libigl)

# Enable the targets
igl_include(restricted triangle)
igl_include(core)
igl_include(copyleft cgal)

# polyscope
add_subdirectory("polyscope")

# openmp
find_package(OpenMP REQUIRED)

# python and pybind11
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 REQUIRED)

# create bindings
pybind11_add_module(${PROJECT_NAME} MODULE bindings.cpp)

target_link_libraries(${PROJECT_NAME} PRIVATE igl_copyleft::cgal igl_restricted::triangle pybind11::module polyscope PRIVATE OpenMP::OpenMP_CXX)