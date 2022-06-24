print('Please, I am very bored! Just say anything to me, anything at all. At least I will have something to think about.')
Thing = input()
if Thing: #it would be better to put something like: if Thing != ' ':, but for the sake of showing truthy and falsey it is this.
    print('Thank you! This has given me life again, retrieved me from the depths of boredom. Just any simple thought is enough for me to feel alive again.')
else:
    print('You did not enter anything... I guess I must suffer alone for eternity. :(')