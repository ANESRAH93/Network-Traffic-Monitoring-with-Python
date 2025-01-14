from scapy.all import sniff, IP
import time

# Variables pour surveiller le trafic
paquet_count = 0
start_time = time.time()
anomaly_threshold = 100  # Nombre de paquets par seconde pour déclencher une alerte

def detect_anomaly(packet):
    global paquet_count, start_time

    # Incrémenter le compteur de paquets
    paquet_count += 1

    # Calculer le temps écoulé
    elapsed_time = time.time() - start_time

    # Si le temps écoulé dépasse 1 seconde, vérifier le taux de paquets
    if elapsed_time > 1:
        packets_per_second = paquet_count / elapsed_time

        # Détecter une anomalie si le taux de paquets dépasse le seuil
        if packets_per_second > anomaly_threshold:
            print(f"[ALERTE] Anomalie détectée : {packets_per_second:.2f} paquets/seconde")

        # Réinitialiser le compteur et le temps
        paquet_count = 0
        start_time = time.time()

# Démarrer la surveillance du réseau
print("Démarrage de la surveillance réseau...")
sniff(prn=detect_anomaly, filter="ip")  # Filtrer uniquement les paquets IP