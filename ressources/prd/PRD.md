## 🔑 Le point clé d'abord

Les branches Git ne sont **pas** un bon outil de découpage pédagogique par chapitre. Une branche sert à isoler un travail temporaire destiné à être fusionné ou supprimé. Un chapitre, lui, est un contenu permanent qui doit coexister avec les autres. Utiliser des branches vous condamne à du cherry-pick permanent dès que vous corrigez une typo dans le README commun.

Il y a une exception, détaillée dans le scénario C.

---

## 1️⃣ Scénario A — Tout en dossiers numérotés sur `main`

```
formation-xxx/
├── README.md              # parcours, prérequis, sommaire
├── 00-setup/
├── 01-fondamentaux/
│   ├── README.md          # objectifs, durée, plan du chapitre
│   ├── slides/
│   ├── demos/
│   ├── exercices/
│   └── solutions/
├── 02-.../
└── ressources/            # cheatsheets, glossaire, liens
```

**+** Vision globale immédiate, un seul `git pull`, refactor transverse trivial, recherche full-repo qui marche, historique linéaire lisible.
**−** Les solutions sont visibles dès le départ (spoil), et l'apprenant voit les chapitres non encore écrits.

---

## 2️⃣ Scénario B — Une branche par chapitre

**+** L'apprenant ne voit que son chapitre ; état du code progressif « prêt à l'emploi ».
**−** Coût de maintenance qui explose : N branches à rebaser à chaque correction commune. Pas de vue d'ensemble. Les apprenants doivent maîtriser Git avant même de commencer. Vos PR n'ont plus de sens. En pratique, c'est le scénario qu'on abandonne au bout de trois semaines.

---

## 3️⃣ Scénario C — Dossiers + tags pour les jalons de code

Structure du scénario A, mais quand la formation construit **une application unique de bout en bout** (chap. 3 ajoute l'auth, chap. 4 la base de données…), on ajoute un dossier `app/` versionné par tags : `v-ch03-fin`, `v-ch04-fin`.

**+** L'apprenant décroché fait `git checkout v-ch03-fin` et repart à niveau. Un tag est immuable, contrairement à une branche.
**−** Ne s'applique que si votre formation a ce fil rouge applicatif.

---

## 4️⃣ Scénario D — Deux repos (formateur privé / apprenants public)

**+** Séparation nette : notes perso, corrigés, examens restent privés.
**−** Double synchronisation manuelle, source de désynchronisation. Rarement rentable pour un formateur seul.

---

## 👍 Ma recommandation

**Scénario A, plus C si fil rouge applicatif.** Un seul repo, un seul `main`, découpage par dossiers numérotés.

Sur les points de friction du scénario A :

**Les solutions.** Ne les cachez pas dans une branche. Deux options robustes : soit un dossier `solutions/` par chapitre assumé (les adultes en formation trichent rarement contre leur propre intérêt), soit une release GitHub `solutions.zip` publiée après chaque session. La seconde protège aussi les futures sessions.

**Les chapitres en construction.** Préfixez-les `_wip-05-...`, ou tenez simplement le sommaire du README à jour comme unique source de vérité : ce qui n'est pas listé n'est pas prêt.

**Les branches, gardez-les pour ce qu'elles font bien :** `feat/chapitre-06` pendant que vous rédigez, mergée dans `main` quand c'est publiable. Vous gardez le bénéfice de l'isolation sans le coût de la divergence permanente.

Quelques détails qui font la différence sur la maintenabilité :

- **Numérotez sur 2 chiffres** (`01-`, `02-`) — le tri lexicographique casse à partir de 10 sinon.
- **Un `README.md` par chapitre** avec objectifs pédagogiques, durée estimée, prérequis. C'est ce qui rend le repo navigable sans vous.
- **`ressources/` à la racine, jamais dupliqué** dans les chapitres : la duplication est l'ennemie de la maintenabilité.
- **CI GitHub Actions** qui exécute les solutions et vérifie les liens morts. Le code d'exemple qui ne compile plus est la première cause de perte de crédibilité en formation.
- **GitHub Pages** sur `main` si vous voulez publier les supports en HTML lisible (Docsify ou MkDocs pointant sur vos dossiers existants, sans réorganisation).
- **Discussions** plutôt qu'Issues pour les questions des apprenants — les Issues restent votre backlog de conception.

Si vous me dites le sujet et le format (durée, présentiel ou async, un fil rouge applicatif ou des chapitres indépendants), je peux vous proposer l'arborescence concrète et un `README` de départ.
