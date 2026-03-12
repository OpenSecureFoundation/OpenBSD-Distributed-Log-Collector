# Conception et développement de Distributed Log Collector

Système de collecte et agrégation de logs entre plusieurs machines : cas d’OpenBSD.

## Objectifs
1. Comprendre les communications inter-nœuds (RPC / messages).
2. Concevoir un système distribué tolérant aux pannes.
3. Appliquer les modèles producteur–consommateur distribués.

## Fonctionnalités attendues
1. Plusieurs agents installés sur différents nœuds → envoient leurs logs.
2. Un Log Aggregator reçoit, stocke et indexe les logs.
3. Support des retransmissions si le serveur central est temporairement indisponible.
4. Interface Web pour consulter :
    - Logs par machine
    - Logs par niveau (INFO, WARN, ERROR)

---

## Mise à jour de l'équipe

### 1. Introduction
Le projet **Distributed Log Collector (DLC)** est une solution de monitoring distribuée conçue pour la centralisation et l'indexation de logs provenant de nœuds hétérogènes. L'objectif est de fournir une visibilité en temps réel sur l'état de santé d'un parc informatique via une architecture découplée.

### 2. Architecture du Système
Le système repose sur le modèle de conception **Producteur-Consommateur** :
* **Les Agents (Producteurs)** : Scripts légers déployés sur les nœuds distants. Ils assurent la capture des événements système et leur transmission vers le concentrateur.
* **L'Agrégateur (Consommateur)** : Serveur centralisé gérant la réception des flux via Sockets TCP, le traitement des trames et la persistance en base de données MariaDB.

### 3. Spécifications Techniques

#### 3.1 Communications Inter-nœuds
La communication est établie via le protocole TCP sur le port **5000**. Le format d'échange suit une logique de sérialisation par délimiteur : `hostname | niveau_gravite | message_systeme`. Ce choix permet une interopérabilité entre différents systèmes d'exploitation (OpenBSD, Kali Linux) sans dépendance logicielle lourde.

#### 3.2 Tolérance aux Pannes
Conformément aux exigences de conception des systèmes distribués, l'agent intègre une logique de **retransmission automatique** (*Retry Mechanism*). En cas de rupture de connectivité avec l'agrégateur, l'agent entre en boucle de temporisation jusqu'à la restauration du service central, garantissant ainsi l'intégrité des données de log.

#### 3.3 Structuration Logicielle
Le projet adopte une approche modulaire pour respecter le principe de [Séparation des préoccupations (SoC)](https://fr.wikipedia.org/wiki/S%C3%A9paration_des_pr%C3%A9occupations) :
* **Backend** : Logique de gestion des Sockets et interaction avec la couche de persistance.
* **Frontend** : Interface de supervision développée avec une séparation stricte entre la logique métier (PHP/PDO), les feuilles de style (CSS) et la couche de présentation (HTML).

### 4. Fonctionnalités Implémentées
* Collecte multi-agents en temps réel.
* Indexation et stockage permanent (MariaDB).
* Filtrage multicritères (Source, Niveau de gravité).
* Visualisation des alertes critiques par récurrence.

### 5. Déploiement
1. **Initialisation** de la base de données via les scripts fournis dans le répertoire `/sql`.
2. **Lancement** du service d'agrégation : `python3 backend/main.py`.
3. **Déploiement** et exécution des agents sur les nœuds cibles : `python3 agents/agent_linux.py`.
