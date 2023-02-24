class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        st_category = self.__find_category_by_id(category.id)

        if st_category is None:
            self.categories.append(category)

    def __find_category_by_id(self, category_id):
        for cat in self.categories:
            if cat.id == category_id:
                return cat


    def add_topic(self, topic):
        st_topic = self.__find_topic_by_id(topic.id)

        if st_topic is None:
            self.topics.append(topic)

    def __find_topic_by_id(self, topic_id):
        for top in self.topics:
            if top.id == topic_id:
                return top


    def add_document(self, document):
        st_docs = self.get_document(document.id)

        if st_docs is None:
            self.documents.append(document)

    def get_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                return doc


    def edit_category(self,category_id: int, new_name:str):
        categ = self.__find_category_by_id(category_id)
        categ.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        top = self.__find_topic_by_id(topic_id)
        top.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        docc = self.get_document(document_id)
        docc.edit(new_file_name)


    def delete_category(self, category_id):
        categ = self.__find_category_by_id(category_id)
        self.categories.remove(categ)

    def delete_topic(self, topic_id):
        topp = self.__find_topic_by_id(topic_id)
        self.topics.remove(topp)

    def delete_document(self, document_id):
        docc = self.get_document(document_id)
        self.documents.remove(docc)

    def __repr__(self):
        return '\n'.join([str(x) for x in self.documents])
                        # може и repr(x)

