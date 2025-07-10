# nexans_simulation_backend.py

# Define decision levels and their numeric values
LEVELS = ['None', 'Low', 'Medium', 'High', 'Very High']
LEVEL_VALUES = {level: i for i, level in enumerate(LEVELS)}  # None=0, ..., Very High=4

# Define KPIs and base values
KPIS = ['Revenue Growth (%)', 'Operating Margin (%)', 'ROCE (%)', 'Customer Satisfaction (%)', 'Market Share (%)']
BASE_KPIS = {
    'Revenue Growth (%)': 5.0,
    'Operating Margin (%)': 10.0,
    'ROCE (%)': 12.0,
    'Customer Satisfaction (%)': 70.0,
    'Market Share (%)': 15.0
}

# Go-to-Market Page
GO_TO_MARKET_DECISIONS = {
    'Price Forecast: Power Transmission': {'Revenue Growth (%)': 0.5, 'Operating Margin (%)': 0.3, 'ROCE (%)': 0.2, 'Customer Satisfaction (%)': 0.1, 'Market Share (%)': 0.4},
    'Price Forecast: Power Grid': {'Revenue Growth (%)': 0.4, 'Operating Margin (%)': 0.25, 'ROCE (%)': 0.15, 'Customer Satisfaction (%)': 0.1, 'Market Share (%)': 0.35},
    'Price Forecast: Power Connect': {'Revenue Growth (%)': 0.3, 'Operating Margin (%)': 0.2, 'ROCE (%)': 0.1, 'Customer Satisfaction (%)': 0.1, 'Market Share (%)': 0.3},
    'Marketing Investment': {'Revenue Growth (%)': 0.6, 'Operating Margin (%)': -0.1, 'ROCE (%)': 0.1, 'Customer Satisfaction (%)': 0.4, 'Market Share (%)': 0.5},
    'Customer Engagement Initiatives': {'Revenue Growth (%)': 0.3, 'Operating Margin (%)': 0.1, 'ROCE (%)': 0.1, 'Customer Satisfaction (%)': 0.6, 'Market Share (%)': 0.3}
}

# Product R&D Innovation Page
PRODUCT_RND_DECISIONS = {
    'High Voltage Cable R&D': {'Revenue Growth (%)': 0.7, 'Operating Margin (%)': 0.2, 'ROCE (%)': 0.3, 'Customer Satisfaction (%)': 0.3, 'Market Share (%)': 0.4},
    'Medium Voltage Cable R&D': {'Revenue Growth (%)': 0.6, 'Operating Margin (%)': 0.25, 'ROCE (%)': 0.25, 'Customer Satisfaction (%)': 0.3, 'Market Share (%)': 0.35},
    'Specialty Cable R&D': {'Revenue Growth (%)': 0.5, 'Operating Margin (%)': 0.2, 'ROCE (%)': 0.2, 'Customer Satisfaction (%)': 0.4, 'Market Share (%)': 0.3},
    'Data/Telecom Cable R&D': {'Revenue Growth (%)': 0.4, 'Operating Margin (%)': 0.15, 'ROCE (%)': 0.15, 'Customer Satisfaction (%)': 0.4, 'Market Share (%)': 0.25},
    'Sustainability & Digitalization R&D': {'Revenue Growth (%)': 0.3, 'Operating Margin (%)': 0.1, 'ROCE (%)': 0.1, 'Customer Satisfaction (%)': 0.5, 'Market Share (%)': 0.2}
}

