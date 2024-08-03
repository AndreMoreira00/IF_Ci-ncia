import serial

porta = "COM4"
velocidade = 9600

conecao = serial.Serial(porta, velocidade)

while True:
  opcao = input("a/A - Led Verde\nb/B - Led Amarelo\nc/C - Led Vermelho\n")
  if opcao == "a":
    conecao.write(b'a')
    
  if opcao == "b":
    conecao.write(b'b')
    
  if opcao == "c":
    conecao.write(b'c')
    
  if opcao == "A":
    conecao.write(b'A')
    
  if opcao == "B":
    conecao.write(b'B')
    
  if opcao == "C":
    conecao.write(b'C')
    
conecao.close()