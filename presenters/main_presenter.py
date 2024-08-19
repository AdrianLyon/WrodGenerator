class MainPresenter:
    def __init__(self, document_model):
        self.document_model = document_model
        self.view = None  # La vista se inicializará más tarde

    def create_view(self):
        # Importamos aquí para evitar el ciclo
        from views.main_view import MainView
        self.view = MainView(self)
        return self.view

    def on_load_document(self):
        file_path = self.view.ask_open_file([("Word Documents", "*.docx")])
        if file_path:
            self.document_model.load_document(file_path)
            self.view.set_save_enabled(True)
            self.view.set_generate_enabled(True)

    def on_save_document(self):
        data = self.view.get_form_data()
        success, errors = self.document_model.fill_form(data)
        if success:
            save_path = self.view.ask_save_path()
            if save_path:
                self.document_model.save_document(save_path)
                self.view.show_success("Document saved successfully!")
        else:
            self.view.show_warning("\n".join(errors))

    def on_generate_documents(self):
        excel_path = self.view.ask_open_file([("Excel Files", "*.xlsx")])
        if excel_path:
            documents = self.document_model.generate_documents_from_excel(excel_path)
            for index, doc in enumerate(documents):
                save_path = self.view.ask_save_path()
                if save_path:
                    doc.save(save_path)
            self.view.show_success("All documents generated successfully!")

    def run(self):
        if not self.view:  # Verificamos si la vista ya fue creada
            self.create_view()
        self.view.run()
