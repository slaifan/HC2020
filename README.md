# HC2020

This project is for designing an algorithm to be used in Google Hashcode 2020 coding competition.
The full details of the challenge can be found in the pdf file in this repo.

## Summary:
Given a description of libraries and books available, plan which books to scan from
which library to maximize the total score of all scanned books, taking into account that
each library needs to be signed up before it can ship books.

## How It Works:
This solution takes a greedy approach. It first sorts the Libraries based on their potential worth in a descending order.
the algorithm then gets _lifetime number of books_ of first (most valuable) Library by calculating

__lifetime value = scan rate * days till deadline after registration__ 

Then it iterates over the next Library and removes the books that have already been scheduled to be scanned and adds the next most valuable books in that Library to the list.
Then it does the same for all Libraries that can be scanned before time runs out.

## Scores:
1. example: 21
1. read on: 5,822,900
1. incunabula: 3,493,443
1. tough choices: 3,493,945
1. so many books: 71,170
1. libraries of the world: 13,512

__TOTAL: 12,894,991__

## Authors:
- [Feysal Kethuda](https://github.com/slaifan)
- [George Bakewell](https://github.com/theonlygusti)
- [Michael Combs](https://github.com/m10653)
- [Maxim Echemenda](https://github.com/maximechemenda)
