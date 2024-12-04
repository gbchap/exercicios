//Construa um programa para ler do teclado um
//intervalo de tempo em segundos, converter
//para horas, minutos e segundos e imprimir o
//resultado. Faça o teste de mesa para uma
//entrada de 72000 segundos.

#include <iostream>
using namespace std;

int main()
{
     
    int segundos;
    int minutos;
    int horas;

    cout << "Digite segundos: ";
    cin >> segundos;

    minutos = segundos / 60;
    horas = minutos / 60;
    minutos = minutos % 60;
    segundos = segundos % 60;

    cout << "Temos " << horas << " horas, " << minutos; 
    cout << " minutos e " << segundos << " segundos.";

    return 0;

}