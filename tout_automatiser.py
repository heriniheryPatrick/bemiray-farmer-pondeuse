import os
import subprocess
import sys


def run_automation():
  base_dir = "/Users/herinihery/Documents/MONOCEROS/python/Bemirayfarmer"
  os.chdir(base_dir)

  python_env = os.path.join(base_dir, ".venv", "bin", "python")

  print("=== ÉTAPE 1 : Aspiration du site afaporc.com ===")
  try:
    subprocess.run([python_env, "copie_site.py"], check=True)
  except subprocess.CalledProcessError as e:
    print(f"Erreur lors de l'aspiration : {e}")
    return

  print("\n=== ÉTAPE 2 : Envoi automatique sur GitHub ===")
  try:
    subprocess.run([python_env, "git_auto_push.py"], check=True)
  except subprocess.CalledProcessError as e:
    print(f"Erreur lors du push Git : {e}")
    return

  print("\n✨ Processus entièrement automatisé terminé avec succès !")


if __name__ == "__main__":
  run_automation()