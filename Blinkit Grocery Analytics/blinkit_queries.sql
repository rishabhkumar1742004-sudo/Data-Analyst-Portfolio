-- ==========================================
-- BLINKIT GROCERY SALES ANALYTICS DATABASE QUERIES
-- Database System: MySQL / SQL Server
-- ==========================================

-- ------------------------------------------
-- 1. DATABASE & TABLES SETUP
-- ------------------------------------------
CREATE DATABASE blinkit_analytics;
USE blinkit_analytics;

-- Create Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100),
    brand VARCHAR(100),
    price DECIMAL(10,2),
    mrp DECIMAL(10,2),
    margin_percentage DECIMAL(5,2),
    shelf_life_days INT,
    min_stock_level INT,
    max_stock_level INT
);

-- Create Customers Table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(150),
    email VARCHAR(150),
    phone VARCHAR(20),
    address VARCHAR(255),
    area VARCHAR(100),
    pincode VARCHAR(20),
    registration_date DATE,
    customer_segment VARCHAR(50),
    total_orders INT,
    avg_order_value DECIMAL(10,2)
);

-- Create Orders Table
CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,
    customer_id INT,
    order_date DATETIME,
    promised_delivery_time DATETIME,
    actual_delivery_time DATETIME,
    delivery_status VARCHAR(50),
    order_total DECIMAL(10,2),
    payment_method VARCHAR(50),
    delivery_partner_id INT,
    store_id INT
);

-- Create Order Items Table (Junction Table)
CREATE TABLE order_items (
    order_id BIGINT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2),
    PRIMARY KEY (order_id, product_id)
);

-- Create Delivery Performance Table
CREATE TABLE delivery_performance (
    order_id BIGINT PRIMARY KEY,
    delivery_partner_id INT,
    promised_time DATETIME,
    actual_time DATETIME,
    delivery_time_minutes INT,
    distance_km DECIMAL(5,2),
    delivery_status VARCHAR(50),
    reasons_if_delayed VARCHAR(255)
);

-- Create Customer Feedback Table
CREATE TABLE customer_feedback (
    feedback_id INT PRIMARY KEY,
    order_id BIGINT,
    customer_id INT,
    rating INT,
    feedback_text TEXT,
    feedback_category VARCHAR(100),
    sentiment VARCHAR(50),
    feedback_date DATE
);

-- Create Marketing Performance Table
CREATE TABLE marketing_performance (
    campaign_id INT,
    campaign_name VARCHAR(100),
    date DATE,
    target_audience VARCHAR(100),
    channel VARCHAR(50),
    impressions INT,
    clicks INT,
    conversions INT,
    spend DECIMAL(10,2),
    revenue_generated DECIMAL(10,2),
    roas DECIMAL(5,2)
);

-- Create Inventory Table
CREATE TABLE inventory (
    product_id INT,
    date DATE,
    stock_received INT,
    damaged_stock INT
);


-- ------------------------------------------
-- 2. DATA CLEANING & STANDARDIZATION
-- ------------------------------------------
-- Fix missing delay reasons in delivery performance
UPDATE delivery_performance 
SET reasons_if_delayed = 'On Time' 
WHERE reasons_if_delayed IS NULL;


-- ------------------------------------------
-- 3. KEY PERFORMANCE INDICATORS (KPIs)
-- ------------------------------------------
-- I. Total Revenue
SELECT CONCAT('₹', ROUND(SUM(order_total)/10000000, 2), ' Cr') AS Total_Revenue
FROM orders;

-- II. Total Orders
SELECT COUNT(*) AS Total_Orders
FROM orders;

-- III. Total Unique Customers
SELECT COUNT(DISTINCT customer_id) AS Total_Customers
FROM orders;

-- IV. Average Order Value (AOV)
SELECT CONCAT('₹', ROUND(AVG(order_total), 2)) AS Avg_Order_Value
FROM orders;

-- V. Average Delivery Time
SELECT ROUND(AVG(delivery_time_minutes), 1) AS Avg_Delivery_Time_Minutes
FROM delivery_performance;

-- VI. On-Time Delivery %
SELECT 
    CONCAT(ROUND(SUM(CASE WHEN delivery_status = 'On Time' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1), '%') AS On_Time_Delivery_Rate
FROM orders;


-- ------------------------------------------
-- 4. BUSINESS PERFORMANCE ANALYSIS
-- ------------------------------------------
-- I. Revenue by Category (Top Categories)
SELECT 
    p.category, 
    CONCAT('₹', ROUND(SUM(oi.quantity * oi.unit_price)/100000, 2), ' Lakh') AS Category_Revenue,
    SUM(oi.quantity) AS Items_Sold
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY SUM(oi.quantity * oi.unit_price) DESC;

-- II. Revenue by Store / Zone
SELECT 
    store_id, 
    CONCAT('₹', ROUND(SUM(order_total)/100000, 2), ' Lakh') AS Store_Revenue,
    COUNT(order_id) AS Total_Orders
FROM orders
GROUP BY store_id
ORDER BY SUM(order_total) DESC;

-- III. Customer Sentiment Analysis
SELECT 
    sentiment, 
    COUNT(*) AS Feedback_Count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customer_feedback), 1) AS Percentage
FROM customer_feedback
GROUP BY sentiment
ORDER BY Feedback_Count DESC;

-- IV. Campaign Marketing Performance (Top Channels by ROAS)
SELECT 
    channel, 
    SUM(spend) AS Total_Spend, 
    SUM(revenue_generated) AS Total_Revenue,
    ROUND(SUM(revenue_generated)/SUM(spend), 2) AS Average_ROAS
FROM marketing_performance
GROUP BY channel
ORDER BY Average_ROAS DESC;

-- V. Inventory Loss Analysis (Top Categories by Damaged Stock)
SELECT 
    p.category, 
    SUM(inv.stock_received) AS Total_Stock_Received,
    SUM(inv.damaged_stock) AS Total_Damaged_Stock,
    ROUND(SUM(inv.damaged_stock) * 100.0 / SUM(inv.stock_received), 2) AS Damage_Rate_Percentage
FROM inventory inv
JOIN products p ON inv.product_id = p.product_id
GROUP BY p.category
ORDER BY Total_Damaged_Stock DESC;
