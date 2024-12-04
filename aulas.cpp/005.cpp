//a) Elabore uma função que receba três valores
//reais e retorne a média aritmética destes valores.
//b) Em seguida, faça um programa (função
//principal) que leia três valores do teclado e imprima
//sua média, utilizando a função da letra a).

#include <iostream>
using namespace std;

float mediaValores (float valor1, float valor2, float valor3) {
    float media;
    media = (valor1 + valor2 + valor3) / 3;
    return media;
    
}
int main() { 
    float valor1, valor2, valor3;
    cout << "Digite 3 numeros para calcular sua media aritmetica: ";
    cin >> valor1 >> valor2 >> valor3;
    cout << "media: " << mediaValores(valor1, valor2, valor3);
    return 0;
}