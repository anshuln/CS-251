cmake_minimum_required(VERSION 3.10)

set(CMAKE_BUILD_TYPE DEBUG)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")

project(build)

add_executable(helloworld
	helloworld.cpp)

find_package (Threads)

add_executable(usespthread	
	usespthread.cpp
	)

target_link_libraries (usespthread ${CMAKE_THREAD_LIBS_INIT})

add_library(MyEngineDynamic SHARED
	myengine/myengine.cpp
	)	
set_target_properties(MyEngineDynamic PROPERTIES PUBLIC_HEADER myengine/myengine.h)

add_library(MyEngineStatic STATIC
	myengine/myengine.cpp
)

install(TARGETS MyEngineDynamic DESTINATION ​/usr/local/lib/)