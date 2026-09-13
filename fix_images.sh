#!/bin/bash

python3 -c "
import re

# Fichier alimentation.html
with open('alimentation.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacement de l'image de fond dans alimentation.html par une image de grains/provende stable
content = re.sub(r'https://images.unsplash.com/[^\"]+', 'https://images.unsplash.com/photo-1574943320219-553eb213f72d?auto=format&fit=crop&w=1200&q=80', content, count=1)

with open('alimentation.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Alimentation.html corrigé.')

# Fichier index.html (carte pondeuses et carte alimentation)
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# On s'assure que les images des cartes index sont propres et stables (alimentation et poules)
# Alimentation
idx_content = re.sub(r'https://images.unsplash.com/photo-1516467508483-a7212febe31a[^\"]*', 'https://images.unsplash.com/photo-1574943320219-553eb213f72d?auto=format&fit=crop&w=600&q=80', idx_content)
# Pondeuses (vraie image de poules pondeuses / élevage)
idx_content = re.sub(r'https://images.unsplash.com/photo-1599814594770-b1d69d4c9423[^\"]*', 'https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=600&q=80', idx_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)
print('Index.html corrigé.')
"
echo "Correction des images terminée !"
