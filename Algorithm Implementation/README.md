AI Search Algorithms Documentation 
Chapter 3: Uniformed and Informed Search Algorithms 
1. Breadth-First Search (BFS) 
● Type: Uniformed Search 
● Idea: Explore all neighbors level by level. 
● Data Structure: Queue 
● Time Complexity: O(b^d) 
● Space Complexity: O(b^d) 
● Where: b = branching factor, d = depth of the shallowest goal 
● Example Graph: 
A 
/ \ 
B   C 
/     
\ 
D       E 
\ 
G 
● Start: A, Goal: G 
● Steps: A → B, C → D, E → G 
● Explanation: All nodes are explored level-by-level. G is found at level 3. 
2. Depth-First Search (DFS) 
● Type: Uniformed Search 
● Idea: Explore as deep as possible along one branch before backtracking. 
● Data Structure: Stack or Recursion 
● Time Complexity: O(b^m) where m is the maximum depth 
● Space Complexity: O(bm) 
● Example Graph: 
A 
| 
B 
| 
D 
| 
G 
● Start: A, Goal: G 
● Steps: A → B → D → G 
● Explanation: It goes deep down one path until it finds the goal or has to backtrack. 
3. Iterative Deepening Search (IDS) 
● Type: Uniformed Search 
● Idea: Combines DFS's space efficiency and BFS's completeness 
● Time Complexity: O(b^d) 
● Space Complexity: O(bd) 
● How it works: Runs DFS with depth limit = 0, 1, 2... until goal is found 
● Example: If goal is at depth 3, IDS does DFS with limit 0, 1, 2, 3 until goal is found 
 
4. Bidirectional Search 
● Type: Uniformed Search 
 
● Idea: Runs two searches — one from start and one from goal — and meets in middle 
 
● Time Complexity: O(b^(d/2)) 
 
● Space Complexity: O(b^(d/2)) 
 
● Example Graph: 
 
Start: A → C → D ← E ← G :Goal 
 
● Explanation: Two searches meet at D 
 
 
5. Depth-Limited Search (DLS) 
● Type: Uniformed Search 
 
● Idea: DFS with a depth limit to avoid going too deep 
 
● Time Complexity: O(b^l) where l is the limit 
 
● Example Graph: 
 
   A 
   / \ 
  B   C 
 /     \ 
D       E 
         \ 
          G 
 
● Explanation: If depth limit = 2, G at depth 3 won't be found 
 
6. Heuristic Search (Greedy Best-First) 
● Type: Informed Search 
● Idea: Selects node with lowest heuristic value (h(n)) 
● Time Complexity: O(b^m) 
● Example Graph: 
A 
|\ 
B C D 
(h=4)(h=2)(h=1) 
● Explanation: Chooses D based on lowest heuristic value 
7. Best-First Search 
● Type: Informed 
● Similar to: Greedy Search but may consider path cost 
● Time Complexity: O(b^m) 
● Example: Same graph as above, but may include edge cost to calculate total cost 
8. A Search Algorithm* 
● Type: Informed 
● Idea: Uses f(n) = g(n) + h(n) 
● g(n) = cost so far, h(n) = estimated cost 
● Time Complexity: Exponential in worst-case (O(b^d)) 
● Optimal: Yes, if h(n) is admissible 
● Example Graph: 
A 
/ \ 
B     C 
(g=1,h=3)(g=2,h=2) 
● Explanation: Chooses node with lowest f(n) = g(n) + h(n) 
9. AO Algorithm* 
● Type: Informed Search (AND-OR Graphs) 
● Idea: Solves problems that can be split into subproblems (like plans) 
● Time Complexity: Depends on branching + solution cost 
● Example Graph: 
A 
/ \ 
AND  OR 
/  \    \ 
B    C    D 
|    
| 
E    F 
● Explanation: Selects path based on combined cost and AND/OR requirements 
Chapter 4: Local Search Algorithms 
10. Hill Climbing 
● Type: Local Search 
● Idea: Keep moving to neighbor with better heuristic 
● Time Complexity: O(n) where n = number of steps till peak 
● Example Graph: 
A(h=6) 
| 
B(h=4) 
| 
D(h=2) 
● Explanation: Climb to lower heuristic. May stop at local maxima. 
11. Beam Search 
● Type: Informed, Local Search 
● Idea: Keep only k best nodes at each level (beam width) 
● Time Complexity: O(kd) 
● Example Graph: 
A 
/ | \ 
B  C  D 
● Beam width = 2 
● Explanation: Keeps top 2 nodes and ignores others 
Chapter 5: Adversarial Search 
12. Minimax Algorithm 
● Type: Adversarial Search 
● Used in: Games like Tic Tac Toe, Chess 
● Idea: Max tries to maximize score, Min tries to minimize it 
● Time Complexity: O(b^d) 
● Example Tree: 
MAX 
/   
\ 
MIN   MIN 
/ \   /  \ 
3   5  2   9 
● Result: MAX picks 5 from left MIN and 9 from right MIN → picks 5 
13. Alpha-Beta Pruning 
● Improvement of: Minimax 
● Idea: Skip branches that won’t affect the final decision 
● Time Complexity: O(b^(d/2)) best case 
● Example: 
MAX 
|-- MIN (3) 
|   
|-- (alpha) 
|-- MIN (pruned) 
● Explanation: Prunes part of tree where better outcome already guaranteed 
Let me know if you need real code examples or visual illustrations! 
