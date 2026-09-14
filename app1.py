from flask import Flask, render_template, request, jsonify
from database import (
    init_db, 
    ajouter_lot_pondeuse, 
    enregistrer_suivi_pondeuse, 
    recuperer_lots_pondeuses_avec_stats
)

app = Flask(__name__)

# Initialisation de la base de données et des tables au démarrage
init_db()

@app.route('/pondeuses')
def page_pondeuses():
    lots = recuperer_lots_pondeuses_avec_stats()
    return render_template('pondeuses.html', lots=lots)

@app.route('/api/lots/ajouter', methods=['POST'])
def api_ajouter_lot():
    data = request.json
    ajouter_lot_pondeuse(
        nom_lot=data.get('nom_lot'),
        souche=data.get('souche', 'ISA Brown'),
        effectif_initial=int(data.get('effectif_initial', 0)),
        date_arrivee=data.get('date_arrivee'),
        age_initial_semaines=int(data.get('age_initial_semaines', 16))
    )
    return jsonify({"succès": True})

@app.route('/api/suivi/ajouter', methods=['POST'])
def api_ajouter_suivi():
    data = request.json
    enregistrer_suivi_pondeuse(
        lot_id=int(data.get('lot_id')),
        date=data.get('date'),
        morts=int(data.get('morts', 0)),
        oeufs_recoltes=int(data.get('oeufs_recoltes', 0)),
        oeufs_casses=int(data.get('oeufs_casses', 0)),
        aliment_consomme_kg=float(data.get('aliment_consomme_kg', 0.0)),
        notes=data.get('notes', '')
    )
    return jsonify({"succès": True})

if __name__ == '__main__':
    app.run(debug=True)