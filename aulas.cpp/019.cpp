//Construa um programa que leia dois valores
//reais x e y, calcule e imprima os valores de w e
//z de acordo com as fórmulas:

//w = (2x + y)/2 e z = 1/w

//Faça o teste de mesa para as entradas x = 1.5
//e y = 2.0.

#include <iostream>
using namespace std;

int main()
{

    float x;
    float y;
    float w;
    float z;

    cout << "escreva dois valores reais para calcularmos: ";
    cin >> x >> y;

    w = (2 * x + y)/2; 
    z = 1 / w;

    cout << "Seus resultados sao " << w << "  " << z;

    return 0;
}