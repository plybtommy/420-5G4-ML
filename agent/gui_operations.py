import customtkinter as ctk

class OperationsView(ctk.CTkFrame):
    def __init__(self, master, library, refresh_callback=None):
        super().__init__(master)
        self.library = library
        self.refresh_callback = refresh_callback
        self.setup_ui()


    def setup_ui(self):
        self.label = ctk.CTkLabel(self, text="Opérations d'Emprunt", font=("Arial", 20))
        self.label.pack(pady=20)

        # Message area
        self.status_label = ctk.CTkLabel(self, text="", font=("Arial", 12), text_color="gray")
        self.status_label.pack(pady=5)

        # Section Emprunter
        self.borrow_frame = ctk.CTkFrame(self)
        self.borrow_frame.pack(pady=10, padx=20, fill="x")
        
        ctk.CTkLabel(self.borrow_frame, text="Emprunter un livre", font=("Arial", 14, "bold")).pack(pady=5)
        
        self.borrow_isbn = ctk.CTkEntry(self.borrow_frame, placeholder_text="ISBN du livre")
        self.borrow_isbn.pack(side="left", padx=5, pady=10, expand=True, fill="x")
        
        self.borrow_user_id = ctk.CTkEntry(self.borrow_frame, placeholder_text="ID Utilisateur")
        self.borrow_user_id.pack(side="left", padx=5, pady=10, expand=True, fill="x")
        
        self.btn_borrow = ctk.CTkButton(self.borrow_frame, text="Emprunter", command=self.borrow_book)
        self.btn_borrow.pack(side="left", padx=5, pady=10)

        # Section Retourner
        self.return_frame = ctk.CTkFrame(self)
        self.return_frame.pack(pady=10, padx=20, fill="x")
        
        ctk.CTkLabel(self.return_frame, text="Retourner un livre", font=("Arial", 14, "bold")).pack(pady=5)
        
        self.return_isbn = ctk.CTkEntry(self.return_frame, placeholder_text="ISBN du livre")
        self.return_isbn.pack(side="left", padx=5, pady=10, expand=True, fill="x")
        
        self.btn_return = ctk.CTkButton(self.return_frame, text="Retourner", fg_color="green", hover_color="darkgreen", command=self.return_book)
        self.btn_return.pack(side="left", padx=5, pady=10)

    def show_message(self, text, is_error=False):
        color = "red" if is_error else "green"
        self.status_label.configure(text=text, text_color=color)
        self.after(3000, lambda: self.status_label.configure(text=""))

    def borrow_book(self):
        isbn = self.borrow_isbn.get()
        user_id = self.borrow_user_id.get()
        if isbn and user_id:
            if self.library.check_out_book(isbn, user_id):
                self.borrow_isbn.delete(0, 'end')
                self.borrow_user_id.delete(0, 'end')
                if self.refresh_callback:
                    self.refresh_callback()
                self.show_message(f"Livre {isbn} emprunté par {user_id}")
            else:
                self.show_message("Erreur : Emprunt impossible (livre indisponible ou ID invalide)", True)
        else:
            self.show_message("Erreur : Veuillez remplir tous les champs", True)


    def return_book(self):
        isbn = self.return_isbn.get()
        if isbn:
            if self.library.return_book(isbn):
                self.return_isbn.delete(0, 'end')
                if self.refresh_callback:
                    self.refresh_callback()
                self.show_message(f"Livre {isbn} retourné avec succès")
            else:
                self.show_message("Erreur : Retour impossible (livre non trouvé ou non emprunté)", True)
        else:
            self.show_message("Erreur : Veuillez saisir un ISBN", True)

