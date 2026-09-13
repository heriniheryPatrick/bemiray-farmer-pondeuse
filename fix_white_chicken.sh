#!/bin/bash

python3 -c "
import re

# URL d'une belle poule blanche (Unsplash stable)
white_chicken_img = 'https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=1200&q=80'

# 1. Mise à jour de chair.html
try:
    with open('chair.html', 'r', encoding='utf-8') as f:
        content = f.read()
    # Remplacement de l'image de fond de l'en-tête
    content = re.sub(r'https://images.unsplash.com/[^\"]+', white_chicken_img, content, count=1)
    with open('chair.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('chair.html mis à jour avec la poule blanche.')
except FileNotFoundError:
    print('chair.html introuvable.')

# 2. Mise à jour de la carte Poulets de Chair dans index.html
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        idx = f.read()
    # On cible l'image de la 3ème carte (poulets de chair)
    idx = re.sub(r'https://images.unsplash.com/photo-1563245372-f21724e3856d[^\"]*', 'https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=600&q=80', idx)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx)
    print('index.html (carte chair) mis à jour.')
except FileNotFoundError:
    print('index.html introuvable.')
"
echo "Mise à jour des images de poules blanches terminée !"
