// exercicios cap. 2

//Construa uma sequência de instruções para calcular o
//volume de um copo com 12 cm de altura e 6 cm de
//diâmetro, da seguinte forma:
//• Declare as variáveis para raio, altura e volume;
//• Inicialize as variáveis cujo valor é conhecido;
//• Calcule o valor do volume e armazene-o na variável.


#include <iostream>
#define PI 3.14
using namespace std;

int main () {
    float raio = 3;
    float altura = 12;
    float volume;

    volume = PI * (raio * raio) * altura;
    cout << volume << " cm.";

    return 0;
}