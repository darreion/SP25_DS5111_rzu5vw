# Lab 08 – Entity Relationship Diagram: Daily Stock Gainer Analysis

##  Overview

This report presents an Entity Relationship Diagram (ERD) and associated design decisions for analyzing a week's worth of daily stock gainer lists from Yahoo and WSJ. The goal is to transform raw scraped `.csv` data into structured tables that support meaningful queries, visualizations, and insights.

---

##  Use Cases

- **Recurring Gainers**: Identify which stock symbols appear on gainers lists multiple times in the week.
- **Price & Volume Distribution**: Create histograms of price/volume across all gainers to understand market movement.
- **Symbol Momentum**: Match repeating symbols with their candlestick data to explore short-term trends.
- **Cross-Source Comparison**: Determine if the same symbols appear on both Yahoo and WSJ lists on the same day.

---

##  Methods / Processing Flow

1. Raw daily `.csv` files (timestamped from cron jobs) are merged into a unified raw table.
2. Intermediate tables are created:
   - One per source (Yahoo, WSJ) with standardized columns.
   - A combined `weekly_gainers` table with columns: `symbol`, `date`, `source`, `price`, `volume`, etc.
   - A frequency table for recurring symbols.
3. Final tables are derived from intermediate ones to support specific visualizations and reports.

---

## ERD Diagram

```mermaid
erDiagram
    RAW_YAHOO ||--|| WEEKLY_GAINERS : merges
    RAW_WSJ ||--|| WEEKLY_GAINERS : merges
    WEEKLY_GAINERS ||--o{ SYMBOL_FREQ : aggregates
    WEEKLY_GAINERS ||--o{ PRICE_HISTOGRAM : analyzes
    WEEKLY_GAINERS ||--o{ CANDLESTICK_DATA : enriches
    CANDLESTICK_DATA ||--o{ FINAL_MOMENTUM : derives
