import random

MYTHES = [
    {
        "titre": "Le Minotaure et le Labyrinthe",
        "culture": "Grecque antique",
        "resume": "Minos enferme le Minotaure dans le Labyrinthe. Thésée, aidé par Ariane, le vainc grâce au fil."
    },
    {
        "titre": "Osiris, Isis et Seth",
        "culture": "Égyptienne antique",
        "resume": "Seth tue Osiris. Isis reconstitue son corps. Horus affronte Seth pour rétablir l’ordre."
    },
    {
        "titre": "Ragnarök",
        "culture": "Nordique",
        "resume": "Bataille finale et fin d’un cycle : destruction, puis renaissance d’un nouveau monde."
    },
]

ENTITES = {
    "zeus": {
        "nom": "Zeus",
        "type": "Entité mythologique",
        "culture": "Grecque antique",
        "description": "Figure centrale des récits mythologiques grecs, souvent associée au ciel et à la foudre.",
        "symbole": "Éclair, aigle",
        "image": "https://img.freepik.com/photos-premium/illustration-du-puissant-dieu-zeus-tonnerre-dans-main-ai_564714-2353.jpg"
    },
    "minotaure": {
        "nom": "Minotaure",
        "type": "Créature mythologique",
        "culture": "Grecque antique",
        "description": "Créature mi-homme mi-taureau liée au mythe du Labyrinthe de Crète.",
        "symbole": "Labyrinthe",
        "image": "https://img.freepik.com/photos-gratuite/portrait-du-minotaure-mythologique_23-2151817214.jpg"
    },
    "ra": {
        "nom": "Rê (Ra)",
        "type": "Entité mythologique",
        "culture": "Égyptienne antique",
        "description": "Figure solaire majeure dans les récits mythologiques de l'Égypte ancienne.",
        "symbole": "Disque solaire",
        "image": "https://1qult.wordpress.com/wp-content/uploads/2016/10/ra1.png"
    },
    "odin": {
        "nom": "Odin",
        "type": "Entité mythologique",
        "culture": "Nordique",
        "description": "Figure associée à la sagesse et aux récits guerriers dans les traditions nordiques.",
        "symbole": "Corbeaux, lance"
        "image" 
    },
}

ARTEFACTS = [
    {
        "nom": "Pierre de Rosette",
        "periode": "Égypte ptolémaïque",
        "lieu": "Découverte en 1799 près de Rosette (Égypte)",
        "info": "Aide au déchiffrement des hiéroglyphes grâce à un texte trilingue."
    },
    {
        "nom": "Masque funéraire de Toutânkhamon",
        "periode": "Nouvel Empire (XVIIIe dynastie)",
        "lieu": "Tombe KV62, Vallée des Rois",
        "info": "Objet emblématique de l’archéologie égyptienne."
    },
]

FACTS = [
    "Le mot 'archéologie' vient du grec 'arkhaios' (ancien) et 'logos' (étude).",
    "La datation au carbone 14 concerne surtout les matières organiques (os, bois, textiles).",
    "Certains sites antiques ont plusieurs couches d’occupation : une ville peut être reconstruite au même endroit."
]

QUIZ_QUESTIONS = [
    {
        "question": "À quoi sert principalement la Pierre de Rosette ?",
        "choix": ["Déchiffrer les hiéroglyphes", "Mesurer le temps", "Construire des pyramides", "Tracer des routes romaines"],
        "bonne_reponse": "Déchiffrer les hiéroglyphes"
    },
    {
        "question": "Dans quel récit apparaît le Minotaure ?",
        "choix": ["Le Labyrinthe de Crète", "Ragnarök", "Gilgamesh", "Osiris et Seth"],
        "bonne_reponse": "Le Labyrinthe de Crète"
    }
]

def random_myth():
    return random.choice(MYTHES)

def random_artifact():
    return random.choice(ARTEFACTS)

def random_fact():
    return random.choice(FACTS)

def random_quiz():
    return random.choice(QUIZ_QUESTIONS)
