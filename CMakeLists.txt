cmake_minimum_required(VERSION 4.0)
project(SolarEngine)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED true)
set_property(GLOBAL PROPERTY USE_FOLDERS ON)
set(CMAKE_SUPPRESS_REGENERATION TRUE)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/$<CONFIGURATION>")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/$<CONFIGURATION>")
add_compile_definitions(UNICODE _UNICODE _CRT_SECURE_NO_WARNINGS)

# Dependencies
add_subdirectory(Dependencies/SDL EXCLUDE_FROM_ALL)
add_subdirectory(Dependencies/cglm EXCLUDE_FROM_ALL)
find_package(OpenGL REQUIRED)

# Engine library
add_subdirectory(Engine)

# Executable
add_subdirectory(main)

set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT "${EXECUTABLE_NAME}")