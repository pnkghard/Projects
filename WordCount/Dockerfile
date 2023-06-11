# Base image
FROM gcc:latest

# Set the working directory inside the container
WORKDIR /WordCount

# Copy the source code to the container
COPY . /WordCount

# Compile the C application
RUN make

# Set the entry point command
CMD ["./main", "input.txt"]