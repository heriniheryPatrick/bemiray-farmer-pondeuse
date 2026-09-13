#!/bin/bash

python3 -c "
import re

# 1. Mise à jour de index.html (les 3 cartes sur la page d'accueil)
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        idx = f.read()
    
    # Carte 1: Alimentation (Céréales / Provende)
    # On remplace l'image de la première carte
    idx = re.sub(
        r'(<div class=\"h-48 overflow-hidden\">\s*<img src=\")[^\"]+(\" alt=\"Alimentation volaille\")',
        r'\1https://images.unsplash.com/photo-1574943320219-553eb213f72d?auto=format&fit=crop&w=600&q=80\2',
        idx
    )
    
    # Carte 2: Pondeuses (Poules pondeuses / nid)
    idx = re.sub(
        r'(<div class=\"h-48 overflow-hidden\">\s*<img src=\")[^\"]+(\" alt=\"Pondeuses\")',
        r'\1https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=600&q=80\2',
        idx
    )
    
    # Carte 3: Poulets de Chair (Votre image locale poulet-chair.jpg)
    idx = re.sub(
        r'(<div class=\"h-48 overflow-hidden\">\s*<img src=\")[^\"]+(\" alt=\"Poulets de chair\")',
        r'\1poulet-chair.jpg\2',
        idx
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx)
    print('index.html mis à jour avec 3 images distinctes.')
except FileNotFoundError:
    print('index.html introuvable.')

# 2. Mise à jour de alimentation.html
try:
    with open('alimentation.html', 'r', encoding='utf-8') as f:
        alt = f.read()
    alt = re.sub(r'<img src=\"https://images.unsplash.com/[^\"]+\" alt=\"Alimentation\"', '<img src=\"https://images.unsplash.com/photo-1574943320219-553eb213f72d?auto=format&fit=crop&w=1200&q=80\" alt=\"Alimentation\"', alt)
    with open('alimentation.html', 'w', encoding='utf-8') as f:
        f.write(alt)
    print('alimentation.html mis à jour.')
except FileNotFoundError:
    pass

# 3. Mise à jour de pondeuses.html / pondeuse.html
for filename in ['pondeuses.html', 'pondeuse.html']:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            pon = f.read()
        pon = re.sub(r'<img src=\"https://images.unsplash.com/[^\"]+\" alt=\"Sacs de provende et alimentation avicole\"', '<img src=\"https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=1200&q=80\" alt=\"Pondeuses\"', pon)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(pon)
        print(f'{filename} mis à jour.')
    except FileNotFoundError:
        pass

# 4. Mise à jour de chair.html
try:
    with open('chair.html', 'r', encoding='utf-8') as f:
        chr_content = f.read()
    chr_content = re.sub(r'<img src=\"https://images.unsplash.com/[^\"]+\" alt=\"Poulets de chair\"', '<img src=\"poulet-chair.jpg\" alt=\"Poulets de chair\"', chr_content)
    with open('chair.html', 'w', encoding='utf-8') as f:
        f.write(chr_content)
    print('chair.html mis à jour.')
except FileNotFoundError:
    pass
"
