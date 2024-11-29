// bindings.cpp
#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <pybind11/stl.h>
#include "total-curvature-estimation/total_curvature_mesh.cpp"
#include "total-curvature-estimation/total_curvature_point_cloud.cpp"

Eigen::VectorXd wrap_mesh(const Eigen::MatrixXd& V, const Eigen::MatrixXi& F, Eigen::MatrixXd N) {
    Eigen::VectorXd k_S;

    igl::per_vertex_normals(V, F, N);
    k_S.resize(V.rows()); 
    
    TotalCurvatureMesh(V, F, N, k_S);
    return k_S;
}

Eigen::VectorXd wrap_cloud(const Eigen::MatrixXd& V, const Eigen::MatrixXd& N) {
    Eigen::VectorXd k_S;
    int K = 20;

    k_S.resize(V.rows()); 

    TotalCurvaturePointCloud(V, N, k_S, K);
    return k_S;
}


// Define the module
PYBIND11_MODULE(TotalCurvatureBindings, m)
{
    m.def("mesh", &wrap_mesh);

    m.def("cloud", &wrap_cloud);
}