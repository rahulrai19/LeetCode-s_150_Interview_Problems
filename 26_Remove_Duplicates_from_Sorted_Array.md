 **LeetCode 26: Remove Duplicates from Sorted Array**

### Intuition

Since the array is already sorted:

```java
[0,0,1,1,1,2,2,3,3,4]
```

Duplicates will always be adjacent.

We maintain:

* `i` → scans the array
* `idx` → position where the next unique element should be placed

Whenever we find a new unique element, we place it at `nums[idx]` and increment `idx`.

---

### Dry Run

```java
nums = [1,1,2]
```

Initial:

```java
i = 1
idx = 1
```

#### i = 1

```java
nums[idx-1] = nums[0] = 1
nums[i] = 1
```

Same → skip

```java
idx = 1
```

#### i = 2

```java
nums[idx-1] = nums[0] = 1
nums[i] = 2
```

Different

```java
nums[1] = 2
idx = 2
```

Array becomes:

```java
[1,2,_]
```

Return:

```java
2
```

---

### Complexity

#### Time

```text
O(n)
```

Single traversal.

#### Space

```text
O(1)
```

In-place modification.

---

### Slightly More Common Interview Version

Most candidates write:

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length == 0) return 0;

        int idx = 1;

        for(int i = 1; i < nums.length; i++) {
            if(nums[i] != nums[idx - 1]) {
                nums[idx++] = nums[i];
            }
        }

        return idx;
    }
}
```

---

### Important Interview Question

Why compare with `nums[idx - 1]` instead of `nums[i - 1]`?

Because `idx - 1` always points to the **last unique element stored in the result portion** of the array.

After modifications, `nums[i-1]` may not represent the last unique element.

---

### One-Line Revision Note

**For a sorted array, keep a write pointer `idx`; whenever `nums[i] != nums[idx-1]`, store it at `nums[idx]` and increment `idx`.**
