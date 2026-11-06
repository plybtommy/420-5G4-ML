# AGENTS.md

## Objectif
Remplacer le menu console de `main.cpp` par une interface graphique Python utilisant `customTkinter`, reliée au code C++ (`Library`, `Book`, `User`, `FileManager`) via `pybind11`.

## Build & Execution
- **Build System**: CMake (C++17)
- **Build Commands**:
  ```bash
  mkdir -p build && cd build && cmake .. && make
  ```
- **Execution**:
  The executable is named `bibliotheque`.
  To specify the data directory:
  ```bash
  ./bibliotheque -d <path_to_data_dir>
  ```
- **Data**: Test files located in `data/books.txt` and `data/users.txt`.

## Avancement
- [ ] Installation des dépendances (pybind11, customtkinter)
- [ ] Création du wrapper Pybind11 (`bindings.cpp`)
- [ ] Mise à jour de CMake pour le module Python
- [ ] Structure de l'application GUI (`LibraryApp`)
- [ ] Vues Livres, Utilisateurs et Opérations
- [ ] Liaison GUI $\rightarrow$ Logique C++
- [ ] Tests de persistance
