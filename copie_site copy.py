from datetime import datetime
import os
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests

# Configuration
TARGET_URL = "https://afaporc.com"
OUTPUT_DIR = "site_copie"
visited_urls = set()

os.makedirs(OUTPUT_DIR, exist_ok=True)


def download_asset(url, folder):
  try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
      parsed_url = urlparse(url)
      filename = os.path.basename(parsed_url.path)
      if not filename or "." not in filename:
        return None

      asset_path = os.path.join(OUTPUT_DIR, folder, filename)
      os.makedirs(os.path.dirname(asset_path), exist_ok=True)

      with open(asset_path, "wb") as f:
        f.write(response.content)
      return f"{folder}/{filename}"
  except Exception:
    pass
  return None


def scrape_and_save(url):
  if url in visited_urls or not url.startswith(TARGET_URL):
    return
  visited_urls.add(url)

  print(f"Traitement : {url}")
  try:
    response = requests.get(url, timeout=10)
    if response.status_code != 200:
      return

    soup = BeautifulSoup(response.text, "html.parser")

    # Traitement des images
    for img in soup.find_all("img", src=True):
      img_url = urljoin(url, img["src"])
      local_img = download_asset(img_url, "images")
      if local_img:
        img["src"] = local_img

    # Traitement des fichiers CSS
    for link in soup.find_all("link", rel="stylesheet"):
      if link.get("href"):
        css_url = urljoin(url, link["href"])
        local_css = download_asset(css_url, "css")
        if local_css:
          link["href"] = local_css

    # Nom du fichier HTML local
    parsed_path = urlparse(url).path.strip("/")
    if not parsed_path:
      filename = "index.html"
    else:
      filename = parsed_path.replace("/", "_") + ".html"

    file_path = os.path.join(OUTPUT_DIR, filename)
    with open(file_path, "w", encoding="utf-8") as f:
      f.write(str(soup))

    # Exploration récursive des liens internes
    for a in soup.find_all("a", href=True):
      next_url = urljoin(url, a["href"])
      if next_url.startswith(TARGET_URL) and next_url not in visited_urls:
        next_url = next_url.split("#")[0]
        scrape_and_save(next_url)

  except Exception as e:
    print(f"Erreur sur {url}: {e}")


if __name__ == "__main__":
  print("Début de l'aspiration du site...")
  scrape_and_save(TARGET_URL)
  print(f"Aspiration terminée ! Fichiers enregistrés dans ./{OUTPUT_DIR}")
