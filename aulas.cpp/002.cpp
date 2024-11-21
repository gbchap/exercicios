// aula do dia 18/11 revisão - cap 3 exercícios

//Vamos fazer um programa que calcula a área de um
//triângulo?
//a) Escreva uma função que recebe dois números
//reais, representando a base e a altura do triângulo,
//e que retorne um valor real representando a área.
//b) Faça um programa em C++ (função principal)
//que leia dois valores reais do teclado, chame a
//função da letra a) e imprima o resultado obtido.

#include <iostream>
using namespace std;

float areaTrianguloCalculo (float nBase, float nAltura) {
    float areaTriangulo;
    areaTriangulo = (nBase * nAltura) / 2;
    return areaTriangulo;
}

int main() {
    float base, altura;
    cout << "Escreva a base e a altura do triangulo: ";
    cin >> base >> altura;
    cout << "O triangulo tem area igual a " << areaTrianguloCalculo(base, altura);
    return 0;
}