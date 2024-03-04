#ex3
#Faça um programa que fale o nome de 5 times de futebol

import random

times_futebol = ["Palmeiras", "Vasco", "Flamengo", "Fluminense", "Fortaleza", "São Paulo", "Grêmio", "Internacional", "Botafogo", "Santos", "Vitoria", "Corinthias", "Curitiba", ]

for i in range(5):
    time = times_futebol[random.randint(0, len(times_futebol))]
    print(f"Time {i+1}: {time}")