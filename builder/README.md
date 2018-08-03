# Barb the Builder

## Problem Statement

Barb the builder has been presented with a request to build a house with
rectangular rooms.

Now, Barb's idea is to represent the house as a matrix consisting of N rows and
M columns where each cell has unit area. The rows are numbered 1 to N from top
to bottom; columns are numbered 1 to M from left to right.

Her plan is to create vertical and horizontal intersecting walls in some rows
and columns. For example, if we denote empty cells with the character `.` and a
wall block with the character `*`, the following depicts the case when n = m = 5
and Barb decides to create walls in the 2nd and 4th rows and similarly for
columns:

```
.*.*.
*****
.*.*.
*****
.*.*.
```

This would create rooms of closed areas (consisting of at least one empty cell)
and open areas which have at least one open boundary. In the above example, we
can see that there is only one room of 1 area unit.

Now, the client comes to Barb and gives her an integer K and asks Barb to
calculate the area of the Kth smallest room in the building.

Write a function which takes the following inputs:

  - Two integers N and M (1 ≤ N, M ≤ 10^6)
  - A tuple R consisting of P (1 ≤ P ≤ 10^4) integers R_1, R_2, ..., R_P
    (1 ≤ R_i ≤ N) in increasing order — denoting that Barb builds a wall in rows
    R_1, R_2, ..., R_p
  - A tuple C consisting of Q (1 ≤ Q ≤ 10^4) integers C_1, C_2, ..., C_Q
    (1 ≤ C_i ≤ M) in increasing sequence — denoting that Barb builds a wall in
    columns C_1, C_2, ..., C_Q
  - An integer K (K ≥ 1) denoting the rank of the area of the required room.

and outputs the area of the required room. It is guaranteed that there exists at
least one room and that K doesn't exceed the number of rooms.

For example, the output of `solution(5, 5, (2, 4), (2, 4), 1)` should be 1.

## My Solution

This one turned out to be harder than it first seemed. This is because my first solution (putting the areas in a big list then sorting it) used too much memory.

To work around this, I instead created a dictionary with the keys as the area and the value as the number of rooms with that area. This meant that data was no longer being repeated over and over, and ran fine.
I also did a similar thing when calculating the widths and heights of the rooms, though this may not have been strictly neccessary in the end.
