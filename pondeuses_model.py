import sqlite3
from datetime import datetime

DB_NAME = "farma_bemiray.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Lots de pondeuses
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lots_pondeuses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_lot TEXT NOT NULL,
            souche TEXT DEFAULT 'ISA Brown',
            effectif_initial INTEGER NOT NULL,
            date_arrivee TEXT NOT NULL,
            age_initial_semaines INTEGER DEFAULT 16,
            statut TEXT DEFAULT 'Actif'
        )
    ''')
    
    # 2. Journal de production et alimentation quotidien
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS suivi_pondeuses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lot_id INTEGER,
            date TEXT NOT NULL,
            morts INTEGER DEFAULT 0,
            oeufs_bons INTEGER DEFAULT 0,
            oeufs_casses INTEGER DEFAULT 0,
            oeufs_sales INTEGER DEFAULT 0,
            poids_moyen_oeuf_g REAL DEFAULT 0.0,
            aliment_consomme_kg REAL DEFAULT 0.0,
            notes TEXT,
            FOREIGN KEY (lot_id) REFERENCES lots_pondeuses (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def ajouter_lot_pondeuse(nom_lot, souche, effectif_initial, date_arrivee, age_initial_semaines):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO lots_pondeuses (nom_lot, souche, effectif_initial, date_arrivee, age_initial_semaines)
        VALUES (?, ?, ?, ?, ?)
    ''', (nom_lot, souche, effectif_initial, date_arrivee, age_initial_semaines))
    conn.commit()
    conn.close()

def enregistrer_suivi(lot_id, date, morts, bons, casses, sales, poids_oeuf, aliment, notes):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO suivi_pondeuses (lot_id, date, morts, oeufs_bons, oeufs_casses, oeufs_sales, poids_moyen_oeuf_g, aliment_consomme_kg, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (lot_id, date, morts, bons, casses, sales, poids_oeuf, aliment, notes))
    conn.commit()
    conn.close()

def recuperer_lots_avec_details():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT l.*, 
               COALESCE(SUM(s.morts), 0) as total_morts,
               COALESCE(SUM(s.oeufs_bons), 0) as total_bons,
               COALESCE(SUM(s.oeufs_casses), 0) as total_casses,
               COALESCE(SUM(s.oeufs_sales), 0) as total_sales,
               COALESCE(SUM(s.aliment_consomme_kg), 0) as total_aliment,
               AVG(NULLIF(s.poids_moyen_oeuf_g, 0)) as moy_poids_oeuf
        FROM lots_pondeuses l
        LEFT JOIN suivi_pondeuses s ON l.id = s.lot_id
        GROUP BY l.id
    ''')
    rows = cursor.fetchall()
    conn.close()
    
    resultats = []
    for row in rows:
        effectif_actuel = row['effectif_initial'] - row['total_morts']
        
        # Calcul de l'âge dynamique en semaines par rapport à la date d'arrivée
        date_arr = datetime.strptime(row['date_arrivee'], '%Y-%m-%d')
        jours_ecoules = (datetime.now() - date_arr).days
        age_actuel_semaines = row['age_initial_semaines'] + (jours_ecoules // 7)
        
        total_oeufs = row['total_bons'] + row['total_casses'] + row['total_sales']
        total_plaques = round(total_oeufs / 30, 1)
        
        # Taux de ponte global (méthode simplifiée ou cumulée)
        taux_ponte_moyen = round((total_oeufs / (row['effectif_initial'] * max(jours_ecoules, 1)) * 100), 1) if jours_ecoules > 0 else 0

        resultats.append({
            "id": row['id'],
            "nom_lot": row['nom_lot'],
            "souche": row['souche'],
            "effectif_initial": row['effectif_initial'],
            "effectif_actuel": effectif_actuel,
            "total_morts": row['total_morts'],
            "age_semaines": age_actuel_semaines,
            "total_oeufs": total_oeufs,
            "total_plaques": total_plaques,
            "total_aliment_kg": round(row['total_aliment'], 1),
            "poids_moyen_oeuf": round(row['moy_poids_oeuf'] or 0, 1),
            "taux_ponte": taux_ponte_moyen
        })
    return resultats