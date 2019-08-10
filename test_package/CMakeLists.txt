cmake_minimum_required(VERSION 3.0)
project(test_package)

find_package(gcem REQUIRED)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE gcem::gcem)
