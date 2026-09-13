#!/bin/bash

python3 -c "
import re

# Remplacement dans chair.html pour pointer vers votre photo locale
try:
    with open('chair.html', 'r', encoding='utf-8') as f:
        content = f.read()
    # On remplace l'image de la bannière par votre image locale poulet-chair.jpg
    content = re.sub(r'https://images.unsplash.com/[^\"]+', 'poulet-chair.jpg', content, count=1)
    with open('chair.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('chair.html configuré avec poulet-chair.jpg')
except FileNotFoundError:
    print('chair.html introuvable.')

# Remplacement dans index.html pour la carte Poulets de Chair
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        idx = f.read()
    idx = re.sub(r'https://images.unsplash.com/photo-1548550023-2bdb3c5beed7[^\"]*', 'poulet-chair.jpg', idx)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx)
    print('index.html mis à jour avec poulet-chair.jpg')
except FileNotFoundError:
    print('index.html introuvable.')
"
