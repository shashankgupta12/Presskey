def dataProcess(keyData):
    # remove backspace and the key for which it was used 
    # print(keyData) 
    for index, data in enumerate(keyData):
        if data.split('-')[1] == 'Key.backspace':
            keyData = [j for i, j in enumerate(keyData) if i not in (index, index - 1)]
            #can use del keyData[index] and del keyData[index - 1] 
            keydata = dataProcess(keyData)
            return keydata
    return keyData

def extractTimings(keyPressData,keyReleaseData):
    keyPressData = [int(data.split('-')[2]) for data in keyPressData]
    keyReleaseData = [int(data.split('-')[2]) for data in keyReleaseData]
    return (keyPressData, keyReleaseData)