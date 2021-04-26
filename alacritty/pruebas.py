with open('alacritty.yml','r') as file:
    data = file.read()

data = data.splitlines()
#print(data)

#X = [line for line in data if line.startswith('family')]
for i in data:
    if i.startswith('    family'):
        print( i )
        comentline = '#'+i
    
