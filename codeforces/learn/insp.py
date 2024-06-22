import calendar


def Bitplus():
    n = int(input())
    x = 0
    for i in range(n):
        a = input()
        if "+" in a:
            x += 1
        else:
            x -= 1
    print(x)

def GiftSetidk():
    n = int(input())
    for i in range(n):
        all = input().split(" ")
        x = int(all[0])
        y = int(all[1])
        a = int(all[2])
        b = int(all[3])
        counter = 0
        count = True
        while count:
            if x >= a and y >= b:
                x -= a
                y -= b
                counter += 1
            elif x >= b and y >= a:
                x -= b
                y -= a
                counter += 1
            else:
                count = False
        print(counter)


def Team():
    n = int(input())
    problemcount = 0
    for i in range(n):
        count = 0
        answer = input().split(" ")
        for i in range(len(answer)):
            answer[i] = int(answer[i])
        for i in answer:
            if i == 1:
                count += 1
        if count >= 2:
            problemcount += 1
    print(problemcount)

def NextRound():
    nk = input().split(" ")
    n = int(nk[0])
    k = int(nk[1])
    print(n, k)
    scores = input().split(" ")
    count = 0
    for i in range(n):
        scores[i] = int(scores[i])
    five = scores[k]
    for i in range(n):
        if scores[i] >= five and scores[i] > 0:
            count += 1
    print(count)


def Beautifulmatrix():
    steps = 0
    matrixes = []
    for i in range(5):
        i = [input().split(" ")]
        matrixes += i
    for i in range(5):
        for j in range(5):
            matrixes[i][j] = int(matrixes[i][j])
    for i in range(5):
        for j in range(5):
            if matrixes[i][j] > 0:
                x = j
                y = i
                break
    while x != 2 or y != 2:
        if x > 2:
            x -= 1
            steps += 1
        elif x < 2:
            x += 1
            steps += 1
        elif y > 2:
            y -= 1
            steps += 1
        elif y < 2:
            y += 1
            steps += 1
    print(steps)


def HelpfulMahts():
    s = input().split("+")
    s.sort()
    print("+".join(s))

def WordCapitalization():
    word = input()
    List = []
    for i in word:
        List.append(i)
    List[0] = List[0].upper()
    s = ""
    for i in List:
        s += i
    print(s)

def Stonesonthetable():
    n = int(input())
    stones = []
    rrg = input()
    counter = 0
    for i in rrg:
        stones.append(i)
    for i in range(n - 1):
        if stones[i] == stones[i + 1]:
            counter += 1
    print(counter)

def BearandBigBrother():
    inpuut = input().split(" ")
    a = int(inpuut[0])
    b = int(inpuut[1])
    year = 0
    while a <= b:
        a *= 3
        b *= 2
        year += 1
    print(year)

def Wrongsubtraction():
    nk = input().split(" ")
    n = int(nk[0])
    k = int(nk[1])
    for i in range(k):
        p = str(n)
        if p[len(p) - 1] == "0":
            n //= 10
        else:
            n -= 1
    print(n)

import string
def Word():
    word = input()
    lower = 0
    upper = 0
    for i in word:
        if i in string.ascii_lowercase:
            lower += 1
        else:
            upper += 1
    if upper > lower:
        word = word.upper()
    else:
        word = word.lower()
    print(word)

def QueueattheSchool():
    nt = input().split(" ")
    n = nt[0]
    t = int(nt[1])
    a = input()
    b = []
    ref = ""
    for i in a:
        b.append(i)
    for k in range(t):
        whre = []
        for i in range(len(b) - 1):
            if b[i] == "B" and b[i + 1] != "B":
                whre.insert( 0,i)
        for j in whre:
            b.pop(j)
            b.insert(j + 1, "B")
    for i in b:
        ref += i
    print(ref)

def Nearlyluckynumber():
    n = input()
    if n.count("7") + n.count("4") == 7 or n.count("7") + n.count("4") == 4:
        print("YES")
    else:
        print("NO")


def Translation():
    s = input()
    t = input()
    n = []
    for i in t:
        n.insert(0, i)
    t = ""
    for i in n:
        t += i
    if t == s:
        print("YES")
    else:
        print("NO")

def ANTONandDanik():
    n = int(input())
    s = input()
    A = s.count("A")
    D = s.count("D")
    if A > D:
        print("Anton")
    elif D > A:
        print("Danik")
    else:
        print("Friendship")


def GeorgeandAccomodation():
    n = int(input())
    rooms = 0
    for i in range(n):
        pq = input().split(" ")
        p = int(pq[0])
        q = int(pq[1])
        if q - p >= 2:
            rooms += 1
    print(rooms)

def Magnets():
    n = int(input())
    Rows = []
    groups = 1
    for i in range(n):
        Rows += [input()]
    for i in range(n - 1):
        if Rows[i] != Rows[i + 1]:
            groups += 1
    print(groups)


def InSearcoanEasyProblem():
    n = int(input())
    counter = 0
    s = input().split(" ")
    if "1" in s:
        print("HARD")
    else:
        print("EASY")

def Hulk():
    c = int(input())
    i = "I"
    s = ""
    it = "it"
    for i in range(1, c + 1):
        if i == 1:
            s += "hate "
        elif i % 2 == 0:
            s += "that I love "
        else:
            s += "that I hate "
    print(f"I {s}it")

def CalculatingFunctionidk():
    n = int(input())
    c = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            c -= i
        else:
            c += i
    print(c)

def IWannaBetheGuyidk():
    n = int(input())
    p = input().split(" ")
    q = input().split(" ")
    counter = 0
    for i in range(1, n + 1):
        if str(i) in p or str(i) in q:
            counter += 1
    if counter == n:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")

def horsesheo():
    n = input().split(" ")
    many = 4
    whatwas = []
    for i in range(len(n)):
        n[i] = int(n[i])
        if n[i] not in whatwas:
            whatwas.append(n[i])
    print(many - len(whatwas))

def ArrivaloftheGeneralidk():
    n = int(input())
    a = input().split(" ")
    max = 0
    minlist = []
    for i in range(n):
        a[i] = int(a[i])
    for i in a:
        if i > max:
            max = i
    maxloc = a.index(max)
    for i in a:
        minlist.insert(0, i)
    min = max
    for i in a:
        if i < min:
          min = i
    minloc = minlist.index(min)
    print(minloc + maxloc)



def UltraFastMathematician():
    first = input()
    second = input()
    s = ""
    for i in range(len(first)):
        if first[i] == "0" and second[i] == "1":
            s += "1"
        elif first[i] == "1" and second[i] == "0":
            s += "1"
        elif first[i] == "0" and second[i] == "0":
            s += "0"
        elif first[i] == "1" and second[i] == "1":
            s += "0"
    print(s)

def Insomniacure():
    klmn = []
    for i in range(4):
        klmn.append(int(input()))
    d = int(input())
    List = []
    if 1 in klmn:
        return d
    for i in range(4):
        mulit = klmn[i]
        while klmn[i] <= d:
            if klmn[i] not in List:
                List.append(klmn[i])
            klmn[i] += mulit
    return len(List)


