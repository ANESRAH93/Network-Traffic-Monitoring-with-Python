# Surveillance réseau avec Python

Ce projet est un script Python qui surveille l'activité réseau et détecte des anomalies, comme une augmentation soudaine du trafic. Il utilise la bibliothèque `scapy` pour capturer et analyser les paquets réseau.

## Fonctionnalités
- Surveillance en temps réel du trafic réseau.
- Détection d'anomalies basées sur le taux de paquets par seconde.
- Filtrage des paquets IP pour une analyse ciblée.

## Technologies utilisées
- **Python** : Langage de programmation principal.
- **Scapy** : Bibliothèque pour la manipulation et l'analyse de paquets réseau.
- **Analyse réseau** : Surveillance et détection d'anomalies.

## Comment exécuter le script

### Prérequis
1. **Installez Python** :
   - Téléchargez et installez Python depuis [python.org](https://www.python.org/downloads/).
   - Assurez-vous que Python est ajouté à votre PATH.

2. **Installez les dépendances** :
   - Exécutez la commande suivante pour installer `scapy` :
     ```bash
     pip install scapy
     ```

### Exécution
1. **Clonez ce dépôt** :
   ```bash
   git clone https://github.com/ANESRAH93/Network-Traffic-Monitoring-with-Python.git

### Naviguez vers le dossier du projet :

cd Network-Traffic-Monitoring-with-Python
### Exécutez le script :
python surveillance_reseau.py
