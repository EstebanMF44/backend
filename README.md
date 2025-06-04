<<<<<<< HEAD
# slides réseau / backend

les slides du cours réseau / backend à l'École des Mines de Paris

## Slides

elles sont faites avec `remark.js` qui part de sources en `markdown`
voir <https://github.com/gnab/remark/wiki> à propos de ce qu'on peut mettre dans le markdown

## Template HTML

chaque slideshow vient avec, par exemple `slides1.html` et `slides1.md`  
le html charge remark.js, et le markdown, qui est transformé en html par remark.js  

du coup tous les html sont semblables, on les a factorisés dans `template.html`:

```bash
# pour mettre à jour les html
python template_run.py
```

si sur macos, on peut obtenir une sorte de mode *watch* en faisant

```bash
echo template.html | entr -rp python template_run.py
```

## Développement

```bash
# start vite dev server
npm run dev

# then in another terminal
open http://localhost:nnnn/index.html
```

## warnings

### slides3

WIP - not reviewed yet
=======
# Documentation de l'API


## Informations Générales

* Toutes les réponses sont au format JSON.
* Les codes de réponse HTTP standards sont utilisés pour indiquer le succès ou l'échec d'une requête.
* Pour les endpoints nécessitant un id, assurez-vous que l'ID est valide et existe dans la base de données, et dans ce cas retourner une erreur *404 Not Found*.

## Vérifier si le serveur est actif

* Endpoint : `/api/alive`
* Méthode : GET
* Description : Vérifie si le serveur est en fonctionnement.
* Réponse :
  + 200 OK : { "message": "Alive" }

## Liste de toutes les associations

* Endpoint : `/api/associations`
* Méthode : GET
* Description : Retourne une liste de toutes les associations.
* Réponse :
  + 200 OK : Liste des ids des associations.

## Détails d'une association

* Endpoint : `/api/association/<int:id>`
* Méthode : GET
* Description : Retourne les détails d'une association spécifique par son ID.
* Réponse :
  + 200 OK : Détails de l'association demandée.
  + 404 Not Found : { "error": "Association not found" }

## Liste de tous les événements

* Endpoint : `/api/evenements`
* Méthode : GET
* Description : Retourne une liste de tous les événements.
* Réponse :
  + 200 OK : Liste des ids des événements.

## Détails d'un événement

* Endpoint : `/api/evenement/<int:id>`
* Méthode : GET
* Description : Retourne les détails d'un événement spécifique par son ID.
* Réponse :
  + 200 OK : Détails de l'événement demandé.
  + 404 Not Found : { "error": "Event not found" }

## Liste des événements d'une association

* Endpoint : `/api/association/<int:id>/evenements`
* Méthode : GET
* Description : Retourne une liste des événements organisés par une association spécifique.
* Réponse :
  + 200 OK : Liste des événements de l'association demandée.

## Liste des associations par type

* Endpoint : `/api/associations/type/<type>`
* Méthode : GET
* Description : Retourne une liste des associations par type (BDE, BDS, BDA, etc.).
* Réponse :
  + 200 OK : Liste des associations filtrées par type.
* Note: cet endpoint n'est pas testé par le frontend pour le moment.
>>>>>>> 901fcd57f6eadd7e2599365486bd717e4b0ca014
