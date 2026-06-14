**Topic: Storage Architecture & B+ Trees**

**1. The Structural Law of B+ Trees**

* **Strict Separation:** Internal nodes *only* store search keys and tree pointers (to guide the search). Leaf nodes *only* store search keys and data pointers (to the actual disk blocks).
* **Perfect Balance:** Every single path from the root to any leaf node is the exact same length. The search time is always predictable ($O(\log n)$).
* **The Sequential Link:** Every leaf node is sequentially linked to the next leaf node via a pointer. This makes **Range Queries** (e.g., `Salary BETWEEN 50000 AND 80000`) blazing fast because the engine just drops to the first leaf and walks straight across the chain.

**2. The Mathematical Order ($p$)**

* The **Order** (represented as $p$ or $n$) is the maximum number of children (pointers) a single node can hold.
* If a node has Order $p$:
* It can hold a maximum of **$p$ pointers**.
* It can hold a maximum of **$p - 1$ keys**.



**3. 🚀 The GATE DA Block Equation (Memorize This!)**
When you build a node, it must fit perfectly inside one physical Disk Block. If it spills over, you double your Disk I/O.
To calculate the maximum Order ($p$) of an **Internal Node**, use this exact equation:

$$(p \times \text{Pointer Size}) + ((p - 1) \times \text{Key Size}) \le \text{Block Size}$$

*(Why? Because one node contains $p$ pointers pointing to children, and $p-1$ keys separating those pointers, and all of those bytes combined cannot exceed the size of the hard drive block.)*

---
**Topic: Storage Architecture & Dynamic Hashing**

**1. The Goal of Hashing**

* To bypass tree traversals entirely and find a physical hard drive block in exactly **$O(1)$ time** using a mathematical Hash Function.

**2. Static Hashing (The Flaw)**

* A fixed number of disk blocks (buckets) are allocated.
* **The Collision Crash:** When multiple records hash to the same bucket, it overflows. The engine creates a linked list of overflow blocks. Search time violently degrades from $O(1)$ to **$O(n)$** because the engine has to scan the linked list.

**3. Extendible Hashing (The GATE Standard)**

* A dynamic structure that uses a **Directory** (stored in RAM) to point to physical **Buckets** (stored on Disk). It uses the binary representation of the hash value to route data.
* **Global Depth ($d$):** The number of binary bits the *Directory* is currently looking at. The Directory always has exactly **$2^d$ entries**.
* **Local Depth ($l$):** The number of binary bits a *specific Bucket* is looking at.
* *Rule:* Local Depth can never be greater than Global Depth ($l \le d$).

**4. 🚀 The GATE DA Splitting Rules (Memorize This!)**
When a new record is inserted and its target Bucket is completely full (Overflow), the engine checks the depths:

* **Scenario A (Local < Global):** $l < d$.
* The directory is already big enough. The engine simply splits the overflowing bucket into two new buckets, increments the Local Depth ($l = l + 1$) for those specific buckets, and redistributes their keys. **The Directory does NOT double.**


* **Scenario B (Local = Global):** $l = d$.
* The directory is maxed out. The engine is forced to **double the entire Directory** ($d = d + 1$), creating $2^d$ new pointers in RAM. Then, it splits the overflowing bucket, increments its Local Depth ($l = l + 1$), and redistributes the keys.



---
