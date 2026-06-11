# Parties prenantes

Qui sont les acteurs du projet, ce qu'ils émettent, ce qu'ils reçoivent et par quels canaux.

## Acteurs internes

| Acteur | Rôle dans la communication | Émet | Reçoit | Canaux |
| --- | --- | --- | --- | --- |
| Product Owner | Pivot central : porte la vision, interface client et management | Vision produit, revue de sprint, communication client, suivi budget/risques, communication finale | Feedback stakeholders, validation client | Mail, Confluence, Meeting, Tableau de bord |
| Scrum Master | Garant des rituels et de l'amélioration continue | Lancement Sprint 0, rétrospectives | Blocages remontés par la Dev Team | Meeting, CR, Fiche rétro |
| Lead Tech | Référent technique | Cadrage et spécifications techniques | Questions techniques de l'équipe | Meeting, Confluence |
| Dev Team | Réalisation et synchronisation quotidienne | Daily Scrum | User stories, spécifications, actions rétro | Meeting (15 min) |

## Acteurs externes

| Acteur | Rôle | Attentes | Fréquence de contact |
| --- | --- | --- | --- |
| Client (360 Learning) | Commanditaire, valide les livrables | Visibilité sur l'avancement, livrables conformes | Mensuelle, plus la vision initiale et le bilan final |
| Management | Sponsor interne, arbitre budget et risques | Rapport d'avancement fiable, alertes précoces | Mensuelle |
| Stakeholders | Parties intéressées, suivent la valeur produite | Démonstrations concrètes des incréments | Bi-hebdomadaire (revues de sprint) |

## Principes retenus

1. Un seul point de contact client : le Product Owner. Ça évite les messages contradictoires et ça protège l'équipe.
2. Transparence vers le management : un risque critique est remonté dès son identification, sans attendre le rapport mensuel.
3. L'équipe Scrum communique en continu en interne : le formel (CR, Confluence) complète l'informel, il ne le remplace pas.

## RACI des communications

| Communication | PO | SM | Lead Tech | Dev Team | Client | Mgmt |
| --- | :-: | :-: | :-: | :-: | :-: | :-: |
| Vision produit | R | C | C | I | I | I |
| Lancement Sprint 0 | A | R | C | I | - | - |
| Daily Scrum | I | A | I | R | - | - |
| Revue de Sprint | R | A | C | C | I | I |
| Rétrospective | C | R | C | C | - | - |
| Communication client | R | I | C | I | A | - |
| Cadrage technique | C | I | R | I | - | - |
| Suivi budget/risques | R | I | C | - | - | A |
| Communication finale | R | C | C | C | I | I |

R = Réalise, A = Approuve, C = Consulté, I = Informé
