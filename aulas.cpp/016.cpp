//Faça um programa que lê uma temperatura em
//graus Celsius e a imprime convertida em graus
//Fahrenheit. A fórmula de conversão é:

//F ← (9*C+160)/5

#include <iostream>
using namespace std;

int main() 
{
    float celsius;
    cout << "Digite a temperatura em graus celsius: ";
    cin >> celsius;
    float fahr;
    
    fahr = (9 * celsius + 160) / 5;
    cout << "Essa temperatura equivale a " << fahr << " graus fahrenheint.";

    return 0;

}