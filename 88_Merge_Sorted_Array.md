# LeetCode 88. Merge Sorted Array

**Difficulty:** Easy

**Pattern:** Two Pointers, Array

**Asked In:** Infosys, TCS, Accenture, 
Amazon, Microsoft, Google (fundamentals)

---

## 1. Problem Statement

You are given two sorted integer arrays `nums1` and `nums2`.

* `nums1` has length `m + n`, where the last `n` elements are `0` and should be ignored.
* `nums2` has length `n`.

Merge `nums2` into `nums1` such that `nums1` becomes one sorted array.

### Example

```java
nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

Output:
[1,2,2,3,5,6]
```

---

# 2. Interview Intuition

A beginner's approach is to copy all elements into a new array and sort it.

But the interviewer expects:

* Both arrays are already sorted.
* Extra space already exists in `nums1`.
* We should merge efficiently.

### Key Observation

If we start from the front, elements get overwritten.

Instead, start from the end where empty spaces already exist.

---

# 3. Brute Force Approach

### Idea

1. Copy all elements of `nums2` into empty positions of `nums1`.
2. Sort entire array.

### Time Complexity

```text
O((m+n) log(m+n))
```

### Space Complexity

```text
O(1)
```

(Not optimal)

---

# 4. Optimized Approach (Three Pointers)

### Idea

Use three pointers:

```text
i = m-1      -> last valid element of nums1
j = n-1      -> last element of nums2
k = m+n-1    -> last position of nums1
```

Compare larger element and place it at position `k`.

Move backwards.

---

## Dry Run

```java
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
```

Initial

```text
i = 2 -> 3
j = 2 -> 6
k = 5
```

Compare:

```text
3 vs 6
```

Place 6

```text
[1,2,3,0,0,6]
```

Move

```text
j=1
k=4
```

Compare:

```text
3 vs 5
```

Place 5

```text
[1,2,3,0,5,6]
```

Move

```text
j=0
k=3
```

Compare:

```text
3 vs 2
```

Place 3

```text
[1,2,3,3,5,6]
```

Move

```text
i=1
k=2
```

Compare:

```text
2 vs 2
```

Place 2

```text
[1,2,2,3,5,6]
```

Done.

---

# 5. Optimal Java Solution

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {

        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;

        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }

        while (j >= 0) {
            nums1[k--] = nums2[j--];
        }
    }
}
```

---

# 6. Complexity Analysis

### Time Complexity

```text
O(m + n)
```

Each element is processed once.

### Space Complexity

```text
O(1)
```

No extra array used.

---

# 7. Edge Cases

### Case 1

```java
nums1 = [0]
m = 0

nums2 = [1]
n = 1
```

Output:

```java
[1]
```

---

### Case 2

```java
nums1 = [1]
m = 1

nums2 = []
n = 0
```

Output:

```java
[1]
```

---

### Case 3

```java
nums1 = [2,0]
m = 1

nums2 = [1]
n = 1
```

Output:

```java
[1,2]
```

---

# 8. Interview Follow-Up Questions

### Q1: Why merge from the end?

Because empty spaces exist at the end of `nums1`. Merging from the front would overwrite valid elements.

---

### Q2: Can we do it in O(1) space?

Yes, this solution already uses O(1) space.

---

### Q3: What if arrays were not sorted?

First sort them, then merge.

---

# 9. Similar Problems

* Merge Two Sorted Lists
* Sort List
* Merge Intervals
* Median of Two Sorted Arrays
* Intersection of Two Arrays

---

# 10. One-Line Revision Note

**When merging two sorted arrays and extra space exists in the first array, use three pointers from the end to achieve O(m+n) time and O(1) space.**


