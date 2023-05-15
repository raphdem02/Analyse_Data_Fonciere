# Analyse_Data_Fonciere DEMARE DELGADO CHEN TD D
Ce projet avait pour but d'analyser les données foncières de 5 années différentes. Le travail sur le projet a été réparti équitablement entre nous trois. Au niveau du GUI, après avoir demandé à notre chargé de TD l'authorisation nous avons décidé d'utiliser Flask au lieu de Django car l'un d'entre nous était déja familier avec ce framework et la différence entre les deux framework est vraiment très faible. Dans ce GUI nous avons pris le parti d'afficher l'ensemble de nos analyses et comparaisons pour toutes les années, accessible grâce à une navbar.De plus on a ajouté un widget pour afficher de maniere dynamique l'argent total dépensé par mois selon les types de mutation(sélectionnable dans le widget) pendant l'année 2019.
# Parti Flask
## Installer Flask et les dépendances nécessaires  
Installer flask de préférence dans un environnement virtuel, ce lien explique comment faire : [https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)  

Naviguer dans le répertoire ``` cd flask_app ```

Pour installer les dépendances nécessaires lancer la commande:

```bash 
$ pip3 install -r requirements.txt
```

## Lancer l'application 
Mettre les variables d'environnement à jour en tapant dans le terminal les commandes ```export FLASK_APP=run.py``` et ```export FLASK_ENV=development```
Puis executer ```flask run```

## Template Flask
La page de garde ainsi que les boutons de navigations proviennent d'un template Flask open source et ont été modifié pour un soucis de gain de temps (et aussi de beauté de la page)

# Parti Data/Notebook

## Data
Nous avons des données trop voluminieuses pour être déposer avec le projet (il y a donc un .gitignore), elles sont trouvables ici: [https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/)

## Analysis.ipynb
Notebook contenant l'analyse de l'année 2022, la même analyse est utilisé pour les autres années en modiifiant quelques lignes et sont trouvables dans le dossier ***notebook_html_versions***.

## Comparaison.ipynb
Notebook contenant la comparaison de différents paramètres entre les 5 années.
