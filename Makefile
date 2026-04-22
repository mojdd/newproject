CC = gcc
CFLAGS = -Wall -O2

# GLAD headers
GLAD_CPPFLAGS = -I glad/include

# GLFW: MSYS2 UCRT64 (adjust if your install path differs)
GLFW_PREFIX ?= C:/msys64/ucrt64
GLFW_CPPFLAGS = -I $(GLFW_PREFIX)/include
# Static GLFW (.a), system libs stay dynamic
GLFW_LIBS = -L $(GLFW_PREFIX)/lib -Wl,-Bstatic -lglfw3 -Wl,-Bdynamic -lgdi32 -luser32 -lshell32

all: b.exe

b.exe: hello.c glad.c
	$(CC) $(CFLAGS) $(GLAD_CPPFLAGS) $(GLFW_CPPFLAGS) hello.c glad.c -o b.exe \
		$(GLFW_LIBS) -lopengl32 -static-libgcc

clean:
	del /Q /F b.exe 2>NUL || rm -f b.exe
