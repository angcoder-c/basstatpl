from basstatpl.core.group import GroupedData
from basstatpl.core.simple import SimpleData

def analysis(data):
    if str(type(data)) == "<class 'list'>":
        if len(data) >= 30:
            return GroupedData(data)
        elif len(data) < 30:
            return SimpleData(data)
            
    elif str(type(data)) == "<class 'dict'>":
        ftype = str(type(list(data.keys())[0]))
        
        if ftype == "<class 'tuple'>":
            return GroupedData(data)
        elif ftype == "<class 'int'>" or ftype == "<class 'float'>":
            if sum(list(data.values())) >= 30:
                return GroupedData(data)
            else:
                return SimpleData(data)