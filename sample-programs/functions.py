def name(name):
    if name[0] not in vowels:
        a = name[1:] + name[0] + 'ay'
        print(a)
    else:
        a = name + 'way'
        print(a)


def numerus(param):
     a = 0
     curr = 0
     prev = 0
     pl = list(param)
     for p in pl:
         curr = int(romanletter.get(p))
         if(prev < curr):
             a -= prev
             a += curr
             a -= prev
         else:
             a += int(romanletter.get(p))
         prev = curr
     return a


def intersect(list1, list2):
      common = []
      for a in list1:
          if a in list2:
              common.append(a)
      return common
