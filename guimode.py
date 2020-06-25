#importing some files to make sure the python don't works with pointer when we don't want to
#tiiish
import copy
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))


# logival and implemented by Hannaneh Habibi , Arshia Mashhadi , Ali Rahimi (PesarAmmehZa)


#todo Shortest path is not complete
#i feel something
# don't shot body

# inWorld = [ [['s']       ,[]                     ,['b']        , ['p'] ]
#             ,[['w']       ,['g', 's' , 'b']      ,['p']         , ['b'] ]
#             ,[['s']       ,[]                    ,['b']         , [] ]
#             ,[ []         ,['b']                ,['p']         , ['b'] ]]

#save up code for input method

inWorld = [ [['b']       ,['s']                     ,['w']        , ['s','g'] ]
           ,[['p']       ,['b']                     ,['s','b']         , [] ]
           ,[['b']       ,['b']                    ,['p']         , ['b'] ]
           ,[ []         ,[]                   ,['b']         , [] ]]

# inWorld =[[[], [], [], ['b']],
# [[], [], ['s', 'b', 'g'], ['p']],
# [[], ['s', 'b'], ['w'], ['s', 'b']],
# [['b'], ['p'], ['s', 'b'], []]]

# inWorld = [[[], ['b', 'b'], ['s', 'p'], ['b']],
# [['b'], ['s', 'p'], ['w', 'b', 'b'], ['s','g']],
# [[], ['b'], ['s'], []],
# [[], [], [], []]]


inWorld = [ [ []       ,['b']                    ,['s']         , ['g'] ]
        ,[ ['b']       ,['p','s']                    ,['w','b']         , ['s'] ]
           ,[ []       ,['b']                    ,['b','s']         , [] ]
           ,[ []       ,['b']                    ,['p']         , ['b'] ]]

# we are inworld[3][0] aren't we ? okay we don't have any plan for that

doneGold = False # It's all about money


#
class bs(): # so this for every block state
    visited = False
    safe = 0   # -1 danger 0 unknown 1 safe
    breez = 0  # -1 not 0 unkown 1 have
    wumpuz = 0 #
    smell = 0
    pit = 0
    probwumpuz = 0
    probpit = 0

# some redundent def for the bad input we select
def haveBreez(x):
    if 'b' in x:
        return True
    False

def haveSmell(x):
    if 's' in x:
        return True
    False

def haveGold(x):
    if 'g' in x:
        return True
    False

def havePit(x):
    if 'p' in x:
        return True
    False

def havewumpuz(x):
    if 'w' in x:
        return True
    False


# neighbor of a block which is in board game
# let's be logical then
def neighbours(cor):
    x = cor[0]
    y = cor[1]
    lst = [(x+1,y) , (x-1,y) , (x,y+1) ,(x,y-1)]
    tmp = []
    for i in range(len(lst)):
        if (lst[i][0] > -1 and lst[i][0] < 4):
            if (lst[i][1] > -1 and lst[i][1] < 4):
                tmp.append(lst[i])
    return tmp

# feel the distance , bring us closer
def lenn(a, b):
    dx = a[0] - b[0]
    dy = a[1] - a[1]

    return abs(dx) + abs(dy)

#change next step by hand for hug the entir AI and test in way that we all want to see
def wanttogo(newx,newy):
    #print()
    innp = input("Want to go " + str(newx) + " " + str(newy) + " Plz enter coordination")
    if innp == "" :
        return newx , newy
    a , b = map(int,innp.split())
    return a , b


