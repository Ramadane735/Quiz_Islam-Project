import random
import tkinter as tk
from tkinter import ttk, messagebox

# ---------------------------------------------
# 1. Données du quiz (questions.json)
# ---------------------------------------------
questions_data = [
    {
        "category": "Coran",
        "questions": [
            {
                "question": "Quelle est la première sourate du Coran ?",
                "options": ["Al-Fatiha", "Al-Baqara", "Al-Imran", "An-Nisa"],
                "answer": 0,
                "time_limit": 15
            },
            {
                "question": "Combien de versets compte la sourate Al-Kawthar ?",
                "options": ["1", "3", "5", "10"],
                "answer": 1,
                "time_limit": 10
            },
            {
                "question": "Quel est le thème principal de la sourate Al-Ikhlas ?",
                "options": ["La création", "L'unicité de Dieu", "La prière", "Le jeûne"],
                "answer": 1,
                "time_limit": 20
            },
            {
                "question": "Quelle sourate est connue comme la 'mère du Livre' ?",
                "options": ["Al-Fatiha", "Al-Baqara", "An-Nas", "Al-Ikhlas"],
                "answer": 0,
                "time_limit": 15
            },
            {
                "question": "Quel est le dernier verset révélé du Coran ?",
                "options": ["Al-Baqara 2:281", "An-Nas 114:6", "Al-Fatiha 1:7", "Al-Ikhlas 112:4"],
                "answer": 0,
                "time_limit": 25
            },
            {
                "question": "Quelle sourate est souvent récitée pour demander la protection contre le mal ?",
                "options": ["Al-Falaq", "An-Nas", "Al-Baqarah", "Al-Ikhlas"],
                "answer": 1,
                "time_limit": 20
            },
            {
                "question": "Combien de sourates le Coran contient-il ?",
                "options": ["114", "120", "99", "150"],
                "answer": 0,
                "time_limit": 10
            },
            {
                "question": "Quelle sourate est connue comme la 'sourate du Trône' ?",
                "options": ["Al-Baqara", "Al-Imran", "An-Nisa", "Al-Ma'idah"],
                "answer": 0,
                "time_limit": 20
            },
            {
                "question": "Quel est le sujet principal de la sourate Al-Baqara ?",
                "options": ["La prière", "Le jeûne", "La foi et la loi islamique", "L'histoire des prophètes"],
                "answer": 2,
                "time_limit": 30
            },
            {
                "question": "Quelle sourate est dédiée à la famille du Prophète Muhammad ?",
                "options": ["Al-Ahzab", "Al-Imran", "An-Nisa", "Al-Mumtahana"],
                "answer": 0,
                "time_limit": 25
            },
        ]
    },
    {
        "category": "Prophètes",
        "questions": [
            {
                "question": "Quel prophète a reçu la révélation du Coran ?",
                "options": ["Moïse", "Jésus", "Muhammad", "Abraham"],
                "answer": 2,
                "time_limit": 20
            },
            {
                "question": "Qui est considéré comme le dernier prophète de l'Islam ?",
                "options": ["Adam", "Noé", "Moses", "Muhammad"],
                "answer": 3,
                "time_limit": 15
            },
            {
                "question": "Quel prophète est connu pour avoir construit la Kaaba ?",
                "options": ["Abraham", "Noé", "David", "Salomon"],
                "answer": 0,
                "time_limit": 25
            },
            {
                "question": "Qui a été englouti par un grand poisson ?",
                "options": ["Jonas", "Moïse", "Jésus", "Muhammad"],
                "answer": 0,
                "time_limit": 20
            },
            {
                "question": "Quel prophète a parlé à Dieu sur le mont Sinaï ?",
                "options": ["Abraham", "Moïse", "Jésus", "Muhammad"],
                "answer": 1,
                "time_limit": 30
            },
            {
                "question": "Qui est le père de tous les prophètes ?",
                "options": ["Adam", "Abraham", "Noé", "David"],
                "answer": 0,
                "time_limit": 15
            },
            {
                "question": "Quel prophète a été sauvé du feu par Dieu ?",
                "options": ["Abraham", "Moïse", "Jésus", "Muhammad"],
                "answer": 0,
                "time_limit": 20
            },
            {
                "question": "Qui a reçu les dix commandements ?",
                "options": ["Abraham", "Moïse", "Jésus", "Muhammad"],
                "answer": 1,
                "time_limit": 25
            },
            {
                "question": "Quel prophète a été connu pour sa grande patience ?",
                "options": ["Job", "Noé", "Moïse", "David"],
                "answer": 0,
                "time_limit": 30
            },
            {
                "question": "Qui est le prophète associé à la naissance miraculeuse ?",
                "options": ["Jésus", "Moïse", "Abraham", "Muhammad"],
                "answer": 0,
                "time_limit": 20
            },
        ]
    },
    
    {
      "category": "Hadiths",
      "questions": [
        {
          "question 1": "Quel est le nom du recueil de hadiths le plus célèbre ?",
          "options": ["Sahih al-Bukhari", "Sahih Muslim", "Sunan Abu Dawood", "Jami` at-Tirmidhi"],
          "answer": 0,
          "time_limit": 25
        },
        {
          "question 2": "Qui est l'auteur du recueil de hadiths 'Sahih Muslim' ?",
          "options": ["Imam al-Bukhari", "Imam Muslim", "Imam Abu Dawood", "Imam at-Tirmidhi"],
          "answer": 1,
          "time_limit": 20
        },
        {
          "question 3": "Quel est le critère principal pour qu'un hadith soit considéré comme authentique ?",
          "options": ["La chaîne de transmission", "Le contenu du hadith", "La popularité du hadith", "L'époque de la révélation"],
          "answer": 0,
          "time_limit": 30
        },
        {
          "question 4": "Quel est le terme utilisé pour désigner les paroles du Prophète Muhammad ?",
          "options": ["Quran", "Hadith", "Sunnah", "Fiqh"],
          "answer": 1,
          "time_limit": 15
        },
        {
          "question 5": "Quelle est la différence entre un hadith sahih et un hadith da'if ?",
          "options": ["Authentique vs faible", "Récent vs ancien", "Court vs long", "Public vs privé"],
          "answer": 0,
          "time_limit": 20
        },
        {
          "question 6": "Quel est le but principal des hadiths dans l'Islam ?",
          "options": ["Expliquer le Coran", "Raconter des histoires", "Promouvoir la culture islamique", "Former des juristes"],
          "answer": 0,
          "time_limit": 25
        },
        {
          "question 7": "Quel est le nom du recueil de hadiths compilé par Abu Dawood ?",
          "options": ["Sunan Abu Dawood", "Sahih al-Bukhari", "Jami` at-Tirmidhi", "Sunan an-Nasa'i"],
          "answer": 0,
          "time_limit": 30
        },
        {
          "question 8": "Qui a dit : 'Les actions ne valent que par leurs intentions' ?",
          "options": ["Abu Huraira", "Anas ibn Malik", "Umar ibn al-Khattab", "Muhammad"],
          "answer": 3,
          "time_limit": 20
        },
        {
          "question 9": "Quel est le terme utilisé pour désigner les actions et les pratiques du Prophète Muhammad ?",
          "options": ["Sunnah", "Hadith", "Fiqh", "Sharia"],
          "answer": 0,
          "time_limit": 15
        },
        {
          "question 10": "Quel est le nom du recueil de hadiths compilé par at-Tirmidhi ?",
          "options": ["Sunan at-Tirmidhi", "Sahih al-Bukhari", "Sunan Abu Dawood", "Jami` at-Tirmidhi"],
          "answer": 3,
          "time_limit": 25
        }
      ]
    },
    {
      "category": "Fiqh",
      "questions": [
        {
          "question 1": "Quelle est la principale source de la jurisprudence islamique ?",
          "options": ["Le Coran", "Les hadiths", "Le consensus des savants", "L'analogie"],
          "answer": 0,
          "time_limit": 30
        },
        {
          "question 2": "Quel est le terme utilisé pour désigner les règles juridiques dans l'Islam ?",
          "options": ["Fiqh", "Sharia", "Sunnah", "Hadith"],
          "answer": 0,
          "time_limit": 20
        },
        {
          "question 3": "Quel est le nom de la prière obligatoire du vendredi ?",
          "options": ["Salat al-Jumu'ah", "Salat al-Maghrib", "Salat al-Isha", "Salat al-Fajr"],
          "answer": 0,
          "time_limit": 15
        },
        {
          "question 4": "Quelle est la principale différence entre le fiqh sunnite et le fiqh chiite ?",
          "options": ["Sources de jurisprudence", "Rituels de prière", "Interprétation du Coran", "Histoire des prophètes"],
          "answer": 0,
          "time_limit": 30
        },
        {
          "question 5": "Quel est le terme utilisé pour désigner l'interprétation du Coran ?",
          "options": ["Tafsir", "Hadith", "Fiqh", "Sunnah"],
          "answer": 0,
          "time_limit": 20
        },
        {
          "question 6": "Quel est le nom de la taxe obligatoire en Islam destinée aux pauvres ?",
          "options": ["Zakat", "Sadaqah", "Khums", "Fitr"],
          "answer": 0,
          "time_limit": 15
        },
        {
          "question 7": "Quel est le terme utilisé pour désigner les actes interdits en Islam ?",
          "options": ["Halal", "Haram", "Mustahabb", "Makruh"],
          "answer": 1,
          "time_limit": 20
        },
        {
          "question 8": "Quelle est la principale différence entre halal et haram ?",
          "options": ["Permis vs interdit", "Obligatoire vs facultatif", "Recommandé vs déconseillé", "Légal vs illégal"],
          "answer": 0,
          "time_limit": 25
        },
        {
          "question 9": "Quel est le terme utilisé pour désigner les actes recommandés en Islam ?",
          "options": ["Halal", "Haram", "Mustahabb", "Makruh"],
          "answer": 2,
          "time_limit": 20
        },
        {
          "question 10": "Quel est le nom de la prière nocturne facultative ?",
          "options": ["Salat al-Tahajjud", "Salat al-Witr", "Salat al-Tarawih", "Salat al-Duha"],
          "answer": 0,
          "time_limit": 25
        }
      ]
    },
    {
      "category": "Histoire de l'Islam",
      "questions": [
        {
          "question 1": "En quelle année a eu lieu l'Hégire ?",
          "options": ["622", "630", "632", "610"],
          "answer": 0,
          "time_limit": 20
        },
        {
          "question 2": "Qui était le premier calife de l'Islam ?",
          "options": ["Abu Bakr", "Omar", "Othman", "Ali"],
          "answer": 0,
          "time_limit": 15
        },
        {
          "question 3": "Quel événement marque le début du calendrier islamique ?",
          "options": ["La naissance du Prophète", "L'Hégire", "La révélation du Coran", "La conquête de La Mecque"],
          "answer": 1,
          "time_limit": 25
        },
        {
          "question 4": "Quelle bataille a eu lieu en 624 et est considérée comme la première bataille de l'Islam ?",
          "options": ["Bataille de Badr", "Bataille de Uhud", "Bataille de Khandaq", "Bataille de Tabuk"],
          "answer": 0,
          "time_limit": 20
        },
        {
          "question 5": "Qui a été le dernier calife de l'Empire omeyyade ?",
          "options": ["Marwan II", "Abd al-Malik", "Yazid I", "Hisham"],
          "answer": 0,
          "time_limit": 30
        },
        {
          "question 6": "Quel est le nom de la dynastie qui a succédé aux Omeyyades ?",
          "options": ["Les Abbassides", "Les Fatimides", "Les Ayyoubides", "Les Mamelouks"],
          "answer": 0,
          "time_limit": 25
        },
        {
          "question 7": "Quel est le nom de la ville où se trouve la mosquée Al-Aqsa ?",
          "options": ["Médine", "La Mecque", "Jérusalem", "Damas"],
          "answer": 2,
          "time_limit": 20
        },
        {
          "question 8": "Qui a fondé la ville de Bagdad ?",
          "options": ["Abu Bakr", "Omar", "Al-Mansur", "Haroun al-Rachid"],
          "answer": 2,
          "time_limit": 30
        },
        {
          "question 9": "Quel est le nom de la bataille qui a eu lieu en 732 et a stoppé l'expansion musulmane en Europe ?",
          "options": ["Bataille de Poitiers", "Bataille de Tours", "Bataille de Badr", "Bataille de Uhud"],
          "answer": 0,
          "time_limit": 25
        },
        {
          "question 10": "Quel est le nom du traité qui a mis fin à la guerre entre les musulmans et les Byzantins en 628 ?",
          "options": ["Traité de Hudaybiyyah", "Traité de Médine", "Traité de Khaybar", "Traité de Tabuk"],
          "answer": 0,
          "time_limit": 20
        }
      ]
    },
    {
      "category": "Géographie islamique",
      "questions": [
        {
          "question 1": "Quelle est la ville sainte de l'Islam ?",
          "options": ["La Mecque", "Médine", "Jérusalem", "Damas"],
          "answer": 0,
          "time_limit": 15
        },
        {
          "question 2": "Quel est le nom de la mosquée la plus sacrée de l'Islam ?",
          "options": ["Mosquée Al-Aqsa", "Mosquée du Prophète", "Mosquée Al-Haram", "Mosquée de Damas"],
          "answer": 2,
          "time_limit": 20
        },
        {
          "question 3": "Dans quel pays se trouve la ville de Médine ?",
          "options": ["Arabie Saoudite", "Égypte", "Syrie", "Irak"],
          "answer": 0,
          "time_limit": 15
        },
        {
          "question 4": "Quelle est la direction vers laquelle les musulmans prient ?",
          "options": ["La Mecque", "Médine", "Jérusalem", "Damas"],
          "answer": 0,
          "time_limit": 10
        },
        {
          "question 5": "Quel est le nom de la montagne où le Prophète Muhammad a reçu la première révélation ?",
          "options": ["Mont Sinaï", "Mont Arafat", "Mont Hira", "Mont Uhud"],
          "answer": 2,
          "time_limit": 20
        },
        {
          "question 6": "Quelle est la capitale de l'Arabie Saoudite ?",
          "options": ["Riyad", "Djeddah", "Médine", "La Mecque"],
          "answer": 0,
          "time_limit": 15
        },
        {
          "question 7": "Quel est le nom du fleuve sacré en Islam ?",
          "options": ["Nil", "Euphrate", "Tigre", "Jourdain"],
          "answer": 1,
          "time_limit": 20
        },
        {
          "question 8": "Quelle ville est connue comme le 'cœur de l'Islam' ?",
          "options": ["La Mecque", "Médine", "Bagdad", "Damas"],
          "answer": 0,
          "time_limit": 15
        },
        {
          "question 9": "Quel est le nom de la mosquée située à Jérusalem ?",
          "options": ["Mosquée Al-Aqsa", "Mosquée Al-Haram", "Mosquée du Prophète", "Mosquée de Damas"],
          "answer": 0,
          "time_limit": 20
        },
        {
          "question 10": "Dans quel pays se trouve la ville de Kairouan, un site important pour les musulmans ?",
          "options": ["Tunisie", "Algérie", "Maroc", "Libye"],
          "answer": 0,
          "time_limit": 25
        }
      ]
    },
    {
      "category": "Croyances islamiques",
      "questions": [
        {
          "question 1": "Combien de piliers de l'Islam y a-t-il ?",
          "options": ["5", "6", "7", "8"],
          "answer": 0,
          "time_limit": 10
        },
        {
          "question 2": "Quel est le premier pilier de l'Islam ?",
          "options": ["La prière", "Le jeûne", "La profession de foi", "La zakat"],
          "answer": 2,
          "time_limit": 15
        },
        {
          "question 3": "Quel est le deuxième pilier de l'Islam ?",
          "options": ["La prière", "Le jeûne", "La profession de foi", "La zakat"],
          "answer": 0,
          "time_limit": 15
        },
        {
          "question 4": "Quel est le troisième pilier de l'Islam ?",
          "options": ["La prière", "Le jeûne", "La profession de foi", "La zakat"],
          "answer": 1,
          "time_limit": 20
        },
        {
          "question 5": "Quel est le quatrième pilier de l'Islam ?",
          "options": ["La prière", "Le jeûne", "La profession de foi", "La zakat"],
          "answer": 3,
          "time_limit": 20
        },
        {
          "question 6": "Quel est le cinquième pilier de l'Islam ?",
          "options": ["Le pèlerinage à La Mecque", "Le jeûne du Ramadan", "La prière quotidienne", "La zakat"],
          "answer": 0,
          "time_limit": 25
        },
        {
          "question 7": "Quel est le nom du mois sacré du jeûne en Islam ?",
          "options": ["Ramadan", "Chawwal", "Dhu al-Hijjah", "Muharram"],
          "answer": 0,
          "time_limit": 15
        },
        {
          "question 8": "Quelle est la signification du mot 'Islam' ?",
          "options": ["Soumission à Dieu", "Paix", "Foi", "Prière"],
          "answer": 0,
          "time_limit": 20
        },
        {
          "question 9": "Quel est le nom de la profession de foi islamique ?",
          "options": ["Shahada", "Zakat", "Salah", "Hajj"],
          "answer": 0,
          "time_limit": 15
        },
        {
          "question 10": "Quel est le nom du pèlerinage obligatoire pour les musulmans ?",
          "options": ["Hajj", "Umrah", "Zakat", "Salah"],
          "answer": 0,
          "time_limit": 20
        }
      ]
    },
    {
      "category": "Éthique islamique",
      "questions": [
        {
          "question 1": "Quel est le principe fondamental de l'éthique islamique ?",
          "options": ["La justice", "La charité", "Le respect des parents", "L'honnêteté"],
          "answer": 0,
          "time_limit": 15
        },
        {
          "question 2": "Quel est le terme utilisé pour désigner l'interdiction de nuire aux autres ?",
          "options": ["Haram", "Halal", "Zakat", "Sadaqah"],
          "answer": 0,
          "time_limit": 20
        },
        {
          "question 3": "Quel est le nom de la charité obligatoire en Islam ?",
          "options": ["Zakat", "Sadaqah", "Khums", "Fitr"],
          "answer": 0,
          "time_limit": 15
        },
        {
          "question 4": "Quel est le terme utilisé pour désigner les actions recommandées en Islam ?",
          "options": ["Halal", "Haram", "Mustahabb", "Makruh"],
          "answer": 2,
          "time_limit": 20
        },
        {
          "question 5": "Quel est le terme utilisé pour désigner les actions déconseillées en Islam ?",
          "options": ["Halal", "Haram", "Mustahabb", "Makruh"],
          "answer": 3,
          "time_limit": 20
        },
        {
          "question 6": "Quel est le nom de la prière du vendredi ?",
          "options": ["Salat al-Jumu'ah", "Salat al-Maghrib", "Salat al-Isha", "Salat al-Fajr"],
          "answer": 0,
          "time_limit": 15
        },
        {
          "question 7": "Quel est le terme utilisé pour désigner l'interdiction de consommer de l'alcool en Islam ?",
          "options": ["Halal", "Haram", "Mustahabb", "Makruh"],
          "answer": 1,
          "time_limit": 20
        },
        {
          "question 8": "Quel est le nom de la prière nocturne facultative ?",
          "options": ["Salat al-Tahajjud", "Salat al-Witr", "Salat al-Tarawih", "Salat al-Duha"],
          "answer": 0,
          "time_limit": 25
        },
        {
          "question 9": "Quel est le terme utilisé pour désigner l'interdiction de la usure en Islam ?",
          "options": ["Riba", "Zakat", "Sadaqah", "Khums"],
          "answer": 0,
          "time_limit": 20
        },
        {
          "question 10": "Quel est le nom de la prière du matin ?",
          "options": ["Salat al-Fajr", "Salat al-Dhuhr", "Salat al-Asr", "Salat al-Maghrib"],
          "answer": 0,
          "time_limit": 15
        }
      ]
    }
]

