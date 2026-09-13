from datetime import datetime
import os
import subprocess


def update_and_push_repo(repo_path):
  if not os.path.exists(repo_path):
    print(f"Erreur : Le dossier {repo_path} n'existe pas.")
    return

  os.chdir(repo_path)
  print(f"Dossier de travail Git : {os.getcwd()}")

  try:
    # Petit fichier de log pour enregistrer chaque mise à jour
    with open("update_log.txt", "a", encoding="utf-8") as f:
      f.write(
          f"Mise à jour du site le :"
          f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
      )

    # Vérifier s'il y a des changements
    status_result = subprocess.run(
        ["git", "status", "--porcelain"], capture_output=True, text=True
    )
    if not status_result.stdout.strip():
      print("Aucune modification détectée sur le site. Rien à envoyer.")
      return

    # Git Add, Commit & Push
    subprocess.run(["git", "add", "."], check=True)
    print("-> Fichiers ajoutés (git add).")

    commit_msg = (
        f"Mise à jour automatique du contenu -"
        f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    print(f"-> Commit effectué : '{commit_msg}'")

    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("-> Modifications envoyées sur GitHub avec succès !")

  except subprocess.CalledProcessError as e:
    print(f"Erreur Git : {e}")


if __name__ == "__main__":
  # On cible le sous-dossier contenant les fichiers du site
  dossier_projet = "./site_copie"
  update_and_push_repo(dossier_projet)
