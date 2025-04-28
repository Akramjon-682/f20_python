import pandas as pd
import sqlite3

# Solutions list
solutions = []

# Connect to the chinook database
conn = sqlite3.connect('task/chinook.db')

# 1. Customer Purchases Analysis

# Find total amount spent by each customer
customer_total = pd.read_sql_query("""
SELECT 
    Customer.CustomerId, 
    Customer.FirstName || ' ' || Customer.LastName AS CustomerName,
    SUM(Invoice.Total) AS TotalSpent
FROM Customer
JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.CustomerId
ORDER BY TotalSpent DESC
""", conn)

# Top 5 customers with highest total purchase
top5_customers = customer_total.head(5)
solutions.append(top5_customers)  # ➡️ 1-savol javobi: top 5 customers

# 2. Album vs. Individual Track Purchases

# Check invoice line and track relation to albums
invoice_items = pd.read_sql_query("""
SELECT 
    il.InvoiceId,
    t.AlbumId
FROM InvoiceLine il
JOIN Track t ON il.TrackId = t.TrackId
""", conn)

# Check if customer bought full albums or individual tracks
invoice_album = pd.read_sql_query("""
SELECT 
    Invoice.InvoiceId,
    Invoice.CustomerId
FROM Invoice
""", conn)

# Merge to see which customer bought which albums
merged = pd.merge(invoice_album, invoice_items, on='InvoiceId')

# Group by customer and album to check track counts
customer_album = merged.groupby(['CustomerId', 'AlbumId']).size().reset_index(name='TracksBought')

# Find total tracks per album
album_tracks = pd.read_sql_query("""
SELECT 
    Album.AlbumId,
    COUNT(Track.TrackId) AS TotalTracks
FROM Album
JOIN Track ON Album.AlbumId = Track.AlbumId
GROUP BY Album.AlbumId
""", conn)

# Merge to compare tracks bought vs total tracks
full_info = pd.merge(customer_album, album_tracks, on='AlbumId')

# Customer prefers individual tracks if TracksBought < TotalTracks
full_info['IndividualPreference'] = full_info['TracksBought'] < full_info['TotalTracks']

# Now check per customer
prefers_individual = full_info.groupby('CustomerId')['IndividualPreference'].any().reset_index()

# Calculate percentage
individual_pref_count = prefers_individual['IndividualPreference'].sum()
total_customers = prefers_individual.shape[0]
percentage_individual_pref = (individual_pref_count / total_customers) * 100
solutions.append(percentage_individual_pref)  # ➡️ 2-savol javobi: % individual buyers

# Close the database connection
conn.close()

# Print solutions
for idx, sol in enumerate(solutions, 1):
    print(f"Solution {idx}:\n{sol}\n")
