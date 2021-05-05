import urllib.request
#import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return booktxt.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    lst = book_to_words(book_url)
    radix_sort(lst)
    return lst

def sort(lst, d = 0):
    l = len(lst)
    if d == 0:
        for i in range(1, l):
            for j in range(1, l):
                if lst[j-1][d].encode('ascii', 'replace') > lst[j][d].encode('ascii', 'replace'):
                    lst[j], lst[j-1] = lst[j-1], lst[j]
    else:
        for i in range(1, l):
            for j in range(1, l):
                if lst[j-1][d].encode('ascii') > lst[j][d].encode('ascii') and lst[j-1][d-1] == lst[j][d-1]:
                    lst[j], lst[j-1] = lst[j-1], lst[j]
    


def radix_sort(lst, s = 35):
    for i in range(len(lst)):
        while len(lst[i]) < s:
            lst[i] += ' '
    for d in range(0, s):
        sort(lst, d)
    for j in range(len(lst)):
        lst[j] = lst[j].replace(' ', '')

    


################################################
#TESTING
################################################
    
def main():
    lst = ['peepoo', 'ball', 'poo', 'fart', 'penis', 'cum', 'poopoo', 'poopee', 'bitch', 'poop']
    radix_sort(lst)
    print(lst)
    print(radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt')[0:200])

if __name__ == '__main__':
    main()
