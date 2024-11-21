//Vamos fazer um programa que calcula a soma e o
//produto de dois números inteiros?
//a) Escreva uma função que recebe dois números
//inteiros, calcula e imprime os valores da soma e
//do produto desses números.
//b) Faça um programa em C++ (função principal)
//que leia dois valores inteiros do teclado e chame a
//função da letra a).

#include <iostream>
using namespace std;

void somaProduto (int numero1, int numero2) {
    int soma, produto;
    soma = numero1 + numero2;
    produto = numero1 * numero2;
    cout << "soma: " << soma << " produto: " << produto;
    return;
}

int main() {
    int valor1, valor2;
    cout << "Escreva dois valores para somar e multiplicar: ";
    cin >> valor1 >> valor2;
    somaProduto(valor1, valor2);
    return 0;
}