# ---------------------------------------------
# 2. Fonction Tkinter pour afficher les questions
# ---------------------------------------------
def afficher_quiz(root, categorie_data):
    # Mélange de l'ordre des questions
    random.shuffle(categorie_data["questions"])

    # Frame pour la catégorie
    frame_cat = ttk.LabelFrame(root, text=categorie_data["category"], padding=10)
    frame_cat.pack(fill="both", expand=True, padx=10, pady=10)

    # Liste pour stocker (IntVar, bonne_réponse)
    controles = []

    # Création des widgets pour chaque question
    for idx, q in enumerate(categorie_data["questions"], start=1):
        # Label de la question
        lbl_q = ttk.Label(frame_cat,
                          text=f"{idx}. {q['question']}",
                          wraplength=700,
                          justify="left")
        lbl_q.pack(anchor="w", pady=(5, 0))

        # IntVar pour la réponse
        var = tk.IntVar(value=-1)
        for opt_idx, opt_txt in enumerate(q["options"]):
            rb = ttk.Radiobutton(frame_cat,
                                 text=opt_txt,
                                 variable=var,
                                 value=opt_idx)
            rb.pack(anchor="w", padx=20)
        # Stockage pour le calcul du score
        controles.append((var, q["answer"]))

    # Fonction de validation
    def valider():
        score = sum(1 for var, bonne in controles if var.get() == bonne)
        total = len(controles)
        messagebox.showinfo("Résultat",
                            f"Vous avez {score} bonne{'s' if score>1 else ''} "
                            f"réponse{'s' if score>1 else ''} sur {total}.")

    # Bouton Valider
    btn = ttk.Button(frame_cat, text="Valider", command=valider)
    btn.pack(pady=10)

