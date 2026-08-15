# 🔀 11 - Automatic PR Factory

## 🎯 Objectifs pédagogiques

- Enchaîner Requirement Agent -> Architecture Agent -> Coding Agent -> Test Agent ->
  Review Agent -> Security Agent -> Evaluation -> PR.
- Faire produire par la PR un contenu exploitable directement par un humain (summary,
  changements d'architecture, fichiers modifiés, tests, analyse de sécurité, score
  d'évaluation, consommation de tokens, coût, risques).
- N'impliquer un humain que lorsque c'est nécessaire (cf. Policy Engine, chapitre 09).

## ✅ Prérequis

- Chapitre 10 (Agentic CI/CD Factory v1.0).

## 🗺️ Plan

1. Chaînage complet des agents métier sur une demande utilisateur réelle.
1. Génération automatique du contenu de la PR.
1. Intégration des scores d'évaluation et du coût dans la PR.
1. Points d'arrêt humains définis par le Policy Engine.

## 📦 Livrable

**PR Factory v1.1** - une demande utilisateur en langage naturel devient une PR GitHub
exploitable. C'est le premier démonstrateur complet du parcours.
