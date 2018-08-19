all: main skiprebuildh
main: main.cpp depend.o depend.h
	g++ -o main main.cpp depend.o
depend.o: depend.cpp depend.h
	g++ -c depend.cpp depend.h
.PHONY:skiprebuildh
skiprebuildh: main.o depend.cpp depend.h
	if [ main.o -nt depend.cpp ]; then \
		touch -r depend.cpp depend.h; \
	else touch -r main.o depend.h; fi
