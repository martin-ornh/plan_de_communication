# Plan de communication projet — Client 360 Learning

> Documentation technique du plan de communication d'un projet mené en méthodologie **Scrum** pour le client **360 Learning**.

## Présentation

Ce dépôt centralise l'ensemble de la documentation liée à la communication du projet : qui communique quoi, à qui, quand, à quelle fréquence et sur quel support. Il sert de référence unique pour l'équipe Scrum, le management et le client.

**Période couverte :** 11/06 → 30/08

## Structure du dépôt

```
.
├── README.md
├── CHANGELOG.md
├── docs/
│   ├── plan-de-communication.md
│   ├── processus-scrum.md
│   ├── parties-prenantes.md
│   ├── guide-contribution.md
│   └── diagrammes/ (mermaid)
│       ├── diagramme-sequence.md
│       └── diagramme-flux.md
└── scripts/
    └── generate_changelog.py
```

## Démarrage rapide

1. **Lire le plan d'action** : [docs/plan-de-communication.md](docs/plan-de-communication.md)
2. **Comprendre les flux** : [docs/diagrammes/diagramme-sequence.md](docs/diagrammes/diagramme-sequence.md)
3. **Identifier les acteurs** : [docs/parties-prenantes.md](docs/parties-prenantes.md)

Les diagrammes sont rédigés en [Mermaid](https://mermaid.js.org/)

## Synthèse du plan de communication

| Communication | Date | Récepteur | Émetteur | Fréquence |
| --- | --- | --- | --- | --- |
| Vision produit | 11/06 | @all | Product Owner | 1 fois |
| Lancement Sprint 0 | 22/06 | Équipe Scrum | Scrum Master | 1 fois |
| Daily Scrum | 25/06 → 05/07 | Équipe Scrum | Dev Team | Quotidien |
| Revue de Sprint | 10/07 | Équipe + Stakeholders | Product Owner | Bi-hebdomadaire |
| Rétrospective de Sprint | 15/07 | Équipe Scrum | Scrum Master | Bi-hebdomadaire |
| Communication client | 20/07 | Client (360 Learning) | Product Owner | Mensuel |
| Cadrage technique | 25/07 | Équipe Dev | Lead Tech | 1 fois |
| Suivi budget/risques | 31/07 → 15/08 | Management | Product Owner | Mensuel |
| Communication finale | 30/08 | Équipe + Stakeholders | Product Owner | 1 fois |

Le tableau complet est disponible dans [docs/plan-de-communication.md](docs/plan-de-communication.md).

## Changelog automatique

Le fichier [CHANGELOG.md](CHANGELOG.md) n'est jamais modifié à la main : il est généré à partir des messages de commit (format Conventional Commits : `feat:`, `fix:`, `docs:`, `chore:`). Le script nécessite Python 3.9 ou plus, sans dépendance externe.

```bash
# depuis la racine du dépôt
python scripts/generate_changelog.py
# sous Windows, remplacer python par py si la commande n'est pas reconnue
```

Le fonctionnement est détaillé dans [docs/guide-contribution.md](docs/guide-contribution.md).

## Acteurs du projet

| Rôle | Responsabilité principale |
| --- | --- |
| **Product Owner** | Vision produit, lien client, reporting management |
| **Scrum Master** | Animation des rituels, amélioration continue |
| **Lead Tech** | Cadrage et spécifications techniques |
| **Dev Team** | Réalisation, daily scrum |
| **Client 360 Learning** | Validation des livrables |

## Licence

Documentation personnelle
