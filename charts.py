import plotly.express as px
import plotly.graph_objects as go

# Hardcoded Grok (xAI) Metrics
grok_metrics = {
    "company_name": "Odin AI",
    "valuation_clean": 20_000_000,            # Estimated ~$20M (see explanation below)
    "total_funding_clean": 0,                 # No public funding as of mid-2025
    "current_employees": 30,                  # Midpoint estimate from LinkedIn (11–50)
    "founded": 2023,                          # From LinkedIn/Tracxn
    "employee_growth": 10,                    # Estimated +10 employees in past year (assume 20 → 30, ~50% growth)
    "funding_per_employee": 0,                # No funding, so $0 per employee
    "valuation_per_employee": 666_667,        # $20M / 30
    "capital_efficiency": 1,                  # Valuation / funding: $20M / $20M bootstrap = 1 (self-funded estimate)
}

def style_fig(fig):
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        legend_title_font_color='white'
    )
    return fig

def valuation_competitors_chart(df):
    import pandas as pd
    df = df[df['company_name'] != 'Shell India Marketing Private Limited']
    odin_valuation = grok_metrics['valuation_clean']
    min_val = odin_valuation * 0.5
    max_val = odin_valuation * 10.0

    competitors = df[(df['valuation_clean'].notnull()) &
                     (df['valuation_clean'] >= min_val) &
                     (df['valuation_clean'] <= max_val)].copy()

    # Fix for pandas 2.x: use pd.concat, not append
    if not (competitors['company_name'] == grok_metrics["company_name"]).any():
        extra_row = pd.DataFrame([{
            'company_name': grok_metrics["company_name"],
            'valuation_clean': grok_metrics["valuation_clean"]
        }])
        competitors = pd.concat([competitors, extra_row], ignore_index=True)

    competitors = competitors.sort_values('valuation_clean', ascending=False)

    fig = px.bar(competitors, x='company_name', y='valuation_clean',
                 title='Valuation of Competitors',
                 labels={'valuation_clean': 'Valuation ($)'})

    fig.add_hline(y=grok_metrics["valuation_clean"],
                  line_dash="dot", line_color="crimson",
                  annotation_text="Odin AI",
                  annotation_position="top left")

    return style_fig(fig)


def growth_scatter_plot(df):
    df = df[df['company_name'] != 'Shell India Marketing Private Limited']
    chart_df = df[df['employee_growth'].notnull() & df['total_funding_clean'].notnull()].copy()
    fig = px.scatter(chart_df, x='employee_growth', y='total_funding_clean',
                     size='current_employees', color='Industry',
                     hover_name='company_name',
                     title='Funding vs Growth Rate (Bubble = Headcount)',
                     labels={'employee_growth': 'Growth (%)', 'total_funding_clean': 'Funding ($)'})
    fig.add_trace(go.Scatter(
        x=[grok_metrics["employee_growth"]],
        y=[grok_metrics["total_funding_clean"]],
        mode='markers+text',
        marker=dict(size=30, color='crimson', line=dict(width=3, color='white'), opacity=1.0, symbol='star'),
        name='Odin AI', text=['Odin AI'], textposition='top right', showlegend=True
    ))
    # Add a small negative offset to y-axis minimum to prevent marker cutoff
    y_max = chart_df['total_funding_clean'].max() * 1.1
    fig.update_yaxes(range=[-y_max * 0.06, y_max], nticks=8)
    return style_fig(fig)

def funding_per_employee_competitors_chart(df):
    import pandas as pd
    df = df[df['company_name'] != 'Shell India Marketing Private Limited']
    odin_fpe = grok_metrics['funding_per_employee']
    min_fpe = max(0, odin_fpe * 0.5)
    max_fpe = odin_fpe * 10.0  # or adjust this range as needed

    competitors = df[(df['funding_per_employee'].notnull()) &
                     (df['funding_per_employee'] >= min_fpe) &
                     (df['funding_per_employee'] <= max_fpe)].copy()

    # Ensure Odin AI is always present
    if not (competitors['company_name'] == grok_metrics["company_name"]).any():
        extra_row = pd.DataFrame([{
            'company_name': grok_metrics["company_name"],
            'funding_per_employee': grok_metrics["funding_per_employee"]
        }])
        competitors = pd.concat([competitors, extra_row], ignore_index=True)

    competitors = competitors.sort_values('funding_per_employee', ascending=False)

    fig = px.bar(competitors, x='company_name', y='funding_per_employee',
                 title='Funding per Employee: Competitors Near Odin AI',
                 labels={'funding_per_employee': 'Funding / Employee ($)'})

    fig.add_hline(y=grok_metrics["funding_per_employee"],
                  line_dash="dot", line_color="crimson",
                  annotation_text="Odin AI",
                  annotation_position="top left")

    fig.add_annotation(
        x='Odin AI',
        y=grok_metrics["funding_per_employee"],
        text=f"${grok_metrics['funding_per_employee']:,.0f}",
        showarrow=True,
        arrowhead=1,
        ax=40,
        ay=0,
        font=dict(color="white", size=14),
        bgcolor="crimson",
        bordercolor="white",
        borderwidth=1
    )

    return style_fig(fig)



