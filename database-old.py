import sqlite3
from datetime import datetime

DB_NAME = "farma_bemiray.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Permet d'accéder aux colonnes par leur nom
    return conn

def init_db():
    """Initialise la base de données et crée les tables si elles n'existent pas"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Table des lots de pondeuses
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_lot TEXT NOT NULL,
            souche TEXT,
            effectif_initial INTEGER NOT NULL,
            date_arrivee TEXT NOT NULL,
            age_initial_semaines INTEGER DEFAULT 16,
            statut TEXT DEFAULT 'Actif'
        )
    ''')
    
    # Table du suivi journalier (production, mortalité, alimentation)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS suivi_journalier (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lot_id INTEGER,
            date TEXT NOT NULL,
            morts INTEGER DEFAULT 0,
            oeufs_recoltes INTEGER DEFAULT 0,
            oeufs_casses INTEGER DEFAULT 0,
            aliment_consomme_kg REAL DEFAULT 0.0,
            notes TEXT,
            FOREIGN KEY (lot_id) REFERENCES lots (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def ajouter_lot(nom_lot, souche, effectif_initial, date_arrivee, age_initial_semaines):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO lots (nom_lot, souche, effectif_initial, date_arrivee, age_initial_semaines)
        VALUES (?, ?, ?, ?, ?)
    ''', (nom_lot, souche, effectif_initial, date_arrivee, age_initial_semaines))
    conn.commit()
    conn.close()

def enregistrer_suivi(lot_id, date, morts, oeufs_recoltes, oeufs_casses, aliment_consomme_kg, notes):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO suivi_journalier (lot_id, date, morts, oeufs_recoltes, oeufs_casses, aliment_consomme_kg, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (lot_id, date, morts, oeufs_recoltes, oeufs_casses, aliment_consomme_kg, notes))
    conn.commit()
    conn.close()

def recuperer_tous_les_lots_avec_stats():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Récupère les lots et calcule les totaux de mortalité et d'œufs via SQLite
    cursor.execute('''
        SELECT l.*, 
               COALESCE(SUM(s.morts), 0) as total_morts,
               COALESCE(SUM(s.oeufs_recoltes), 0) as total_oeufs,
               COALESCE(SUM(s.oeufs_casses), 0) as total_casses,
               COALESCE(SUM(s.aliment_consomme_kg), 0) as total_aliment
        FROM lots l
        LEFT JOIN suivi_journalier s ON l.id = s.lot_id
        GROUP BY l.id
    ''')
    rows = cursor.fetchall()
    conn.close()
    
    resultats = []
    for row in rows:
        effectif_actuel = row['effectif_initial'] - row['total_morts']
        total_plaques = round(row['total_oeufs'] / 30, 1) # 1 plateau = 30 œufs
        
        resultats.append({
            "id": row['id'],
            "nom_lot": row['nom_lot'],
            "souche": row['souche'],
            "effectif_initial": row['effectif_initial'],
            "effectif_actuel": effectif_actuel,
            "date_arrivee": row['date_arrivee'],
            "total_morts": row['total_morts'],
            "total_oeufs": row['total_oeufs'],
            "total_casses": row['total_casses'],
            "total_plaques": total_plaques,
            "total_aliment_kg": row['total_aliment']
        })
    return resultats