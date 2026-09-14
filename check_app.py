import urllib.request
import urllib.error
import socket

URL = "http://127.0.0.1:8080/pondeuses"
PORT = 8080

def verifier_port():
    print(f"[*] Vérification du port {PORT} sur la machine locale...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        resultat = s.connect_ex(('127.0.0.1', PORT))
        if resultat == 0:
            print(f"[SUCCÈS] Le port {PORT} est ouvert et à l'écoute.")
            return True
        else:
            print(f"[ERREUR] Aucun service ne répond sur le port {PORT}. Avez-vous bien lancé 'python app.py' ?")
            return False

def tester_requete_http():
    print(f"\n[*] Test d'accès HTTP vers : {URL}")
    try:
        req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            code = response.getcode()
            print(f"[SUCCÈS] Connexion réussie ! Code HTTP reçu : {code}")
            print("[INFO] La page est accessible et renvoie du contenu.")
    except urllib.error.HTTPError as e:
        print(f"[ERREUR HTTP] Le serveur a répondu avec le code d'erreur : {e.code} ({e.reason})")
        if e.code == 403:
            print("-> Indice : Erreur 403 (Accès refusé). Vérifiez si une règle de sécurité ou un décorateur de route restreint l'accès dans votre app.py.")
    except urllib.error.URLError as e:
        print(f"[ERREUR RÉSEAU] Impossible de joindre le serveur : {e.reason}")
    except Exception as e:
        print(f"[ERREUR INATTENDUE] {e}")

if __name__ == "__main__":
    print("--- DIAGNOSTIC DU SERVEUR FARMA BeMiray ---\n")
    if verifier_port():
        tester_requete_http()
    print("\n--- FIN DU DIAGNOSTIC ---")