def valuation_per_employee_competitors_chart(df):
    import pandas as pd
    df = df[df['company_name'] != 'Shell India Marketing Private Limited']
    odin_vpe = grok_metrics['valuation_per_employee']
    min_vpe = max(0, odin_vpe * 0.5)
    max_vpe = odin_vpe * 10.0  # or adjust this range as needed

    competitors = df[(df['valuation_per_employee'].notnull()) &
                     (df['valuation_per_employee'] >= min_vpe) &
                     (df['valuation_per_employee'] <= max_vpe)].copy()

    # Ensure Odin AI is always present
    if not (competitors['company_name'] == grok_metrics["company_name"]).any():
        extra_row = pd.DataFrame([{
            'company_name': grok_metrics["company_name"],
            'valuation_per_employee': grok_metrics["valuation_per_employee"]
        }])
        competitors = pd.concat([competitors, extra_row], ignore_index=True)

    competitors = competitors.sort_values('valuation_per_employee', ascending=False)

    fig = px.bar(competitors, x='company_name', y='valuation_per_employee',
                 title='Valuation per Employee: Competitors Near Odin AI',
                 labels={'valuation_per_employee': 'Valuation / Employee ($)'})

    fig.add_hline(y=grok_metrics["valuation_per_employee"],
                  line_dash="dot", line_color="crimson",
                  annotation_text="Odin AI",
                  annotation_position="top left")

    fig.add_annotation(
        x='Odin AI',
        y=grok_metrics["valuation_per_employee"],
        text=f"${grok_metrics['valuation_per_employee']:,.0f}",
        showarrow=True,
        arrowhead=1,
        ax=40,
        ay=0,
        font=dict(color="white", size=14),
        bgcolor="crimson",
        bordercolor="white",
        borderwidth=1
    )

    return style_fig(fig)


def headcount_vs_valuation_competitors_chart(df):
    import pandas as pd
    df = df[df['company_name'] != 'Shell India Marketing Private Limited']
    odin_valuation = grok_metrics['valuation_clean']
    odin_employees = grok_metrics['current_employees']

    # You can tune these ranges for what counts as a "competitor"
    min_val = odin_valuation * 0.5
    max_val = odin_valuation * 120
    min_emp = max(1, odin_employees * 0)
    max_emp = odin_employees * 5.0

    # Filter competitors close in both valuation and headcount
    competitors = df[
        (df['valuation_clean'].notnull()) &
        (df['current_employees'].notnull()) &
        (df['valuation_clean'] >= min_val) & (df['valuation_clean'] <= max_val) &
        (df['current_employees'] >= min_emp) & (df['current_employees'] <= max_emp)
    ].copy()

    # Ensure Odin AI is always present
    if not (competitors['company_name'] == grok_metrics["company_name"]).any():
        extra_row = pd.DataFrame([{
            'company_name': grok_metrics["company_name"],
            'valuation_clean': grok_metrics["valuation_clean"],
            'current_employees': grok_metrics["current_employees"],
            'Industry': 'AI'
        }])
        competitors = pd.concat([competitors, extra_row], ignore_index=True)

    fig = px.scatter(
        competitors,
        x='current_employees',
        y='valuation_clean',
        color='Industry',
        hover_name='company_name',
        title='Current Employees vs Valuation ($): Odin AI and Closest Peers',
        labels={'current_employees': 'Employees', 'valuation_clean': 'Valuation ($)'}
    )

    # Highlight Odin AI as a unique marker with label
    fig.add_trace(go.Scatter(
        x=[grok_metrics["current_employees"]],
        y=[grok_metrics["valuation_clean"]],
        mode='markers+text',
        marker=dict(size=20, color='crimson', line=dict(width=1, color='black')),
        name='Odin AI',
        text=['Odin AI'],
        textposition='top right'
    ))

    # Y-axis: from a little below zero to Odin AI's valuation + 3B
    buffer = 0.06 * (odin_valuation + 3_000_000_000)
    fig.update_yaxes(range=[-buffer, odin_valuation + 3_000_000_000], dtick=500_000_000)

    return style_fig(fig)



def funding_vs_founding_year(df):
    df = df[df['company_name'] != 'Shell India Marketing Private Limited']
    chart_df = df[df['founded'].notnull()].copy()

    fig = px.scatter(
        chart_df,
        x='founded',
        y='total_funding_clean',
        color='company_name',
        hover_name='company_name',
        title='Funding vs Year Founded',
        labels={'total_funding_clean': 'Funding ($)'}
    )

    fig.add_trace(
        go.Scatter(
            x=[grok_metrics["founded"]],
            y=[grok_metrics["total_funding_clean"]],
            mode='markers+text',
            marker=dict(size=20, color='crimson', line=dict(width=1, color='black')),
            name='Odin AI',
            text=['Odin AI'],
            textposition='top right'
        )
    )

    # Give y-axis a small negative buffer to prevent marker cutoff at bottom
    y_max = 500_000_000
    buffer = y_max * 0.06  # 6% buffer below zero, ~30M if y_max is 500M
    fig.update_yaxes(range=[-buffer, y_max], nticks=10)

    return style_fig(fig)


