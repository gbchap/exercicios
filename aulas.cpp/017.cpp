/*
Faça um programa que lê um valor de salário
mínimo e o salário de um funcionário. O programa
deve calcular e imprimir quantos salários mínimos
esse funcionário ganha.
Após fazer o programa, verifique se seu programa
está correto fazendo o teste de mesa com as
entradas 800.00 e 2030.40.
*/

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{

float salMin;
float salPessoa;
salMin = 1412;

cout << "Digite salario do funcionario: " ;
cin >> salPessoa;

float numeroDeSal;
numeroDeSal = salPessoa / salMin;

cout << "O funcionario ganha " << setprecision(2) << numeroDeSal << " Salarios minimos.";

return 0;

}