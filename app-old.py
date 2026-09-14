from flask import Flask, render_template, request, jsonify
from pondeuses_model import LotPondeuses

app = Flask(__name__)

# Base de données simulée en mémoire (ou à connecter à SQLite / PostgreSQL)
base_de_donnees_lots = [
    LotPondeuses("Lot A - Bâtiment 1", 1000, "2026-02-15")
]

@app.route('/pondeuses')
def page_pondeuses():
    # Prépare les données pour les afficher dans la page HTML
    stats_lots = [lot.obtenir_statistiques() for lot in base_de_donnees_lots]
    return render_template('pondeuses.html', lots=stats_lots)

@app.route('/api/ajouter_production', methods=['POST'])
def api_ajouter_production():
    data = request.json
    nom_lot = data.get('nom_lot')
    
    # Recherche du lot correspondant
    lot = next((l for l in base_de_donnees_lots if l.nom_lot == nom_lot), None)
    if not lot:
        return jsonify({"erreur": "Lot introuvable"}), 404
        
    lot.enregistrer_jour(
        date=data.get('date'),
        morts=int(data.get('morts', 0)),
        oeufs_recoltes=int(data.get('oeufs_recoltes', 0)),
        aliment_consomme_kg=float(data.get('aliment', 0))
    )
    return jsonify({"succès": True, "stats": lot.obtenir_statistiques()})

if __name__ == '__main__':
    app.run(debug=True)