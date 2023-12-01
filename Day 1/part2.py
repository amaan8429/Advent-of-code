# from data import lines

lines="""eightwone""" 

numbers = {
    "one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,
}

def first_digit(s):
    for ch in s:
        if ch.isdigit():
            return ch
    return ''

def last_digit(s):
    for ch in s[::-1]:
        if ch.isdigit():
            return ch
    return ''


def part2():
    l={}
    for i in numbers:
        a = lines.find(i)
        if a > -1:
            l[a]=i
    print(l)
    new_dict = {k:l[k] for k in sorted(l)}
    print(new_dict)
    

        







# def part2():
#     for line in lines.split('\n'):
#         l = []
#         m=[]
#         for i in numbers:
#             a = line.find(i)
#             if a > -1:
#                 l.append(a)
#                 l.sort()
#         for j in 
#         print(l)
#         print(m)
                    

                

        
    
        
            
           
    
        

        
part2()

        










# for line in lines.split('\n'):





