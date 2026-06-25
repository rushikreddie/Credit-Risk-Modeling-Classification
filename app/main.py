import streamlit as st
import streamlit.components.v1 as components
from prediction_helper import predict

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CreditIQ · Risk Engine",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, .stApp {
    background: #0A0F1E !important;
    color: #E8EDF5 !important;
    font-family: 'Inter', sans-serif;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── Top nav bar ── */
.nav-bar {
    background: rgba(10,15,30,0.95);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(0,212,184,0.15);
    padding: 18px 48px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 999;
}
.nav-logo {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #E8EDF5;
    letter-spacing: -0.5px;
}
.nav-logo span { color: #00D4B8; }
.nav-badge {
    background: rgba(0,212,184,0.12);
    border: 1px solid rgba(0,212,184,0.3);
    color: #00D4B8;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    padding: 5px 12px;
    border-radius: 20px;
}

/* ── Main layout ── */
.main-layout {
    display: grid;
    grid-template-columns: 1fr 420px;
    gap: 0;
    min-height: calc(100vh - 65px);
}

/* ── Left panel ── */
.left-panel {
    padding: 40px 48px;
    border-right: 1px solid rgba(255,255,255,0.06);
}
.panel-eyebrow {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #00D4B8;
    margin-bottom: 8px;
}
.panel-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 28px;
    font-weight: 700;
    color: #E8EDF5;
    letter-spacing: -0.5px;
    margin-bottom: 6px;
    line-height: 1.2;
}
.panel-subtitle {
    color: #6B7A99;
    font-size: 14px;
    line-height: 1.5;
    margin-bottom: 36px;
}

/* ── Section headers ── */
.section-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 20px;
    margin-top: 36px;
}
.section-header:first-of-type { margin-top: 0; }
.section-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #00D4B8;
    flex-shrink: 0;
}
.section-label {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    color: #8B9BB8;
}
.section-line {
    flex: 1;
    height: 1px;
    background: rgba(255,255,255,0.07);
}

/* ── Derived metric pill ── */
.metric-pill {
    background: rgba(0,212,184,0.08);
    border: 1px solid rgba(0,212,184,0.2);
    border-radius: 12px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 24px;
}
.metric-pill-label {
    font-size: 13px;
    color: #6B7A99;
    font-weight: 500;
}
.metric-pill-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #00D4B8;
}
.metric-pill-sub {
    font-size: 11px;
    color: #4A5568;
    margin-top: 2px;
}

/* ── Streamlit widget overrides ── */
div[data-testid="stNumberInput"] label,
div[data-testid="stSelectbox"] label,
div[data-testid="stSlider"] label {
    font-size: 12px !important;
    font-weight: 500 !important;
    color: #8B9BB8 !important;
    letter-spacing: 0.5px !important;
    text-transform: uppercase !important;
    margin-bottom: 4px !important;
}

div[data-testid="stNumberInput"] input {
    background: rgba(26,34,53,0.8) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 10px !important;
    color: #E8EDF5 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    padding: 12px 16px !important;
    transition: border-color 0.2s;
}
div[data-testid="stNumberInput"] input:focus {
    border-color: rgba(0,212,184,0.5) !important;
    box-shadow: 0 0 0 3px rgba(0,212,184,0.08) !important;
    outline: none !important;
}

div[data-testid="stSelectbox"] > div > div {
    background: rgba(26,34,53,0.8) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 10px !important;
    color: #E8EDF5 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 15px !important;
    font-weight: 600 !important;
}

/* Dropdown options */
div[data-testid="stSelectbox"] ul {
    background: #1A2235 !important;
    border: 1px solid rgba(0,212,184,0.2) !important;
    border-radius: 10px !important;
}
div[data-testid="stSelectbox"] li {
    color: #E8EDF5 !important;
    font-family: 'Inter', sans-serif !important;
}
div[data-testid="stSelectbox"] li:hover {
    background: rgba(0,212,184,0.1) !important;
}

