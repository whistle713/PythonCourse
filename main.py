 
from math import floor
from os.path import join

from sympy.codegen.cfunctions import Sqrt


def nearest_sq(n):

    num = int(n/2)
    new_num = last_num=0
    for i in range(0,num+2):
        new_num = i*i
        if new_num>n:
            break
        last_num = new_num
    if (new_num-n) < (n-last_num):
        return new_num
    elif (new_num-n) > (n-last_num):
        return last_num
    else:
        return n





def bouncing_ball(h, bounce, window):
   num = 0
   if (h>0)and(0<bounce<1)and(window<h):
        num=1
        h *= bounce
        while h > window:
            h*=bounce
            num+=2
        return num
   else:
       return -1




def valid_braces(string):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in string:
            if char in mapping:
                if stack :
                    top_element = stack.pop()
                    if mapping[char] != top_element:
                        return False
                else:
                    return  False
            else:
                stack.append(char)
        return not stack


def create_dict(keys, values):
    values_len = len(values)
    res = {}
    i  = 0
    for key in keys:
        if i != values_len:
             res[key] =values[i]
             i=i+1
        else:
            res[key] = 'None'
    return  res


def even_or_odd(number):
    if number %2==0:
        return "Even"
    else:
        return "Odd"

def solution(number):
    if number < 0:
        return -1
    else :
        sum = 0
        for i in range(number):
            if i %3 ==0 or i % 5 == 0:
                sum=sum+i
    return  sum






def duplicate_encode(word):
    res = []
    word = word.lower()
    print(word)
    for i in range(len(word)):
        if word.count(word[i]) >1:
            res.append(')')
        else:
            res.append('(')
        realres=""
    for i in range(len(res)):
        realres+=res[i]
    return realres


def get_count(sentence):
     res =0
     for i in sentence:
         if i == 'a' or i=='i' or i =='e' or i=='u' or i=='o':
            res = res + 1
     return res


def recoverSecret(triplets): #
    list=[]
    for item in triplets:
        for i in item:
            if i not in list:
                list.append(i)


def disemvowel(string_):
    res=[]
    for i in string_:
         if i not in ['a', 'e', 'i', 'o', 'u','A','I','E','O','U']:
             res.append(i)
    return "".join(res)


def spin_words(sentence):
    list=sentence.split(" ")
    res=[]
    for i in range(len(list)):
        if len(list[i]) >=5:
            temp=list[i]
            temp=temp[::-1]
            res.append(temp)
        else:
            res.append(list[i])
    return " ".join(res)



def find_outlier(integers):
     list_o = []
     list_j = []
     for i in range(len(integers)):
          if integers[i] % 2 ==0:
              list_o.append(integers[i])
          else:
              list_j.append(integers[i])
     print(list_j)
     print(list_o)
     if len(list_j) == 1:
         return  list_j[0];
     else:
         return list_o[0];




def digital_root(n):
    if n <10:
        return n
    sum = 0
    while n != 0:
        sum =sum+n%10
        n=n//10
    return digital_root(sum)


def array_diff(a, b):
    res = []
    for i in a:
        if i not in b:
            res.append(i)
    return  res


def tower_builder(n_floors):
    space_num=0
    xin_num=0
    str_ =""
    str = ""
    tempres=""
    list_res=[]
    for i in range(n_floors):
        str_ = ""
        str = ""
        space_num = n_floors-i-1
        xin_num= 2*i+1
        for i in range(xin_num):
            str=str+"*"
        for i in range (space_num):
            str_=str_+" "
        tempres=str_+str+str_
        list_res.append(tempres)
    return list_res





def is_pangram(s):
    temp=[]
    list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in s.upper():
        if i in list:
            temp.append(i)
    return  set(temp)==set(list)




#12

#13



def move_zeros(lst):

    a = 0
    res = []
    for i in lst:
        if i != 0:
            res.append(i)
        else:
            a=a+1
    for i in range(a):
        res.append(0)
    return res



#������Ǯ���ܺ�







def count_deaf_rats(town):

    res = 0
    ple = 0
    town_=town.replace(' ','')
    list = []
    for i in range(len(town_)):
        if town_[i] == 'P':
            ple = i
        else:
            list.append(town_[i])




def count_developers(lst):
     
    res = 0
    for i in range(len(lst)):
        
        dict= lst[i]
        
        if dict.get('continent') == 'Europe' and dict.get('language') == 'JavaScript':
            res+=1
    return res


def zero(fun = None): #your code here
    if fun:
        return fun(0)
    return 0
def one(fun = None): #your code here
    if fun:
        return fun(1)
    return 1
def two(fun = None): #your code here
    if fun:
        return fun(2)
    return 2
def three(fun = None): #your code here
    if fun:
        return fun(3)
    return 3
def four(fun = None): #your code 
    if fun:
        return fun(4)
    return 4
def five(fun = None): #your code here
     if fun:
        return fun(5)
     return 5
def six(fun = None): #your code here
     if fun:
        return fun(6)
     return 6
def seven(fun = None): #your code here
    if fun:
        return fun(7)
    return 7
def eight(fun = None): #your code here
    if fun:
        return fun(8)
    return 8
def nine(fun = None): #your code here
    if fun:
        return fun(9)
    return 9
def plus(a): #your code here
    return lambda x: x + a
def minus(a): #your code here
   return lambda x: x - a
def times(a): #your code here
    return lambda x: x * a
def divided_by(a): #your code here
    return lambda x: x // a


if __name__ == '__main__':
        #print(solution(10))23
        #print(duplicate_encode("dDIn")) # ))((
        #print(get_count("aeiou")) ##5

        # triplets = [
        #     ['t', 'u', 'p'],
        #     ['w', 'h', 'i'],
        #     ['t', 's', 'u'],
        #     ['a', 't', 's'],
        #     ['h', 'a', 'p'],
        #     ['t', 'i', 's'],
        #     ['w', 'h', 's']
        # ]
        #print(recoverSecret(triplets))
        #print(disemvowel( "This website is for losers LOL!"))#Ths wbst s fr lsrs LL!
        #print(spin_words("Hey fellow warriors")) #Hey wollef sroirraw
        #print(digital_root(493193))
        #print(array_diff([1,2,2,2,3],[2]))
        # print(tower_builder(6))
        # print(is_pangram("The quick brown fox jumps over the lazy dog "))
        # print(move_zeros([2, 0, 0, 1]))
        # print(count_deaf_rats("~O~O~O~O P"))

        # lst = [
        # { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
        # { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
        # { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
        # { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
        # ]
        # print(count_developers(lst))
        # print(eight(divided_by(three())))
        