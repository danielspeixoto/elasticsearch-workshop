import xml.etree.ElementTree as ETree


class XMLRepository:
    POSTS = "Posts"

    def __init__(self, data_path):
        self.data_path = data_path
        self.paths = [self.POSTS]
        self.dict = {}
        questions = None
        for path in self.paths:
            content = self.retrieve(path)
            questions = self.question_xml_to_df(content)
        self.questions_repo = questions

    def question_xml_to_df(self, xml):
        def question():
            for event, row in xml:
                post = row.attrib
                if XMLRepository.is_question(post):
                    yield post
        return question

    def retrieve(self, path):
        return ETree.iterparse(self.data_path + "/" + path + ".xml")

    @staticmethod
    def is_question(question):
        return "ParentId" not in question

    def data(self):
        return self.questions_repo()
