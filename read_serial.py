import serial
import time
import csv

# Configuração da porta serial e taxa de baud
porta_serial = "COM3"  # Ajuste conforme necessário
baud_rate = 9600

# Conectando à porta serial
try:
    arduino = serial.Serial(porta_serial, baud_rate, timeout=1)
    print(f"Conectado ao Arduino na porta {porta_serial}")
except Exception as e:
    print(f"Erro ao conectar ao Arduino: {e}")
    exit()

# Abrindo o arquivo CSV em modo de escrita contínua
with open("dados.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    
    # Verifica se o cabeçalho já foi escrito
    file.seek(0, 2)  # Move para o final do arquivo
    if file.tell() == 0:
        writer.writerow(["User", "Data"])  # Cabeçalho do arquivo CSV

    # Loop para leitura da porta serial
    while True:
        try:
            if arduino.in_waiting > 0:  # Verifica se há dados disponíveis
                data = arduino.readline().decode('utf-8').strip()  # Lê os dados
                
                if data.isdigit():  # Verifica se o dado é um número inteiro
                    user = int(data)
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Horário atual
                    writer.writerow([user, timestamp])  # Escreve no CSV
                    file.flush()  # Garante que os dados sejam gravados imediatamente
                    print(f"User: {user}, Data: {timestamp}")

            time.sleep(1)  # Intervalo para evitar leitura excessiva
        except Exception as e:
            print(f"Erro durante a execução: {e}")
            break

