cmake_minimum_required (VERSION 3.10)
project(imtui_py VERSION 0.1)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(IMTUI_PATH external/imtui)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")
set(CMAKE_CXX_FLAGS "${CMAKE_C_FLAGS} -fPIC -std=c++14 -Wno-error -DImTextureID=int -DIMGUI_DISABLE_OBSOLETE_FUNCTIONS=1")

add_subdirectory(${IMTUI_PATH}
${CMAKE_BINARY_DIR}/imtui
EXCLUDE_FROM_ALL
)

add_subdirectory(external/pybind11)

set(DEFAULT_LINK_LIBS imtui imtui-ncurses)

# Python interface
pybind11_add_module(_imtui_py pyiface.cpp)
target_link_libraries(_imtui_py PRIVATE ${DEFAULT_LINK_LIBS})
# The deargui derived bits need direct access to ImGui headers
target_include_directories(_imtui_py PRIVATE ${IMTUI_PATH}/third-party/imgui/imgui)
