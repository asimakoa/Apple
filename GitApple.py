import math
import datetime as dt
import streamlit as st
from scipy.stats import norm

# -------------------------------
# Black-76 Call Option Pricing
# -------------------------------
def black76_call(F, K, T, sigma, r):
    """
    Black-76 formula for call option on a forward.
    F : forward price of underlying
    K : strike
    T : time to expiry (in years)
    sigma : volatility (decimal, e.g. 0.25)
    r : risk-free rate (decimal)
    """
    if T <= 0 or sigma <= 0:
        return max(0.0, F - K) * math.exp(-r * T)

    d1 = (math.log(F / K) + 0.5 * sigma**2 * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    call = math.exp(-r * T) * (F * norm.cdf(d1) - K * norm.cdf(d2))
    return call

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("📈 Simple Black-76 Call Option Pricer")

st.write("Enter your parameters below:")

F = st.number_input("Spot / Forward price (F)", min_value=0.01, value=200.0, step=1.0)
K = st.number_input("Strike (K)", min_value=0.01, value=210.0, step=1.0)
T = st.number_input("Time to expiry (years)", min_value=0.0001, value=0.5, step=0.1)
sigma = st.number_input("Volatility (σ, % p.a.)", min_value=0.0001, value=25.0, step=0.1) / 100
r = st.number_input("Risk-free rate (r, % p.a.)", value=4.0, step=0.1) / 100

# Compute price
price = black76_call(F, K, T, sigma, r)

st.success(f"💰 Call Option Price: **{price:.4f}**")

st.caption("Model: Black-76 (lognormal forward). All rates continuously compounded.")
