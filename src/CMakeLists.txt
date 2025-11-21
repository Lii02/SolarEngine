set(EXECUTABLE_NAME ${PROJECT_NAME})
add_executable(${EXECUTABLE_NAME})
file(GLOB_RECURSE SOURCES "*.cpp" "*.cxx")
file(GLOB_RECURSE HEADERS "*.h")
target_sources(${EXECUTABLE_NAME} PRIVATE
    ${SOURCES}
    ${HEADERS}
)
target_include_directories(${EXECUTABLE_NAME} PUBLIC "${PROJECT_SOURCE_DIR}/Dependencies/SDL/include")
target_link_libraries(${EXECUTABLE_NAME} PUBLIC
    ${ENGINE_NAME}
    SDL3::SDL3
)