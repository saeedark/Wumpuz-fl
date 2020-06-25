#importing some files to make sure the python don't works with pointer when we don't want to
#tiiish
import copy


# logival and implemented by Hannaneh Habibi , Arshia Mashhadi , Ali Rahimi (PesarAmmehZa)


#todo Shortest path is not complete
#i feel something
# don't shot body

inWorld = [ [['s']       ,[]                     ,['b']        , ['p'] ]
            ,[['w']       ,['g', 's' , 'b']      ,['p']         , ['b'] ]
            ,[['s']       ,[]                    ,['b']         , [] ]
            ,[ []         ,['b']                ,['p']         , ['b'] ]]

#save up code for input method

inWorld = [ [['b']       ,['s']                     ,['w']        , ['g'] ]
           ,[['p']       ,['b']                     ,['s','b']         , [] ]
           ,[['b']       ,['b']                    ,['p']         , ['b'] ]
           ,[ []         ,[]                   ,['b']         , [] ]]


inWorld = [[[],        ['b'],   ['p'],      ['b']],
            [[],      ['b'],    ['b'],      ['g']],
            [['b'],   ['p'],    ['s', 'b'], []],
                [[], ['s', 'b'], ['w'],     ['s']]]

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
    probWumpuz = 0
    probpits = 0

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

def haveWumpuz(x):
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

#change next step by hand for fuck the entir AI and test in way that we all want to see
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
probpitsls = {}
probWumpuzls = {}
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
else:
    wrld[3][0].breez = -1

if haveSmell(inWorld[3][0]) :
    wrld[3][0].smell = 1
else:
    wrld[3][0].smell = -1
wrld[3][0].wumpuz = -1
wrld[3][0].pit = -1



while(not doneGold):
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
        if havePit(placestate):
            print("This fucking place have pit and our AI is just a loser")
            break # brak while
        else:
            wrld[x][y].pit = -1
        if haveWumpuz(placestate):
            print("This fucking place have Wumpuz and our AI is just a loser")
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
                wrld[xx][yy].probpits += 1
                probpitsls[(xx,yy)] = wrld[xx][yy].probpits
                probdanger[(xx,yy)] = wrld[xx][yy].probpits + wrld[xx][yy].probWumpuz
                if wrld[xx][yy].probpits == 3 :
                    wrld[xx][yy].pit = 1
                    if (xx,yy) in probpitsls:
                        del probpitsls[(xx,yy)]
                if ((xx == 0 and yy == 3) or (x==3 and yy==3) or (xx == 3 and yy==0)and wrld[xx][yy].probpits == 2):
                    wrld[xx][yy].pit = 1

    if wrld[x][y].smell == 1 :
        for i in range(len(lst)):
            xx = lst[i][0]
            yy = lst[i][1]
            if wrld[xx][yy].safe == 0 and itsnew:
                wrld[xx][yy].probWumpuz += 1
                probWumpuzls[(xx,yy)] = wrld[xx][yy].probWumpuz
                probdanger[(xx,yy)] = wrld[xx][yy].probpits + wrld[xx][yy].probWumpuz
                if wrld[xx][yy].probWumpuz == 3 :
                    wrld[xx][yy].wumpuz = 1
                # if wrld[xx][yy].probWumpuz == 3 :
                #     wrld[xx][yy].wumpuz = 1
                if ((xx == 0 and yy == 3) or (x==3 and yy==3) or (xx == 3 and yy==0)and wrld[xx][yy].probWumpuz == 2):
                    wrld[xx][yy].wumpuz = 1

    # these next two if is added by arshia and is a significant boost in logic
    # a small notic can change lots of thing
    if wrld[x][y].smell == -1 :
        for i in range(len(lst)):
            xx = lst[i][0]
            yy = lst[i][1]
            wrld[xx][yy].wumpuz = -1
            if (xx,yy) in probWumpuzls:
                del probWumpuzls[(xx,yy)]

    if wrld[x][y].breez == -1:
        for i in range(len(lst)):
            xx = lst[i][0]
            yy = lst[i][1]
            wrld[xx][yy].pit = -1
            if (xx,yy) in probpitsls:
                del probpitsls[(xx,yy)]


    #this is our good luck if next if be always True
    if wrld[x][y].smell == -1 and wrld[x][y].breez == -1  :

        for i in range(len(lst)):

            xx = lst[i][0]
            yy = lst[i][1]
            wrld[xx][yy].safe = 1
            if wrld[xx][yy].visited == 0 :
                unvisitedSafe.add((xx,yy))



#Nextmove

    # this is where we really write our AI
    # but this isn't AI , it's only lots of if and for
    # for what ????
    # tell us

    print(" probpit is ", probpitsls)
    print(" probWumpuz is ", probWumpuzls)
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




    # We select the least probable if we don't have another good solution in our our damned Artifical Intelligence Mind
    # AAAHHhh

    minvalue = 100


    # for key in probpitsls:
    #     value = probpitsls[key]
    #     for e in been:
    #         if lenn(key,e):
    #             if value < minvalue :
    #                 minkey = key
    #                 minvalue = value
    # #print("min " ,minvalue)
    # del probpitsls[minkey]

# define danger instead of pit

    for key in probdanger:
        value = probdanger[key]
        for e in been:
            if lenn(key,e):
                if value < minvalue :
                    minkey = key
                    minvalue = value
    #print("min " ,minvalue)
    del probdanger[minkey]
    del probpitsls[minkey]

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
