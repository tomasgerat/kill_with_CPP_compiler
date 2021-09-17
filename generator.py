VAL=2000
with open('main.cpp', 'w') as f:
    f.write('#include <iostream>\n')
    f.write('using namespace std;\n')
    for i in range(VAL):
        s='template<int n>struct funStruct'+str(i)+'{enum{val=funStruct'+str(i)+'<n-1>::val};};'
        f.write(s)
        s='template<>struct funStruct'+str(i)+'<0>{enum{val='+str(i)+'};};'
        f.write(s)
    f.write('int main(){')
    for i in range(VAL):
        s='cout<<funStruct'+str(i)+'<900>::val<<endl;'
        f.write(s)
    f.write('return 0;')
    f.write('}')
