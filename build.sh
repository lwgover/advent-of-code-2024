#!/bin/bash

# Check if a source file is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <source_file>"
    exit 1
fi

# Define variables
SOURCE_FILE=$1
FOLDER_NAME="build"
EXECUTABLE_NAME="program"

# Create a build folder
mkdir -p $FOLDER_NAME

# Compile the program
gcc $SOURCE_FILE -o $FOLDER_NAME/$EXECUTABLE_NAME

# Check for compilation errors
if [ $? -eq 0 ]; then
    echo "Compilation successful. Executable created at $FOLDER_NAME/$EXECUTABLE_NAME"
else
    echo "Compilation failed."
    exit 1
fi

