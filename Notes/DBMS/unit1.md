**Topic: Functional Dependencies (The DNA of a Table)**

**1. Definition and Notation**

* **Concept:** A strict mathematical constraint between two sets of attributes in a database table.
* **Notation:** $X \rightarrow Y$ (Read as: "X functionally determines Y").
* **Terminology:** * $X$ is the **Determinant**.
* $Y$ is the **Dependent**.



**2. The Duplicate Rule (The GATE Validator)**
To prove if $X \rightarrow Y$ is mathematically valid inside a table, apply this strict rule:

* If two tuples (rows) have the **exact same value for $X$**, they **MUST have the exact same value for $Y$**.
* If $X_{1} = X_{2}$, then $Y_{1}$ MUST equal $Y_{2}$.
* *Failure State:* If you see "Raj" map to "CS" in one row, and "Raj" map to "EE" in another row, the dependency is broken and invalid.

**3. Types of Dependencies**

* **Trivial Dependency:** $X \rightarrow Y$ is trivial if $Y$ is a subset of $X$.
* *Example:* $\{Roll\_No, Name\} \rightarrow Name$. (This is always valid by default).


* **Non-Trivial Dependency:** $X \rightarrow Y$ where $Y$ is not a subset of $X$.
* *Example:* $Roll\_No \rightarrow Dept$. (This is the type we care about for Normalization).



---

**Topic: Armstrong’s Axioms & Attribute Closure ($X^+$)**

**Part 1: Armstrong’s Axioms (The Rules of Manipulation)**
These are the mathematical laws used to find hidden Functional Dependencies.

* **The 3 Primary Rules:**
1. **Reflexivity:** If $Y$ is a subset of $X$, then $X \rightarrow Y$. *(A set can always determine a piece of itself).*
2. **Augmentation:** If $X \rightarrow Y$, then $XZ \rightarrow YZ$. *(You can attach the same attribute to both sides).*
3. **Transitivity:** If $X \rightarrow Y$ and $Y \rightarrow Z$, then $X \rightarrow Z$. *(The chain reaction).*


* **The 2 Derived Rules:**
4. **Union:** If $X \rightarrow Y$ and $X \rightarrow Z$, then $X \rightarrow YZ$. *(You can safely combine the right side).*
5. **Decomposition:** If $X \rightarrow YZ$, then $X \rightarrow Y$ and $X \rightarrow Z$.
* **GATE FATAL TRAP:** You can split the right side. You can **NEVER** split the left side. (If $AB \rightarrow C$, you cannot say $A \rightarrow C$ and $B \rightarrow C$).



**Part 2: The Attribute Closure Algorithm ($X^+$)**

* **Definition:** $X^+$ is the complete set of all attributes that can be mathematically determined by $X$.
* **The Goal:** To find the **Candidate Key**.

**The Step-by-Step Execution:**

1. Pick your starting attribute(s), let's call it $X$.
2. Initialize your closure set with itself: $X^+ = \{X\}$
3. Scan your list of given Functional Dependencies (FDs).
4. If the left side of an FD is completely contained inside your current $X^+$, add the right side of that FD to your $X^+$.
5. Repeat Step 3 and 4 until the $X^+$ stops growing.
6. **The Candidate Key Test:** If your final $X^+$ contains **every single attribute** in the table, then $X$ is officially a Candidate Key.


**The Essential Attribute Rule:**
If an attribute is completely missing from the Right-Hand Side (RHS) of all given Functional Dependencies, it is an Essential Attribute.
An Essential Attribute MUST be a part of every single Candidate Key you find. You calculate the closure of the Essential Attribute first. If it doesn't give you all columns, you start combining it with the left-hand side attributes (like $W$ and $X$) until it does.

---
**Topic: Normalization - 1NF, Attribute Classification, and 2NF**

**1. First Normal Form (1NF): The Atomicity Rule**

* **The Rule:** Every attribute (column) in a table must hold **atomic (indivisible) values**.
* **The Violation:** No arrays, no comma-separated lists, and no multi-valued attributes in a single cell.
* *Example:* A column `Skills` containing `Python, Java, C++` in one row violates 1NF.

**2. The GATE Classifier: Prime vs. Non-Prime**
Before testing for 2NF or 3NF, you must calculate the Candidate Key(s) and divide your columns into two camps:

* **Prime Attribute:** Any column that is a part of **ANY** Candidate Key.
* **Non-Prime Attribute:** Any column that is **NOT** a part of any Candidate Key.

**3. Second Normal Form (2NF): The Partial Dependency Rule**

* **The Prerequisite:** The table must already be in 1NF.
* **The Rule:** There must be **ZERO Partial Dependencies**.
* **What is a Partial Dependency?** It happens when a *proper subset* of a composite Candidate Key functionally determines a Non-Prime attribute.
* **Mathematical Violation Pattern:** $Proper\_Subset\_of\_CK \rightarrow Non\_Prime\_Attribute$
* *Translation:* A non-key column shouldn't depend on just "half" of the Primary Key. It must depend on the whole key.



**4. 🚀 The Ultimate GATE Shortcut (2NF)**

* If the Candidate Key of a table consists of only a **single attribute** (e.g., $CK = \{Roll\_No\}$), it is mathematically impossible to have a proper subset.
* **Conclusion:** Any table with a single-attribute Candidate Key is **automatically in 2NF**.

---

The notebook is unlocked. We are now in the 'Effective notes' phase of your learning framework.

Copy these exact rules down. The mathematical formula for 3NF is arguably the most important shortcut you will memorize for your GATE DA exam. It completely bypasses the need to manually trace messy transitive dependencies.

---
**Topic: Third Normal Form (3NF) & Transitive Dependencies**

**1. The Prerequisites**

* The table must already satisfy **1NF** and **2NF**.