# Plants Management Page
PLANTS_MANAGEMENT_DECISIONS = {
    'Plant Expansion: Power Transmission': {'Revenue Growth (%)': 0.6, 'Operating Margin (%)': 0.3, 'ROCE (%)': 0.4, 'Customer Satisfaction (%)': 0.1, 'Market Share (%)': 0.3},
    'Plant Expansion: Power Grid': {'Revenue Growth (%)': 0.5, 'Operating Margin (%)': 0.25, 'ROCE (%)': 0.35, 'Customer Satisfaction (%)': 0.1, 'Market Share (%)': 0.25},
    'Plant Expansion: Power Connect': {'Revenue Growth (%)': 0.4, 'Operating Margin (%)': 0.2, 'ROCE (%)': 0.3, 'Customer Satisfaction (%)': 0.1, 'Market Share (%)': 0.2},
    'Automation & Efficiency': {'Revenue Growth (%)': 0.3, 'Operating Margin (%)': 0.4, 'ROCE (%)': 0.4, 'Customer Satisfaction (%)': 0.2, 'Market Share (%)': 0.2},
    'Supply Chain Resilience': {'Revenue Growth (%)': 0.2, 'Operating Margin (%)': 0.3, 'ROCE (%)': 0.3, 'Customer Satisfaction (%)': 0.3, 'Market Share (%)': 0.2}
}

# Corporate Page
CORPORATE_DECISIONS = {
    'Employee Training & Upskilling': {'Revenue Growth (%)': 0.3, 'Operating Margin (%)': 0.1, 'ROCE (%)': 0.1, 'Customer Satisfaction (%)': 0.5, 'Market Share (%)': 0.2},
    'Talent Acquisition': {'Revenue Growth (%)': 0.4, 'Operating Margin (%)': 0.1, 'ROCE (%)': 0.1, 'Customer Satisfaction (%)': 0.4, 'Market Share (%)': 0.3},
    'Retention & Engagement': {'Revenue Growth (%)': 0.3, 'Operating Margin (%)': 0.1, 'ROCE (%)': 0.1, 'Customer Satisfaction (%)': 0.6, 'Market Share (%)': 0.2},
    'ESG & Corporate Social Responsibility': {'Revenue Growth (%)': 0.2, 'Operating Margin (%)': 0.05, 'ROCE (%)': 0.05, 'Customer Satisfaction (%)': 0.5, 'Market Share (%)': 0.1},
    'Digital Transformation': {'Revenue Growth (%)': 0.4, 'Operating Margin (%)': 0.2, 'ROCE (%)': 0.2, 'Customer Satisfaction (%)': 0.4, 'Market Share (%)': 0.3}
}

def calculate_kpi_impact(decisions_dict, decisions_impact):
    """
    Calculate KPI results for a set of decisions and their levels.
    :param decisions_dict: dict of decision_name -> level string
    :param decisions_impact: dict of decision_name -> dict of KPI impacts
    :return: dict of KPI -> value
    """
    kpi_results = {kpi: BASE_KPIS[kpi] for kpi in KPIS}
    for decision, level in decisions_dict.items():
        level_val = LEVEL_VALUES.get(level, 0)
        impact_weights = decisions_impact.get(decision, {})
        for kpi, weight in impact_weights.items():
            kpi_results[kpi] += weight * level_val
    return {k: round(v, 2) for k, v in kpi_results.items()}

def calculate_overall_kpis(all_decisions):
    """
    Calculate overall KPIs for all pages combined.
    :param all_decisions: dict with keys: 'go_to_market', 'product_rnd', 'plants_management', 'corporate'
                          each value is a dict of decision_name -> level
    :return: dict of KPI -> value
    """
    combined_decisions = {}
    combined_decisions.update(all_decisions.get('go_to_market', {}))
    combined_decisions.update(all_decisions.get('product_rnd', {}))
    combined_decisions.update(all_decisions.get('plants_management', {}))
    combined_decisions.update(all_decisions.get('corporate', {}))
    # Combine all decision weights
    all_weights = {}
    all_weights.update(GO_TO_MARKET_DECISIONS)
    all_weights.update(PRODUCT_RND_DECISIONS)
    all_weights.update(PLANTS_MANAGEMENT_DECISIONS)
    all_weights.update(CORPORATE_DECISIONS)
    return calculate_kpi_impact(combined_decisions, all_weights)
