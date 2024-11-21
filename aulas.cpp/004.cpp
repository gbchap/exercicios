//a) Escreva uma função que recebe dois números
//inteiros e imprime a soma, o produto, a diferença, o
//quociente e o resto entre esses dois números.
//b) Faça um programa em C++ (função principal)
//que leia dois inteiros do teclado e chame a função
//da letra a).
//c) Teste seu programa com os valores 11 e 3.

#include <iostream>
using namespace std;

void calculadora (int numero1, int numero2) {
    int soma, sub, prod, quociente, resto;
    soma = numero1 + numero2;
    sub = numero1 - numero2;
    prod = numero1 * numero2;
    quociente = numero1 / numero2;
    resto = numero1 % numero2;
    cout << "soma: " << soma;
    cout << "\nsubtracao: " << sub;
    cout << "\nproduto: " << prod;
    cout << "\nquociente: " << quociente;
    cout << "\nresto: " << resto;
    return;
}

int main() {

    int valor1, valor2;
    cout << "Digite os dois numeros para a calculadora: ";
    cin >> valor1 >> valor2;
    calculadora(valor1, valor2);
    return 0;
}