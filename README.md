# Conception et développement de Distributed Log Collector, un système de collecte et agrégation de logs entre plusieurs machines: cas d’OpenBSD

# Objectifs:
1. Comprendre les communications inter-nœuds (RPC / messages).
2. Concevoir un système distribué tolérant aux pannes.
3. Appliquer les modèles producteur–consommateur distribués.

# Fonctionnalités attendues
1. Plusieurs agents installés sur différents nœuds → envoient leurs logs.
2. Un Log Aggregator reçoit, stocke et indexe les logs.
3. Support des retransmissions si le serveur central est temporairement indisponible.
4. Interface Web pour consulter :
    - logs par machine
    - logs par niveau (INFO, WARN, ERROR)

# NB: README à mettre à jour progressivement par l'équipe.
