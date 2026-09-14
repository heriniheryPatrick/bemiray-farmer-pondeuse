from flask import Flask, render_template, request, jsonify
from pondeuses_model import init_db, ajouter_lot_pondeuse, enregistrer_suivi, recuperer_lots_avec_details

# 1. Initialisation de l'application Flask
app = Flask(__name__)
init_db()

# 2. Page d'accueil centrale FARMA BeMiray
@app.route('/')
def index():
    return render_template('index.html')

# 3. Module Pondeuses
@app.route('/pondeuses')
def page_pondeuses():
    lots = recuperer_lots_avec_details()
    return render_template('pondeuses.html', lots=lots)

# 4. Module Alimentation
@app.route('/alimentation')
def page_alimentation():
    return render_template('alimentation.html')

# 5. API - Ajout d'un lot de pondeuses
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

# 6. API - Enregistrement du suivi journalier
@app.route('/api/suivi/ajouter', methods=['POST'])
def api_ajouter_suivi():
    data = request.json
    enregistrer_suivi(
        lot_id=int(data.get('lot_id')),
        date=data.get('date'),
        morts=int(data.get('morts', 0)),
        bons=int(data.get('oeufs_bons', 0)),
        casses=int(data.get('oeufs_casses', 0)),
        sales=int(data.get('oeufs_sales', 0)),
        poids_oeuf=float(data.get('poids_moyen_oeuf_g', 0.0)),
        aliment=float(data.get('aliment_consomme_kg', 0.0)),
        notes=data.get('notes', '')
    )
    return jsonify({"succès": True})

if __name__ == '__main__':
    app.run(port=8080, debug=True)