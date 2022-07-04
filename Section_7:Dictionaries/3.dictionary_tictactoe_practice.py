import pprint
theBoard = {'top-L':' ', 'top-M':' ', 'top-R':' ', 'mid-L':' ', 'mid-M':' ', 'mid-R':' ', 'low-L':' ', 'low-M':' ', 'low-R':' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)

#maybe make the full game later?  This is just an intro to using data structures. You can't actually play the game.