set(ENGINE_NAME Engine)
add_library(${ENGINE_NAME} STATIC)
file(GLOB_RECURSE SOURCES "*.cpp" "*.cxx")
file(GLOB_RECURSE HEADERS "*.h")

target_sources(${ENGINE_NAME} PRIVATE
    ${SOURCES}
    ${HEADERS}
)
target_include_directories(${ENGINE_NAME} PUBLIC "${PROJECT_SOURCE_DIR}/Dependencies/SDL/include")
target_precompile_headers(${ENGINE_NAME} PUBLIC Precompiled.h)