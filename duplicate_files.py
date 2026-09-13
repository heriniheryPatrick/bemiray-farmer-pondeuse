import os
import hashlib

def obtenir_hash_fichier(chemin_fichier):
    """Calcule le hash MD5 d'un fichier pour identifier les doublons stricts."""
    hasher = hashlib.md5()
    try:
        with open(chemin_fichier, 'rb') as f:
            # Lecture par blocs pour économiser la mémoire
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return None

def supprimer_doublons_mp3():
    # Dossiers principaux à analyser sur votre Mac
    dossiers_a_scanner = [
        os.path.expanduser("~/Music"),
        os.path.expanduser("~/Downloads"),
        os.path.expanduser("~/Documents"),
        os.path.expanduser("~/Desktop")
    ]
    
    fichiers_vus = {} # Dictionnaire pour stocker les hashs : {hash: premier_chemin}
    doublons_supprimes = 0
    
    print("Analyse des dossiers et recherche des doublons MP3 en cours...")
    
    for dossier in dossiers_a_scanner:
        if os.path.exists(dossier):
            for root, dirs, files in os.walk(dossier):
                for file in files:
                    if file.lower().endswith('.mp3'):
                        chemin_complet = os.path.join(root, file)
                        
                        # Calcul du hash du fichier
                        file_hash = obtenir_hash_fichier(chemin_complet)
                        if not file_hash:
                            continue
                        
                        # Si le hash existe déjà, c'est un doublon exact
                        if file_hash in fichiers_vus:
                            try:
                                os.remove(chemin_complet)
                                print(f"Supprimé (doublon) : {chemin_complet}")
                                print(f"   -> Conservé : {fichiers_vus[file_hash]}")
                                doublons_supprimes += 1
                            except Exception as e:
                                print(f"Erreur lors de la suppression de {chemin_complet}: {e}")
                        else:
                            # Premier exemplaire rencontré, on le mémorise
                            fichiers_vus[file_hash] = chemin_complet
                            
    print(f"\nNettoyage terminé ! {doublons_supprimes} fichier(s) MP3 en double ont été supprimés.")

if __name__ == "__main__":
    supprimer_doublons_mp3()