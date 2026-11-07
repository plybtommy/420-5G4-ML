# Plan de Migration GUI (customTkinter + pybind11)

## Phase 1 : Préparation et Liaison (Le "Pont" C++ -> Python)
- [x] Installation des dépendances (`pybind11`, `customtkinter`).
- [x] Création du wrapper Pybind11 (`bindings.cpp`) pour exposer `Library`, `Book`, `User` et `FileManager`.
- [x] Mise à jour de CMake pour compiler un module Python (`pybind11_add_module`).

## Phase 2 : Développement Itératif des Vues (Interface -> Liaison -> Test)
- [x] **Vue Livres** :
    - Interface (liste, ajout, suppression).
    - Liaison avec les méthodes C++ correspondantes.
    - Test de fonctionnement.
- [x] **Vue Utilisateurs** :
    - Interface (gestion des membres).
    - Liaison avec les méthodes C++ correspondantes.
    - Test de fonctionnement.
- [x] **Vue Opérations** :
    - Interface (emprunts et retours).
    - Liaison avec les méthodes C++ correspondantes.
    - Test de fonctionnement.

## Phase 3 : Fonctionnalités Avancées
- [x] **Recherche** : Implémentation des filtres par titre et auteur.
- [x] **Statistiques** : Affichage du nombre total de livres, disponibles et empruntés.
- [x] **Sauvegarde** : Liaison avec `FileManager` pour persister les données.

## Phase 4 : Finalisation
- [x] Tests de bout en bout et vérification de la persistance des données.
- [x] Nettoyage du code.
