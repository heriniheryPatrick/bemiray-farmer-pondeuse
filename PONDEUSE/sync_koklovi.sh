#!/bin/bash

# Configuration
URL_API="https://koklovi.com/api/v1/dashboard"
TOKEN_ACCES="VOTRE_TOKEN_ICI" # Remplacez par votre token d'accès réel
FICHIER_SORTIE="koklovi_data.json"

echo "Connexion à la plateforme Koklovi en cours..."

# Exécution de la requête HTTP avec curl
reponse_http=$(curl -s -o "$FICHIER_SORTIE" -w "%{http_code}" -X GET "$URL_API" \
    -H "Authorization: Bearer $TOKEN_ACCES" \
    -H "Content-Type: application/json")

# Vérification du code de retour HTTP
if [ "$reponse_http" -eq 200 ]; then
    echo "Succès ! Données synchronisées et enregistrées dans '$FICHIER_SORTIE'."
    
    # Optionnel : Afficher un aperçu des données récupérées si l'outil 'jq' est installé sur votre Mac
    if command -v jq &> /dev/null; then
        echo "--- Aperçu des données ---"
        jq . "$FICHIER_SORTIE"
    fi
else
    echo "Erreur lors de la synchronisation (Code HTTP : $reponse_http)."
    echo "Vérifiez votre URL d'API ou votre jeton d'accès."
    # Supprimer le fichier de sortie vide ou invalide
    rm -f "$FICHIER_SORTIE"
fi