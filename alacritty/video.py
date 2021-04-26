import argparse #llibreria de arguments
from pathlib import Path #llibreria de paths
from sys import stderr #importa standart error

#definicuio de la classe error
class MyError(Exception):
    pass




def copy(src,destination):
    print(src.absolute(),destination.absolute())

def cli():
    parser = argparse.ArgumentParser(
        prog = 'video',
        description= 'video tutorial practice'
    )
    parser.add_argument(
        '-o','--override',
        help = 'optional parameter'
    )
    parser.add_argument(
        'source',
        type= Path,#fa que l'argument sigui un path 
        help= 'missatge de ajuda de source'
    )
    parser.add_argument(
        'destination',
        type= Path,#fa que l'argument sigui un path 
        help= 'missatge de ajuda de destination'
    )

    return parser.parse_args()
    #retorna els arguments que li hem passat


def main ():
    args = cli()
    #copy(args.source,args.destination)
    print(args)


if __name__ == '__main__':
    main()
