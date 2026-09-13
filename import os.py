import os
import requests
from bs4 import BeautifulSoup

# URL cible
URL = "https://koklovi.com"
OUTPUT_DIR = "/users/herinihery/documents/Bemirayfarmer/PONDEUSE"

print(f"Téléchargement du contenu de {URL}...")
response = requests.get(URL)

if response.status_code == 200:
    # 1. Sauvegarde de la page HTML brute
    html_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"[+] Fichier HTML sauvegardé : {html_path}")

    # 2. Extraction et nettoyage du contenu textuel principal
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Supprimer les scripts et styles superflus
    for script in soup(["script", "style"]):
        script.extract()
        
    text = soup.get_text(separator='\n')
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    clean_text = '\n'.join(chunk for chunk in chunks if chunk)

    text_path = os.path.join(OUTPUT_DIR, "contenu_aspire.txt")
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(clean_text)
    print(f"[+] Contenu textuel extrait et sauvegardé : {text_path}")

else:
    print(f"[-] Erreur lors de l'accès au site : Code {response.status_code}")