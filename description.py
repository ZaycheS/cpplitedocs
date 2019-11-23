class Description:
    __detailed_desc = ''
    __brief_desc = ''
    keywords = list()

    def set_detailed_desc(self, detailed_desc):
        self.__detailed_desc = detailed_desc

    def set_brief_desc(self, brief_desc):
        self.__brief_desc = brief_desc

    def get_detailed_desc(self):
        return self.__detailed_desc

    def get_brief_desc(self):
        return self.__brief_desc

    def add_keyword(self, keyword):
        self.keywords.append(keyword)
