# 09 - Agent Security & Governance

## Objectifs pédagogiques

- Distinguer identité agent vs identité utilisateur/admin.
- Définir des permissions granulaires (read repo, write branch, create/merge PR, deploy).
- Mettre en place un sandbox interdisant l'accès aux secrets et à la production.
- Définir les points de passage obligatoire humain (human-in-the-loop).

## Prérequis

- Chapitre 08 (Evaluation Framework v0.8).

## Plan

1. Modèle d'identité : Agent != User, Agent != Admin.
1. Matrice de permissions par action.
1. Sandboxing : ce que le Coding Agent ne doit jamais pouvoir lire/écrire.
1. Politique human-in-the-loop : quelles actions restent automatiques, lesquelles
   nécessitent une validation humaine.

## Livrable

**Policy Engine v0.9** - un fichier de policies déclaratif (`auto` / `human`) appliqué à
chaque action de l'agent, de la création de branche au déploiement en production.
