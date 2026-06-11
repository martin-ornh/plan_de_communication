# Diagrammes de flux

Vue d'ensemble des échanges : qui parle à qui, et sur quel support. Même remarque que pour le diagramme de séquence : il faut un previewer compatible Mermaid (GitHub, GitLab, VS Code avec l'extension dédiée, ou https://mermaid.live).

## Flux global des communications

```mermaid
flowchart TB
    subgraph EQUIPE[Equipe Scrum]
        PO[Product Owner]
        SM[Scrum Master]
        LT[Lead Tech]
        DEV[Dev Team]
    end

    subgraph EXTERNE[Externe]
        CLI[Client 360 Learning]
        MGT[Management]
        STK[Stakeholders]
    end

    PO -- Vision produit --> DEV
    PO -- Vision produit --> STK
    SM -- Lancement Sprint 0 --> DEV
    DEV -- Daily Scrum 15 min --> DEV
    PO -- Revue de Sprint --> STK
    SM -- Retrospective --> DEV
    PO <-- Validation des livrables --> CLI
    LT -- Cadrage technique --> DEV
    PO -- Suivi budget et risques --> MGT
    PO -- Communication finale --> STK
```

## Cycle de sprint

```mermaid
flowchart LR
    A([Sprint 0 le 22/06]) --> B[Sprint Planning]
    B --> C[Sprint en cours]
    C --> D[Daily Scrum quotidien]
    D --> C
    C --> E[Revue de Sprint]
    E --> F[Retrospective]
    F --> G{Dernier sprint ?}
    G -- Non --> B
    G -- Oui --> H([Communication finale le 30/08])

    E -.-> STK[Stakeholders]
    E -.-> CLI[Client 360 Learning]
```

## Matrice émetteur / récepteur

```mermaid
flowchart LR
    subgraph Emetteurs
        E1[Product Owner]
        E2[Scrum Master]
        E3[Lead Tech]
        E4[Dev Team]
    end
    subgraph Recepteurs
        R1[Equipe Scrum]
        R2[Stakeholders]
        R3[Client]
        R4[Management]
    end

    E1 --> R1 & R2 & R3 & R4
    E2 --> R1
    E3 --> R1
    E4 --> R1
```

On voit que le Product Owner concentre toutes les communications externes (client, management, stakeholders). Le Scrum Master, le Lead Tech et la Dev Team ne communiquent qu'en interne, c'est voulu : un seul point de contact vers l'extérieur évite les messages contradictoires.
