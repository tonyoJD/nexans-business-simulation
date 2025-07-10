from NixessimulationBackend import (
    LEVELS,
    GO_TO_MARKET_DECISIONS,
    PRODUCT_RND_DECISIONS,
    PLANTS_MANAGEMENT_DECISIONS,
    CORPORATE_DECISIONS,
    calculate_kpi_impact,
    calculate_overall_kpis
)

import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Nexans Business Simulation",
    page_icon="🔌",
    layout="wide"
)

# Title and description
st.title("🔌 Nexans Strategic Investment Simulation")
st.markdown("**Strategic Decision Tool for Executive Team**")
st.markdown("---")

# Sidebar for inputs
st.sidebar.header("Investment Allocation")
st.sidebar.markdown("Allocate €500M across three strategic opportunities:")

# Investment allocation sliders
offshore_wind = st.sidebar.slider("Offshore Wind Cables (%)", 0, 100, 40)
grid_modernization = st.sidebar.slider("Grid Modernization (%)", 0, 100, 40)
data_center = st.sidebar.slider("Data Center Infrastructure (%)", 0, 100, 20)

# Ensure total equals 100%
total_allocation = offshore_wind + grid_modernization + data_center
if total_allocation != 100:
    st.sidebar.error(f"Total allocation: {total_allocation}%. Must equal 100%")
else:
    st.sidebar.success(f"Total allocation: {total_allocation}% ✓")

# Main simulation logic
def calculate_kpis(offshore_pct, grid_pct, datacenter_pct):
    # Base KPIs
    base_revenue_growth = 5.0
    base_operating_margin = 10.0
    base_roce = 12.0
    base_customer_satisfaction = 70.0
    base_market_share = 15.0
    
    # Investment impacts
    revenue_growth = base_revenue_growth + (
        offshore_pct * 0.25 + grid_pct * 0.15 + datacenter_pct * 0.20
    ) / 100
    
    operating_margin = base_operating_margin + (
        offshore_pct * 0.08 + grid_pct * 0.12 + datacenter_pct * 0.05
    ) / 100
    
    roce = base_roce + (
        offshore_pct * 0.15 + grid_pct * 0.10 + datacenter_pct * 0.08
    ) / 100
    
    customer_satisfaction = base_customer_satisfaction + (
        offshore_pct * 0.05 + grid_pct * 0.03 + datacenter_pct * 0.08
    ) / 100
    
    market_share = base_market_share + (
        offshore_pct * 0.06 + grid_pct * 0.04 + datacenter_pct * 0.03
    ) / 100
    
    return {
        'Revenue Growth (%)': round(revenue_growth, 1),
        'Operating Margin (%)': round(operating_margin, 1),
        'ROCE (%)': round(roce, 1),
        'Customer Satisfaction (%)': round(customer_satisfaction, 1),
        'Market Share (%)': round(market_share, 1)
    }

# Calculate results
if total_allocation == 100:
    results = calculate_kpis(offshore_wind, grid_modernization, data_center)
    
    # Display results
    st.header("📊 Strategic Impact Analysis")
    
    # KPI metrics in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Revenue Growth", f"{results['Revenue Growth (%)']}%", f"+{results['Revenue Growth (%)'] - 5.0:.1f}%")
    
    with col2:
        st.metric("Operating Margin", f"{results['Operating Margin (%)']}%", f"+{results['Operating Margin (%)'] - 10.0:.1f}%")
    
    with col3:
        st.metric("ROCE", f"{results['ROCE (%)']}%", f"+{results['ROCE (%)'] - 12.0:.1f}%")
    
    with col4:
        st.metric("Customer Satisfaction", f"{results['Customer Satisfaction (%)']}%", f"+{results['Customer Satisfaction (%)'] - 70.0:.1f}%")
    
    with col5:
        st.metric("Market Share", f"{results['Market Share (%)']}%", f"+{results['Market Share (%)'] - 15.0:.1f}%")
    
    # Investment breakdown
    st.header("💰 Investment Breakdown")
    investment_data = {
        'Investment Area': ['Offshore Wind Cables', 'Grid Modernization', 'Data Center Infrastructure'],
        'Allocation (%)': [offshore_wind, grid_modernization, data_center],
        'Amount (€M)': [offshore_wind * 5, grid_modernization * 5, data_center * 5]
    }
    st.table(pd.DataFrame(investment_data))

else:
    st.warning("⚠️ Please adjust allocation to total 100% to see results")

# Footer
st.markdown("---")
st.markdown("*Nexans Strategic Investment Simulation - Executive Decision Support Tool*")
