# Plan de Migration GUI (customTkinter + pybind11)

## Phase 1 : Préparation et Liaison (Le "Pont" C++ -> Python)
- [ ] Installation des dépendances (`pybind11`, `customtkinter`).
- [ ] Création du wrapper Pybind11 (`bindings.cpp`) pour exposer `Library`, `Book`, et `User`.
- [ ] Mise à jour de CMake pour compiler un module Python (`pybind11_add_module`).

## Phase 2 : Architecture de l'Interface (GUI)
- [ ] Structure de l'application (`LibraryApp`) avec navigation latérale.
- [ ] Développement de la vue "Livres" (liste, ajout, suppression).
- [ ] Développement de la vue "Utilisateurs" (gestion des membres).
- [ ] Développement de la vue "Opérations" (emprunts et retours).

## Phase 3 : Intégration et Logique
- [ ] Création d'une couche intermédiaire Python pour l'instanciation de la `Library` C++.
- [ ] Liaison des événements GUI aux méthodes C++.
- [ ] Gestion des erreurs et affichage d'alertes.

## Phase 4 : Finalisation
- [ ] Tests de bout en bout et vérification de la persistance des données.
- [ ] Nettoyage du code.
