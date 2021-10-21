from basstatpl.core.group import GroupedData
from basstatpl.core.simple import SimpleData

class Analysis:
    def __init__(self, data = None):
        if str(type(data)) == "<class 'list'>":
            if len(data) >= 30:
                self.als = GroupedData(data)
            elif len(data) < 30:
                self.als = SimpleData(data)

        elif str(type(data)) == "<class 'dict'>":
            ftype = str(type(list(data.keys())[0]))

            if ftype == "<class 'tuple'>":
                self.als = GroupedData(data)
            elif ftype == "<class 'int'>" or ftype == "<class 'float'>":
                if sum(list(data.values())) >= 30:
                    self.als = GroupedData(data)
                else:
                    self.als = SimpleData(data)