/* Number input stepper buttons */
div[data-testid="stNumberInput"] button {
    background: rgba(0,212,184,0.1) !important;
    border-color: rgba(0,212,184,0.2) !important;
    color: #00D4B8 !important;
    border-radius: 8px !important;
}
div[data-testid="stNumberInput"] button:hover {
    background: rgba(0,212,184,0.2) !important;
}

/* ── Calculate button ── */
div[data-testid="stButton"] button {
    background: linear-gradient(135deg, #00D4B8 0%, #00A896 100%) !important;
    color: #0A0F1E !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 32px !important;
    width: 100% !important;
    margin-top: 12px !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 24px rgba(0,212,184,0.25) !important;
}
div[data-testid="stButton"] button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 32px rgba(0,212,184,0.35) !important;
}
div[data-testid="stButton"] button:active {
    transform: translateY(0) !important;
}

/* ── Right panel ── */
.right-panel {
    background: rgba(14,20,35,0.6);
    padding: 40px 36px;
    position: sticky;
    top: 65px;
    height: calc(100vh - 65px);
    overflow-y: auto;
    display: flex;
    flex-direction: column;
}
.result-eyebrow {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #4A5568;
    margin-bottom: 32px;
    text-align: center;
}

/* ── Score gauge ── */
.gauge-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 32px;
}
.gauge-svg { overflow: visible; }
.gauge-score-text {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 52px;
    font-weight: 700;
    fill: #E8EDF5;
    text-anchor: middle;
    dominant-baseline: middle;
}
.gauge-label-text {
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    fill: #6B7A99;
    text-anchor: middle;
}
.gauge-rating-text {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 18px;
    font-weight: 700;
    text-anchor: middle;
    dominant-baseline: middle;
}

/* ── Result cards ── */
.result-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 28px;
}
.result-card {
    background: rgba(26,34,53,0.7);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 18px 16px;
    text-align: center;
}
.result-card-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #4A5568;
    margin-bottom: 8px;
}
.result-card-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 26px;
    font-weight: 700;
}

/* ── Risk bar ── */
.risk-bar-wrap { margin-bottom: 28px; }
.risk-bar-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}
.risk-bar-label {
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    color: #6B7A99;
}
.risk-bar-pct {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 15px;
    font-weight: 700;
}
.risk-bar-track {
    width: 100%;
    height: 8px;
    background: rgba(255,255,255,0.07);
    border-radius: 4px;
    overflow: hidden;
}
.risk-bar-fill {
    height: 100%;
    border-radius: 4px;
    transition: width 0.8s cubic-bezier(0.4,0,0.2,1);
}

/* ── Decision banner ── */
.decision-banner {
    border-radius: 14px;
    padding: 18px 20px;
    display: flex;
    align-items: flex-start;
    gap: 14px;
}
.decision-icon { font-size: 22px; flex-shrink: 0; margin-top: 1px; }
.decision-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 4px;
}
.decision-body {
    font-size: 13px;
    line-height: 1.5;
    opacity: 0.8;
}

/* ── Empty state ── */
.empty-state {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 40px 20px;
}
.empty-icon {
    font-size: 48px;
    margin-bottom: 20px;
    opacity: 0.3;
}
.empty-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 18px;
    font-weight: 600;
    color: #4A5568;
    margin-bottom: 8px;
}
.empty-body {
    font-size: 13px;
    color: #2D3748;
    line-height: 1.5;
    max-width: 220px;
}

/* ── Score range legend ── */
.score-legend {
    display: flex;
    gap: 6px;
    justify-content: center;
    margin-top: 12px;
    flex-wrap: wrap;
}
.legend-item {
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 11px;
    color: #4A5568;
}
.legend-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
}

/* ── Column gaps ── */
div[data-testid="stHorizontalBlock"] { gap: 20px !important; }

/* ── Remove extra padding on columns ── */
div[data-testid="column"] { padding: 0 8px !important; }

