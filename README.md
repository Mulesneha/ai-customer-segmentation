# 🛒 AI Customer Segmentation

An interactive **Machine Learning web application** that analyzes customer purchasing behavior and automatically segments customers using **RFM Analysis** and **K-Means Clustering**.

🔗 **Live Demo:**
https://ai-customer-segmentation-34mfuhvssyv7pqry6qexfj.streamlit.app/

---

## 📌 Overview

Understanding customer behavior is essential for businesses to create personalized marketing strategies.

This project uses **RFM Analysis** and **K-Means Clustering** to divide customers into meaningful groups based on:

* **Recency** — How recently a customer purchased
* **Frequency** — How frequently a customer purchases
* **Monetary** — How much a customer spends

The results are presented through an interactive **Streamlit dashboard** with visualizations and business insights.

---

## ✨ Features

### 📊 Customer Analytics

* Customer transaction analysis
* RFM score calculation
* Recency analysis
* Purchase frequency analysis
* Customer monetary value analysis

### 🤖 Machine Learning

* Data preprocessing
* Log transformation
* Feature standardization using `StandardScaler`
* K-Means clustering
* Customizable number of customer segments

### 📈 Interactive Visualizations

* Customer distribution by segment
* RFM distribution charts
* 2D customer segmentation visualization
* Interactive 3D customer segmentation visualization
* Segment summary tables

### 💡 Business Insights

The application provides actionable insights for different customer groups, such as:

* 🏆 VIP Customers
* 💎 Loyal Customers
* 🌱 Potential Customers
* ⚠️ At-Risk Customers
* 😴 Lost Customers

### 📥 Export

* Download the segmented customer data as a CSV file.

---

## 🧠 Machine Learning Workflow

```text
Customer Transaction Data
          ↓
     Data Cleaning
          ↓
      RFM Analysis
          ↓
   Log Transformation
          ↓
   Feature Standardization
          ↓
     K-Means Clustering
          ↓
   Customer Segmentation
          ↓
 Visualization & Insights
```

---

## 📊 RFM Analysis

### 🔵 Recency

Measures how recently a customer made a purchase.

**Lower Recency = More Recent Customer**

### 🟢 Frequency

Measures how frequently a customer makes purchases.

**Higher Frequency = More Loyal Customer**

### 🟠 Monetary

Measures the total amount spent by a customer.

**Higher Monetary Value = Higher Customer Value**

---

## 🤖 K-Means Clustering

The application uses **K-Means Clustering** to group customers with similar purchasing behavior.

The number of clusters can be adjusted directly from the Streamlit sidebar.

For example:

```text
Cluster 1 → 🏆 VIP Customers
Cluster 2 → 💎 Loyal Customers
Cluster 3 → 🌱 Potential Customers
Cluster 4 → ⚠️ At-Risk Customers
```

---

## 🛠️ Technologies Used

| Technology     | Purpose                      |
| -------------- | ---------------------------- |
| Python         | Core programming             |
| Pandas         | Data processing              |
| NumPy          | Numerical computation        |
| Scikit-learn   | Machine Learning             |
| K-Means        | Customer clustering          |
| StandardScaler | Feature scaling              |
| Plotly         | Interactive visualizations   |
| Streamlit      | Web application & deployment |

---

## 📁 Project Structure

```text
ai-customer-segmentation/
│
├── app.py
├── requirements.txt
├── README.md
│
└── data/
    └── customers.csv
```

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/ai-customer-segmentation.git
```

### 2. Navigate to the project

```bash
cd ai-customer-segmentation
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open at:

```text
http://localhost:8501
```

---

## 📦 Dataset

The project includes a sample customer transaction dataset:

```text
data/customers.csv
```

The dataset contains information such as:

* Customer ID
* Invoice number
* Invoice date
* Quantity
* Unit price

The application calculates the customer's total spending using:

```text
Total Amount = Quantity × Unit Price
```

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

🔗 **Live Application:**
https://ai-customer-segmentation-34mfuhvssyv7pqry6qexfj.streamlit.app/

---

## 🎯 Business Applications

Customer segmentation can help businesses:

* 🎁 Create personalized offers
* 💎 Reward loyal customers
* 🔥 Target high-value customers
* ⚠️ Re-engage at-risk customers
* 📢 Improve marketing campaigns
* 💰 Increase customer lifetime value
* 📈 Improve customer retention

---

## 🔮 Future Improvements

Planned improvements include:

* [ ] Elbow Method for optimal cluster selection
* [ ] Silhouette Score evaluation
* [ ] Automatic RFM scoring
* [ ] Customer Lifetime Value prediction
* [ ] AI-generated customer insights
* [ ] Personalized product recommendations
* [ ] Upload custom customer datasets
* [ ] Advanced dashboard filters
* [ ] Downloadable reports

---

## 👩‍💻 Author

**Sneha Mule**

Computer Science & Engineering Student
Interested in **Data Science, Machine Learning, AI, and Full-Stack Development**.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!
