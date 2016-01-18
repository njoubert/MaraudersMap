all:
		g++ -std=c++11 -O3 -c person.cc -o person.o
		g++ -std=c++11 -O3 -c sim.cc -o sim.o
		g++ -std=c++11 -O3 -c main.cc -o main.o 
		g++ main.o sim.o person.o -o sim

clean:
		rm -f *.o sim
