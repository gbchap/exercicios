/*
exercício do moodle (atividade 4);
*/

#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

float decomposicao(int x){
    
    int n100, n50, n20, n10, n5, n2, n1;
    
    n100 = x / 100;
    n50 = (x-n100*100)/ 50;
    n20 = ((x-n100*100)-n50*50)/ 20;
    n10 = (((x-n100*100)-n50*50)-n20*20)/ 10;
    n5 = ((((x-n100*100)-n50*50)-n20*20)-n10*10) / 5;
    n2 = (((((x-n100*100)-n50*50)-n20*20)-n10*10)-n5*5) /2;
    n1 = ((((((x-n100*100)-n50*50)-n20*20)-n10*10)-n5*5)-n2*2);
    
    cout << x << endl;
    cout << setprecision(1)<< n100 << " nota(s) de R$ 100,00" <<endl;
    cout << setprecision(1)<< n50 << " nota(s) de R$ 50,00" <<endl;
    cout << setprecision(1)<< n20 << " nota(s) de R$ 20,00" <<endl;
    cout << setprecision(1)<< n10 << " nota(s) de R$ 10,00" <<endl;
    cout << setprecision(1)<< n5  << " nota(s) de R$ 5,00" <<endl;
    cout << setprecision(1)<< n2  << " nota(s) de R$ 2,00" <<endl;
    cout << setprecision(1)<< n1  << " nota(s) de R$ 1,0";
    
    return 0;
}
int main()
{
    int x;
    cin >> x;
    cout << decomposicao(x);
    return 0;
}