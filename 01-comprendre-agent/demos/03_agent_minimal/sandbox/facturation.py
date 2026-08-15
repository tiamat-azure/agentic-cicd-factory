"""Mini-module métier du bac à sable. Il contient un bug volontaire."""

TAUX_TVA = 0.20


def total_ht(lignes: list[dict]) -> float:
    return sum(ligne["prix_unitaire"] * ligne["quantite"] for ligne in lignes)


def appliquer_remise(montant: float, pourcentage: float) -> float:
    # BUG VOLONTAIRE : on soustrait le pourcentage au lieu d'appliquer un ratio.
    return montant - pourcentage


def total_ttc(lignes: list[dict], remise_pct: float = 0.0) -> float:
    ht = appliquer_remise(total_ht(lignes), remise_pct)
    return round(ht * (1 + TAUX_TVA), 2)
