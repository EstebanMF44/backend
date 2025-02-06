class: middle, slide_title

<img class="slide_title_mpt" src="static/media/logos/logo_mines_paris.png">
<img class="slide_title_cnrs" src="static/media/logos/logo_cnrs.jpg">

<!-- <img class="slide_title_armines" src="static/media/logos/logo_armines.jpg"> -->
<img class="left_panel" src="static/media/logos/mines_paris_lampe.png">

# Programmes coopérants 🚀

## Côté Serveur !

<p> <strong><i>Basile Marchand</i></strong><sup> 1</sup></p>

.footnote[1 - Plateforme SISDev, Centre des Matériaux, MINES Paris - CNRS - Université PSL]

---

layout: true
<img class="slide_header_mpt" src="static/media/logos/logo_mines_paris.png">
<img class="slide_header_cnrs" src="static/media/logos/logo_cnrs.jpg">

<!-- <img class="slide_header_armines" src="static/media/logos/logo_armines.jpg"> -->

<div class="slide_footer">
    <div class="wrap">
        <span>2025 - <i> Réseaux & Backend</i> - 2/3: Coté Serveur! </span>
    </div>
</div>

---

# Récap de la semaine dernière

.center[Architecture classique Client <-> Serveur avec des variations peer-to-peer, three-tier, ... ]

.cols[
.fifty[
.center[<img src="static/media/osi-model.svg" width="60%">]
]
.fifty[
Un modèle OSI en 7 couches

.center[<img src="static/media/ip-address.svg" width="20%">]

Un protocole HTTP(S) pour le web

.center[
<img src="static/media/http-request.svg" width="60%">
]

]
]

---

# Quel est le rôle du serveur ?

.center[
<img src="static/media/client-server.svg" width="60%">
]

--

.center[🥱 Attendre et attendre et attendre ... 🥱]

--

Et de temps en temps 🥳 il doit traiter une requête !

---

class: center, middle

# Serveur et serveur deux choses différentes

**_Attention_** il y a deux significations à serveur ...

.center[

<iframe src="https://giphy.com/embed/xU9TT471DTGJq" width="480" height="365" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
]

---

# Serveur et serveur deux choses différentes

## Le serveur hardware

.center[
<img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1634&q=80" width="50%">
]

.center[C'est la machine **physique ou virtuelle** connectée au réseau qui va recevoir des paquets de données mais en aucun cas ne s'occupera du traitement de ces données]

---

# Serveur et serveur deux choses différentes

## Le serveur hardware : différents types

.center[Serveur physique vs serveur virtuel (VPS) ]

<div style="position: absolute; bottom: 15%; left: 15%">
<img src="static/media/bare-metal.svg" width="80%">
</div>

--

<div style="position: absolute; bottom: 15%; right: 10%">
<img src="static/media/vps.svg" width="80%">
</div>

--

<div style="position: absolute; bottom: 10%; left: 20%">
Différentes solutions : On Premise vs Cloud (OVH, Azure, GCP, AWS, ... )
</div>

---

# Serveur et serveur deux choses différentes

## Le serveur "software"

.center[
<img src="static/media/server-app.svg" width="65%">
]

C'est l'application (au sens logiciel) qui va s'occuper de