def AntonandLetters():
    first = input()
    List = []
    for i in first:
        if i not in List and i in string.ascii_lowercase:
            List.append(i)
    print(len(List))


def Pangram():
    n = int(input())
    word = input().lower()
    List = []
    if n >= 26:
        for i in word:
            if i not in List:
                List.append(i)
        if len(List) == 26:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


def Collectingcoons():
    n = int(input())
    for i in range(n):
        abcd = input().split(" ")
        for i in range(len(abcd)):
            abcd[i] = int(abcd[i])
        d = abcd[3]
        abcd.pop()
        maxi = 0
        for i in abcd:
            if i > maxi:
                maxi = i
        allindexes = [0, 1, 2]
        indexmax = abcd.index(maxi)
        allindexes.pop(indexmax)
        allminus = 0
        for i in allindexes:
            allminus += abcd[indexmax] - abcd[i]
        d -= allminus
        if d % 3 == 0 and d >= 0:
            print('YES')
        else:
            print("NO")


def Brainsphotos():
   nm = input().split(" ")
   colors = []
   for i in range(int(nm[0])):
       colors += input().split(" ")
   for i in colors:
       if i == 'C' or i == 'M' or i == 'Y':
           return "#Color"
   return "#Black&White"

def SerejaandDima():
    n = int(input())
    card = input().split(" ")
    S = 0
    D = 0
    sturn = True
    for i in range(n):
        if int(card[0]) > int(card[len(card) - 1]):
            if sturn:
                S += int(card[0])
                card.pop(0)
                sturn = False
            else:
                D += int(card[0])
                card.pop(0)
                sturn = True
        else:
            if sturn:
                S += int(card[len(card) - 1])
                card.pop(len(card) - 1)
                sturn = False
            else:
                D += int(card[len(card) - 1])
                card.pop(len(card) - 1)
                sturn = True
    print(f"{S} {D}")


def Vanyaandcubes():
    n = int(input())
    counter = 1
    countdodo = 0
    rows = 0
    while n > 0:
        countdodo += counter
        counter += 1
        rows += 1
        n -= countdodo
    if n == 0:
        print(rows)
    else:
        print(rows - 1)

def GennadyandaCarGame():
    card = input()
    cards = input().replace(" ", "")
    for i in card:
        for j in cards:
            if i == j:
                return "YES"
    return "NO"

def FafaandhisCompany():
    n = int(input())
    ways = 0
    for i in range(1, n):
        a = n
        a -= i
        if a%i == 0:
            ways += 1
    print(ways)

def Mahmoudandehabandtheevenoddgame():
    n = int(input())
    Mahmoudsturn = True
    Mahmoudlsot = False
    Ehablost = False
    a = 0
    while not Mahmoudlsot and not Ehablost:
        if Mahmoudsturn:
            if n%2 == 0 and n >= 2:
                Ehablost = True

            elif n%2 != 0 and n >= 2:
                a = n - 1
            else:
                Mahmoudlsot = True
        else:
            if n%2 == 1 and n >= 1:
                Mahmoudlsot = True
            elif n%2 == 0 and n >= 1:
                a = n - 1
            else:
                Ehablost = False
        n -= a
        if Mahmoudsturn == True:
            Mahmoudsturn = False
        else:
            Mahmoudsturn = True
    if Mahmoudlsot == True:
        print("Ehab")
    else:
        print("Mahmoud")


def FloorNumber():
    t = int(input())
    for i in range(t):
        nx = input().split(" ")
        n = int(nx[0])
        x = int(nx[1])
        aparteements = 2
        floor = 1
        while n > aparteements:
            aparteements += x
            floor += 1
        print(floor)


def VustheCossackandaContest():
    nmk = input().split(" ")
    n = int(nmk[0])
    m = int(nmk[1])
    k = int(nmk[2])
    if n <= m and n <= k:
        print("Yes")
    else:
        print("No")

def NightattheMuseum():
    word = input()
    rotations = 0
    lower = string.ascii_lowercase + string.ascii_lowercase + string.ascii_lowercase
    loc = lower.index("a", 26, 2 * 26)

    for i in word:
       cplus = loc
       cminus = loc
       keep = True
       while keep:
           if i == lower[cplus] or i == lower[cminus]:
               keep = False
           else:
               cplus += 1
               cminus -= 1
               rotations += 1
               loc = lower.index(i, 26, 2 * 26)
    print(rotations)


def OrdinarYnumbers():
    n = int(input())
    for i in range(n):
        k = int(input())
        counter = 0
        for j in range(1, k + 1):
            a = str(j)
            if len(a) == a.count(a[0]):
                counter += 1
        print(counter)


def DieRoll():
    n = input().split(" ")
    y = int(n[0])
    w = int(n[1])
    number = 0
    dec = 6
    if y >= w:
        for i in range(y, 7):
            number += 1
    else:
        for i in range(w, 7):
            number += 1
    if number%6 == 0:
        number = number // 6
        dec = 1
    elif number%3 == 0:
        number = number//3
        dec = 2
    elif number%2 == 0:
        number = number // 2
        dec = 3
    print(f"{number}/{dec}")

def Borze():
    n = input()
    l = ""
    k = ""
    for i in n:
        if i == "." and len(l) == 0:
            k += "0"
        else:
            l += i
            if len(l) == 2:
                if l == "-.":
                    k += "1"
                    l = ""
                else:
                    k += "2"
                    l = ""
    print(k)

def FairPlayoff():
    n = int(input())
    for i in range(n):
        loser = {}
        winner = {}
        count = 0
        k = input().split(" ")
        if int(k[0]) > int(k[1]):
           loser["one"] = int(k[1])
           winner["two"] = int(k[0])
        else:
            loser["one"] = int(k[0])
            winner["two"] = int(k[1])
        if int(k[2]) > int(k[3]):
            loser["two"] = int(k[3])
            winner["one"] = int(k[2])
        else:
            loser["two"] = int(k[2])
            winner["one"] = int(k[3])
        for i in loser:
            if loser[i] < winner[i]:
                count += 1
        if count >= 2:
            print("YES")
        else:
            print("NO")


def Bustoudaylanbd():
    n = int(input())
    s = []
    rem = -1
    first = True
    ss = ""
    for i in range(n):
        s += input().split("|")
    for i in range(len(s)):
        if s[i] == "OO" and first:
            rem = i
            s[i] = "++"
            first = False
    for i in range(len(s)):
        if i % 2 == 0:
            ss += s[i] + "|"

        else:
            ss += s[i] + "\n"
    if not first:
        print("YES")
        print(ss)
    else:
        print("NO")

def Maximumincrease():
    n = int(input())
    arraa = input().split(" ")
    for i in range(len(arraa)):
        arraa[i] = int(arraa[i])
    counter = {}
    for i in  range(n):
        counter[i] = 0
    count = 0
    last = 0
    for i in arraa:
        if i > last:
            last = i
            counter[count] += 1
        else:
            last = i
            count += 1
            counter[count] += 1
    max = 0
    for i in range(n):
        if counter[i] > max:
            max = counter[i]
    print(max)


