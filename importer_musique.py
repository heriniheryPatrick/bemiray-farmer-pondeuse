import os
import subprocess

def trouver_et_importer_mp3():
    # Dossiers principaux à scanner sur votre Mac
    dossiers_a_scanner = [
        os.path.expanduser("~/Music"),
        os.path.expanduser("~/Downloads"),
        os.path.expanduser("~/Documents"),
        os.path.expanduser("~/Desktop")
    ]
    
    print("Recherche automatique des fichiers MP3 sur le Mac...")
    fichiers_mp3 = set()
    
    # Recherche récursive de tous les .mp3
    for dossier in dossiers_a_scanner:
        if os.path.exists(dossier):
            for root, dirs, files in os.walk(dossier):
                for file in files:
                    if file.lower().endswith('.mp3'):
                        chemin_complet = os.path.join(root, file)
                        fichiers_mp3.add(chemin_complet)
                        
    print(f"{len(fichiers_mp3)} fichier(s) MP3 trouvé(s). Importation en cours...")
    
    compteur = 0
    for chemin_complet in fichiers_mp3:
        # Script AppleScript pour l'application Musique
        applescript = f'''
        tell application "Music"
            add (POSIX file "{chemin_complet}")
        end tell
        '''
        
        try:
            subprocess.run(['osascript', '-e', applescript], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"Importé avec succès : {os.path.basename(chemin_complet)}")
            compteur += 1
        except subprocess.CalledProcessError:
            print(f"Échec pour : {os.path.basename(chemin_complet)}")
            
    print(f"\nOpération terminée ! {compteur} fichier(s) ajouté(s) à Apple Musique sans intervention.")

if __name__ == "__main__":
    trouver_et_importer_mp3()