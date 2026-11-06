cmake_minimum_required(VERSION 3.21)
project(bibliotheque)

# Find pybind11
find_package(pybind11 REQUIRED)

# Build the main executable (console version)
file(GLOB EXE_SOURCES "main.cpp" "library.cpp" "book.cpp" "user.cpp" "filemanager.cpp")
add_executable(bibliotheque ${EXE_SOURCES})

# Build the Python module
pybind11_add_module(bibliotheque_py bindings.cpp library.cpp book.cpp user.cpp filemanager.cpp)

set_target_properties(bibliotheque bibliotheque_py PROPERTIES
    CXX_STANDARD 17
    CXX_STANDARD_REQUIRED YES
    CXX_EXTENSIONS NO
)

target_compile_options(bibliotheque PRIVATE -Wall -Wextra -Wpedantic)
target_compile_options(bibliotheque_py PRIVATE -Wall -Wextra -Wpedantic)
