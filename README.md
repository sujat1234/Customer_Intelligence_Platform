# Customer Intelligence Platform

A customer analytics dashboard that uses RFM analysis and K-Means clustering to segment customers based on their purchasing behavior.

## Overview

The Customer Intelligence Platform analyzes customer transaction data and groups customers into meaningful segments.

The goal is to help businesses understand:

- Which customers are highly valuable
- Which customers are loyal
- Which customers may be at risk of leaving
- Which customers are newly acquired
- Which high-value customers purchase occasionally

The project combines data analysis, machine learning, and a Flask-based web dashboard to turn customer data into actionable insights.

## Key Features

- RFM (Recency, Frequency, Monetary) analysis
- K-Means customer segmentation
- Interactive customer segment filtering
- Revenue and customer distribution charts
- RFM summary metrics
- Individual customer search
- Customer-level analytics
- Segment-based business recommendations
- Responsive dashboard interface

## Customer Segments

The platform categorizes customers into five groups:

- **Champions** — High-value and highly engaged customers
- **Loyal Customers** — Customers with consistent purchasing behavior
- **At Risk** — Customers who may need re-engagement
- **New Customers** — Recently acquired customers
- **High-Value Occasional** — High-spending customers who purchase less frequently

## RFM Analysis

RFM analysis evaluates customers using three factors:

- **Recency** — How recently a customer made a purchase
- **Frequency** — How frequently a customer places orders
- **Monetary** — How much a customer spends

These features are used to understand customer behavior and create meaningful customer segments.

## Machine Learning

The project uses **K-Means Clustering** to group customers with similar purchasing behavior.

## Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML
- CSS
- JavaScript
- Chart.js

## Project Structure

```text
customer-intelligence-platform/
│
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── data/
│   └── customer_segments.csv
│
├── requirements.txt
├── README.md
└── .gitignore