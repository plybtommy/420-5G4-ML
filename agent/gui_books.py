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
        self.label = ctk.CTkLabel(self, text="Gestion des Livres", font=("Arial", 20))
        self.label.pack(pady=20)

        # Formulaire d'ajout
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.pack(pady=10, padx=20, fill="x")

        self.entry_title = ctk.CTkEntry(self.form_frame, placeholder_text="Titre")
        self.entry_title.pack(side="left", padx=5, pady=10, expand=True, fill="x")

        self.entry_author = ctk.CTkEntry(self.form_frame, placeholder_text="Auteur")
        self.entry_author.pack(side="left", padx=5, pady=10, expand=True, fill="x")

        self.entry_isbn = ctk.CTkEntry(self.form_frame, placeholder_text="ISBN")
        self.entry_isbn.pack(side="left", padx=5, pady=10, expand=True, fill="x")

        self.add_button = ctk.CTkButton(self.form_frame, text="Ajouter", command=self.add_book)
        self.add_button.pack(side="left", padx=5, pady=10)

        # Zone de suppression
        self.delete_frame = ctk.CTkFrame(self)
        self.delete_frame.pack(pady=10, padx=20, fill="x")

        self.entry_delete_isbn = ctk.CTkEntry(self.delete_frame, placeholder_text="ISBN du livre à supprimer")
        self.entry_delete_isbn.pack(side="left", padx=5, pady=10, expand=True, fill="x")

        self.delete_button = ctk.CTkButton(self.delete_frame, text="Supprimer", fg_color="red", hover_color="darkred", command=self.delete_book)
        self.delete_button.pack(side="left", padx=5, pady=10)

        # Liste des livres
        self.book_list_frame = ctk.CTkScrollableFrame(self, width=500, height=300)
        self.book_list_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.refresh_book_list()

    def add_book(self):
        title = self.entry_title.get()
        author = self.entry_author.get()
        isbn = self.entry_isbn.get()

        if title and author and isbn:
            if self.library.add_book(bibliotheque_py.Book(title, author, isbn)):
                self.entry_title.delete(0, 'end')
                self.entry_author.delete(0, 'end')
                self.entry_isbn.delete(0, 'end')
                self.refresh_book_list()
            else:
                print("Erreur : Un livre avec cet ISBN existe déjà.")

    def delete_book(self):
        isbn = self.entry_delete_isbn.get()
        if isbn:
            if self.library.remove_book(isbn):
                self.entry_delete_isbn.delete(0, 'end')
                self.refresh_book_list()
            else:
                print("Erreur : Aucun livre trouvé avec cet ISBN.")

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
