g++ -c -pipe -O2 -std=gnu++11 -Wall -Wextra -fPIC  -I. -I/usr/lib/qt/mkspecs/linux-g++ -o main.o main.cpp
g++ -Wl,-O1 -o compiler_killer main.o  
