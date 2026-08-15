# 02 - Tools, Function Calling & environnement

## Objectifs pédagogiques

- Comprendre que la puissance d'un agent vient de son environnement d'action.
- Construire des tools : filesystem, git, shell, pytest, HTTP, GitHub.
- Maîtriser schémas, structured outputs, validation, gestion d'erreurs, permissions,
  idempotence, timeouts.

## Prérequis

- Chapitre 01 (Agent v0.1).

## Plan

1. Anatomie d'un tool : nom, description, schéma d'entrée/sortie.
1. Structured output et validation (ex. Pydantic / JSON Schema).
1. Gestion des erreurs, timeouts, idempotence des tools.
1. Permissions : ce que l'agent a le droit de faire.
1. Construction des tools `list_files`, `read_file`, `write_file`, `run_tests`,
   `git_diff`.

## Livrable

**Agent v0.2 - Coding Agent** - l'agent reçoit "Ajoute une fonction X au projet", modifie
un petit repository et exécute ses tests.