#solving Shortest path problem for this Question is an extra work we hope you notice the time we thing on this.
def shortestPath(wwr , www , wwwb): # where we are , where we were , where we wanna be :))))))))
    #print(wwr,www,wwwb)
    #print(www)
    ways = [[wwr]]

    while(True):

        tmp = copy.deepcopy(ways)
        for i in range(len(tmp)):
            last =  tmp[i]
            possiblenext = neighbours(last[-1])
            for j in range(len(possiblenext)):
                if possiblenext[j] in www or (possiblenext[j][0] == wwwb[0] and possiblenext[j][1] == wwwb[1]):
                    x = copy.deepcopy(last)
                    x.append(possiblenext[j])
                    if possiblenext[j][0] == wwwb[0] and possiblenext[j][1] == wwwb[1]:
                        return x[1:len(x)-1]
                    tmp.append(x)
        ways  = tmp
    # returnlist = []
    # for i in ways:
    #
    #     if i[-1][0] == wwwb[0] and i[-1][1]:
    #         returnlist.append(i)
    #
    # maxlen = 100
    # returnway = []
    # for i in range(returnlist):
    #     if len(i) < maxlen:
    #         returnway = i
    print("??? ina")
    return False


#working lists
# this list is in our Artifical Mind
#so respect them
# they matters very to us

wrld = []
been = {(3,0)}
probpitls = {}
probwumpuzls = {}
probdanger = {}
unvisitedSafe = set()

#location = (3, 0 ,1) # 2 for up , 3 for left ,4  for down ,1  for right
location = [3, 0]

# making our knowing world to work with in our Mind
# the AI don't know nothing about the realitty
# it's all probability which leads us to our goal
# why there is always goal
# need a game without goal , withous score
#nothing
# I Mean Hich
for i in range(4):
    tmp = []
    for j in range(4):
         a = bs()
         tmp.append(a)
    wrld.append(tmp)


#initialising our place ;)))
wrld[3][0].visited = True
wrld[3][0].safe = 1
if haveBreez(inWorld[3][0]) :
    wrld[3][0].breez = 1
    wrld[3][1].probpit += 1
    wrld[2][0].probpit += 1
    if wrld[3][1].probpit > 0 :
        probpitls[(3,1)] = wrld[3][1].probpit
    if wrld[2][0].probpit > 0 :
        probpitls[(2,0)] = wrld[2][0].probpit
else:
    wrld[3][0].breez = -1

if haveSmell(inWorld[3][0]) :
    wrld[3][0].smell = 1
    wrld[3][1].probwumpuz +=1
    wrld[2][0].probwumpuz +=1
    if (wrld[3][1].probwumpuz > 0):
        probwumpuzls[(3,1)] = wrld[3][1].probwumpuz
    if (wrld[2][0].probwumpuz > 0):
        probwumpuzls[(2,0)] = wrld[2][0].probwumpuz
else:
    wrld[3][0].smell = -1
wrld[3][0].wumpuz = -1
wrld[3][0].pit = -1

if wrld[2][0].probpit + wrld[2][0].probwumpuz > 0 :
    probdanger[(2,0)] = wrld[2][0].probpit + wrld[2][0].probwumpuz
if wrld[3][1].probpit + wrld[3][1].probwumpuz > 0 :
    probdanger[(3,1)] = wrld[3][1].probpit + wrld[3][1].probwumpuz

