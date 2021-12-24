#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Enter the text: ")
    i = s.count('+')
    j = s.count('-')
    counter = i + j

print("The number of '-' and '+': ", counter)
