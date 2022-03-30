cmake_minimum_required(VERSION 3.1.5)
# set(CMAKE_CXX_STANDARD 17)

project(register)

set(DNPCOMP_ENABLE_PYTORCH ON)
set(Torch_DIR /opt/conda/lib/python3.7/site-packages/torch/share/cmake/Torch)
find_package(Torch REQUIRED)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")

include_directories(include/ ${TORCH_INCLUDE_DIRS})

# add_library(target_lib src/main.cpp)

add_executable(register src/main.cpp src/nms.cpp)

target_link_libraries(register "${TORCH_LIBRARIES}")
set_property(TARGET register PROPERTY CXX_STANDARD 14)
