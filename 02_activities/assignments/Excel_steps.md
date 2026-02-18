## Viz 2 (Excel, Mac): Create a PivotTable Heatmap from `viz2_ward_category_long.csv`

### 1) Import the CSV
1. Open **Microsoft Excel (Mac)**.
2. Go to **File → Import…**
3. Select **CSV file** and choose `data/processed/viz2_ward_category_long.csv`.
4. When prompted, confirm the delimiter is **Comma**, then import into a **new worksheet**.

### 2) Insert a PivotTable
1. Click any cell in the imported table.
2. Go to **Insert → PivotTable…**
3. Use the full imported range/table as the data source.
4. Choose **New Worksheet** as the PivotTable location, then click **OK**.

### 3) Configure PivotTable fields
In the PivotTable Fields pane:
- Drag **Ward** → **Rows**
- Drag **Service Request Type** → **Columns**
- Drag **n** → **Values**

Confirm the Values summary is **Sum of n**:
- Click the **n** field under *Values* → **Value Field Settings…** → select **Sum** → **OK**.

### 4) Turn on Grand Total column
1. Click inside the PivotTable.
2. Go to **PivotTable Analyze** (or **PivotTable Design**) → **Grand Totals**
3. Select **On for Rows and Columns** (adds a Grand Total *column* on the right).

### 5) Sort wards by total (largest to smallest)
1. Click a number in the **Grand Total** column (far right).
2. Go to **Data → Sort → Sort Largest to Smallest**.

### 6) Apply heatmap coloring (conditional formatting)
1. Select only the PivotTable **value cells** (the numeric body, excluding headers and totals).
2. Go to **Home → Conditional Formatting → Color Scales** and choose a **single sequential** scale (light → dark).

### 7) Export for submission
- Export as PDF: **File → Print** → set scaling to **Fit all columns on one page** → **PDF → Save as PDF**.
