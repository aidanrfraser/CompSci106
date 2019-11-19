from cisc106 import assertEqual
def find(world):
    """
    Finds chomper in the world
    """
    if world[0] == 'V':
        return 0
    elif world[0] == '>':
        return 0
    elif world[0] == '<':
        return 0
    else:
        return 1 + find(world[1:])
def lookright(world):
    """
    Looks right for food
    """
    if not world:
        return False
    else:
        if world[0] == '1':
            return True
        else:
            return lookright(world[1:])
def lookleft(world):
    """
    Looks left for food
    """
    if world[0] == 'V':
        return False
    if world[0] == '>':
        return False
    else:
        if world[0] == '1':
            return True
        else:
            return lookleft(world[1:])
def replace(want, replacer, world):
    """
    Replaces a number in a string
    """
    if not world:
        return world
    else:
        if world[0] == want:
            return replacer + world[1:]
        else:
            return world[0:1] + replace(want, replacer, world[1:])
def moveleft(world):
    """
    Moves chomper left
    """
    return world[0:(find(world) - 2)] + '> 0' + world[(find(world) + 1):]
def moveright(world):
    """
    Moves chomper right
    """
    return world[0:find(world)] + '0 <' + world[(find(world) + 3):]
def chomperhelper(world, state):
    """
    Helps chomper move around
    """
    if state == '>':
        if lookleft(world):
            world = moveleft(world)
            print(world)
            return chomperhelper(world, '>')
        else:
            print(world)
            return chomperhelper(world, '<')
    elif state == '<':
        if lookright(world):
            world = moveright(world)
            print (world)
            return chomperhelper(world, '<')
        else:
            world = replace('<', 'V', world)
            chomper(world)
def chomper(world):
    """
    base function for chomper
    """
    print(world)
    if lookleft(world):
        return chomperhelper(replace('V', '>', world), '>')
    elif lookright(world):
        return chomperhelper(replace('V', '<', world), '<')
    else:
        print('Done!')
#tests
assertEqual(replace('V','>','V'), '>')
assertEqual(replace('V','>','V 0 0'), '> 0 0')
assertEqual(lookright('V 1'), True)
assertEqual(lookright('V'), False)
assertEqual(lookright('V 0 0 1'), True)
assertEqual(find('V'), 0)
assertEqual(find('>'), 0)
assertEqual(find('<'), 0)
assertEqual(find('0 0 V'), 4)
assertEqual(lookleft('1 0'), True)
assertEqual(lookleft('0 1'), True)
assertEqual(lookleft('V'), False)
assertEqual(lookleft('0 0 0 0 0 V'), False)
assertEqual(lookleft('> 0 0 0 0 0 1'), False)