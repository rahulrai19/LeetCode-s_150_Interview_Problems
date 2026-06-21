# LeetCode 27. Remove Element

**Difficulty:** Easy
**Pattern:** Two Pointers, Array In-Place Modification
**Asked In:** Infosys, Accenture, Cognizant, TCS, Amazon (fundamentals)

---

# 1. Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place.

Return the number of elements that are not equal to `val`.

The first `k` elements of `nums` should contain the remaining elements.

### Example

```java
Input:
nums = [3,2,2,3]
val = 3

Output:
2

nums becomes:
[2,2,_,_]
```

---

# 2. Interview Intuition

We need to remove elements **without using another array**.

### Key Observation

Keep a pointer that tracks where the next valid element should be placed.

Whenever an element is not equal to `val`, copy it to the valid position.

---

# 3. Brute Force Approach

### Idea

Create a new array and copy all elements except `val`.

### Time Complexity

```text
O(n)
```

### Space Complexity

```text
O(n)
```

Not allowed because the problem asks for in-place modification.

---

# 4. Optimized Approach (Two Pointers)

### Idea

Use:

```text
i -> traverses the array
k -> position of next valid element
```

When:

```text
nums[i] != val
```

place it at index `k` and increment `k`.

---

## Dry Run

```java
nums = [3,2,2,3]
val = 3
```

Initial

```text
k = 0
```

### i = 0

```text
nums[0] = 3
```

Ignore.

---

### i = 1

```text
nums[1] = 2
```

Store at index 0

```text
[2,2,2,3]
k = 1
```

---

### i = 2

```text
nums[2] = 2
```

Store at index 1

```text
[2,2,2,3]
k = 2
```

---

### i = 3

```text
nums[3] = 3
```

Ignore.

---

Result

```text
k = 2
```

First 2 elements:

```text
[2,2]
```

---

# 5. Optimal Java Solution

```java
class Solution {
    public int removeElement(int[] nums, int val) {

        int k = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[k++] = nums[i];
            }
        }

        return k;
    }
}
```

---

# 6. Complexity Analysis

### Time Complexity

```text
O(n)
```

Single traversal.

### Space Complexity

```text
O(1)
```

In-place modification.

---

# 7. Edge Cases

### Case 1

```java
nums = [1]
val = 1
```

Output:

```text
0
```

---

### Case 2

```java
nums = [1]
val = 2
```

Output:

```text
1
```

---

### Case 3

```java
nums = [2,2,2,2]
val = 2
```

Output:

```text
0
```

---

### Case 4

```java
nums = []
val = 1
```

Output:

```text
0
```

---

# 8. Alternative Approach (When Order Doesn't Matter)

### Idea

Swap unwanted elements with the last element.

```java
class Solution {
    public int removeElement(int[] nums, int val) {

        int n = nums.length;
        int i = 0;

        while (i < n) {
            if (nums[i] == val) {
                nums[i] = nums[n - 1];
                n--;
            } else {
                i++;
            }
        }

        return n;
    }
}
```

### Complexity

```text
Time : O(n)
Space: O(1)
```

Useful when maintaining order is not required.

---

# 9. Interview Follow-Up Questions

### Q1: Why use two pointers?

One pointer scans the array, while the other tracks where valid elements should be stored.

---

### Q2: Is the relative order preserved?

Yes, in the first solution.

---

### Q3: Which solution is faster?

The swap-with-last approach may perform fewer writes when there are many occurrences of `val`, but it does not preserve order.

---

# 10. Pattern Recognition

When the problem says:

* Remove elements in-place
* Return new length
* Do not use extra space

Think:

```text
Two Pointers + Overwrite Valid Elements
```

---

# 11. One-Line Revision Note

**Use a write pointer `k`; copy every element not equal to `val` to `nums[k]` and return `k`.**
