class LotPondeuses:
    def __init__(self, nom_lot, effectif_initial, date_arrivee, age_initial_semaines=16):
        self.nom_lot = nom_lot
        self.effectif_initial = effectif_initial
        self.date_arrivee = date_arrivee
        self.age_initial_semaines = age_initial_semaines
        self.mortalite_totale = 0
        self.historique_production = []  # Liste de dictionnaires par jour

    def enregistrer_jour(self, date, morts=0, oeufs_recoltes=0, aliment_consomme_kg=0):
        """Enregistre les données journalières d'un lot"""
        self.mortalite_totale += morts
        effectif_actuel = self.effectif_initial - self.mortalite_totale
        
        # Taux de ponte (% Hen-Day) = (Oeufs récoltés / Effectif actuel) * 100
        taux_ponte = (oeufs_recoltes / effectif_actuel * 100) if effectif_actuel > 0 else 0
        
        # Consommation par sujet en grammes
        conso_par_sujet = (aliment_consomme_kg * 1000 / effectif_actuel) if effectif_actuel > 0 else 0

        jour_data = {
            "date": date,
            "effectif_actuel": effectif_actuel,
            "morts": morts,
            "oeufs_recoltes": oeufs_recoltes,
            "taux_ponte": round(taux_ponte, 2),
            "conso_sujet_g": round(conso_par_sujet, 1)
        }
        self.historique_production.append(jour_data)
        return jour_data

    def obtenir_statistiques(self):
        effectif_actuel = self.effectif_initial - self.mortalite_totale
        total_oeufs = sum(j["oeufs_recoltes"] for j in self.historique_production)
        total_plaques = total_oeufs / 30  # 1 plateau = 30 œufs
        
        return {
            "lot": self.nom_lot,
            "effectif_actuel": effectif_actuel,
            "mortalite_totale": self.mortalite_totale,
            "total_oeufs": total_oeufs,
            "total_plaques": round(total_plaques, 1)
        }

# --- Exemple d'utilisation ---
if __name__ == "__main__":
    lot1 = LotPondeuses(nom_lot="Lot B1 - ISA Brown", effectif_initial=500, date_arrivee="2026-01-10")
    
    # Simulation d'un jour de production
    lot1.enregistrer_jour(date="2026-06-01", morts=1, oeufs_recoltes=450, aliment_consomme_kg=55)
    
    print(lot1.obtenir_statistiques())