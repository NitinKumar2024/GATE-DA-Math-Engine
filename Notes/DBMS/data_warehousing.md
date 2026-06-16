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
