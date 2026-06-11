"""Génère CHANGELOG.md à partir des commits git (format Conventional Commits).

A lancer depuis la racine du dépôt :
    py scripts/generate_changelog.py
    py scripts/generate_changelog.py 1.2.0
"""

import re
import subprocess
import sys
from datetime import date
from pathlib import Path

SECTIONS = {
    "feat": "Nouveautés",
    "fix": "Corrections",
    "docs": "Documentation",
    "chore": "Maintenance",
}

# Découpe un message de commit comme "feat(plan): ajout du calendrier" en
# trois morceaux : le type (feat), la portée optionnelle (plan) et la
# description (ajout du calendrier). Un commit qui ne suit pas ce format
# ne matche pas et sera simplement ignoré.
COMMIT_RE = re.compile(r"^(feat|fix|docs|chore)(?:\((.+?)\))?: (.+)$")

ENTETE = """# Changelog

Toutes les évolutions notables de cette documentation sont listées ici.
Ce fichier est **généré automatiquement** par `scripts/generate_changelog.py`
à partir des commits au format [Conventional Commits](https://www.conventionalcommits.org/fr/).

"""


def git(*args):
    res = subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8")
    return res.stdout.strip()


version = sys.argv[1] if len(sys.argv) > 1 else "Unreleased"

# commits depuis le dernier tag (ou tout l'historique s'il n'y a pas de tag)
dernier_tag = git("describe", "--tags", "--abbrev=0")
plage = f"{dernier_tag}..HEAD" if dernier_tag else "HEAD"
log = git("log", plage, "--no-merges", "--pretty=%s|%h")

# classement des commits par section
groupes = {titre: [] for titre in SECTIONS.values()}
for ligne in log.splitlines():
    sujet, _, sha = ligne.rpartition("|")
    m = COMMIT_RE.match(sujet)
    if m:
        type_commit, portee, description = m.groups()
        prefixe = f"**{portee}** : " if portee else ""
        groupes[SECTIONS[type_commit]].append(f"- {prefixe}{description} (`{sha}`)")

if not any(groupes.values()):
    print("Aucun commit conventionnel depuis le dernier tag : changelog inchangé.")
    sys.exit(0)

# construction de la nouvelle section
titre = f"## [{version}]" if version == "Unreleased" else f"## [{version}] - {date.today()}"
bloc = [titre, ""]
for nom, entrees in groupes.items():
    if entrees:
        bloc += [f"### {nom}", "", *entrees, ""]

# on conserve les versions déjà présentes dans le fichier,
# sauf une éventuelle section Unreleased qu'on remplace
anciennes = ""
changelog = Path("CHANGELOG.md")
if changelog.exists():
    texte = changelog.read_text(encoding="utf-8")
    pos = texte.find("## [")
    if pos != -1:
        anciennes = texte[pos:]
        if anciennes.startswith("## [Unreleased]"):
            suivant = anciennes.find("## [", 1)
            anciennes = anciennes[suivant:] if suivant != -1 else ""

changelog.write_text(ENTETE + "\n".join(bloc) + "\n" + anciennes, encoding="utf-8")
print(f"CHANGELOG.md mis à jour : {titre} ({sum(map(len, groupes.values()))} entrées).")
