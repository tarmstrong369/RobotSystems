import Maneuvers

man=Maneuvers
inp=1
print('Choose a Maneuver!  A is Back and Forth, B is Parallel Park to the Right, C is Parallel Park to the Left, and D is 3 Point Turn.')
print('Press any other key to stop!')
while not inp==0:
    inp=str(input())
    if inp in ['A','a']:
        print('Back and Forth')
        man.forward_backward()
    elif inp in ['B', 'b']:
        print('Parallel Park to the Right')
        man.Parallel_ParkR()
    elif inp in ['C', 'c']:
        print('Parallel Park to the Left')
        man.Parallel_ParkL()
    elif inp in ['D', 'd']:
        print('3 Point Turn')
        man.K_Turn()
    else:
        inp=0