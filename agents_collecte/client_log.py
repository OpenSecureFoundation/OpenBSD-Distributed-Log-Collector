import socket
import time

def envoyer_log(message):
    serveur = ('127.0.0.1', 5000)
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(serveur)
            sock.send(message.encode())
            sock.close()
            break # Succès
        except socket.error:
            print("Connexion impossible, nouvelle tentative...")
            time.sleep(5)

envoyer_log("kali|INFO|Test du mécanisme de retransmission")
