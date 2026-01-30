"""
Python Data Visualization Assignment - Starter Code

This starter code provides sample datasets and template functions to help you
create visualizations using matplotlib and plotly.
"""

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# ============================================================================
# SAMPLE DATA
# ============================================================================

# Sample 1: Monthly sales data
months = ['January', 'February', 'March', 'April', 'May', 'June']
sales = [15000, 18000, 12000, 22000, 19000, 25000]

# Sample 2: Student test scores
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace']
math_scores = [85, 92, 78, 95, 88, 76, 91]
english_scores = [90, 88, 85, 92, 95, 80, 87]

# Sample 3: Random data for scatter plot
np.random.seed(42)
x_data = np.random.randn(100)
y_data = 2 * x_data + np.random.randn(100)
colors = np.random.randint(1, 5, 100)

# ============================================================================
# TASK 1: MATPLOTLIB VISUALIZATIONS
# ============================================================================

def create_matplotlib_visualizations():
    """
    Create at least two matplotlib visualizations.
    
    TODO: Implement this function to:
    1. Create a line plot showing monthly sales trends
    2. Create a bar chart comparing student scores
    3. Add titles, labels, and legends
    4. Customize colors and styling
    5. Save one chart as a PNG file
    """
    
    # Example 1: Line plot for sales data
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Line plot
    ax1.plot(months, sales, marker='o', linewidth=2, markersize=8, color='#2E86AB')
    ax1.set_title('Monthly Sales Trend', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Month', fontsize=12)
    ax1.set_ylabel('Sales ($)', fontsize=12)
    ax1.grid(True, alpha=0.3)
    
    # Bar chart
    ax2.bar(students[:4], math_scores[:4], color='#A23B72', label='Math')
    ax2.bar(students[:4], english_scores[:4], color='#F18F01', alpha=0.7, label='English')
    ax2.set_title('Student Scores Comparison', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Students', fontsize=12)
    ax2.set_ylabel('Score', fontsize=12)
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('assignments/python-data-visualization/sales_visualization.png', dpi=300)
    print("✓ Matplotlib visualization saved as 'sales_visualization.png'")
    plt.show()


# ============================================================================
# TASK 2: PLOTLY INTERACTIVE VISUALIZATIONS
# ============================================================================

def create_plotly_visualizations():
    """
    Create interactive plotly visualizations.
    
    TODO: Implement this function to:
    1. Create an interactive line plot with hover tooltips
    2. Create an interactive scatter plot with color coding
    3. Add interactivity features (hover, zoom, pan)
    4. Save visualizations as HTML files
    """
    
    # Example 1: Interactive line plot
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(
        x=months,
        y=sales,
        mode='lines+markers',
        name='Sales',
        line=dict(color='#2E86AB', width=3),
        marker=dict(size=10),
        hovertemplate='<b>%{x}</b><br>Sales: $%{y:,.0f}<extra></extra>'
    ))
    
    fig_line.update_layout(
        title='Monthly Sales Trend (Interactive)',
        xaxis_title='Month',
        yaxis_title='Sales ($)',
        hovermode='x unified',
        template='plotly_white'
    )
    
    fig_line.write_html('assignments/python-data-visualization/sales_interactive.html')
    print("✓ Interactive line plot saved as 'sales_interactive.html'")
    fig_line.show()
    
    # Example 2: Interactive scatter plot
    fig_scatter = px.scatter(
        x=x_data,
        y=y_data,
        color=colors,
        size=np.abs(y_data),
        title='Interactive Scatter Plot',
        labels={'x': 'X Values', 'y': 'Y Values'},
        hover_data={'x': ':.2f', 'y': ':.2f', 'color': True},
        color_continuous_scale='Viridis'
    )
    
    fig_scatter.update_layout(
        hovermode='closest',
        template='plotly_white'
    )
    
    fig_scatter.write_html('assignments/python-data-visualization/scatter_interactive.html')
    print("✓ Interactive scatter plot saved as 'scatter_interactive.html'")
    fig_scatter.show()


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("Starting Data Visualization Assignment...")
    print()
    
    print("Creating matplotlib visualizations...")
    create_matplotlib_visualizations()
    print()
    
    print("Creating plotly interactive visualizations...")
    create_plotly_visualizations()
    print()
    
    print("✓ Assignment complete! Check the generated files.")