def Jugglingletters():
    n = int(input())

    for i in range(n):
        k = int(input())
        s = ""
        map = {}
        possible = True
        for i in range(k):
            s += input()
        for i in s:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
        for i in map:
            if map[i] % k != 0:
                possible = False
        if possible:
            print("YES")
        else:
            print("NO")


def Panoramixsprediction():
    nm = input().split(" ")
    n = int(nm[0])
    m = int(nm[1])
    first = True
    for i in range(n + 1, m):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            first = False
            break
    if first:
        count = 0
        for j in range(2, m):
            if m % j == 0:
                count += 1
        if count == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


def ThreepilesofCanides():
    k = int(input())
    for i in range(k):
        n = input().split(" ")
        canides = 0
        for i in n:
            canides += int(i)
        if canides % 2 != 0:
            canides -=1
        print(canides//2)


def filename():
    n = int(input())
    name = input()
    more = 0
    map = {}
    map[more] = 0
    count = 0
    for i in name:
        if i == "x":
            map[more] += 1
        elif map[more] != 0:
            more += 1
            map[more] = 0
    for i in map:
        if map[i] >= 3:
            while map[i] > 2:
                map[i] -= 1
                count += 1
    print(count)


def Football():
    map = {}
    current = 0
    s = input()
    f= s[0]
    map[current] = 0
    check = False
    for i in s:
        if i == f:
            map[current] += 1
        else:
            current += 1
            map[current] = 1
            f = i
    for i in map:
        if map[i] >= 7:
            check = True
    if check:
        print("YES")
    else:
        print("NO")

def CombinationLock1():
    n = int(input())
    fl = input()
    sl = input()
    count = 0
    for i in range(n):
        goup = int(fl[i])
        god = int(fl[i])
        cu = 0
        cd = 0
        keep = True
        while keep:
            if goup + 1 <= 9:
                goup += 1
                cu += 1
            else:
                goup = 0
                cu += 1
            if god - 1  >= 0:
                god -= 1
                cd += 1
            else:
                god = 9
                cd += 1
            if goup == int(sl[i]):
                count += cu
                keep = False
            elif god == int(sl[i]):
                count += cd
                keep = False
    print(count)

def Watermelon():
    n = int(input())
    down = n//2
    up = n - down
    rge = up
    for i in range(rge):
        if up%2 == 0 and down%2 == 0:
            return print("YES")
        else:
            if up + 1 < n and down - 1 > 0:
                up += 1
                down -= 1
            else:
                return print("NO")


def Dominopiling():
    nk = input().split(" ")
    n = int(nk[0])
    k = int(nk[1])
    mnk = n * k
    print(mnk//2)

def yetanotherBookshelf():
    n = int(input())
    for i in range(n):
        le = int(input())
        K = input().split(" ")
        SK = []
        lili = []
        for i in range(le):
            if i + 1 <= le - 1:
                if K[i] == "1" and K[i + 1] == "1":
                    lili.append(i)
        lili.reverse()
        for i in lili:
            K.pop(i)
        coun = 0
        while K.count("1") > 1:
            f = K.index("1")
            K.pop(f)
            K.insert(f + 1, "1")
            f += 1
            if K[f + 1] == "1":
                K.pop(f)
            coun += 1
        print(coun)

def Combinationlockittakestolong():
    n = int(input())
    fl = input()
    sl = input()
    counter = 0
    for i in range(n):
        up = int(fl[i])
        down = int(fl[i])
        while True:
            if up + 1 <= 9:
                up += 1
            else:
                up = 0
            if down - 1 >= 0:
                down -= 1
            else:
                down = 9
            counter += 1
            if up == int(sl) or down == int(sl):
                break


def iwannabetheguytolong():
    n = int(input())
    lvl = input().split(" ")
    lvls = input().split(" ")
    for i in range(1, n + 1):
        if str(i) not in lvl and str(i) not in lvls:
            return print("Oh, my keyboard!")
    return print("I become the guy.")

def giftsettolong():
    n = int(input())
    for i in range(n):
        rb = input().split(" ")
        x = int(rb[0])
        y = int(rb[1])
        a = int(rb[2])
        b = int(rb[3])
        giftset = 0
        while True:
            if x - a >= 0 and y - b >= 0:
                x -= a
                y -= b
                giftset += 1
            elif x - b >= 0 and y - a >= 0:
                x -= b
                y -= a
                giftset += 1
            else:
                break
        print(giftset)



def uniquwbidauctiontime():
    n = int(input())
    for i in range(n):
        k = int(input())
        list = input().split(" ")
        o = -1
        for i in range(k):
            if list.count(list[i]) == 1:
                if o == -1 or list[i] < o:
                    o = list[i]
        if o != -1:
            print(list.index(o) + 1)
        else:
            print(o)


def equalizepriceagain():
    n = int(input())
    for i in range(n):
        k = int(input())
        numbers = input().split(" ")
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        total = 0
        for i in numbers:
            total += i
        if total%k == 0:
            print(total//k)
        else:
            while total%k != 0:
                total += 1
            print(total//k)

def shortsubstrings():
    n = int(input())
    for i in range(n):
        s = input()
        laist = []
        for i in range(len(s)):
            if i%2 != 0 and i != len(s) - 1:
                laist.append(i)
        laist.reverse()
        s = list(s)
        for i in laist:
            s.pop(i)
        sa = ""
        for i in s:
            sa += i
        print(sa)

def policerecruits():
    n = int(input())
    k = input().split(" ")
    officers = 0
    crimes = 0
    for i in k:
        if int(i) == -1:
            if officers == 0:
                crimes += 1
            else:
                officers -= 1
        else:
            officers += int(i)
    print(crimes)


def thenewyear():
    xxx = input().split(" ")
    for i in range(len(xxx)):
        xxx[i] = int(xxx[i])
    xxx.sort()
    way = 0
    way += abs(int(xxx[1]) - int(xxx[0]))
    way += abs(int(xxx[1]) - int(xxx[2]))
    print(way)


def frogjumpingtimelimit():
    n = int(input())
    for i in range(n):
        abk = input().split(" ")
        a = int(abk[0])
        b = int(abk[1])
        k = int(abk[2])
        all = 0
        for i in range(k):
            if i % 2 == 0:
                all += a
            else:
                all -= b
        print(all)


def patrickandshopping():
    d = input().split(" ")
    d3 = 0
    for i in range(len(d)):
        if int(d[i]) > d3:
            d3 = int(d[i])
    d.pop(d.index(str(d3)))
    d1 = int(d[0])
    d2 = int(d[1])
    distance = d1 + d2
    if d3 <= distance:
        distance += d3
    else:
        distance += distance
    print(distance)


def Freeicecream():
    nx = input().split(" ")
    n = int(nx[0])
    ice = int(nx[1])
    diskid = 0
    for i in range(n):
        k = input().split(" ")
        if k[0] == "+":
            ice += int(k[1])
        else:
            if ice >= int(k[1]):
                ice -= int(k[1])
            else:
                diskid += 1
    print(ice, diskid)

def Reviewsite():
    t = int(input())
    for i in range(t):
        n = int(input())
        upvotes = 0
        votes = input().split(" ")
        for i in votes:
            if i != "2":
                upvotes += 1
        print(upvotes)

def Lastyeasrtssubstring():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        if s[0:4] == "2020" or s[n - 4: n] == "2020":
            print("YES")
        elif s[0:3] == "202" and s[n - 1] == "0":
            print("YES")
        elif s[n - 3: n] == "020" and s[0] == "2":
            print("YES")
        elif s[0:2] == "20" and s[n - 2] == "20":
            print("YES")
        elif s[n - 2: n] == "20" and s[0:2] == "20":
            print("YES")
        else:
            print("NO")

def Arena():
    t = int(input())
    for i in range(t):
        n = int(input())
        heros = input().split(" ")
        heorsint = [int(i) for i in heros]
        heorsint.sort()
        min = heorsint[0]
        winner = n - (heorsint.count(min))
        print(winner)

def twoRabbitstoolongbutright():
    t = int(input())
    for i in range(t):
        xyab = input().split(" ")
        x = int(xyab[0])
        y = int(xyab[1])
        a = int(xyab[2])
        b = int(xyab[3])
        seconds = 0
        while x < y:
            x += a
            y -= b
            seconds += 1
        if x == y:
            print(seconds)
        else:
            print(-1)


def systemofequations():
    nm = input().split(" ")
    n = int(nm[0])
    m = int(nm[1])
    nm = [int(i) for i in nm]
    nm.sort()
    count = 0
    for i in range(nm[0] + 1):
        for j in range(nm[0] + 1):
            if i**2 + j == n and j**2 + i == m:
                count += 1
    print(count)


def polycarpwspockets():
    n = int(input())
    coins = input().split(" ")
    coins = [int(i) for i in coins]
    pocket = 0
    for i in coins:
        nmumbver = coins.count(i)
        if nmumbver > pocket:
            pocket = nmumbver
    print(pocket)


def repeaqtijgcipher():
    n = int(input())
    s = input()
    counter = 0
    rep = 1
    ns = ""
    while counter < n:
        counter += rep
        ns += (s[counter - 1])
        rep += 1
    print(ns)


def Neaarestinterestingnumber():
    a = input()
    s = int(a)
    while True:
        if sum(int(i) for i in str(s)) % 4 == 0:
            return print(s)
        else:
            s += 1


def therearetwotzpesofburgers():
    t = int(input())
    for i in range(t):
        ess = input().split(" ")
        ess = [int(i) for i in ess]
        price = input().split(" ")
        buns = int(ess[0])
        totalmoney = 0
        first = True
        if int(price[0]) > int(price[1]):
            patties = ess[1]
            otherpatties = ess[2]
            money = int(price[0])
            othermoney = int(price[1])
        else:
            patties = ess[2]
            otherpatties = ess[1]
            money = int(price[1])
            othermoney = int(price[0])
        keep = True
        while keep:
            if buns - 2 >= 0 and patties - 1 >= 0:
                buns -= 2
                patties -= 1
                totalmoney += money
            elif buns - 2 >= 0 and patties == 0:
                if first:
                    patties = otherpatties
                    money = othermoney
                    first = False
                else:
                    print(totalmoney)
                    keep = False
            else:
                print(totalmoney)
                keep = False


def threeswimmerstimelimitebutseemsright():
    t = int(input())
    for i in range(t):
        pabc = input().split(" ")
        pabc = [int(i) for i in pabc]
        a = 0
        b = 0
        c = 0
        p = pabc[0]
        keep = True
        while keep:
            if a < p:
                a += pabc[1]
            if b < p:
                b += pabc[2]
            if c < p:
                c += pabc[3]
            if a >= p and b >= p and c >= p:
                list = [a - p, b - p, c - p]
                list.sort()
                print(list[0])
                keep = False

def Gregsworkout():
    n = int(input())
    training = input().split(" ")
    training = [int(i) for i in training]
    map = [0, 0, 0]
    current = 0
    for i in training:
        map[current] += i
        if current < 2:
            current += 1
        else:
            current = 0
    sorte = []
    for i in map:
        sorte.append(i)
    sorte.sort()
    index = map.index(sorte[2])
    if index == 0:
        print("chest")
    elif index == 1:
        print("biceps")
    else:
        print("back")


def heisttimelimitebutseemsright():
    n = int(input())
    all = input().split(" ")
    all = [int(i) for i in all]
    all.sort()
    counter = 0
    for i in range(all[0], all[len(all) - 1]):
        if i not in all:
            counter += 1
    print(counter)

def nonzero():
    t = int(input())
    for i in range(t):
        n = int(input())
        numbers = input().split(" ")
        count = numbers.count("0")
        for i in range(count):
            ind = numbers.index("0")
            numbers.pop(ind)
            numbers.insert(ind, "1")
        numbers = [int(i) for i in numbers]
        if sum(numbers) == 0:
            count += 1
        print(count)

def distinctdigits():
    lr = input().split(" ")

    for i in range(int(lr[0]), int(lr[1]) + 1):
        couynt = []
        for j in str(i):
            if j not in couynt:
                couynt.append(j)
        if len(couynt) == len(str(i)):
            return print(i)
    else:
        return print(-1)

def dawidandbagsofcandies():
    bags = input().split(" ")
    bags = [int(i) for i in bags]
    bags.sort()
    if bags[0] + bags[3] == bags[1] + bags[2]:
        print("YES")
    elif bags[3] == bags[0] + bags[1] + bags[2]:
        print("YES")
    else:
        print("NO")

def lastminuteenhancements():
    t = int(input())
    for i in range(t):
        n = int(input())
        notes = input().split(" ")
        lists = []
        for i in notes:
            if int(i) not in lists:
                lists.append(int(i))
            elif  int(i) + 1 not in lists:
                lists.append(int(i) + 1)
        print(len(lists))

def Cakeminator():
    rc =input().split(" ")
    cake = []
    pices = 0
    rows = 0
    for i in range(int(rc[0])):
        cake.append([i for i in input()])
    for i in range(int(rc[1])):
        count = 0
        for j in range(int(rc[0])):
            if cake[j][i] == ".":
                count +=1
            if count == int(rc[0]):
                pices += count
                rows += 1
    for i in range(int(rc[0])):
        if "S" not in cake[i]:
            pices += (int(rc[1]) - rows)
    print(pices)

def CME():
    t = int(input())
    for i in range(t):
        n = int(input())
        four = 4
        while four < n:
            four += 2
        print(four - n)


def FriendsandCandies():
     t = int(input())
     for i in range(t):
         n = int(input())
         cadies = input().split(" ")
         cadies = [int(i) for i in cadies]
         all = sum(cadies)%n

         count = 0
         if all != 0:
             print(-1)
         else:
            for i in cadies:
                if i > sum(cadies)//n:
                    count += 1
            print(count)


def tworivalstudents():
    t= int(input())
    for i in range(t):
        nxab = input().split(" ")
        n = int(nxab[0])
        x = int(nxab[1])
        if int(nxab[2]) >= int(nxab[3]):
            bigger = int(nxab[2])
            smaller = int(nxab[3])
        else:
            bigger = int(nxab[3])
            smaller = int(nxab[2])
        for i in range(x):
            if bigger < n:
                bigger += 1
            elif smaller > 1:
                smaller -= 1
            else:
                break
        print(bigger - smaller)

def OmkarandPassword():
    t = int(input())
    for i in range(t):
        n = int(input())
        array = input().split(" ")
        array = [int(i) for i in array]
        pointer = 0
        while array.count(array[0]) != len(array):

            if array[pointer] != array[pointer + 1]:
                array.insert(pointer, array[pointer] + array[pointer + 1])
                array.pop(pointer)
                array.pop(pointer + 1)
            else:
                if pointer + 1 < len(array) - 1:
                    pointer += 1
                else:
                    pointer = 0
        print(len(array))


def tanyaasndstairways():
    n = int(input())
    k = input().split(" ")
    k = [int(i) for i in k]
    last = []
    storeys = k.count(1)
    for i in range(n - 1):
        if k[i] >= k[i + 1]:
            last.append(k[i])
    last.append(k[n - 1])
    print(storeys)
    printable = ""
    for i in last:
        printable += str(i) + " "
    print(printable)




def adjacentreplacements():
    t = int(input())
    wowowo = input()
    wo = wowowo.split(" ")
    wo = [int(i) for i in wo]
    for i in range(t):
       if wo[i] % 2 == 0:
           wo[i] -= 1
    s = ""
    for i in wo:
        s += str(i) + " "
    print(s)


def Divideit():
    t = int(input())
    for i in range(t):
        n = int(input())
        counter = 0
        while n > 1:
            if n%2 == 0:
                n = n//2
                counter += 1
            elif n%3 == 0:
                n = (2*n)//3
                counter += 1
            elif n % 5 == 0:
                n = (4 * n) // 5
                counter += 1
            else:
                counter = -1
                break
        print(counter)

def DiverseTeam():
    nk = input().split(" ")
    n = int(nk[0])
    k = int(nk[1])
    rating = input().split(" ")
    list = []
    s = ""
    for i in range(n):
        if rating[i] not in list:
            list.append(rating[i])
            s += str(i + 1) + " "
        if len(list) == k:
            print("YES")
            return print(s)
    return print("NO")


def phoenixandgold():
    t = int(input())
    for i in range(t):
        nx = input().split(" ")
        n = int(nx[0])
        x = int(nx[1])
        gold = input().split(" ")
        gold = [int(i) for i in gold]
        count = 0
        s = ""
        if sum(gold) == x:
            print("NO")
        else:
            while len(gold) != 0:
                for i in range(len(gold)):
                    if i < len(gold):
                        if gold[i] + count != x:
                            count += gold[i]
                            s += str(gold[i]) + " "
                            gold.pop(i)
            print("YES")
            print(s)


def ingamechat():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        c = 0
        for i in s:
            if i == ")":
                c += 1
            else:
                c = 0
        if c > n - c:
            print("Yes")
        else:
            print("No")



def IntegerSAequencedividing():
    list = [int(i) for i in range(1, int(input()) + 1)]
    list.reverse()
    A = 0
    B = 0
    while len(list) > 0:
        if len(list) != 1:
            one = list[0]
            two = list[1]
            list.pop(0)
            list.pop(0)
        else:
            one = list[0]
            list.pop(0)
            two = 0
        if abs((A + one) - (B + two) <= abs((B + one) - (A + two))):
            A += one
            B += two
        else:
            A += two
            B += one
    print(abs(A - B))


def shortestpathwithobstacle():
    t = int(input())
    for i in range(t):
        s = input()
        A = [int(i) for i in input().split(" ")]
        B = [int(i) for i in input().split(" ")]
        F = [int(i) for i in input().split(" ")]
        distance = abs(A[0] - B[0]) + abs(A[1] - B[1])
        if ((A[0] == B[0] and A[0] == F[0] and min(A[1], B[1]) < F[1] and F[1] < max(A[1], B[1]))
         or (A[1] == B[1] and A[1] == F[1] and min(A[0], B[0]) < F[0] and F[0] < max(A[0], B[0]))):
            distance += 2
        print(distance)

def Removeduplicates():
    t = int(input())
    numbers = input().split(" ")
    numbers.reverse()
    removed = []
    for i in numbers:
        if i not in removed:
            removed.append(i)
    removed.reverse()
    s = ""
    for i in removed:
        s += i + " "
    print(len(removed))
    print(s)


def Threestrings():
    t= int(input())
    for i in range(t):
        a = input()
        b = input()
        c = input()
        work = True
        for i in range(len(a)):
            if a[i] != c[i] and b[i] != c[i]:
                work = False
        if work:
            print("YES")
        else:
            print("NO")

def specifictastesofandre():
    t = int(input())
    for i in range(t):
        li = [1 for i in range(int(input()))]
        s = ""
        for i in li:
            s += str(i) + " "
        print(s)

def dejavu():
    t = int(input())
    for i in range(t):
        s = input()
        if s + "a" == "a" + s:
            print("NO")
        else:
            sl = list(s + "a")
            rsl = []
            for i in sl:
                rsl.insert(0, i)
            if  sl != rsl:
                print("YES")
                print(s + "a")
            else:
                print("YES")
                print("a" + s)


def buythestring():
    t = int(input())
    for i in range(t):
        ncch = [int(i) for i in input().split(" ")]
        s = input()
        money = 0
        for i in s:
            if i == "0":
                money += min(ncch[1], ncch[2] + ncch[3])
            else:
                money += min(ncch[2], ncch[1] + ncch[3])
        print(money)


def Keyraces():
    svvtt = [int(i) for i in input().split(" ")]
    first = ((2 * svvtt[3]) + (svvtt[0] * svvtt[1]))
    scond = ((2 * svvtt[4]) + (svvtt[0] * svvtt[2]))
    if first > scond:
        print("Second")
    elif first < scond:
        print("First")
    else:
        print("Friendship")

def Angrystudents():
     t = int(input())
     for i in range(t):
         len = int(input())
         s = list(input())
         counter = 0
         counterlist = [0, ]
         if s.count("A") != 0:
             firstp = s.index("A")
             for i in range(firstp, len):
                 if s[i] == "P":
                     counter += 1
                 else:
                     counterlist.append(counter)
                     counter = 0
             counterlist.append(counter)
         print(max(counterlist))



def Frence():
    t = int(input())
    for i in range(t):
        d = sum([int(i) for i in input().split(" ")]) - 1
        print(d)

def playongwhithdice():
    ab = [int(i) for i in input().split(" ")]
    a = ab[0]
    b = ab[1]
    awins = 0
    draw = 0
    bwins = 0
    for i in range(1, 7):
        if abs(i - a) < abs(i - b):
            awins += 1
        elif abs(i - a) > abs(i - b):
            bwins += 1
        else:
            draw += 1
    print(awins, draw, bwins)


def arrayandpeaks():
    t = int(input())
    for i in range(t):
        n, k = [int(i) for i in input().split(" ")]
        listaa =  [i for i in range(1, n - k + 1)]
        listoo = [i for i in range(n - k + 1, n + 1)]
        s = ""
        if len(listaa) > len(listoo):
            for i in range(len(listaa)):
                s += str(listaa[0]) + " "
                listaa.pop(0)
                if len(listoo) != 0:
                    s += str(listoo[0]) + " "
                    listoo.pop(0)
        else:
            s = "-1"
        print(s)


def mishkaandContest():
    n, k = [int(i) for i in input().split()]
    problems = [int(i) for i in input().split()]
    fp = 0
    sp = 0
    first = True
    for i in problems:
        if i <= k and first:
            fp += 1
        elif i > k and first:
            first = False
        elif i <= k and not first:
            sp += 1
        else:
            sp = 0
    print(sp + fp)


def gotanygrapes():
    xyz = [int(i) for i in input().split(" ")]
    abc = [int(i) for i in input().split(" ")]
    c = 0
    for i in range(3):
        c += abc[i]
        c -= xyz[i]
        if c < 0:
            return print("NO")
    return print("YES")

def stringgenerations():
    t = int(input())
    ABC = ["a", "b", "c"]

    for i in range(t):
        s = ''
        n, k = input().split(" ")
        for i in range(int(n)):
            s += ABC[i%3]
        print(s)


def gradeallocation():
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split(" ")]
        scores = [int(i) for i in input().split(" ")]
        summa = sum(scores)
        if summa >= m:
            print(m)
        else:
            print(summa)


def shashaandsticks():
    n, k = [int(i) for i in input().split(" ")]
    counter = n//k
    if counter % 2 == 0:

        print("NO")
    else:
        print("YES")


def Hoteliero():
    n = int(input())
    s = []
    for i in input():
        s.append(i)
    rooms = [0 for i in range(10)]
    for i in s:
        if i == "L":
            index = rooms.index(0)
            rooms[index] = 1
        elif i == "R":
            rooms.reverse()
            index = rooms.index(0)
            rooms[index] = 1
            rooms.reverse()
        else:
            index = int(i)
            rooms[index] = 0
    f = ""
    for i in rooms:
        f += str(i)
    print(f)

def barrels():
    t = int(input())
    for i in range(t):
        n, k = [int(i) for i in input().split(" ")]
        barrels = [int(i) for i in input().split(" ")]
        maxbarrelcount = barrels.pop(barrels.index(max(barrels)))
        for i in range(k):
            maxbarrelindex = barrels.index(max(barrels))
            maxbarrelcount += barrels[maxbarrelindex]
            barrels.pop(maxbarrelindex)
        print(maxbarrelcount)


def lovetriangle():
    n = int(input())
    planes = [int(i) - 1 for i in input().split(" ")]
    for i in range(n):
        if planes[planes[planes[i]]] == i:
            return print("YES")
    return print("NO")


def lovesong():
    n, q = [int(i) for i in input().split(" ")]
    s = input()
    for i in range(q):
        l, r = [int(i) for i in input().split(" ")]
        l -= 1
        substr = s[l:r]
        c = 0
        for i in substr:
            c += string.ascii_lowercase.index(i) + 1
        print(c)

def coins():
    n , S = [int(i) for i in input().split(" ")]
    if S % n == 0:
        print(S // n)
    else:
        print(S // n + 1)


def penandpencils9():
    t = int(input())
    for i in range(t):
        a, b, c, d, k = [int(i) for i in input().split(" ")]
        x, y = 0, 0
        x += (a//c)
        if a%c != 0:
            x += 1
        y = (b//d)
        if b%d != 0:
            y += 1
        if (y + x) <= k:
            print(x, y)
        else:
            print(-1)

def phonenumber():
    t = int(input())
    for i in range(2):
        n = int(input())
        number = input()
        if "8" in number:
            if n - number.index("8") >= 10:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")


def cars():
    n = int(input())
    cards = [int(i) for i in input().split(" ")]
    playercount = n // 2
    eachplayer = sum(cards)//playercount
    for i in range(n):
        if cards[i] != 0:
            x = cards[i]
            cards.pop(i)
            cards.insert(i, 0)
            y = cards.index(eachplayer - x)
            cards.pop(y)
            cards.insert(y, 0)
            print(i + 1, y + 1)


def suffixthree():
    t = int(input())
    for i in range(t):
        l = input().split("_")
        s = l[len(l) - 1]
        if "po" == s[len(s) - 2:]:
            print("FILIPINO")
        elif "desu" == s[len(s) - 4:] or "masu" == s[len(s) - 4:]:
            print("JAPANESE")
        else:
            print("KOREAN")

def roconaissance2():
    n = int(input())
    map = {}
    l = [int(i) for i in input().split(" ")]
    p = []
    for i in l:
        p.append(i)
    p.sort()
    for i in range(n - 1):
        map[abs(p[i] - p[i + 1])] = p[i], p[i + 1]
    print(map)
    c, v = map[min(map)]
    print(l.index(c) + 1, l.index(v, l.index(c) + 1) + 1)


def Waterbuying():
    t = int(input())
    for i in range(t):
        n,a,b = [int(i) for i in input().split(" ")]
        cost = min(2 * a, b)
        money = (cost * (n//2))

        if n%2 != 0:
            money += a
        print(money)

def alovea():
    s = input()
    acount = s.count("a")
    rest = len(s) - acount
    if rest >= acount:
        rest = acount - 1
    print(acount + rest)


def I_love_username():
    n = int(input())
    list = [int(i) for i in input().split(" ")]
    count = 0
    min = list[0]
    list.pop(0)
    max = min
    for i in list:
        if i < min:
            min = i
            count += 1
        elif i > max:
            max = i
            count += 1
    print(count)


def vaszathehipster():
    ab = [int(i) for i in input().split(" ")]
    ab.sort()
    print(ab[0], ((ab[1] - ab[0])//2))


def Newyearandhurry():
    n,k = [int(i) for i in input().split(" ")]
    leftminutes = 240 - k
    c = 0
    for i in range(1, n + 1):
        leftminutes -= (i*5)
        if leftminutes < 0:
            return print(c)
        c += 1
    return print(n)

def designtutoriallearnmathfrommath():
    n = int(input())
    if n%2 == 0:
        print(8, n-8)
    else:
        print(9, n - 9)


def yetantoherintegerproblem():
    t = int(input())
    for i in range(t):
        ab = [int(i) for i in input().split(" ")]
        ab.sort()
        a, b = ab
        counter = 0
        while b - a >= 10:
            a += 10
            counter += 1
        if a != b:
            counter += 1
        print(counter)

def twoarraysandswaps():
    t = int(input())
    for i in range(t):
        n,k = [int(i) for i in input().split(" ")]
        array_A = [int(i) for i in input().split(" ")]
        array_B = [int(i) for i in input().split(" ")]
        array_B.sort()
        array_A.sort()
        for i in range(k):
            if array_A[0] < array_B[len(array_B) - 1]:
                array_A.pop(0)
                array_A.insert(n, array_B[len(array_B) - 1])
                array_B.pop(len(array_B) - 1)
        print(sum(array_A))


def TeamOlympiad():
    t = int(input())
    students = [int(i) for i in input().split(" ")]
    if students.count(1) <= students.count(2):
        n = students.count(1)
    else:
        n = students.count(2)
    if students.count(3) < n:
        n = students.count(3)
    print(n)
    for i in range(n):
        print(students.index(1) + 1, students.index(2) + 1, students.index(3) + 1)
        students.insert(students.index(1), 0)
        students.pop(students.index(1))
        students.insert(students.index(2), 0)
        students.pop(students.index(2))
        students.insert(students.index(3), 0)
        students.pop(students.index(3))

def holidayofequality():
    n = int(input())
    array = [int(i) for i in input().split(" ")]
    burles = 0
    mae = max(array)
    for i in array:
        burles += (mae - i)
    print(burles)

def choosingteams():
    n, k = [int(i) for i in input().split(" ")]
    members = [int(i) for i in input().split(" ")]
    a = []
    for i in members:
        if i + k <= 5:
            a.append(i)
    print(len(a)//3)

def Do_Not_Be_Distracted():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        a = []
        l = True
        for i in s:
            a.append(i)
        s = []
        for i in range(1, n):
            if a[i] == a[i - 1]:
                s.append(i)
        s.reverse()
        for i in s:
            a.pop(i)
        for i in a:
            if a.count(i) != 1:
                 l = False
        if l == False:
            print("NO")
        else:
            print("YES")


def boringapartments():
    t = int(input())
    for i in range(t):
        sa = input()
        number = int(sa[0])
        count = 10 * (number - 1)
        if len(sa) == 1:
            count += 1
        elif len(sa) == 2:
            count += 3
        elif len(sa) == 3:
            count += 6
        else:
            count += 10
        print(count)

def AmusingJoke():
    first = input()
    second = input()
    allleter = input()
    skk = first + second
    if sorted(skk) == sorted(allleter):
        print("YES")
    else:
        print("NO")


def AmusingJokenexttry():
    first = input()
    second = input()
    allleter = input()
    skk = first + second
    if len(skk) == len(allleter):
        for i in skk:
            if i in allleter:
                if skk.count(i) == allleter.count(i):
                    pass
                else:
                    return print("NO")
            else:
                return print("NO")
    else:
        return print("NO")
    return print("YES")

def sumroundnumbvers():
    t = int(input())
    for i in range(t):
        n = input()
        print(len(n) - n.count("0"))
        if len(n) - n.count("0") != 1:
            s = ""
            zeros = ""
            for i in range(len(n) - 1):
                zeros += "0"
            n = [i for i in n]
            for i in range(len(n)):
                if n[i] != "0":
                    s += n[i] + zeros + " "
                zeros = zeros[0:len(zeros) - 1]
            print(s)
        else:
            print(n)


def buyashovel():
    k,r = [int(i) for i in input().split(" ")]
    for i in range(1, 11):
        ww = i * k
        if ww % 10 == 0 or  (ww % 10) == r:
            return print(i)


def MinimalSquare():
    t = int(input())
    for i in range(t):
        ab = [int(i) for i in input().split(" ")]
        ab.sort()
        a, b = ab
        if 2 * a >= b:
            print((2 * a)**2)
        else:
            print(b**2)

def Bachgoldproblem():
    n = int(input())
    k = n//2
    print(k)
    s = ""
    for i in range(k - 1):
        s += "2 "
    if n%2 == 0:
        s += "2"
    else:
        s += "3"
    print(s)


def HQ9plus():
    p = input()
    if "H" in p or "Q" in p or "9" in p:
        print("YES")
    else:
        print("NO")


def evenoddstimelimit():
    n,k = [int(i) for i in input().split(" ")]
    current = 0
    list = []
    for i in range(1, n + 1):
        if i %2 == 1:
            list.insert(current, i)
            current += 1
        else:
            list.append(i)
    print(list[k - 1])

def Kefaandfirststeps():
    n = int(input())
    a = [int(i) for i in input().split(" ")]
    list = []
    row = 0
    current = 0
    for i in a:
        if i >= current:
            row += 1
            current = i
        else:
            list.append(row)
            row = 1
            current = i
    list.append(row)
    print(max(list))

def GravityFlip():
    n = int(input())
    a= [int(i) for i in input().split(" ")]
    a.sort()
    s = ""
    for i in a:
        s += str(i) + " "
    print(s)

def Dubstep():
    s = input()
    ss = ""
    c = 0
    l = []
    for i in s:
        if ss == "WUB":
            ss = ""
            c += 1
        if i == "W" and len(l) - 1 == c:
            if ss != "":
                l[c] += ss
            ss = ""
        elif i == "W":
            if ss != "":
                l.insert(c, ss)
            ss = ""
        ss += i
    if ss != "WUB":
        l.append(ss)
    ss = ""
    for i in l:
        ss += i + " "
    print(ss)

def Twins():
    n = int(input())
    a = [int(i) for i in input().split(" ")]
    a.sort()
    a.reverse()
    c = 0
    summe = 0
    while summe <= (sum(a)/2):
        summe += a[c]
        c += 1
    print(c)


def Puzzles():
    n,m = [int(i) for i in input().split(" ")]
    f = [int(i) for i in input().split(" ")]
    f.sort()
    c = 0
    l = []
    while c + n < m:
        l.append((f [c + n - 1] - f[c]))
        c += 1
    print(min(l))

def GamewithSticdks():
    nm = [int(i) for i in input().split(" ")]
    if min(nm) % 2 == 0:
        print("Malvika")
    else:
        print("Akshat")

def OddDivisor():
    t = int(input())
    for i in range(t):
        n = int(input())
        possible = False
        for i in range(3, n//2 + 1):
            if i %2 == 1 and n%2 == 0:
                possible = True
                break
        if possible:
            print("YES")
        else:
            print("NO")

def SellingHamburgers():
    t = int(input())
    for i in range(t):
        n = int(input())
        cutomers = [int(i) for i in input().split(" ")]
        allprice = []
        for i in cutomers:
            price = i
            currewnt = 0
            for j in cutomers:
                if price <= j:
                    currewnt += price
            allprice.append(currewnt)
        print(max(allprice))

def Candies():
    n, m = [int(i) for i in input().split(" ")]
    minues = (n % m)
    list = [n//m for i in range(m)]
    c = -1
    for i in range(minues):
        list[c] += 1
        c -= 1
    s = ""
    for i in list:
        s += str(i) + " "
    print(s)

def Secondpriceauction():
    n = int(input())
    p = [int(io) for io in input().split(" ")]
    indexmax = p.index(max(p))
    p.remove(max(p))
    print(indexmax + 1, max(p))

def Fakenews():
    s = input()
    heidi = ["h", "e", "i", "d", "i"]
    c = 0
    for i in s:
        if i == heidi[c] == "i" and c == 4:
            return print("YES")
        elif i == heidi[c]:
            c += 1
    return print("NO")

def PashyaandHamsters():
    n,a ,b = [ int(i) for i in input().split(" ")]
    a = [ int(i) for i in input().split(" ")]
    b = [int(i) for i in input().split(" ")]
    s = ""
    for i in range(1, n + 1):
        if i in a:
            s += "1 "
        else:
            s += "2 "
    print(s)


def phonecode():
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(input())
    similar = 0
    for i in range(len(numbers[0])):
        x = numbers[0][i]
        for j in numbers:
            if x != j[i]:
                return print(similar)
        similar += 1
    return print(similar)


def ConstructtheString():
    t = int(input())
    for i in range(t):
        n,a,b = [ int(i) for i in input().split(" ")]
        s = []
        for i in range(b):
            s.append(string.ascii_lowercase[i])

        while len(s) < a:
            s.append(s[-1])
        for i in range(n - a):
            s.append(s[i % a])
        k = ""
        for i in s:
            k += f"{i}"
        print(k)


def yearofunioversityentrance():
    n = int(input())
    years = [int(i) for i in input().split(" ")]
    years.sort()
    print(years[len(years) //2])


def ForgottenEpisode():
    n = int(input())
    we = [int(i) for i in input().split(" ")]
    for i in range(1, n + 1):
        if i not in we:
            return print(i)



def SeriesofCrimes():
    n,m = [int(i) for i in input().split(" ")]
    points = []
    for i in range(n):
        line = input()
        for j in range(len(line)):
            if line[j] == "*":
                points.append([i + 1, j + 1])
    k = []
    op = []
    for j in range(2):
        op = []
        for i in range(3):
            op.append(points[i][j])
        for i in op:
            if op.count(i) == 2:
                op.remove(i)
                op.remove(i)
        k.append(op[0])
    print(k[0],k[1])

def KanaandDragonQuestgame():
    t = int(input())
    for i in range(t):
        x,n,m = [int(i) for i in input().split(" ")]
        while x//2 >= 10 and n > 0:
            n -= 1
            x = (x//2) + 10
        if x/10 <= m:
            print("YES")
        else:
            print("NO")

def CaseofZerosandKOnes():
    n = int(input())
    s = input()
    l = []
    l.append(s.count("0"))
    l.append(s.count("1"))
    print(max(l) - min(l))

def chores(): #solutioons seems wrong
    n, a, b = [int(i) for i in input().split(" ")]
    h = [int(i) for i in input().split(" ")]
    h.sort()
    if h[b - 1] == h[b]:
        print(0)
    else:
        print(h[b - 1])

def Helpfarawaykongdom():
    number = input().split(".")
    if number[0][len(number[0]) - 1] == "9":
        print("GOTO Vasilisa.")
    else:
        if float(f"0.{number[1]}") < 0.5:
            print(number[0])
        else:
            print(int(number[0]) + 1)


def elc(string, letter):
    for i in string:
        if i in letter:
            return True

def PasswordCheck():
    s = input()
    if len(s) >=5 and elc(s, string.ascii_lowercase) and elc(s, string.ascii_uppercase) and elc(s,string.digits):
        print("Correct")
    else:
        print("Too weak")

def keyboard():
    q = "qwertyuiop"
    w = "asdfghjkl;"
    e = "zxcvbnm,./"
    qwe = q + w + e
    leftorright = input()
    if leftorright == "R":
        Move = -1
    else:
        Move = 1
    sequenz = input()
    s = ""
    for i in range(len(sequenz)):
        s += qwe[qwe.index(sequenz[i]) + Move]
    print(s)


def Sale():
    n,m = [int(i) for i in input().split(" ")]
    a = [int(i) for i in input().split(" ")]
    a.sort()
    s = []
    for i in a:
        if i < 0:
            s.append(i)
        else:
            break
    s.reverse()
    while len(s) > m:
        s.pop(0)
    print(abs(sum(s)))


def spzketalks():
    n = int(input())
    id = [int(i) for i in input().split(" ")]
    c = 0
    for i in id:
        if i != 0:
            if id.count(i) == 2:
                c += 1
                id.remove(i)
            elif id.count(i) >= 3:
                return print(-1)
    print(c)

def HoodmatrixElements():
    n = int(input())
    matix = []
    c = 0
    used = []
    for i in range(n):
        matix.append([int(i) for i in input().split(" ")])

    for i in range(n):
        c += matix[i][(n//2)]
        used.append(f"{i} {n//2}")
    for i in range(n):
        if f"{n//2} {i}" not in used:
            c += matix[(n // 2)][i]
            used.append(f"{n//2} {i}")
            
    for i in range(n):
        if f"{i} {i}" not in used:

            c += matix[i][i]
            used.append(f"{i} {i}")
    for i in range(n):
        if f"{i} {(n - 1) - i}" not in used:
            c += matix[i][(n - 1) - i]
            used.append(f"{i} {(n - 1) - i}")
    print(c)


def GoodmatrixElements():
    n = int(input())
    matix = []
    c = 0
    used = []
    for i in range(n):
        matix.append([int(i) for i in input().split(" ")])
    for i in range(n):
        if f"{i} {n // 2}" not in used:
            c += matix[i][(n // 2)]
            used.append(f"{i} {n // 2}")
        if f"{n // 2} {i}" not in used:
            c += matix[(n // 2)][i]
            used.append(f"{n // 2} {i}")
        if f"{i} {i}" not in used:
            c += matix[i][i]
            used.append(f"{i} {i}")
        if f"{i} {(n - 1) - i}" not in used:
            c += matix[i][(n - 1) - i]
            used.append(f"{i} {(n - 1) - i}")
    print(c)


def DetermineLine():
    n = int(input())
    possible = []
    for k in range(n):
        if len(possible) == 0:
            possible = [int(i) for i in input().split(" ")]
        else:
            s = [int(i) for i in input().split(" ")]
            for i in possible:
                if i not in s:
                    possible.remove(i)
    s = []
    for i in possible:
        if i not in s:
            s.append(i)
    k = ""
    for i in s:
        k += f"{i} "
    print(k)

def FilliungDiamons():
    N = int(input())
    for i in range(N):
        print(input())

def Businesstrip():
    k = int(input())
    a = [int(i) for i in input().split(" ")]
    if sum(a) < k:
        return print(-1)
    a.sort()
    a.reverse()
    current = []
    i = 0
    while sum(current) < k:
        current.append(a[i])
        i += 1
    print(len(current))

def diplomasandCertificates():
    n, k = [int(i) for i in input().split(" ")]
    i = n//(2*(k + 1))
    print(i, i * k, n - (i + i * k))

GoodmatrixElements()