/* ── Scrollbar styling ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(0,212,184,0.2); border-radius: 2px; }
</style>
""", unsafe_allow_html=True)


# ── Helpers ───────────────────────────────────────────────────────────────────

def get_rating_config(rating: str):
    configs = {
        "Poor":      {"color": "#E85454", "bg": "rgba(232,84,84,0.1)",   "border": "rgba(232,84,84,0.25)",   "icon": "⚠️", "decision": "High Risk — Decline",      "body": "Applicant profile indicates elevated default probability. Recommend rejection or require significant collateral."},
        "Average":   {"color": "#F5A623", "bg": "rgba(245,166,35,0.1)",  "border": "rgba(245,166,35,0.25)",  "icon": "🔍", "decision": "Moderate Risk — Review",     "body": "Profile warrants closer scrutiny. Consider conditional approval with enhanced monitoring or co-applicant requirement."},
        "Good":      {"color": "#4CAF82", "bg": "rgba(76,175,130,0.1)",  "border": "rgba(76,175,130,0.25)",  "icon": "✅", "decision": "Low Risk — Likely Approve", "body": "Applicant demonstrates solid creditworthiness. Standard approval process with routine monitoring recommended."},
        "Excellent":  {"color": "#00D4B8", "bg": "rgba(0,212,184,0.1)",  "border": "rgba(0,212,184,0.25)",   "icon": "⬡",  "decision": "Very Low Risk — Approve",   "body": "Strong profile with excellent repayment indicators. Priority processing recommended with competitive rate offering."},
    }
    return configs.get(rating, configs["Average"])


def build_animated_gauge(score: int, rating: str, color: str, prob_pct: float) -> str:
    """Returns a self-contained animated HTML gauge for st.components.v1.html."""
    bar_color = "#E85454" if prob_pct > 50 else "#F5A623" if prob_pct > 25 else "#4CAF82"
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: transparent; font-family: 'Inter', sans-serif; }}

  .gauge-shell {{
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 8px 0 4px;
  }}

  svg#gauge {{ overflow: visible; }}

  /* ── Pulsing outer ring ── */
  @keyframes pulse-ring {{
    0%   {{ r: 108; opacity: 0.55; }}
    50%  {{ r: 116; opacity: 0.15; }}
    100% {{ r: 108; opacity: 0.55; }}
  }}
  #pulse-ring {{ animation: pulse-ring 2.4s ease-in-out infinite; }}

  /* ── Arc fill animation ── */
  #arc-fill {{
    transition: stroke-dashoffset 1.4s cubic-bezier(0.22, 1, 0.36, 1);
  }}

  /* ── Cap dot animation ── */
  #cap-dot {{
    transition: cx 1.4s cubic-bezier(0.22, 1, 0.36, 1),
                cy 1.4s cubic-bezier(0.22, 1, 0.36, 1);
  }}

  /* ── Score counter ── */
  #score-num {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 54px;
    font-weight: 700;
    fill: #E8EDF5;
    text-anchor: middle;
    dominant-baseline: middle;
    letter-spacing: -1px;
  }}
  #score-label {{
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    font-weight: 600;
    fill: #4A5568;
    text-anchor: middle;
    letter-spacing: 2px;
  }}
  #rating-label {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 16px;
    font-weight: 700;
    text-anchor: middle;
    dominant-baseline: middle;
    fill: {color};
    letter-spacing: 0.5px;
  }}

  /* ── Legend ── */
  .legend {{
    display: flex;
    gap: 14px;
    justify-content: center;
    margin-top: 10px;
    flex-wrap: wrap;
  }}
  .legend-item {{
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 11px;
    color: #4A5568;
    font-family: 'Inter', sans-serif;
  }}
  .dot {{
    width: 7px; height: 7px;
    border-radius: 50%;
    flex-shrink: 0;
  }}

  /* ── Stat row ── */
  .stat-row {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    width: 100%;
    max-width: 340px;
    margin-top: 18px;
  }}
  .stat-card {{
    background: rgba(26,34,53,0.7);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 16px;
    text-align: center;
  }}
  .stat-card-label {{
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: #4A5568;
    margin-bottom: 8px;
  }}
  .stat-card-value {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 26px;
    font-weight: 700;
  }}

  /* ── Risk bar ── */
  .risk-wrap {{
    width: 100%;
    max-width: 340px;
    margin-top: 16px;
  }}
  .risk-header {{
    display: flex;
    justify-content: space-between;
    margin-bottom: 8px;
  }}
  .risk-header-label {{
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #6B7A99;
  }}
  .risk-header-pct {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 14px;
    font-weight: 700;
    color: {bar_color};
  }}
  .risk-track {{
    width: 100%;
    height: 7px;
    background: rgba(255,255,255,0.07);
    border-radius: 4px;
    overflow: hidden;
  }}
  .risk-fill {{
    height: 100%;
    border-radius: 4px;
    background: {bar_color};
    width: 0%;
    transition: width 1.4s cubic-bezier(0.22, 1, 0.36, 1);
  }}

  /* ── Decision banner ── */
  .banner {{
    width: 100%;
    max-width: 340px;
    margin-top: 16px;
    border-radius: 14px;
    padding: 16px 18px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
    border: 1px solid rgba(255,255,255,0.06);
  }}
  .banner-icon {{ font-size: 20px; flex-shrink: 0; margin-top: 1px; }}
  .banner-title {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 4px;
  }}
  .banner-body {{
    font-size: 12px;
    line-height: 1.5;
    color: rgba(232,237,245,0.65);
  }}
