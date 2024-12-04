//Faça um programa que leia três notas de um
//aluno, calcule e imprima a média ponderada,
//sabendo que as notas possuem peso 2, 3 e 5.
//Faça o teste de mesa com as notas 10, 8 e 9
//como entrada.

#include <iostream>
using namespace std;

int main()
{

    float nota1;
    float nota2;
    float nota3;

    cout << "Digite as 3 notas dos alunos para saber a media: " ;
    cin >> nota1 >> nota2 >> nota3;

    float media;
    media = (2 * nota1 + 3 * nota2 + 5 * nota3) / 10;

    cout << "a media e " << media;

return 0;
}
