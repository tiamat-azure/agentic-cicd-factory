from facturation import appliquer_remise, total_ht, total_ttc

LIGNES = [
    {"prix_unitaire": 100.0, "quantite": 2},
    {"prix_unitaire": 50.0, "quantite": 1},
]


def test_total_ht():
    assert total_ht(LIGNES) == 250.0


def test_appliquer_remise_dix_pourcent():
    # 10 % de remise sur 250 -> 225
    assert appliquer_remise(250.0, 10.0) == 225.0


def test_total_ttc_sans_remise():
    assert total_ttc(LIGNES) == 300.0
