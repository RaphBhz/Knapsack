# Knapsack
<img src="https://www.aidedd.org/dnd/images-om/bag-of-devouring.jpg" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="500" height="500" />

This project is part of my 2021 university year's project list.

In this repository you will find three possible algorithm solutions for the famous Knapsack problem.

## Greedy
The first solution is called the greedy solution. The items are ordered by their value / weight ratio. Then, the items with the best ratios are added until our knapsack is full.
The main asset of this solution is that it has a very low complexity of O(nlogn) if we include the sorting of the item list. However, its drawback is that it does not provide an
efficient solution.

## 'Best' Solution
This algorithm ...

## Optimal Solution
Finally, the optimal solution is the one that offers the real solution to our problem. It is capable of fiding the absolute perfect answer by considering all the possibilities
of the problem by examining each item. Unfortunately, its time complexity of O(2^n) prevents us from seeing solutions of really complex scenarios.