.center[**Recevoir**, **Traiter** et **Répondre** aux requètes HTTP (ou autres d'ailleurs)]

Différentes solutions : Apache (40%), Nginx (20%), IIS (10%), ...

.footnote[Source : [https://fr.hostadvice.com/marketshare/server/](https://fr.hostadvice.com/marketshare/server/) ]

---

# Héberger plusieurs serveurs HTTP(S) sur un même serveur physique ?

.center[OUI 🎯 il suffit de se partager le port 80 🤝]

.center[<img src="static/media/virtual-host.svg" width="80%">]

--

.center[Il suffit de configurer au niveau du serveur HTTP des **Virtual Host**]

--

<div style="position: absolute; top: 38%; left:15%">
<img src="static/media/servername-mines.png" width="40%">
</div>

<div style="position: absolute; top: 38%; left:55%">
<img src="static/media/servername-cpp.png" width="70%">
</div>

.center[
le "routage" entre les deux sites se fait au niveau du Header `Host:` de la requête HTTP
]
---

# Un mot sur le serverless

.center[Un serveur traditionnel passe son temps à attendre ...

🥱

]

.center[**_Un serve rless est un serveur qui n'attend pas_**]

Le principe est de découper le traitement en petites **tâches indépendantes** (fonctions) qui seront exécutées **à la demande**

.cols[
.fifty[

## Avantages

- Pas de gestion de serveur
- Pas de coût fixe
- Évolutif

]
.fifty[

## Inconvénients/Difficultés

- Temps de démarrage
- Coût à l'usage
- Difficulté de débogage
- Stateless

]
]

Coût plus faible pour les fournisseurs car ils peuvent optimiser l'utilisation des ressources

---

# Tous les serveurs font la même chose ?

**Deux applications**

.center[Sites statiques vs dynamiques]

.cols[
.fifty[

<iframe src="https://cpp.bmarchand.fr/controlSection.html" width="100%" height="400px" frameBorder="0"></iframe>

    ]

.fifty[

<iframe width="100%" height="400px" src="https://xkcd.com"></iframe>

    ]

]

---

# Site statique

.center[Le serveur http ne fait qu'une seule et unique chose
<br><br>
**_lire des fichiers_** html, png, jpg, pdf, .... et **_envoyer le contenu au client_**
]

<br><br>

.center[
<a href="http://cpp.bmarchand.fr" target="_blank"> <img src="static/media/site-static.svg" width="90%"></a>
]

---

# Site dynamique

.center[Le serveur http va devoir travailler **avec d'autres services** <br>afin de produire le résultat final pouvant être envoyé au client]

.center[
<a href="http://bmarchand.fr/research/activities" target="_blank">
<img src="static/media/dynamic-site1.svg" width="50%">
</a>
]

--

.center[
<a href="https://rep.mines-paristech.fr" target="_blank">
<img src="static/media/cerebro.png" width="50%">
</a>
]

---

# Solutions d'hébergement gratuit

.cols[
.fifty[

## Sites statiques

- GitHub Pages (nous y sommes !)
- readthedocs.io (les cours de S1)
- GitLab Pages
- Netlify
- Vercel
- ...

]
.fifty[

## Sites dynamiques

- ~~Heroku~~
- Glitch
- Repl.it
- PythonAnywhere
- Vercel (serverless)
- ...

]

]

.center[Plein d'offres sur le marché, à vous de choisir celle qui vous convient le mieux]

Attention en revanche :

.center[**_Gratuit_** ne veut pas dire **_sans limite_**]

---

# Le serveur web : un besoin de perf 🚀

.cols.bottom[

.sixty[
  <img src="static/media/performance.svg" width="700px">
]

.fourty[
  Comment faire pour que tout le monde

  ait une réponse en un temps raisonnable ?

  ⏳️
]

]

---

# Solutions techniques

.center[<img src="static/media/concurrency.svg" width="70%">]

.center[Utilisation du parallélisme de tâches processus/thread et/ou programmation asynchrone]

---

# Et au fait il répond quoi le serveur à GET ?

.cols[
.fifty[
.center[<img src="static/media/http-request.svg" width="100%">]
]
.fifty[
.center[<img src="static/media/response-format.svg" width="100%">]
]
]

<br><br>
Possible de voir les requêtes et réponses dans votre navigateur via
`Outils de développement > Network`

--

<div style="position: absolute; top: 38%; left:15%">
<img src="static/media/chrome-request-headers.png" width="40%">
</div>

<div style="position: absolute; top: 38%; left:55%">
<img src="static/media/chrome-response-headers.png" width="70%">
</div>

---

# Faisons un serveur http de base

```sh
# dans votre terminal:
# on va dans le repo du cours
cd /bla-bla-bla/backend

# pour lancer le serveur
python -m http.server
# ... à ce stade le terminal est bloqué
# pour tuer le serveur tapez "Control-C"
```

puis ouvrez dans votre navigateur `http://localhost:8000/index.html` (*)

--

.cols[

.cols.center.fourty[
  On peut aussi le faire "à la main" en Python 🐍

  📢 ⚠️ On regarde le fichier `minimal_server.py`

  ```bash
  $ cd python/
  $ python minimal_server.py
  ```
]

.sixty[

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler

handler = SimpleHTTPRequestHandler

print("Open this in your browser:\nhttp://localhost:9000/index.html")

httpd = HTTPServer(('', 9000),  handler)
httpd.serve_forever()
```
]

]

.footnote.small[
  (*) vous pouvez aussi le faire avec votre adresse IP - [on en a parlé ici](slides1.html#my-ip-address)
 ]

<!-- [http://bit.ly/3EeuLLo](http://bit.ly/3EeuLLo)

<img src="static/media/qrcode/http_server.png" width="20%"> -->

---

# Traitement des requêtes

Le fonctionnement interne d'un serveur HTTP est assez simple

1. **Écouter** sur un port (80 par défaut)
2. **Accepter** une connexion
3. **Lire** la requête
4. **Traiter** la requête
5. **Envoyer** la réponse
6. **Fermer** la connexion

Le point important est la transition entre les étapes 3 et 4 qui est le coeur du serveur HTTP
car définit la manière dont le serveur va traiter la requête.

---

# Exemple fait à la main

.center[
[http://bit.ly/3EeuLLo](http://bit.ly/3EeuLLo)
]

.center[
<img src="static/media/qrcode/http_server.png" width="20%">
]

📢 ⚠️ On regarde les fichiers `more_advance_server.py` et `more_more_advance_server.py`

---

# of course il existe des frameworks pour ça&nbsp;!

---

# Les frameworks

Réponse à un besoin mais lequel ?

.center[***Cadre de développement simplifié***]

En gros un guide <strike> spirituel </strike>, permettant de développer simplement des applications spécifiques.

.center[

<iframe src="https://giphy.com/embed/MZW5o8f5RaH0Q" width="480" height="197" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

]

---

# Framework vs Librairie

.center[Frameworks, Librairies, même chose ? <br> ]

--

.cols[
.fifty[
.center[<b> Librairies </b>]

Ensemble de programmes effectuant des opérations spécifiques, que vous allez utiliser de manière ponctuelle au sein de vos programmes en suivant votre propre logique.

<br>

Par exemple `NumPy` en Python 🐍 est une librairie

.center[
<img src="static/media/library.png" width="70%">
]

]
.vertbar[]
.fifty[
.center[<b> Framework </b>]

Cadre de développement dans lequel le développeur vient s'inscrire, i.e. développer des fonctionnalités/comportements. Là ce n'est plus le développeur qui fixe sa logique mais le framework.

<br>

Un code à trou 🕳️ en quelque sorte

.center[
<img src="static/media/framework_concept.png" width="70%">
]

]
]

---

# Frontend, backend

.center[⚠️ Framework web un terme très, trop, générique ⚠️]

.cols[
.fifty[

.center[Framework frontend]

.center[

  <img src="static/media/framework_frontend.png" width=50%>
]

Focalisé sur le développement d'application côté client.

]
.vertbar[]
.fifty[

.center[Framework backend]

.center[

  <img src="static/media/framework_backend.png" width=100%>
]

Focalisé sur le développement côté serveur

]
]

---

# Les grands principes des framework backend

.center[
<img src="static/media/framework_routes.png" width=100%>
]

A cela un framework complet ajoute des fonctionnalités de :
.center[`Web Template`, `Sécurité`, `Accès à des bases de données`]

---

# Framework Flask

Micro-framework Python 🐍 développé depuis 2010.
<br><br>
.center[
<img src="static/media/logos/logo_flask.png" width=40% />
]
<br><br>
🚧 Micro-framework ne veut pas dire pas utilisable sur des gros projets ⚠️
<br><br>
.center[
Pinterest, Airbnb, Trivago, ...
]
<br><br>
Micro-framework car noyau très léger et minimaliste mais pouvant être enrichi avec des extensions.

---

# Le setup de base

## Installation

```bash
pip install flask
```

--

## Minimal working example

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

.center[
Une fois lancé -> [http://localhost:5000](http://localhost:5000)
]

.center[? C'est quoi .clignote[`@app.route('/')`] ?]

---

# Les routes

`@app.route` est un décorateur qui permet d'associer une fonction à une URL et un type de requête HTTP.

Dans sa version complète on peut écrire :

```python
@app.route('/hello', methods=['GET', 'POST'])
def hello():
  if request.method == 'POST':
    ## traitement
  elif request.method == 'GET':
    ## traitement
  else:
    return "Méthode non autorisée", 405
```

---

class: center, middle

# On a fini ...

<br><br>

--

# ... ou pas en fait

.center[<iframe src="https://giphy.com/embed/3ohs7XbAurbpO5jIBy" width="480" height="267" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>]

---

# Petite pause mise en pratique

**Objectif** : Mettre en place une API permettant d'accéder au contenu de fichier CSV

Vous avez [https://github.com/ue22-p24/network-frontend-apitester](https://github.com/ue22-p24/network-frontend-apitester) un frontend tout fait !

Et vous avez [https://github.com/ue22-p24/network-backend-api-skeleton](https://github.com/ue22-p24/network-backend-api-skeleton) un backend à compléter

L'api du backend doit **impérativement** respecter les routes documentées dans le README.

---

# Un petit point sécurité 🔒

Quelle différence entre

.center[HTTP et HTTP**S**]

.center[❓]

--

.center[Oui oui c'est le **S** de **S**ecure 😓]

Grosso modo :

.center[
Enrobage du protocôle HTTP dans une couche de chiffrement <br><br><br>
pour garantir la sécurité de l'utilisateur
]

.center[<img src="static/media/https.jpg" width="40%">]

---

# HTTP un truc pas safe ?

.cols[
.fifty[
***Alors oui le HTTP de base n'est pas sécurisé***
]
.fifty[
.center[

<iframe src="https://giphy.com/embed/1FMaabePDEfgk" width="200" height="200" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
]
]
]

--

.cols[
.fifty[
.center[

<iframe src="https://giphy.com/embed/dZA4cLPCvSs1s5aCm7" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
]
  ]
  .fifty[
    ***Mais ce n'est pas très grave dans pleins de cas***
]
]

---

# Le risque du HTTP

<br>

.cols[
.fifty[
<img src="static/media/http_not_safe.png" width="100%">
]
.fifty[

<img src="static/media/https_safe.png" width="100%">

]
]

.center[Le principe est donc de renfermer la requête HTTP et les informations qu'elle contient <br><br> dans un message crypté]

---

# Principes de chiffrement

En pratique le chiffrement fonctionne avec un système clé publique/clé privée

.center[
<img src="static/media/tls.png" width="60%">
]

---

# Autorité de certification

.center[Tiers de confiance <br><br> qui va générer les certificats permettant le chiffrement et l'authentification de l'identité des correspondants]

Possible de générer ses propres certificat soi-même mais ils ne sont pas considérés comme valide par les clients standards.

.center[<img src="static/media/logos/openssl.png" width="20%">]

Pour générer des certificats gratuitement il existe l'initiative **Let's Encrypt**

.center[<img src="static/media/logos/letsencrypt.png" width="30%">]

---

class: center, middle

# Et maintenant c'est fini ?

.center[<iframe src="https://giphy.com/embed/I1nwVpCaB4k36" width="400" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>]

---

# Les cookies 🍪

Faisons une pause goûter 🤤

.center[

<iframe src="https://giphy.com/embed/3o6MbitgftpbGFP3B6" width="480" height="362" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
]

.center[
Ca fait parti de ces petites choses ***cachées*** dans le header des réponses http.
]

---

# Concrètement c'est quoi ?

Un 🍪 HTTP c'est
.center[données qu’un serveur envoie à un client]

.cols[
.fifty[
<img src="static/media/cookie1.png" width="100%">
]
.fifty[
<img src="static/media/cookie2.png" width="100%">
]
]

.center[stockée sur le client (dans le navigateur) <br> **renvoyée** au serveur à chaque nouvelle requête]

.center[ <img src="static/media/cookie3.png" width="40%">]

---

# Quel intérêt ?

Les cookies sont là pour enrichir le HTTP.

.center[HTTP = protocole sans état]

En gros impossible pour un serveur HTTP de savoir si deux requètes viennent d'une même client ou pas 😵‍💫

.center[comment rester authentifier alors ?]

**_La solution_**

.center[Les cookies 🍪 parce que ça laisse des miettes]

Concrètement on va pouvoir stocker :

.center[Un session ID, des préférences utilisateur (light/dark theme, langue, ...)]

---

# Mettre des cookies

Rien de plus simple, dans l'en-tête de la réponse serveur à une requête client il suffit d'ajouter
<br><br>
.center[
`Set-Cookie: <name>=<value>; <attributs...>`
]
<br><br>
Attributs de Cookie

- `Expires` : durée de vie (date/heure)
- `Max-Age` : durée de vie (seconde)
- `Domain` : noms de domaine pour lesquels le cookie est renvoyé [par exemple](https://www.mat.minesparis.psl.eu)
- `Path` : chemin particulier pour lesquels le cookie est renvoyé
- `Secure` : si autorise ou pas l'envoie via HTTP et non HTTPS
- `HttpOnly` : si autorise ou pas l'accès via autre chose de du http(s)

---

# Quelques rêgles à suivre

.center[<img src="static/media/logos/cnil.jpg" width="30%">]
.center[https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies](https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies)

- Internautes doivent être informé et donner leur consentement avant le dépôt de certains cookies
  - ❌ Traçage publicitaire / réseaux sociaux
  - ✔️ Cookie pour dire qu'on refuse les cookies [exemple](https://cpp.bmarchand.fr), panier d'achat, authentification, ...
- Recueillir le consentement
  - Bouton refusé aussi visible que celui accepté
  - Possibilité de choisir les cookies
  - Facilité de retrait du consentement

---

# Rajoutons un Cookie dans notre serveur

.center[[http://bit.ly/410qbdD](http://bit.ly/410qbdD)]

.center[
<img src="static/media/qrcode/cookie.png" width="20%">
]

---

# HTTP + 🍪 suffisant pour tout faire ?

.center[
<br><br>

<iframe src="https://giphy.com/embed/XymaJlgorUL8vOfF88" width="480" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
]

---

# Mais pourquoi ?

.cols[
.thirty[
<img src="static/media/http.png" width="80%">
]
.sixty[

    <br><br>

Fonctionnement de HTTP très rigide
<br><br>
.center[question/réponse]
<br><br>
Impossible pour le serveur d'être à l'origine de l'échange
.center[Assez limitant en fait 😮‍💨]

.cols[
.fifty[
<img src="static/media/limitation1.png" width="100%">
]
.fifty[
<img src="static/media/limitation2.png" width="100%">

]

]

]
]

---

# Websocket

.center[En 2011 révolution arrivée de Websocket 🤯]

.cols[
.fifty[
<br><br>
.center[connexion **bidirectionnelle** entre un client et le serveur
<br><br>on parle de connexion *full-duplex*
<br><br>Permet au serveur de ***pousser*** des informations vers le client sans que ce dernier n'est rien demandé 😲
]
]
.fifty[
.center[<img src="static/media/ws.png" width="70%">]
]
]

---

# Comment ça marche

Très simplement en fait !

.center[Première étape on établie une connexion vers un serveur WebSocket <br> via <br>
`ws://mon-super-server.com` ou `wss://mon-super-server.com`
]

.center[Une fois la connexion établie <br><br>on doit simplement se mettre en état d'écoute à des évènements particuliers]

Quatre types d'évènements

.center[`onopen` 📖, `onclose` 📕, `onerror` 🚨, `onmessage` 📥]

Et à chaque évènement on va venir associer une action

---

# Par exemple :

.cols[
.fifty[

```javascript
var socket = new WebSocket("ws://localhost:3060/ws");

socket.onopen = function (e) {
  alert("[open] Connection established");
  alert("Sending to server");
  socket.send("My name is John");
};

socket.onmessage = function (event) {
  alert(`[message] Data received from server: ${event.data}`);
};

socket.onclose = function (event) {
  if (event.wasClean) {
    alert(
      `[close] Connection closed cleanly,
      code=${event.code} reason=${event.reason}`
    );
  } else {
    // e.g. server process killed or network down
    // event.code is usually 1006 in this case
    alert("[close] Connection died");
  }
};

socket.onerror = function (error) {
  alert(`[error] ${error.message}`);
};
```

]
.fifty[

```python
from tornado.websocket import websocket_connect

def on_message( msg ):
    print(f"[In on message] {msg}")

ws = await websocket_connect("ws://localhost:3060/ws",
  on_message_callback=on_message)

await ws.write_message("coucou")
await ws.write_message("byebye")
await ws.write_message("vive la MMC")

```

⚠️ Vous voyez apparaître le mot clé `await` que vous ne connaissez pas en Python 🐍

C'est lié à la programmation asynchrone. Pour plus de détails je vous encourage à faire un tour sur le Mooc

.center[*Python : des fondamentaux aux concepts avancés du langage*]

]
]

---

# En pratique

## Une messagerie instantannée !

.center[[http://bit.ly/3xu599H](http://bit.ly/3xu599H)]

.center[
<img src="static/media/qrcode/tornado.png" width="20%">
]

---

# In the next episode

.cols[
.fifty[
.center[<iframe src="https://giphy.com/embed/xTiTnBdvZgewvjTBAs" width="400" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>]
]
.fifty[
.center[<iframe src="https://giphy.com/embed/RbSmVaVGptW03Wjw3a" width="480" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>]
]
]

.center[Un tour d'horizon du **Framework `Flask`** <br>
qui va vous simplifier la vie pour tous les développements Web]
