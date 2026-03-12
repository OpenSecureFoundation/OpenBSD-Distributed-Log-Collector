from noyau_reseau import NoyauReseau

def traiter_flux():
    serveur = NoyauReseau(port=5000)
    while True:
        connexion, adresse = serveur.demarrer_ecoute()
        donnees = connexion.recv(1024).decode()
        print(f"[+] Reçu de {adresse}: {donnees}")
        # Logique d'insertion SQL à ajouter ici
        connexion.close()

if __name__ == "__main__":
    traiter_flux()
