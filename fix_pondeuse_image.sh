#!/bin/bash

python3 -c "
import re

# URL d'une image stable représentant une poule pondeuse
pondeuse_img = 'https://images.unsplash.com/photo-1599814594770-b1d69d4c9423?auto=format&fit=crop&w=1200&q=80'

# 1. Mise à jour de pondeuses.html / pondeuse.html
for filename in ['pondeuses.html', 'pondeuse.html']:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        # Remplacement de l'image de la bannière en haut
        content = re.sub(r'https://images.unsplash.com/[^\"]+', pondeuse_img, content, count=1)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'{filename} mis à jour avec la photo de poule pondeuse.')
    except FileNotFoundError:
        pass

# 2. Mise à jour de la carte Pondeuses dans index.html
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        idx = f.read()
    # On cible l'image de la 2ème carte (pondeuses)
    idx = re.sub(r'https://images.unsplash.com/photo-1599814594770-b1d69d4c9423[^\"]*', 'https://images.unsplash.com/photo-1599814594770-b1d69d4c9423?auto=format&fit=crop&w=600&q=80', idx)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx)
    print('index.html (carte pondeuses) mis à jour.')
except FileNotFoundError:
    print('index.html introuvable.')
"
echo "Mise à jour des images de pondeuses terminée !"
