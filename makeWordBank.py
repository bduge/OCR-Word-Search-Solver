def toBank(array):
    grid = []
    
    length = array.index('\n')
    grid.append(array[:length])
    array = array[length:]
    
    while array:
        array = array[1:]
        try:
            length = array.index('\n')
            grid.append(array[:length])
            array = array[length:]
        except:
            grid.append(array[0:])
            array = []
    
    bank = []

    for word in grid:
        bank.append(''.join(word))

    return bank



    



  