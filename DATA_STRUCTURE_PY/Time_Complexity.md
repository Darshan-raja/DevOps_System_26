What is Time complexity?

Time complexity is a concept in computer science that describes the performance or complexity of an algorithm in terms of the amount of time it takes to run as a function of the size of the input to the program. It is a mathematical property of an algorithm that measures the amount of time taken by an algorithm to run as the size of the input increases.




| Complexity        | Growth Rate    | Typical Use Case                     |
|-------------------|----------------|--------------------------------------|
| `O(1)`            | Constant        | Array access                         |
| `O(log n)`        | Logarithmic     | Binary search                        |
| `O(n)`            | Linear          | Linear search                        |
| `O(n log n)`      | Linearithmic    | Merge sort, Quick sort               |
| `O(n^2)`          | Quadratic       | Bubble sort, nested loops            |
| `O(n^3)`          | Cubic           | Matrix operations                    |
| `O(2^n)`          | Exponential     | Recursive brute-force algorithms     |
| `O(n!)`           | Factorial       | Permutations, combinatorial problems |
| `O(2^{2^n})`      | Double Exponential | Advanced logic/automata problems  |


✅ What does count in Space Complexity?
1. Simple Variables (like count = 0)

Yes — they are counted, but they use constant space, so:

🟢 count = 0 → Space Complexity: O(1)
Because it always takes the same space, no matter if your input is 10 or 10,000 elements.
