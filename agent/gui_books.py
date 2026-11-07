import customtkinter as ctk
import sys
import os
from gui_operations import OperationsView


# Add the build directory to sys.path to import the compiled module
sys.path.append(os.path.join(os.getcwd(), "build"))
import bibliotheque_py

class BookView(ctk.CTkFrame):
    def __init__(self, master, library, file_manager):
        super().__init__(master)
        self.library = library
        self.file_manager = file_manager
        self.setup_ui()

    def setup_ui(self):
        self.label = ctk.CTkLabel(self, text="Gestion des Livres", font=("Arial", 20))
        self.label.pack(pady=20)

        # Message area
        self.status_label = ctk.CTkLabel(self, text="", font=("Arial", 12), text_color="gray")
        self.status_label.pack(pady=5)


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

        # Zone de recherche
        self.search_frame = ctk.CTkFrame(self)
        self.search_frame.pack(pady=10, padx=20, fill="x")

        self.entry_search = ctk.CTkEntry(self.search_frame, placeholder_text="Rechercher par titre ou auteur...")
        self.entry_search.pack(side="left", padx=5, pady=10, expand=True, fill="x")

        self.search_button = ctk.CTkButton(self.search_frame, text="Rechercher", command=self.search_books)
        self.search_button.pack(side="left", padx=5, pady=10)

        self.reset_search_button = ctk.CTkButton(self.search_frame, text="Réinitialiser", command=self.refresh_book_list)
        self.reset_search_button.pack(side="left", padx=5, pady=10)

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

    def show_message(self, text, is_error=False):
        color = "red" if is_error else "green"
        self.status_label.configure(text=text, text_color=color)
        # Reset message after 3 seconds
        self.after(3000, lambda: self.status_label.configure(text=""))

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
                self.show_message(f"Livre '{title}' ajouté avec succès")
            else:
                self.show_message("Erreur : Un livre avec cet ISBN existe déjà.", True)
        else:
            self.show_message("Erreur : Veuillez remplir tous les champs", True)

    def delete_book(self):
        isbn = self.entry_delete_isbn.get()
        if isbn:
            if self.library.remove_book(isbn):
                self.entry_delete_isbn.delete(0, 'end')
                self.refresh_book_list()
                self.show_message(f"Livre {isbn} supprimé")
            else:
                self.show_message("Erreur : Aucun livre trouvé avec cet ISBN.", True)
        else:
            self.show_message("Erreur : Veuillez saisir un ISBN", True)

    def search_books(self):
        query = self.entry_search.get()
        if not query:
            self.refresh_book_list()
            return

        results = self.library.search_books_by_title(query)
        author_results = self.library.search_books_by_author(query)
        
        all_results = {book.isbn: book for book in results + author_results}.values()
        
        self.update_book_list_display(all_results)
        if not all_results:
            self.show_message("Aucun livre trouvé pour cette recherche", True)
        else:
            self.show_message(f"{len(all_results)} livre(s) trouvé(s)")

    def refresh_book_list(self):
        self.entry_search.delete(0, 'end')
        self.update_book_list_display(self.library.get_all_books())

    def update_book_list_display(self, books):
        for widget in self.book_list_frame.winfo_children():
            widget.destroy()

        for book in books:
            book_text = f"{book.title} - {book.author} (ISBN: {book.isbn}) [{'Disponible' if book.is_available else 'Emprunté'}]"
            lbl = ctk.CTkLabel(self.book_list_frame, text=book_text, anchor="w")
            lbl.pack(fill="x", padx=10, pady=5)

class StatsView(ctk.CTkFrame):
    def __init__(self, master, library, file_manager):
        super().__init__(master)
        self.library = library
        self.file_manager = file_manager
        self.setup_ui()

    def setup_ui(self):
        self.label = ctk.CTkLabel(self, text="Statistiques de la Bibliothèque", font=("Arial", 20))
        self.label.pack(pady=20)

        # Message area
        self.status_label = ctk.CTkLabel(self, text="", font=("Arial", 12), text_color="gray")
        self.status_label.pack(pady=5)

        self.stats_frame = ctk.CTkFrame(self)
        self.stats_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.lbl_total_books = ctk.CTkLabel(self.stats_frame, text="", font=("Arial", 16))
        self.lbl_total_books.pack(pady=10)

        self.lbl_available_books = ctk.CTkLabel(self.stats_frame, text="", font=("Arial", 16))
        self.lbl_available_books.pack(pady=10)

        self.lbl_borrowed_books = ctk.CTkLabel(self.stats_frame, text="", font=("Arial", 16))
        self.lbl_borrowed_books.pack(pady=10)

        self.lbl_total_users = ctk.CTkLabel(self.stats_frame, text="", font=("Arial", 16))
        self.lbl_total_users.pack(pady=10)

        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=20)

        self.refresh_button = ctk.CTkButton(self.button_frame, text="Actualiser", command=self.update_stats)
        self.refresh_button.pack(side="left", padx=10)

        self.save_button = ctk.CTkButton(self.button_frame, text="Sauvegarder", fg_color="green", hover_color="darkgreen", command=self.save_data)
        self.save_button.pack(side="left", padx=10)

        self.update_stats()

    def update_stats(self):
        total_books = self.library.get_total_books()
        available = self.library.get_available_book_count()
        borrowed = self.library.get_checked_out_book_count()
        total_users = len(self.library.get_all_users())

        self.lbl_total_books.configure(text=f"Nombre total de livres : {total_books}")
        self.lbl_available_books.configure(text=f"Livres disponibles : {available}")
        self.lbl_borrowed_books.configure(text=f"Livres empruntés : {borrowed}")
        self.lbl_total_users.configure(text=f"Nombre total d'utilisateurs : {total_users}")

    def save_data(self):
        # Use the file manager from MainApp (will be passed in init)
        if self.file_manager and self.file_manager.save_library_data(self.library):
            self.show_message("Données sauvegardées avec succès")
        else:
            self.show_message("Erreur lors de la sauvegarde", True)

    def show_message(self, text, is_error=False):
        color = "red" if is_error else "green"
        self.status_label.configure(text=text, text_color=color)
        self.after(3000, lambda: self.status_label.configure(text=""))