# ---------------------------------------------
# 3. Point d'entrée principal
# ---------------------------------------------
def main():
    # Sélection de la catégorie à afficher (index 0 = "Coran")
    categorie = questions_data[0]

    root = tk.Tk()
    root.title("Quiz Islamique")
    root.geometry("800x600")

    # Canvas + Scrollbar pour le défilement
    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    conteneur = ttk.Frame(canvas)

    conteneur.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=conteneur, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Affichage du quiz
    afficher_quiz(conteneur, categorie)

    root.mainloop()

if __name__ == "__main__":
    main()

# Description détaillée du jeu Quiz_Islam

# Ce jeu est une application interactive de quiz basée sur Python et Tkinter. 
# Il est conçu pour tester et améliorer vos connaissances sur divers aspects de l'Islam, 
# tels que le Coran, les Prophètes, les Hadiths, la jurisprudence islamique (Fiqh), 
# l'histoire de l'Islam, la géographie islamique, les croyances islamiques et l'éthique islamique.

# Fonctionnalités principales :
# 1. **Interface utilisateur conviviale** :
#    - L'application utilise Tkinter pour créer une interface graphique simple et intuitive.
#    - Les questions sont affichées dans une interface défilable pour une meilleure navigation.

# 2. **Catégories variées** :
#    - Le jeu propose plusieurs catégories de questions, chacune couvrant un domaine spécifique de l'Islam.
#    - Chaque catégorie contient un ensemble de questions soigneusement sélectionnées.

