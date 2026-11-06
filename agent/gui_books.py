import customtkinter as ctk
import sys
import os

# Add the build directory to sys.path to import the compiled module
sys.path.append(os.path.join(os.getcwd(), "build"))
import bibliotheque_py


class BookView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion de la Bibliothèque - Livres")
        self.geometry("600x400")

        # Initialisation de la bibliothèque et chargement des données
        self.library = bibliotheque_py.Library()
        self.file_manager = bibliotheque_py.FileManager("data/books.txt", "data/users.txt")
        self.file_manager.load_library_data(self.library)

        self.setup_ui()

    def setup_ui(self):
        self.label = ctk.CTkLabel(self, text="Liste des Livres", font=("Arial", 20))
        self.label.pack(pady=20)

        self.book_list_frame = ctk.CTkScrollableFrame(self, width=500, height=300)
        self.book_list_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.refresh_book_list()

    def refresh_book_list(self):
        # Nettoyer la liste actuelle
        for widget in self.book_list_frame.winfo_children():
            widget.destroy()

        # Récupérer les livres via le module C++
        books = self.library.get_all_books()
        for book in books:
            book_text = f"{book.title} - {book.author} (ISBN: {book.isbn}) [{'Disponible' if book.is_available else 'Emprunté'}]"
            lbl = ctk.CTkLabel(self.book_list_frame, text=book_text, anchor="w")
            lbl.pack(fill="x", padx=10, pady=5)

if __name__ == "__main__":
    app = BookView()
    app.mainloop()