class UserView(ctk.CTkFrame):
    def __init__(self, master, library):
        super().__init__(master)
        self.library = library
        self.setup_ui()

    def setup_ui(self):
        self.label = ctk.CTkLabel(self, text="Gestion des Utilisateurs", font=("Arial", 20))
        self.label.pack(pady=20)

        # Message area
        self.status_label = ctk.CTkLabel(self, text="", font=("Arial", 12), text_color="gray")
        self.status_label.pack(pady=5)


        # Formulaire d'ajout
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.pack(pady=10, padx=20, fill="x")

        self.entry_name = ctk.CTkEntry(self.form_frame, placeholder_text="Nom")
        self.entry_name.pack(side="left", padx=5, pady=10, expand=True, fill="x")

        self.entry_id = ctk.CTkEntry(self.form_frame, placeholder_text="ID Utilisateur")
        self.entry_id.pack(side="left", padx=5, pady=10, expand=True, fill="x")

        self.add_button = ctk.CTkButton(self.form_frame, text="Ajouter", command=self.add_user)
        self.add_button.pack(side="left", padx=5, pady=10)

        # Liste des utilisateurs
        self.user_list_frame = ctk.CTkScrollableFrame(self, width=500, height=300)
        self.user_list_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.refresh_user_list()

    def show_message(self, text, is_error=False):
        color = "red" if is_error else "green"
        self.status_label.configure(text=text, text_color=color)
        self.after(3000, lambda: self.status_label.configure(text=""))

    def add_user(self):
        name = self.entry_name.get()
        user_id = self.entry_id.get()

        if name and user_id:
            if self.library.add_user(bibliotheque_py.User(name, user_id)):
                self.entry_name.delete(0, 'end')
                self.entry_id.delete(0, 'end')
                self.refresh_user_list()
                self.show_message(f"Utilisateur '{name}' ajouté")
            else:
                self.show_message("Erreur : Un utilisateur avec cet ID existe déjà.", True)
        else:
            self.show_message("Erreur : Veuillez remplir tous les champs", True)

    def refresh_user_list(self):

        for widget in self.user_list_frame.winfo_children():
            widget.destroy()

        users = self.library.get_all_users()
        for user in users:
            user_text = f"ID: {user.user_id} - Nom: {user.name}"
            lbl = ctk.CTkLabel(self.user_list_frame, text=user_text, anchor="w")
            lbl.pack(fill="x", padx=10, pady=5)

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion de la Bibliothèque")
        self.geometry("700x500")

        # Handle window close event for automatic save
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Shared library and file manager
        self.library = bibliotheque_py.Library()
        self.file_manager = bibliotheque_py.FileManager("data/books.txt", "data/users.txt")
        self.file_manager.load_library_data(self.library)

        # Tab view
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(padx=20, pady=20, fill="both", expand=True)

        self.tabview.add("Livres")
        self.tabview.add("Utilisateurs")
        self.tabview.add("Opérations")
        self.tabview.add("Statistiques")

        # Views
        self.book_view = BookView(self.tabview.tab("Livres"), self.library, self.file_manager)
        self.book_view.pack(fill="both", expand=True)

        self.user_view = UserView(self.tabview.tab("Utilisateurs"), self.library)
        self.user_view.pack(fill="both", expand=True)

        self.ops_view = OperationsView(self.tabview.tab("Opérations"), self.library, refresh_callback=self.book_view.refresh_book_list)
        self.ops_view.pack(fill="both", expand=True)

        self.stats_view = StatsView(self.tabview.tab("Statistiques"), self.library, self.file_manager)
        self.stats_view.pack(fill="both", expand=True)

    def on_closing(self):
        self.file_manager.save_library_data(self.library)
        self.destroy()




if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
