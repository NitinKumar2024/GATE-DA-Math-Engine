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