import socket

class NoyauReseau:
    def __init__(self, port=5000):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def demarrer_ecoute(self):
        self.socket.bind(('0.0.0.0', self.port))
        self.socket.listen(10)
        print(f"[*] Serveur actif sur le port {self.port}...")
        return self.socket.accept()