</style>
</head>
<body>
<div class="gauge-shell">

  <!-- SVG GAUGE -->
  <svg id="gauge" viewBox="0 0 320 220" width="320" height="220" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <!-- Glow for cap dot -->
      <filter id="capglow" x="-80%" y="-80%" width="260%" height="260%">
        <feGaussianBlur in="SourceGraphic" stdDeviation="5" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
      <!-- Arc gradient from zone colors -->
      <linearGradient id="arcGrad" gradientUnits="userSpaceOnUse" x1="60" y1="185" x2="260" y2="30">
        <stop offset="0%"   stop-color="#E85454"/>
        <stop offset="33%"  stop-color="#F5A623"/>
        <stop offset="66%"  stop-color="#4CAF82"/>
        <stop offset="100%" stop-color="#00D4B8"/>
      </linearGradient>
    </defs>

    <!-- Pulsing outer ring (only shown when score >= 650) -->
    <circle id="pulse-ring" cx="160" cy="120" r="108"
      fill="none" stroke="{color}" stroke-width="1"
      opacity="{0.4 if score >= 650 else 0}"/>

    <!-- Track arc (240° from 210° to 90° clockwise, i.e. -150° start) -->
    <!-- We draw arcs using stroke-dasharray on a full circle trick -->
    <!-- circumference of r=100: 2π×100 = 628.318 -->
    <!-- 240° of 360° = 628.318 × (240/360) = 418.879 -->
    <circle id="arc-track" cx="160" cy="120" r="100"
      fill="none"
      stroke="rgba(255,255,255,0.07)"
      stroke-width="14"
      stroke-linecap="round"
      stroke-dasharray="418.879 628.318"
      stroke-dashoffset="-52.36"
      transform="rotate(-210 160 120)"/>

    <!-- Filled arc (animated) -->
    <circle id="arc-fill" cx="160" cy="120" r="100"
      fill="none"
      stroke="url(#arcGrad)"
      stroke-width="14"
      stroke-linecap="round"
      stroke-dasharray="0 628.318"
      stroke-dashoffset="-52.36"
      transform="rotate(-210 160 120)"/>

    <!-- Threshold tick marks at 500, 650, 750 -->
    <!-- 500: (500-300)/600 × 240 = 80° from start -->
    <!-- 650: 140°, 750: 180° -->
    <g id="ticks" stroke="rgba(255,255,255,0.18)" stroke-width="2" stroke-linecap="round">
      <!-- 500 tick: -210+80 = -130° -->
      <line x1="160" y1="18" x2="160" y2="34" transform="rotate(-130 160 120)"/>
      <!-- 650 tick: -210+140 = -70° -->
      <line x1="160" y1="18" x2="160" y2="34" transform="rotate(-70 160 120)"/>
      <!-- 750 tick: -210+180 = -30° -->
      <line x1="160" y1="18" x2="160" y2="34" transform="rotate(-30 160 120)"/>
    </g>

    <!-- Small zone labels -->
    <text x="54"  y="192" font-family="Inter,sans-serif" font-size="10" fill="#E85454" text-anchor="middle" font-weight="600">300</text>
    <text x="266" y="192" font-family="Inter,sans-serif" font-size="10" fill="#00D4B8" text-anchor="middle" font-weight="600">900</text>

    <!-- Animated end-cap dot -->
    <circle id="cap-dot" cx="60" cy="185" r="7"
      fill="{color}" filter="url(#capglow)" opacity="0"/>

    <!-- Score number (JS counter) -->
    <text id="score-num" x="160" y="112">300</text>
    <text id="score-label" x="160" y="148">CREDIT SCORE</text>
    <text id="rating-label" x="160" y="172">{rating.upper()}</text>
  </svg>

  <!-- Legend -->
  <div class="legend">
    <div class="legend-item"><div class="dot" style="background:#E85454"></div>Poor 300–499</div>
    <div class="legend-item"><div class="dot" style="background:#F5A623"></div>Avg 500–649</div>
    <div class="legend-item"><div class="dot" style="background:#4CAF82"></div>Good 650–749</div>
    <div class="legend-item"><div class="dot" style="background:#00D4B8"></div>Excellent 750+</div>
  </div>

  <!-- Stat cards -->
  <div class="stat-row">
    <div class="stat-card">
      <div class="stat-card-label">Credit Score</div>
      <div class="stat-card-value" style="color:{color};" id="score-card">—</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Default Risk</div>
      <div class="stat-card-value" style="color:{bar_color};">{prob_pct:.1f}%</div>
    </div>
  </div>

  <!-- Risk bar -->
  <div class="risk-wrap">
    <div class="risk-header">
      <div class="risk-header-label">Default Probability</div>
      <div class="risk-header-pct">{prob_pct:.2f}%</div>
    </div>
    <div class="risk-track">
      <div class="risk-fill" id="risk-fill"></div>
    </div>
  </div>