**2. The Core Rule: No Transitive Dependencies**

* **Definition:** A transitive dependency occurs when a Non-Prime attribute determines another Non-Prime attribute.
* **Mathematical Violation:** $Non\_Prime \rightarrow Non\_Prime$
* *Example:* $Emp\_ID \rightarrow Dept\_ID$, and $Dept\_ID \rightarrow Location$. (Here, changing a department's location forces you to update every employee's record, causing data anomalies).

**3. 🚀 The Ultimate GATE 3NF Formula**
To prove a table is in 3NF, examine **every single Functional Dependency** ($X \rightarrow Y$). For the table to pass, **every** FD must satisfy at least **ONE** of the following two conditions:

* **Condition 1 (Left Side):** $X$ is a Super Key or Candidate Key.

*If an FD fails both Condition 1 and Condition 2, the table instantly fails 3NF.*

**4. The GATE "Prime-RHS" Exception**

* Examiners will try to trick you with an FD where the left side is clearly not a key. Do not immediately fail it! Always check the right side. If the right side is a Prime Attribute, the FD is mathematically protected and **passes 3NF**.

---

The notebook is unlocked. We are finalizing the 'Effective notes' phase for the normalization hierarchy. Let's see this through to the absolute end.

Copy these final architectural laws. Because BCNF is the strictest normal form, it is also the fastest to test during an exam if you know exactly where to look.

---
**Topic: Boyce-Codd Normal Form (BCNF)**

**1. The Prerequisite**

* The table must already mathematically satisfy **3NF**.

**2. The Absolute Law of BCNF**

* For every non-trivial Functional Dependency ($X \rightarrow Y$), the Left Side ($X$) **MUST** be a Super Key or Candidate Key.

**3. The GATE DA Execution Strategy**

* **No Exceptions:** BCNF completely deletes the "Right Side is Prime" loophole from 3NF.
* **The Speed Test:** Do not even look at the right side of the arrow. Scan the left side of every single FD. If you see a left side that is not a Candidate Key, the table instantly fails BCNF.

**4. 🚀 The Ultimate GATE Shortcuts (BCNF)**

* If a table is in BCNF, it is mathematically guaranteed to be in 3NF, 2NF, and 1NF.
* **The 2-Attribute Rule:** Any relation with exactly two attributes (e.g., `R(A, B)`) is **always** in BCNF, regardless of the dependencies.

---

---
**Topic: Lossless Join Decomposition & Spurious Tuples**

**1. The Core Hazard: Spurious Tuples**

* **Definition:** Fake, mathematically generated rows that appear when a database engine tries to join two poorly decomposed tables together.
* **Cause:** Joining tables on a common column that contains duplicate values (is not a key). This causes a cross-multiplication of matching records, corrupting the original data state.

**2. The 3 Mathematical Laws of Lossless Decomposition**
If a relation $R$ is decomposed into two sub-relations, $R_1$ and $R_2$, the split is guaranteed to be **Lossless** if and only if it satisfies all three conditions:

* **Law 1: The Attribute Preservation (Union Rule)**

$$R_1 \cup R_2 = R$$



*Meaning:* Every column from the original table must be present in the new sub-tables. No attributes can be dropped or lost.
* **Law 2: The Common Attribute (Intersection Rule)**

$$R_1 \cap R_2 \neq \emptyset$$



*Meaning:* The sub-tables must share at least one common attribute. A completely disjoint split cannot be joined back together.
* **Law 3: The Key Constraint (The GATE Golden Rule)**

$$(R_1 \cap R_2) \rightarrow R_1 \quad \text{OR} \quad (R_1 \cap R_2) \rightarrow R_2$$



*Meaning:* The common attribute (the intersection) **must** be a Super Key or Candidate Key in at least **one** of the decomposed relations.

---

---

### 🚀 Quick-Check Elimination Strategy for Exams

When checking a question for lossless join properties:

1. Instantly scan for a common attribute between the split schemas. If none exists, stop—it's **Lossy**.
2. Find the closure of that common attribute *only within the functional dependencies that apply to that specific sub-table*.
3. If it cannot determine all columns of either $R_1$ or $R_2$, it is **Lossy**.

---
**Topic: Dependency Preservation in Decomposition**

**1. The Core Objective**

* When a table $R$ is decomposed into sub-tables ($R_1, R_2, ... R_n$), every single original Functional Dependency (FD) must still be enforceable **without** joining the tables back together.

**2. The Law of Direct Preservation**

* An FD ($X \rightarrow Y$) is **directly preserved** if both $X$ and $Y$ belong to the exact same decomposed sub-table ($R_i$).
* *Example:* If $A \rightarrow B$, and we have a sub-table $R_1(A, B, C)$, the dependency is preserved. If we only have $R_1(A, C)$ and $R_2(B, D)$, the dependency is lost.

**3. The Indirect Preservation Rule (The GATE Trap)**

* If an FD ($X \rightarrow Y$) is split across tables, do not immediately fail it!
* You must check if the lost FD can be **logically derived** (using Transitivity or Armstrong's Axioms) from the FDs that *were* successfully preserved in the sub-tables. If it can be derived, the decomposition is still Dependency Preserving.

**4. 🚀 The Ultimate GATE Normalization Trade-Off (Memorize This!)**
This is a guaranteed 1-mark or 2-mark theoretical question in GATE DA:

* **Third Normal Form (3NF):** It is mathematically guaranteed that you can always achieve a decomposition into 3NF that is **BOTH** Lossless and Dependency Preserving.
* **Boyce-Codd Normal Form (BCNF):** It is mathematically guaranteed to be Lossless. However, **BCNF does NOT guarantee Dependency Preservation.** Sometimes, to reach perfect BCNF architecture, you are mathematically forced to sacrifice a dependency.

---