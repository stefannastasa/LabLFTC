cmake_minimum_required(VERSION 3.26)
project(MLP_homework)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(MLP_homework
        dictionary/Dictionar.cpp
        dictionary/Dictionar.h
        dictionary/IteratorDictionar.cpp
        dictionary/IteratorDictionar.h
        dictionary/list.h
        main.cpp)
