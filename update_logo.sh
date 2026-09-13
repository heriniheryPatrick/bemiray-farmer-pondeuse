#!/bin/bash

LOGO_TAG='<img src="logo-bemiray.jpg" alt="Logo BeMiray Farmer" class="w-12 h-12 object-cover rounded-xl shadow-md">'

for file in index.html alimentation.html pondeuses.html pondeuse.html chair.html; do
    if [ -f "$file" ]; then
        # Remplacement propre de l'ancienne balise de logo/émoji par la nouvelle balise image
        python3 -c "
with open('$file', 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Cherche le bloc du logo (soit un emoji, soit une div BM, soit une ancienne image) et le remplace
new_content = re.sub(
    r'<div class=\"flex items-center space-x-3 mb-4 md:mb-0\">.*?</div>\s*<div>', 
    '''<div class=\"flex items-center space-x-3 mb-4 md:mb-0\">
    <img src=\"logo-bemiray.jpg\" alt=\"Logo BeMiray Farmer\" class=\"w-12 h-12 object-cover rounded-xl shadow-md\">
    <div>''', 
    content, 
    flags=re.DOTALL
)

if new_content == content:
    # Alternative pattern if structure differs slightly
    new_content = re.sub(
        r'<div class=\"flex items-center space-x-3 mb-4 md:mb-0\">.*?<h1',
        '''<div class=\"flex items-center space-x-3 mb-4 md:mb-0\">
    <img src=\"logo-bemiray.jpg\" alt=\"Logo BeMiray Farmer\" class=\"w-12 h-12 object-cover rounded-xl shadow-md\">
    <div>
    <h1''',
        content,
        flags=re.DOTALL
    )

with open('$file', 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f'Mis à jour : {file}')
"
    fi
done

echo "Mise à jour des logos terminée avec succès !"
