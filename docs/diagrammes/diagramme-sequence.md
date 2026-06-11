# Diagramme de séquence des communications

Ce diagramme montre l'enchaînement des communications du projet, du lancement (11/06) à la clôture (30/08).

Si le diagramme s'affiche en texte brut dans votre éditeur, il faut un previewer compatible Mermaid : sur VS Code, installer l'extension "Markdown Preview Mermaid Support". Sinon coller le bloc de code dans https://mermaid.live. GitHub et GitLab l'affichent nativement.

## Séquence globale du projet

```mermaid
sequenceDiagram
    autonumber
    actor PO as Product Owner
    actor SM as Scrum Master
    actor LT as Lead Tech
    actor DEV as Dev Team
    actor STK as Stakeholders
    actor CLI as Client 360 Learning

    Note over PO,CLI: Phase de cadrage

    PO->>DEV: Vision produit (11/06, Mail + Confluence)
    PO->>STK: Vision produit
    PO->>CLI: Vision produit

    SM->>DEV: Lancement Sprint 0, presentation des user stories (22/06)

    Note over DEV,SM: Boucle de sprint (25/06 au 05/07)

    loop Chaque jour ouvre, 15 min
        DEV->>DEV: Daily Scrum, avancement quotidien
        DEV-->>SM: Remontee des blocages
    end

    Note over PO,STK: Fin de sprint (toutes les 2 semaines)

    PO->>STK: Revue de Sprint, demo des increments (10/07)
    STK-->>PO: Feedback
    SM->>DEV: Retrospective (15/07)
    DEV-->>SM: Actions d'amelioration (fiche retro + CR)

    Note over PO,CLI: Point client mensuel

    PO->>CLI: Presentation des livrables (20/07)
    CLI-->>PO: Validation (fiche suivi + CR + mail)

    LT->>DEV: Cadrage technique (25/07, Confluence)

    Note over PO,STK: Pilotage mensuel (31/07 au 15/08)

    PO->>STK: Suivi budget et risques (Mail + Tableau de bord)
    STK-->>PO: Arbitrages eventuels

    Note over PO,CLI: Cloture

    PO->>STK: Communication finale, bilan et suite (30/08)
    PO->>CLI: Bilan du projet (Meeting + CR)
```

## Zoom sur la validation client

```mermaid
sequenceDiagram
    autonumber
    actor DEV as Dev Team
    actor PO as Product Owner
    actor CLI as Client 360 Learning

    DEV->>PO: Increment termine (fin de sprint)
    PO->>PO: Verification par rapport a la Definition of Done
    PO->>CLI: Demonstration du livrable (Meeting)
    alt Livrable valide
        CLI-->>PO: Validation (fiche suivi signee)
        PO->>DEV: Go pour le sprint suivant
        PO->>CLI: Compte rendu + confirmation par mail
    else Reserves ou refus
        CLI-->>PO: Liste des ecarts constates
        PO->>DEV: Retours integres au backlog
        Note over DEV,PO: Correction au sprint suivant puis nouvelle presentation
    end
```

## Lecture

- Flèche pleine (`->>`) : l'émetteur initie la communication.
- Flèche pointillée (`-->>`) : réponse ou retour.
- Le bloc `loop` correspond à une communication récurrente, le bloc `alt` à un embranchement (validé / refusé).

Remarque : les accents ont été retirés à l'intérieur des diagrammes pour éviter les soucis de rendu selon les versions de Mermaid.
