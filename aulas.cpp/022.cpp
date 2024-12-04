DÚVIDA

//Uma empresa contratou um médico para avaliar
//todos os seus funcionários na própria sede da empresa. Para
//que cada funcionário saiba o horário agendado para sua
//consulta médica, você deverá fazer um programa que lê a
//matrícula do funcionário e informa o dia e horário da consulta.
//Observe que:
//• As matrículas dos funcionários são números consecutivos
//entre 1 e 30 (inclusive). Os funcionários serão atendidos em
//ordem crescente de matrícula.
//• As consultas duram uma hora e serão realizadas em uma
//única semana, de 2a a 6a. O médico estará disponível das 8
//às 14h.
//Para a matrícula 24, por exemplo, o programa deverá imprimir
//a saída: 5a-feira as 13:00 horas

#include <iostream>
using namespace std;

int main()
{
    int consulta;
    int dias;
    int horas;

    cout << "Digite o numero da sua consulta: ";
    cin >> consulta;

    dias > 1 && dias < 7;
    horas > 7 && horas < 14;
    consulta = dias * horas;

    cout << dias << "a-feira as " << horas << ":00 horas.";

    return 0;

}