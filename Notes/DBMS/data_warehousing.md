**Topic: Data Transformation & Normalization**

**1. Min-Max Normalization**

* **The Objective:** Maps data linearly to a specific bounded range, most commonly $[0, 1]$. It preserves the exact relationships among the original data values.
* **The General Formula:**

$$x_{new} = \frac{x - x_{min}}{x_{max} - x_{min}} \times (new\_max - new\_min) + new\_min$$


* **The Standard Formula (for a $[0, 1]$ range):**

$$x_{new} = \frac{x - x_{min}}{x_{max} - x_{min}}$$


* **The Architectural Flaw:** It is catastrophically sensitive to outliers. A single massive outlier artificially inflates the $x_{max}$ denominator, which aggressively compresses all the *normal* data points into a tiny, indistinguishable cluster near zero.

**2. Z-Score Normalization (Standardization)**

* **The Objective:** Scales data based on its statistical variance rather than fixed boundaries.
* **The Formula:**

$$x_{new} = \frac{x - \mu}{\sigma}$$



*(Where $\mu$ is the Mean and $\sigma$ is the Standard Deviation).*
* **The Mathematical Guarantee:** After a Z-Score transformation, the new feature column will *always* have a **Mean ($\mu$) exactly equal to $0$** and a **Standard Deviation ($\sigma$) exactly equal to $1$**.
* **The Advantage:** It handles outliers gracefully. An outlier does not crush the surrounding data; it simply receives a very high positive or negative Z-Score (e.g., $+4.5$), while the bulk of the data safely distributes around $0$.

**3. 🚀 The GATE DA Selection Heuristics**

* If an algorithm requires strictly bounded inputs (e.g., Neural Network activation functions expecting values between $0$ and $1$) $\rightarrow$ **Use Min-Max**.
* If the dataset contains extreme outliers, or if the algorithm calculates distances and assumes normally distributed data (e.g., K-Means Clustering, PCA) $\rightarrow$ **Use Z-Score**.

---
**Topic: Data Warehousing (Multidimensional Schemas)**

**1. The Star Schema (The Speed King)**

* **The Architecture:** A single central Fact Table connected directly to multiple Dimension Tables. It looks like a star.
* **The Normalization Rule:** Dimension tables are strictly **Denormalized**. They contain redundant data (e.g., repeating the country "India" millions of times for every city).
* **The Advantage:** Blazing fast read operations. To filter data by any dimension, it requires exactly **1 JOIN** between the Fact table and that specific Dimension table.
* **The Trade-off:** Sacrifices hard drive space due to data redundancy.

**2. The Snowflake Schema (The Storage Saver)**

* **The Architecture:** A central Fact Table, but the Dimension tables branch outwards into smaller sub-dimension tables. It looks like a snowflake.
* **The Normalization Rule:** Dimension tables are strictly **Normalized**. (e.g., The `Location` dimension splits into a separate `City` table and a separate `Country` table).
* **The Advantage:** Highly optimized storage space. Zero redundant data.
* **The Trade-off:** Slower query performance. Aggregating high-level data now requires complex **Multi-level JOIN chains**.

**3. 🚀 The GATE DA Identification Heuristics**

* If the schema has a Fact table and multiple Dimensions, but **every dimension connects directly to the Fact table** with no branching $\rightarrow$ **Star Schema**.
* If a question explicitly states that a Database Administrator decided to **"normalize the dimension tables"** $\rightarrow$ The architecture instantly transforms into a **Snowflake Schema**.

---
**Topic: Advanced Data Transformation & OLAP Warehousing**

**1. Discretization (Binning)**

* **The Goal:** Transforming continuous numerical variables into discrete categorical bins.
* **Equal-Width:** Divides the range into equal intervals (e.g., $0-10, 10-20$). *Vulnerable to skewed data leaving empty bins.*
* **Equal-Frequency:** Ensures every bin contains the exact same *number of records*. *Handles outliers and skewed data perfectly.*

**2. Sampling (The Stratified Rule)**

* **The Goal:** Extracting a smaller subset of data that mathematically represents the massive whole.
* **The GATE Rule:** Never use blind random sampling for imbalanced data (e.g., Fraud Detection). Always use **Stratified Sampling**, which guarantees the original class ratios (e.g., $99\%$ Normal, $1\%$ Fraud) are preserved exactly in the extracted sample.

**3. Compression (Dimensionality Reduction)**

* **The Goal:** Reducing the physical byte size of the dataset.
* **Lossless:** Original data can be perfectly reconstructed.
* **Lossy (PCA):** Principal Component Analysis mathematically compresses multiple columns into fewer dimensions. You lose exact raw values, but preserve the underlying variance and relationships.

**4. Concept Hierarchies (OLAP Navigation)**

* **Roll-up:** Zooming *out*. Aggregating data up the hierarchy. (e.g., Moving from `City` $\rightarrow$ `State` $\rightarrow$ `Country`, or `Daily` $\rightarrow$ `Monthly`).
* **Drill-down:** Zooming *in*. Revealing finer details down the hierarchy. (e.g., Moving from `Yearly` $\rightarrow$ `Quarterly` $\rightarrow$ `Monthly`).

**5. 🚀 OLAP Measures (The Highly Tested Math Rules)**
A "Measure" is the numerical fact in the center of your Star Schema. You must classify how it can be aggregated:

* **Additive:** Completely safe to SUM across *all* dimensions. (e.g., `Quantity Sold`, `Total Revenue`).
* **Semi-Additive:** Safe to SUM across some dimensions (like Location), but **mathematically invalid to SUM across Time**. (e.g., `Inventory Level`, `Bank Balance`. You cannot add yesterday's inventory to today's inventory).
* **Non-Additive:** Invalid to SUM across *any* dimension. Must use averages or recalculations. (e.g., `Profit Margin %`, `Discount Rate`, `Temperature`).

---

Box the **Semi-Additive** time constraint in red ink. If they give you a table of "Warehouse Inventory", and ask you for the monthly total, the answer is *never* a SUM; it is either the Average or the Last-Day value.

---
