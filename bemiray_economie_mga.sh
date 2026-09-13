cat << 'EOF' > bemiray_economie_mga.sh
#!/bin/bash

echo "=================================================="
echo " FICHE TECHNIQUE ET ECONOMIQUE - PONDEUSES (MGA)"
echo " Projet : BeMiray Farmer (Madagascar)"
echo " Effectif de référence : 500 Sujets"
echo "=================================================="

# Paramètres de base (500 sujets)
EFFECTIF=500
TAUX_PONTE_REF=75
DUREE_PONTE_MOIS=18

echo ""
echo "--- 1. INDICATEURS TECHNIQUES DE REFERENCE ---"
echo "Effectif initial : $EFFECTIF poussins"
echo "Taux de ponte de référence : $TAUX_PONTE_REF %"
echo "Production journalière estimée : ~330 à 337 œufs/jour (~11 alvéoles)"
echo ""

echo "--- 2. ELEMENTS ECONOMIQUES (en Ariary - MGA) ---"
INVESTISSEMENT_MGA=2805000
CHARGES_24M_MGA=6795000
PRODUIT_OEUFS_MGA=8019000
PRODUIT_REFORME_MGA=810000
PRODUIT_TOTAL_MGA=8829000
MARGE_BRUTE_MGA=2033511
RATIO_PRODUITS_CHARGES=1.3

echo "• Investissement initial : $INVESTISSEMENT_MGA MGA"
echo "• Charges opérationnelles (24 mois) : $CHARGES_24M_MGA MGA"
echo "  (dont ~78,6% dédiés à l'alimentation locale)"
echo "• Produit brut (Vente œufs sur 18 mois) : $PRODUIT_OEUFS_MGA MGA"
echo "• Produit brut (Vente poules réformées) : $PRODUIT_REFORME_MGA MGA"
echo "• Revenu total brut : $PRODUIT_TOTAL_MGA MGA"
echo "• Marge brute opérationnelle : $MARGE_BRUTE_MGA MGA"
echo "• Ratio Produits / Charges : $RATIO_PRODUITS_CHARGES"
echo "=================================================="
EOF