def fdump(smth, mode="a"):
    with open("C:/Users/Anuar/Desktop/debug.txt", mode=mode) as file:
        dumpstr = dump(smth, True)
        print(dumpstr, file=file)


def dump(smth, returnResult = False, spaceCount=4, useStr=True):    
    NL = "\n"
    DELIM = " => "

    def atomicToStr(smth):
        if isinstance(smth, str):
            return "'"+smth+"'"
        else:
            return str(smth)

    def main(node, level):
        def pieceDict(data):
            if len(data)==0: return "{}"
            piece = ""
            piece+=NL+shift+"{"
            for index, item in data.items():
                piece+=(NL + (shift + indent) + atomicToStr(index) + DELIM)                
                piece+=main(item, level + 1)
            piece+=(NL + shift + "}")
            return piece
    
        def pieceList(data):
            if len(data)==0: return "[]"
            piece = ""
            piece+=NL+shift+"["
            for index, item in enumerate(data):
                piece+=(NL + (shift + indent) + atomicToStr(index) + DELIM)                
                piece+=main(item, level + 1)
            piece+=(NL + shift + "]")
            return piece

        def pieceTuple(data):
            if len(data)==0: return "()"
            piece = ""
            piece+=NL+shift+"("
            for index, item in enumerate(data):
                piece+=(NL + (shift + indent) + atomicToStr(index) + DELIM)                
                piece+=main(item, level + 1)
            piece+=(NL + shift + ")")
            return piece
            

        shift = " " * spaceCount * (level)
        indent = " " * spaceCount
        ret = ""

        if (useStr and type(node).__str__ is not object.__str__):
            ret+=str(node)
        elif isinstance(node, dict):
            ret+=pieceDict(node)
        elif hasattr(node, '__dict__'):
            ret+=pieceDict(vars(node))
        elif isinstance(node, list):
            ret+=pieceList(node)
        elif isinstance(node, tuple):
            ret+=pieceTuple(node)
        else:
            strnode = atomicToStr(node)
            if '\n' in strnode :  strnode = NL + shift + strnode.replace('\n', NL+shift)             
            ret+=strnode
        return ret


    result = main(smth, 0).strip()
    if returnResult==True: 
        return result
    else: 
        print(result)
        return None
    