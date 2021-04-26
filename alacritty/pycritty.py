#/bin/python3


def opacity(data,opacity):
    counterline = 0
    for line in data:
        
        if line.startswith('background_opacity'):
            data[counterline] = 'background_opacity: '+opacity
            return data



def 

