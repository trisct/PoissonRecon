project("SurfaceReconstruction")
cmake_minimum_required(VERSION 3.0)

set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)

add_executable(PoissonRecon src/PoissonRecon.cpp)
target_include_directories(PoissonRecon PRIVATE "${PROJECT_SOURCE_DIR}")
target_compile_features(PoissonRecon PRIVATE cxx_std_17)
target_link_libraries(PoissonRecon PRIVATE jpeg png z Threads::Threads)
set_target_properties(PoissonRecon PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${PROJECT_SOURCE_DIR}/bin")

add_executable(SSDRecon src/SSDRecon.cpp)
target_include_directories(SSDRecon PRIVATE "${PROJECT_SOURCE_DIR}")
target_compile_features(SSDRecon PRIVATE cxx_std_17)
target_link_libraries(SSDRecon PRIVATE jpeg png z Threads::Threads)
set_target_properties(SSDRecon PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${PROJECT_SOURCE_DIR}/bin")
