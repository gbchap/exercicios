//Construa uma sequência de instruções para determinar
//qual a quantidade de segundos exata de um dia,
//considerando que possui 23 horas, 56 minutos e 4
//segundos. Assim como no exercício anterior, declare
//variáveis, inicialize-as e, por fim, realize o cálculo,
//armazenando o resultado.

#include <iostream>
using namespace std;

int main()
{

    int horas = 23;
    int minutos = 56;
    int segundos = 4;

    horas;
    minutos = horas * 60;
    segundos = minutos * 60;

    cout << segundos;

    return 0;
}