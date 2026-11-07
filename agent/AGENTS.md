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
- [x] Installation des dépendances (pybind11, customtkinter)
- [x] Création du wrapper Pybind11 (`bindings.cpp`) incluant `FileManager`
- [x] Mise à jour de CMake pour le module Python
- [x] Vue Livres : Interface $\rightarrow$ Liaison C++ $\rightarrow$ Test

- [x] Vue Utilisateurs : Interface $\rightarrow$ Liaison C++ $\rightarrow$ Test
- [x] Vue Opérations : Interface $\rightarrow$ Liaison C++ $\rightarrow$ Test
- [x] Implémentation Recherche, Statistiques et Sauvegarde
- [x] Tests de persistance