</div>

<script>
(function() {{
  const TARGET_SCORE = {score};
  const MIN = 300, MAX = 900;
  const CIRCUMFERENCE = 2 * Math.PI * 100;   // 628.318
  const ARC_SPAN = CIRCUMFERENCE * (240 / 360); // 418.879

  // Fraction of the arc to fill (0–1)
  const frac = (TARGET_SCORE - MIN) / (MAX - MIN);
  const fillLen = frac * ARC_SPAN;

  const arcFill  = document.getElementById('arc-fill');
  const capDot   = document.getElementById('cap-dot');
  const scoreNum = document.getElementById('score-num');
  const scoreCard = document.getElementById('score-card');
  const riskFill = document.getElementById('risk-fill');

  // ── Compute cap dot position ──────────────────────────────────────────────
  // Arc starts at -210° (from rotate transform) = -210 - 90 = -300° in SVG coords
  // Each degree along arc: start angle in actual SVG = -210 + 270 = 60° below positive-x... 
  // simpler: parametric.  Centre (160,120), r=100.
  // Arc drawn with transform="rotate(-210 160 120)" and starts at top (0° = 3 o'clock in SVG).
  // Point on circle at angle θ from 3-o'clock: (160 + 100cos(θ), 120 + 100sin(θ))
  // The arc goes from angle (-210)° to (-210 + 240)° = 30°, measured from 3-o-clock.
  // So end angle of fill = -210 + frac*240  (degrees from 3 o'clock)

  function polarXY(deg) {{
    const rad = deg * Math.PI / 180;
    return {{
      x: 160 + 100 * Math.cos(rad),
      y: 120 + 100 * Math.sin(rad)
    }};
  }}

  const startDeg = -210;
  const endDeg   = startDeg + frac * 240;
  const capPos   = polarXY(endDeg);

  // ── Score counter animation ───────────────────────────────────────────────
  const DURATION = 1400; // ms
  let startTime = null;

  function easeOut(t) {{
    return 1 - Math.pow(1 - t, 3);
  }}

  function animate(ts) {{
    if (!startTime) startTime = ts;
    const elapsed = ts - startTime;
    const t = Math.min(elapsed / DURATION, 1);
    const e = easeOut(t);

    // Update score counter
    const current = Math.round(MIN + e * (TARGET_SCORE - MIN));
    scoreNum.textContent = current;
    scoreCard.textContent = current;

    // Update arc fill
    const currentFill = e * fillLen;
    arcFill.setAttribute('stroke-dasharray', currentFill + ' ' + CIRCUMFERENCE);

    // Move cap dot
    const currentDeg = startDeg + e * frac * 240;
    const pos = polarXY(currentDeg);
    capDot.setAttribute('cx', pos.x.toFixed(2));
    capDot.setAttribute('cy', pos.y.toFixed(2));
    capDot.setAttribute('opacity', t > 0.05 ? 1 : 0);

    if (t < 1) {{
      requestAnimationFrame(animate);
    }} else {{
      scoreNum.textContent = TARGET_SCORE;
      scoreCard.textContent = TARGET_SCORE;
      arcFill.setAttribute('stroke-dasharray', fillLen + ' ' + CIRCUMFERENCE);
      capDot.setAttribute('cx', capPos.x.toFixed(2));
      capDot.setAttribute('cy', capPos.y.toFixed(2));
    }}
  }}

  // ── Risk bar animation ────────────────────────────────────────────────────
  setTimeout(() => {{
    riskFill.style.width = Math.min({prob_pct:.2f}, 100).toFixed(1) + '%';
  }}, 200);

  // ── Kick off ──────────────────────────────────────────────────────────────
  requestAnimationFrame(animate);
}})();
</script>
</body>
</html>
"""


# ── Nav bar ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="nav-bar">
  <div class="nav-logo">Credit<span>IQ</span></div>
  <div class="nav-badge">Risk Engine v2</div>
</div>
""", unsafe_allow_html=True)