while(not doneGold):
    #print(inWorld)
    # make gui dadadadda
    # w = 200
    # h = 200
    # for a in range (4):
    #     for b in range(4):
    #         i = b
    #         j = a
    #         back = (95,95,100)
    #         if wrld[a][b].safe == 1 :
    #             back = (73,22,88) # green
    #         if wrld[a][b].visited == 1 :
    #             back = (38,115,215) #blue
    #         if wrld[a][b].pit ==1 :
    #             back = (3,3,3) #black
    #         if wrld[a][b].wumpuz ==1 :
    #             back = (252,6,6) #red
    #         pygame.draw.rect(screen, back, pygame.Rect(i*w+1+i, j*h+1+j, w, h))
    #
    #         if wrld[a][b].breez == 1:
    #             pygame.draw.circle(screen,(255,255,255),(i*w+1+i + 30 ,j*h+1+j + 30 ),15)
    #
    #         if wrld[a][b].breez == 1:
    #             pygame.draw.circle(screen,(233,140,32),(i*w+1+i + 30 ,j*h+1+j + 170 ),15)
    #
    # j =location[0]
    # i =location[1]
    # pygame.draw.circle(screen,(233,140,32),(i*w+1+i + 100 ,j*h+1+j + 100 ),70)
    #
    #
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         done = True
    # pygame.display.flip()
    #print(" been is with current location ", been)


    # so this place seems cozy , let's check it
    print(" Where we are is " , end="")
    x = location[0]
    y = location[1]
    tt = [x,y]
    print(tt)

    itsnew = False
    placestate = inWorld[x][y]
    if (wrld[x][y].visited == 0):
        itsnew = True
        if havePit(placestate) and wrld[x][y].safe != 1:
            print("This huging place have pit and our AI is just a loser")
            break # brak while
        else:
            wrld[x][y].pit = -1
        if havewumpuz(placestate) and wrld[x][y].safe != 1:
            print(wrld[x][y].safe )
            print(x,y)
            print("This huging place have wumpuz and our AI is just a loser")
            break # break while
        else:
            wrld[x][y].wumpuz = -1
        wrld[x][y].safe = 1
        if haveGold(placestate):
            print("Yeah! We are the Winner")
            break
        if haveSmell(placestate):
            wrld[x][y].smell = 1
        else:
            wrld[x][y].smell = -1
        if haveBreez(placestate):
            wrld[x][y].breez = 1
        else:
            wrld[x][y].breez = -1
    wrld[x][y].visited = 1
    wrld[x][y].safe = 1

    #modifing mode
    lst = neighbours([x,y])

    # we are going to know sth that's matters
    # And if love is just a fleeting whim
    # then why is it you never dimmed away

    if wrld[x][y].breez == 1 :
         for i in range(len(lst)):
            xx = lst[i][0]
            yy = lst[i][1]
            if wrld[xx][yy].safe == 0 and itsnew:
                wrld[xx][yy].probpit += 1
                probpitls[(xx,yy)] = wrld[xx][yy].probpit
                probdanger[(xx,yy)] = wrld[xx][yy].probpit + wrld[xx][yy].probwumpuz
                if wrld[xx][yy].probpit == 3 :
                    wrld[xx][yy].pit = 1
                    if (xx,yy) in probpitls:
                        del probpitls[(xx,yy)]
                        del probdanger[(xx,yy)]
                if (((xx == 0 and yy == 3) or (x==3 and yy==3) or (xx == 3 and yy==0))and wrld[xx][yy].probpit == 2):
                    wrld[xx][yy].pit = 1

    if wrld[x][y].smell == 1 :
        for i in range(len(lst)):
            xx = lst[i][0]
            yy = lst[i][1]
            if wrld[xx][yy].safe == 0 and itsnew:
                wrld[xx][yy].probwumpuz += 1
                probwumpuzls[(xx,yy)] = wrld[xx][yy].probwumpuz
                probdanger[(xx,yy)] = wrld[xx][yy].probpit + wrld[xx][yy].probwumpuz
                if wrld[xx][yy].probwumpuz == 3 :
                    wrld[xx][yy].wumpuz = 1
                    wrld[xx][yy].safe = 1
                    unvisitedSafe.add((xx,yy))
                    probwumpuzls = {}
                # if wrld[xx][yy].probwumpuz == 3 :
                #     wrld[xx][yy].wumpuz = 1
                if (((xx == 0 and yy == 3) or (x==3 and yy==3) or (xx == 3 and yy==0))and wrld[xx][yy].probwumpuz == 2):
                    wrld[xx][yy].safe = 1
                    wrld[xx][yy].wumpuz = 1
                    unvisitedSafe.add((xx,yy))
                    probwumpuzls = {}

    # these next two if is added by arshia and is a significant boost in logic
    # a small notic can change lots of thing
    if wrld[x][y].smell == -1 :
        for i in range(len(lst)):
            xx = lst[i][0]
            yy = lst[i][1]
            wrld[xx][yy].wumpuz = -1
            if (xx,yy) in probwumpuzls:
                del probwumpuzls[(xx,yy)]

    if wrld[x][y].breez == -1:
        for i in range(len(lst)):
            xx = lst[i][0]
            yy = lst[i][1]
            wrld[xx][yy].pit = -1
            if (xx,yy) in probpitls:
                probdanger[(xx,yy)] -= probpitls[(xx,yy)]
                if probdanger[(xx,yy)] == 0:
                    del probdanger[(xx,yy)]
                del probpitls[(xx,yy)]


    #this is our good luck if next if be always True
    if wrld[x][y].smell == -1 and wrld[x][y].breez == -1  :

        for i in range(len(lst)):

            xx = lst[i][0]
            yy = lst[i][1]
            wrld[xx][yy].safe = 1
            if wrld[xx][yy].visited == 0 :
                unvisitedSafe.add((xx,yy))



