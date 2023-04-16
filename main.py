 
from math import floor
from operator import le
from os.path import join
from queue import Empty
from turtle import width


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
def count_deaf_rats(town):
    total = town.replace(' ', '')
    splitP = total.split('P')
  
    left = 0
    right = 0

    # 遍历每个老鼠来�?�查它�?否耳聋
    for i in range(0,len(splitP[0]),2):
        if splitP[0][i:i+2] == 'O~':
            left +=1
    for i in range(0,len(splitP[1]),2):
        if splitP[1][i:i+2] == '~O':
            right +=1

    return left + right
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







def countDeafRats(town):
    total = town.replace(' ', '')
    splitP = total.split('P')
  
    left = 0
    right = 0

    # ����ÿ��������������Ƿ����
    for i in range(0,len(splitP[0]),2):
        if splitP[0][i:i+2] == 'O~':
            left +=1
    for i in range(0,len(splitP[1]),2):
        if splitP[1][i:i+2] == '~O':
            right +=1

    return left + right





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



def shorten_number(suffixes, base):
    def process_number(n):
        try:
            number = int(n)
        except:
            return str(n)
        if number < base:
            return str(number)+suffixes[0]
        i = 0
        while number >= base and i < len(suffixes) - 1:
            number /= base
            i += 1
        return '{:.0f}{}'.format(int(number), suffixes[i])
    return process_number

     

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def  is_worth_it(self):
        temp = self.draft - (self.crew*1.5)
        if temp > 20:
            return True
        else:
            return False



class Block:
        def __init__(self,param):
            self.width = param[0]
            self.length = param[1]
            self.height = param[2]
            self.volume = param[0]*param[1]*param[2]
            self.surface_area=2*param[0]*param[1]+2*param[1]*param[2]+2*param[0]*param[2]

        def get_width(self):
             return self.width

        def get_length(self):
            return self.length

        def get_height(self):
            return  self.height


        def get_volume(self):
            return  self.volume

        def get_surface_area(self):
            return self.surface_area
      
         




def naughty_or_nice(data):
             
            res  =0
            for _vals in data.values():
                for val in _vals.values():
                    if val == "Naughty":
                        res+=1
                    else: res-=1
            
            if res > 0:return 'Naughty!'
            else : return 'Nice!'
            
# TODO: complete this class

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.list = collection
        self.max_items = items_per_page
        self.page = len(self.list)//self.max_items
        if  len(self.list)%self.max_items != 0:
            self.page +=1
        

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.list)

    # returns the number of pages
    def page_count(self):
        return self.page

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if (page_index+1) > self.page:return -1
        elif (page_index+1) == self.page:
            temp  = len(self.list)
            return  temp - (self.max_items*(temp-1))
        else:return self.max_items


    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        temp  =len(self.list)
        if temp < (item_index+1): return -1
        else:
            t= (item_index+1)//self.max_items
            if (item_index+1)%self.max_items !=0:t+=1
            return t-1

def hamming(n):
    ham_list = [1]
    i2, i3, i5 = 0, 0, 0
    for i in range(1, n):
        m = min(ham_list[i2]*2, ham_list[i3]*3, ham_list[i5]*5)
        ham_list.append(m)
        if ham_list[i] == ham_list[i2]*2:
            i2 += 1
        if ham_list[i] == ham_list[i3]*3:
            i3 += 1
        if ham_list[i] == ham_list[i5]*5:
            i5 += 1
    return ham_list[n-1]



# def merge_sort(left, right,arr):
     
#         mid = left+right>>1
#         if  left == right: return 0
#         merge_sort(left, mid,arr)
#         merge_sort(mid+1,right,arr)

#         i=left
#         j = mid+1
#         q=[]
#         temp =0
#         while i <= mid and j <=right:
#             if arr[i] > arr[j]: 
#                 temp = mid-i+1
#                 q.append(arr[j])
                


            
class Vector:
    def __init__(self, components):
        self.components = components
        
    def __str__(self):
        return '({})'.format(','.join(str(x) for x in self.components))
    
    def equals(self, other):
        return self.components == other.components
    
    def add(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of equal length to add")
        new_components = [x + y for x, y in zip(self.components, other.components)]
        return Vector(new_components)
        
    def subtract(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of equal length to subtract")
        new_components = [x - y for x, y in zip(self.components, other.components)]
        return Vector(new_components)
        
    def dot(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of equal length to take the dot product")
        dot_product = sum([x * y for x, y in zip(self.components, other.components)])
        return dot_product
    
    def norm(self):
        squared_sum = sum([x ** 2 for x in self.components])
        return squared_sum ** 0.5



    


#     return res




def smaller(nums):
    def merge_sort(enum):
        mid = len(enum) // 2
        if mid:
            left, right = merge_sort(enum[:mid]), merge_sort(enum[mid:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
    smaller = [0] * len(nums)
    merge_sort(list(enumerate(nums)))
    return smaller
    


    
if __name__ == '__main__':
        print("hello world")
        #print(solution(10))23
        # print(duplicate_encode("dDIn")) # ))((
        # print(get_count("aeiou")) ##5

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
        # filter1 = shorten_number( ['pippi', 'TB', 'k', 'PB', 'mm'],1839); 
        # print(filter1('43'))
        # EmptyShip =   Ship(0,0)
        # print(EmptyShip.is_worth_it())
        # b = Block([2,4,6]) #-> create a `Block` object with a width of `2` a length of `4` and a height of `6`

        # print(b.get_width()) #-> return 2

        # print(b.get_length())# -> return 4

        # print(b.get_height()) #-> return 6

        # print(b.get_volume()) #-> return 48

        # print(b.get_surface_area()) #-> return 88
        # test = {'January': {'1': 'Naughty','2': 'Naughty',  '31': 'Nice'},'February': {
        # '1': 'Nice','2': 'Naughty', '28': 'Nice'}} 
        # print(naughty_or_nice(test))
        # helper = PaginationHelper(['a','b','c','d','e','f'], 4)
        # helper.page_count() # should == 2
        # helper.item_count() # should == 6
        # helper.page_item_count(0)  # should == 4
        # helper.page_item_count(1) # last page - should == 2
        # helper.page_item_count(2) # should == -1 since the page is invalid

        # # page_index takes an item index and returns the page that it belongs on
        # helper.page_index(5) # should == 1 (zero based index)
        # helper.page_index(2) # should == 0
        # helper.page_index(20) # should == -1
        # helper.page_index(-10) # should == -1 because negative indexes are invalid


        # print(hamming(1))
        # print(hamming(2))
        # print(hamming(3))
        # print(hamming(4))
        arr =[5, 4, 3, 2, 1]
        print( '({})'.format(', '.join(str(arr) for x in arr)))

    # print(smaller(arr))