# ── Two-column layout via st.columns ─────────────────────────────────────────
left_col, right_col = st.columns([3, 2], gap="large")

with left_col:
    st.markdown("""
    <div style="padding: 40px 0 0 0;">
      <div class="panel-eyebrow">Borrower Assessment</div>
      <div class="panel-title">Credit Risk Analysis</div>
      <div class="panel-subtitle">Enter applicant details below to generate an instant risk score powered by our ML model trained on 50,000+ loan records.</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Section 1: Personal & Loan ────────────────────────────────────────────
    st.markdown("""
    <div class="section-header">
      <div class="section-dot"></div>
      <div class="section-label">Personal & Loan Details</div>
      <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        age = st.number_input("Age", min_value=18, max_value=100, step=1, value=28)
    with c2:
        income = st.number_input("Annual Income (₹)", min_value=0, step=10000, value=1200000)
    with c3:
        loan_amount = st.number_input("Loan Amount (₹)", min_value=0, step=10000, value=2560000)

    # Derived LTI ratio
    lti = loan_amount / income if income > 0 else 0
    lti_color = "#E85454" if lti > 5 else "#F5A623" if lti > 3 else "#00D4B8"
    lti_status = "High — review carefully" if lti > 5 else "Moderate" if lti > 3 else "Healthy"
    st.markdown(f"""
    <div class="metric-pill">
      <div>
        <div class="metric-pill-label">Loan-to-Income Ratio</div>
        <div class="metric-pill-sub">{lti_status}</div>
      </div>
      <div class="metric-pill-value" style="color:{lti_color};">{lti:.2f}×</div>
    </div>
    """, unsafe_allow_html=True)

    d1, d2, d3 = st.columns(3)
    with d1:
        residence_type = st.selectbox("Residence Type", ["Owned", "Rented", "Mortgage"])
    with d2:
        loan_purpose = st.selectbox("Loan Purpose", ["Education", "Home", "Auto", "Personal"])
    with d3:
        loan_type = st.selectbox("Loan Type", ["Unsecured", "Secured"])

    # ── Section 2: Repayment Profile ──────────────────────────────────────────
    st.markdown("""
    <div class="section-header">
      <div class="section-dot"></div>
      <div class="section-label">Repayment Profile</div>
      <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    e1, e2, e3 = st.columns(3)
    with e1:
        loan_tenure_months = st.number_input("Tenure (months)", min_value=0, step=1, value=36)
    with e2:
        avg_dpd_per_delinquency = st.number_input("Avg DPD", min_value=0, value=20,
            help="Average Days Past Due per delinquency event")
    with e3:
        delinquency_ratio = st.number_input("Delinquency Ratio (%)", min_value=0, max_value=100, step=1, value=30)

    # ── Section 3: Credit Profile ─────────────────────────────────────────────
    st.markdown("""
    <div class="section-header">
      <div class="section-dot"></div>
      <div class="section-label">Credit Profile</div>
      <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    f1, f2 = st.columns(2)
    with f1:
        credit_utilization_ratio = st.number_input("Credit Utilization (%)", min_value=0, max_value=100, step=1, value=30)
    with f2:
        num_open_accounts = st.number_input("Open Loan Accounts", min_value=1, max_value=4, step=1, value=2)

    # ── CTA button ────────────────────────────────────────────────────────────
    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
    calculate = st.button("⬡  Run Risk Assessment")


# ── Right panel ───────────────────────────────────────────────────────────────
with right_col:
    st.markdown('<div style="padding: 40px 0 0 0;">', unsafe_allow_html=True)

    if calculate:
        probability, credit_score, rating = predict(
            age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
            delinquency_ratio, credit_utilization_ratio, num_open_accounts,
            residence_type, loan_purpose, loan_type
        )

        cfg = get_rating_config(rating)
        prob_pct = probability * 100

        # Animated gauge + stat cards + risk bar — all in one iframe component
        st.markdown('<div class="result-eyebrow">Assessment Result</div>', unsafe_allow_html=True)
        gauge_html = build_animated_gauge(credit_score, rating, cfg["color"], prob_pct)
        components.html(gauge_html, height=520, scrolling=False)

        # Decision banner
        st.markdown(f"""
        <div class="decision-banner" style="background:{cfg['bg']}; border: 1px solid {cfg['border']};">
          <div class="decision-icon">{cfg['icon']}</div>
          <div>
            <div class="decision-title" style="color:{cfg['color']};">{cfg['decision']}</div>
            <div class="decision-body">{cfg['body']}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        # Empty state
        st.markdown("""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center;
                    padding: 80px 20px; text-align:center;">
          <div style="font-size:56px; margin-bottom:24px; opacity:0.2;">⬡</div>
          <div style="font-family:'Space Grotesk',sans-serif; font-size:18px; font-weight:600;
                      color:#2D3748; margin-bottom:10px;">Awaiting Input</div>
          <div style="font-size:13px; color:#1E2A3A; line-height:1.6; max-width:220px;">
            Fill in the applicant details and click <strong style="color:#2D3748;">Run Risk Assessment</strong> to generate a credit score.
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)