#Nextmove



    # the py game drw mode with bad type which is causing us leave our mind from arrow to shot the loved Wumpus
    w = 200
    h = 200
    for a in range (4):
        for b in range(4):
            i = b
            j = a
            back = (95,95,100) #gray
            if wrld[a][b].probpit > 0 or wrld[a][b].probwumpuz >0 :
                back = (250,150 - (wrld[a][b].probwumpuz + wrld[a][b].probpit)*30,150 - (wrld[a][b].probwumpuz + wrld[a][b].probpit)*30)
            if wrld[a][b].safe == 1 :
                back = (38,188,143) # green
            if wrld[a][b].visited == 1 :
                back = (38,115,215) #blue
            if wrld[a][b].pit ==1 :
                back = (3,3,3) #black
            if wrld[a][b].wumpuz ==1 :
                back = (252,6,6) #red
            pygame.draw.rect(screen, back, pygame.Rect(i*w+1+i, j*h+1+j, w, h))

            if wrld[a][b].breez == 1:
                pygame.draw.circle(screen,(255,255,255),(i*w+1+i + 30 ,j*h+1+j + 30 ),15)

            if wrld[a][b].smell == 1:
                pygame.draw.circle(screen,(233,140,32),(i*w+1+i + 30 ,j*h+1+j + 170 ),15)


    j =location[0]
    i =location[1]
    pygame.draw.circle(screen,(113,38,188),(i*w+1+i + 100 ,j*h+1+j + 100 ),70)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()

        # this is where we really write our AI
        # but this isn't AI , it's only lots of if and for
        # for what ????
        # tell us


    print(" probpit is ", probpitls)
    print(" probwumpuz is ", probwumpuzls)
    print(" probDanger is ", probdanger)
    input()
    if len(unvisitedSafe) > 0:

        ttt = unvisitedSafe.pop()
        newx = ttt[0]  # Selecting randow but guess the shortest path
        newy = ttt[1]
        waystomove = shortestPath((location[0],location[1]),been,(newx,newy))
        if len(waystomove) > 0:
            print("this" , end="")
            print(waystomove)
        newx , newy = wanttogo(newx,newy)
        location[0] = newx
        location[1] = newy
        been.add((newx,newy))

        continue

    allpodiibleneighbour = []
    for i in been:
        neighbortmp = neighbours(i)
        for i in neighbortmp:
            if i not in allpodiibleneighbour:
                if wrld[i[0]][i[1]].wumpuz == -1 and wrld[i[0]][i[1]].pit == -1 and wrld[i[0]][i[1]].visited == False:
                    allpodiibleneighbour.append(i)

    if len(allpodiibleneighbour) > 0 :
        print(allpodiibleneighbour , " Why neighbour")
        ttt = allpodiibleneighbour[0]
        newx = ttt[0]  # Selecting randow but guess the shortest path
        newy = ttt[1]
        waystomove = shortestPath((location[0],location[1]),been,(newx,newy))
        if len(waystomove) > 0:
            print(waystomove)
        newx , newy = wanttogo(newx,newy)
        location[0] = newx
        location[1] = newy
        been.add((newx,newy))
        continue

    # at this place we must decide that if we can shot or not ?

    numberof2 = 0
    keylist = []
    for key in  probwumpuzls :
        if probwumpuzls[key] == 2:
            numberof2 +=1
            keylist.append(key)


    if numberof2 == 2: # must select random but let's not do that
        select = keylist[0] # for killliiing
        if havewumpuz(inWorld[select[0]][select[1]]) == 'w' :
            inWorld[select[0]][select[1]].remove('w')
            print("yeah we killed Wupus succesfully")
            for key in probdanger :
                probdanger[key] -= probwumpuz[key]
                if probdanger[key] == 0 :
                    del probdanger[key]
            probwumpuz = {}
            wrld[select[0]][select[1]].safe == 1
        else:
            select1 = keylist[1]
            havewumpuz(inWorld[select1[0]][select1[1]]) != 'w'
            wrld[select1[0]][select1[1]].safe == 1
            wrld[keylist[0][0]][keylist[0][1]].probwumpuz = 4
            wrld[keylist[0][0]][keylist[0][1]].wumpuz = 1
    # elif (numberof2 ==1 ):
    #     select = keylist[0]
    #     print(select)
    #     if havewumpuz(inWorld[select[0]][select[1]]) :
    #         print("yeah we killed Wupus succesfully")
    #         inWorld[select[0]][select[1]].remove('w')
    #
    #         neitmp = neighbours(select)
    #         for i in neitmp:
    #             wrld[i[0]][i[1]].smell = 0
    #             wrld[i[0]][i[1]].probwumpuz = 0
    #             inWorld[i[0]][i[1]].remove('s')
    #             if (wrld[i[0]][i[1]].probwumpuz == 0 and wrld[i[0]][i[1]].probpit == 0):
    #                 unvisitedSafe.add((i[0],i[1]))
    #
    #         for key in probwumpuzls :
    #             probdanger[key] -= probwumpuzls[key]
    #             if probdanger[key] == 0 :
    #                 del probdanger[key]
    #         probwumpuzls = {}
    #         wrld[select[0]][select[1]].safe == 1
    #         unvisitedSafe.add((select[0],select[1]))
    #
    #         location[0] = select[0]
    #         location[1] = select[1]
    #         been.add((newx,newy))
    #         continue
    #     else:
    #         print("we have lost our chanse")

    # We select the least probable if we don't have another good solution in our our loved Artifical Intelligence Mind
    # AAAHHhh

    minvalue = 100


    # for key in probpitls:
    #     value = probpitls[key]
    #     for e in been:
    #         if lenn(key,e):
    #             if value < minvalue :
    #                 minkey = key
    #                 minvalue = value
    # #print("min " ,minvalue)
    # del probpitls[minkey]

# define danger instead of pit
    minset = False
    for key in probdanger:
        value = probdanger[key]
        for e in been:
            if lenn(key,e):
                if value < minvalue :
                    minkey = key
                    minset = True
                    minvalue = value

    #print("min " ,minvalue)
    if minset and (len(probdanger) > 0):
        tmp = copy.deepcopy(minkey)
        for key, value in probdanger.items():
            if key == minkey:
                del probdanger[minkey]
                break
        for key, value in probpitls.items():
            if key == minkey:
                del probpitls[minkey]
                break

    newx = minkey[0]  # Selecting randow but guess the shortest path
    newy = minkey[1]
    waystomove = shortestPath((location[0],location[1]),been,(newx,newy))
    if len(waystomove) > 0:
        print(waystomove)
    newx , newy = wanttogo(newx,newy)
    location[0] = newx
    location[1] = newy
    been.add((newx,newy))

#this is the end line
