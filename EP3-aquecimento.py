# -*- coding: utf-8 -*-

"""
     Nome do aluno: GUSTAVO PINHEIRO DE OLIVEIRA
     Número USP: 13687800
     Curso: ASTRONOMIA
     Disciplina: MAC0115 Introdução à Computação
     Turma 24
     Exercício-Programa EP3-aquecimento

     DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.
     TODAS AS PARTES ORIGINAIS DESTE EXERCÍCIO-PROGRAMA FORAM
     DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
     DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
     OU PLÁGIO.
     DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS DESTE
     PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A SUA DISTRIBUIÇÃO.
     ESTOU CIENTE QUE OS CASOS DE PLÁGIO E DESONESTIDADE ACADÊMICA
     SERÃO TRATADOS SEGUNDO OS CRITÉRIOS DIVULGADOS NA PÁGINA DA
     DISCIPLINA.

"""
import math

grav = 6.67 * (10 ** (-11))

def main():

    bodies = [[[] for j in range(5)] for i in range(2)]

    for i in range(2):
        bodies[i] = [float(x) for x in input().split()]

    t = int(input())
    dt = int(input())

    k = (t / dt) + 1
    num_de_linhas = 0

    # PRINT DA POSIÇÃO INICIAL DA LUA
    print("{:.5e}".format(bodies[1][0]), "{:.5e}".format(bodies[1][1]))

    while (num_de_linhas < k):
        body_terra = bodies[0]
        body_lua = bodies[1]

        distancia = dist(body_terra, body_lua)

        forcas = fg(1, bodies, distancia)

        fx = forcas[0]
        fy = forcas[1]

        body_lua = atualiza(bodies[1], fx, fy, dt)
        print("{:.5e}".format(body_lua[0]), "{:.5e}".format(body_lua[1]))

        bodies = [body_terra, body_lua]

        num_de_linhas += 1

def dist(body_a, body_b):
    '''
    (list, list) -> (float)

    Esta função recebe dois corpos body_a, body_b.
    Retorna a distância entre os mesmos.
    '''
    dist = []

    # OBTENDO A DISTÂNCIA X
    distx_a = body_a[0]
    distx_b = body_b[0]
    distx = distx_a - distx_b

    # OBTENDO A DISTÂNCIA Y
    disty_a = body_a[1]
    disty_b = body_b[1]
    disty = disty_a - disty_b

    soma_distancia = (distx ** 2) + (disty ** 2)

    dist = math.sqrt(soma_distancia)

    dist = round(dist, 10)

    return dist


def fg(id, bodies, dist):
    '''
    (int, list, float) -> (float)

    Esta função recebe um inteiro id, uma lista de
    corpos bodies e um float com o valor da distância.
    Retorna  a força resultante no corpo bodies[id].
    '''
    fx, fy = 0, 0

    massa_sistema = 1
    for i in range(len(bodies)):
        massa_sistema = massa_sistema * (bodies[i][4])

    distx = bodies[id][0]
    disty = bodies[id][1]

    forca = - (grav * massa_sistema / (dist ** 2))

    fx = forca * distx / dist
    fy = forca * disty / dist

    fx = round(fx, 10)
    fy = round(fy, 10)

    return fx, fy

def atualiza(body, fx, fy, dt):
    '''
    (list, float, float, float) -> (list)

    Esta função recebe um corpo, as forças fx, fy
    atuando no mesmo e um intervalo	de tempo dt
    e retorna o corpo atualizado após o intervalo.
    '''

    new_body = [0, 0, 0, 0, 0]

    rx = body[0]
    ry = body[1]
    vx = body[2]
    vy = body[3]
    massa = body[4]

    # DADOS EM X
    aceleracao_x = round((fx / massa), 10)
    new_vx = round((vx + dt * aceleracao_x), 10)
    new_rx = round((rx + dt * new_vx), 10)

    # DADOS EM Y
    aceleracao_y = round((fy / massa), 10)
    new_vy = round((vy + dt * aceleracao_y), 10)
    new_ry = round((ry + dt * new_vy), 10)

    new_body[0] = round(new_rx, 10)
    new_body[1] = round(new_ry, 10)
    new_body[2] = round(new_vx, 10)
    new_body[3] = round(new_vy, 10)
    new_body[4] = round(massa, 10)

    return new_body

main()
