//Elabore um programa completo que imprima o dobro, o
//triplo e o quadrado do valor x. O valor de x pode ser
//escolhido por você ao inicializar a variável. Supondo que o
//valor de x é 3, a saída de seu programa deve ser:

//Valor: 3
//Dobro de 3: 6
//Triplo de 3: 9
//Quadrado de 3: 9

//Use variáveis para armazenar
//os valores numéricos que
//deverão ser impressos.

#include <iostream>
using namespace std;

int main() 
{

float x = 3;
float dobro = x * 2;
float triplo = x * 3;
float quadrado = x * x;
cout << "Valor: " << x;
cout << "\nDobro de 3: " << dobro;
cout << "\nTriplo de 3: " << triplo;
cout << "\nQuadrado de 3: " << quadrado;

return 0;

}
