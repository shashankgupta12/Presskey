def dataProcessKeyPress(keyData):
    # remove backspace and the key for which it was used 
    for index, data in enumerate(keyData):
        if data.split('-')[1] == 'Key.backspace':
            # if the key pressed before backspace was a special symbol then remove the associated shift key also
            if keyData[index - 1].split('-')[1] in ["'@'", "'#'", "'$'", "'%'", "'*'", "'!'", "'^'", "'&'", "'('", "')'", "'<'", "'>'", "'?'", "':'", "'{'", "'{'"]:
                keyData = [j for i, j in enumerate(keyData) if i not in (index, index - 1, index - 2)]
            else:
                keyData = [j for i, j in enumerate(keyData) if i not in (index, index - 1)]
            keydata = dataProcessKeyPress(keyData)
            return keydata
    return keyData

def dataProcessKeyRelease(keyData):
    # remove backspace and the key for which it was used 
    for index, data in enumerate(keyData):
        if data.split('-')[1] == 'Key.backspace':
            if keyData[index - 1].split('-')[1] in ['Key.shift', 'Key.shift_r']:
                keyData = [j for i, j in enumerate(keyData) if i not in (index, index - 1, index - 2)]
            # sometimes the shift key is released before the special symbol and hence the key released before the backspace
            # is a number (or a special symbol sharing the same key); in this case the number along with shift preceeding it is
            # also removed but not the case where a number is preceeded by a shift key and the shift key is preceeded by a
            # special symbol
            elif keyData[index - 1].split('-')[1] in ["'1'", "'2'", "'3'", "'4'", "'5'", "'6'", "'7'", "'8'", "'9'", "'0'", "'-'", "'['", "']'", "';'", "','", "'.'", "'/'"] and keyData[index - 2].split('-')[1] in ['Key.shift', 'Key.shift_r'] and not keyData[index - 3].split('-')[1] in ["'@'", "'#'", "'$'", "'%'", "'*'", "'!'", "'^'", "'&'", "'('", "')'", "'<'", "'>'", "'?'", "':'", "'{'", "'{'"]:
                keyData = [j for i, j in enumerate(keyData) if i not in (index, index - 1, index - 2)]
            else:
                keyData = [j for i, j in enumerate(keyData) if i not in (index, index - 1)]
            keydata = dataProcessKeyRelease(keyData)
            return keydata
    return keyData

def removeExtraShift(keyPressData, keyReleaseData):
    shift = ['Key.shift', 'Key.shift_r']
    for index, data in enumerate(keyPressData):
        if data.split('-')[1] in shift and keyPressData[index - 1].split('-')[1] in shift:
            keyPressData = [j for i, j in enumerate(keyPressData) if not i == index - 1]
            keyReleaseData = [j for i, j in enumerate(keyReleaseData) if not i == index - 1]
            keyPressData, keyReleaseData = removeExtraShift(keyPressData, keyReleaseData)
            return (keyPressData, keyReleaseData)
    return (keyPressData, keyReleaseData)

def swapShift(keyPressData, keyReleaseData):
    shift = ['Key.shift', 'Key.shift_r']
    for index, data in enumerate(keyPressData):
        if data.split('-')[1] in shift and keyReleaseData[index].split('-')[1] not in shift and keyReleaseData[index + 1].split('-')[1] in shift:
            keyReleaseData[index], keyReleaseData[index + 1] = keyReleaseData[index + 1], keyReleaseData[index]
            keyPressData, keyReleaseData = swapShift(keyPressData, keyReleaseData)
            return (keyPressData, keyReleaseData)
    return (keyPressData, keyReleaseData)

def removeExtraKeys(keyData):
    for index, data in enumerate(keyData):
        # here it is very important to remove '-' because if it is not removed then upon timing extraction error occurs
        # because it splits the string on hyphon and entry number 2 is no longer an integer; and to remove a hyphon the 
        # entry which is to be removed is "'" because upon splitting on hyphon entry [1] is "'"
        if data.split('-')[1] in ["'", 'Key.down', 'Key.alt', 'Key.tab', 'Key.up', 'Key.right', 'Key.left', 'Key.num_lock']:
            keyData = [j for i, j in enumerate(keyData) if not i == index]
            keyData = removeExtraKeys(keyData)
            return keyData
    return keyData

def extractTimings(keyPressData,keyReleaseData):
    keyPressData = [int(data.split('-')[2]) for data in keyPressData]
    keyReleaseData = [int(data.split('-')[2]) for data in keyReleaseData]
    return (keyPressData, keyReleaseData)