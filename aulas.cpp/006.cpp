//Considerando a fórmula para o cálculo da
//distância entre dois pontos (x1, y1) e (x2, y2):
//a) Escreva uma função que receba como
//parâmetros as coordenadas de dois pontos e retorne
//a distância entre eles.
//b) Escreva um programa em C++ (função principal)
//que leia do teclado as coordenadas dos 3 vértices
///de um triângulo, calcule e imprima o perímetro deste
//triângulo, chamando a função anterior.

#include <iostream>
#include <cmath>
using namespace std;

float calculoDist(int x1, int x2, int y1, int y2)
{
    int calculo;
    calculo = sqrt(pow((x2 - x1), 2) * pow((y2 - y1), 2));
    cout << calculo;
    return 0;
}

int main()
{
    int x1, x2, x3, y1, y2, y3, vert1, vert2, vert3;


    cout << "Digite as coordenadas de 3 vertices de um triangulo: ";
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    calculoDist(x1, y1, x2, y2) + calculoDist(x2, y2, x3, y3) + calculoDist(x3, y3, x1, y1);

    return 0;

}