# 3. **Questions aléatoires** :
#    - Les questions dans chaque catégorie sont mélangées aléatoirement pour offrir une expérience unique à chaque partie.

# 4. **Options de réponse multiples** :
#    - Chaque question propose plusieurs options de réponse, et l'utilisateur doit sélectionner la bonne réponse.

# 5. **Calcul automatique du score** :
#    - Une fois que l'utilisateur a répondu à toutes les questions, il peut cliquer sur le bouton "Valider" pour voir son score.
#    - Le score est calculé automatiquement en comparant les réponses de l'utilisateur avec les bonnes réponses.

# 6. **Limite de temps pour chaque question** (optionnel) :
#    - Bien que non implémentée dans l'interface actuelle, chaque question a une limite de temps associée dans les données, 
#      ce qui peut être utilisé pour ajouter une contrainte de temps dans une version future.

# 7. **Extensibilité** :
#    - Les données des questions sont stockées dans une structure Python facile à modifier.
#    - De nouvelles catégories et questions peuvent être ajoutées sans modifier le code principal.

# 8. **Résultats clairs** :
#    - Une boîte de dialogue affiche le score final de l'utilisateur, indiquant le nombre de bonnes réponses sur le total.

# Instructions pour jouer :
# - Lancez l'application en exécutant le script `quiz_app.py`.
# - Une catégorie de questions sera affichée (par défaut, la catégorie "Coran").
# - Lisez chaque question et sélectionnez la réponse correcte en cliquant sur les boutons radio.
# - Une fois toutes les questions répondues, cliquez sur "Valider" pour voir votre score.
# - Pour changer de catégorie, modifiez la variable `categorie` dans la fonction `main()`.

# Ce jeu est idéal pour les étudiants, les enseignants ou toute personne souhaitant approfondir ses connaissances sur l'Islam de manière ludique et interactive.

