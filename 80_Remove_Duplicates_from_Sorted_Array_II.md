# LeetCode 80. Remove Duplicates from Sorted Array II

* **Difficulty:** Medium
* **Pattern:** Two Pointers
* **Tags:** Array, In-Place Modification

---

# Problem Statement

Given a sorted integer array `nums`, remove some duplicates in-place such that each unique element appears **at most twice**.

Return the new length `k`.

The first `k` elements of `nums` should contain the final result.

---

## Example 1

```java
Input: nums = [1,1,1,2,2,3]

Output: 5

nums = [1,1,2,2,3,_]
```

---

## Example 2

```java
Input: nums = [0,0,1,1,1,1,2,3,3]

Output: 7

nums = [0,0,1,1,2,3,3,_,_]
```

---

# Intuition

In Problem 26, we allowed only one occurrence.

Here, we can keep **two occurrences**.

### Key Observation

Since the array is sorted:

```java
[1,1,1,1,2,2]
```

If the current element equals the element located **two positions before the write pointer**, it would become the third occurrence.

So we skip it.

---

# Approach (Two Pointers)

Maintain:

```text
idx = next position to write
```

The first two elements can always stay.

Start from index 2.

For each element:

```java
if(nums[i] != nums[idx - 2])
```

then it can be kept.

Store it at:

```java
nums[idx]
```

and increment `idx`.

---

# Dry Run

```java
nums = [1,1,1,2,2,3]
```

Initial:

```text
idx = 2
```

### i = 2

```text
nums[2] = 1
nums[idx-2] = nums[0] = 1
```

Same → Skip

```text
idx = 2
```

---

### i = 3

```text
nums[3] = 2
nums[idx-2] = nums[0] = 1
```

Different → Keep

```text
nums[2] = 2
idx = 3
```

Array:

```java
[1,1,2,2,2,3]
```

---

### i = 4

```text
nums[4] = 2
nums[idx-2] = nums[1] = 1
```

Different → Keep

```text
nums[3] = 2
idx = 4
```

---

### i = 5

```text
nums[5] = 3
nums[idx-2] = nums[2] = 2
```

Different → Keep

```text
nums[4] = 3
idx = 5
```

Result:

```java
[1,1,2,2,3,_]
```

Return:

```java
5
```

---

# Java Solution

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int idx = 2;
        for(int i=2;i<nums.length;i++){
            if(nums[i]!=nums[idx-2]){
                nums[idx] = nums[i];
                idx++;
            }
        }
        return idx;
    }
}
```

---

# Complexity Analysis

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

# Why Compare With idx - 2?

Suppose:

```java
[1,1]
```

already exists in valid portion.

Current element:

```java
1
```

If we insert it:

```java
[1,1,1]
```

which violates the rule.

Checking:

```java
nums[i] == nums[idx - 2]
```

detects the third occurrence immediately.

---

# Pattern Recognition

Whenever the question says:

* Sorted Array
* Keep at most K duplicates

Think:

```text
Compare current element with nums[idx - K]
```

For this problem:

```text
K = 2
```

---

# Similar Problems

* LeetCode 26 – Remove Duplicates from Sorted Array
* LeetCode 27 – Remove Element
* LeetCode 283 – Move Zeroes

---

# Interview Follow-Up

### What if each number can appear at most 3 times?

Replace:

```java
nums[idx - 2]
```

with

```java
nums[idx - 3]
```

and initialize:

```java
idx = 3
```

---

# One-Line Revision Note

**For a sorted array allowing at most two duplicates, keep an element only if it differs from `nums[idx - 2]`; this guarantees no element appears more than twice.**
