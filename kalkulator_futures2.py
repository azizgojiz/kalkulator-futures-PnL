import streamlit as st

def futures_pnl_calculator(entry_price, target_price, stoploss_price, margin, leverage, position_type='long'):
    position_size = margin * leverage
    coin_amount = position_size / entry_price

    if position_type == 'long':
        profit = (target_price - entry_price) * coin_amount
        loss = (entry_price - stoploss_price) * coin_amount
    elif position_type == 'short':
        profit = (entry_price - target_price) * coin_amount
        loss = (stoploss_price - entry_price) * coin_amount
    else:
        return {"error": "Invalid position type. Use 'long' or 'short'."}

    return {
        "Profit jika TP tercapai": round(profit, 2),
        "Kerugian jika SL kena": round(loss, 2),
        "Ukuran Posisi (USDT)": round(position_size, 2),
        "Jumlah Koin": round(coin_amount, 6)
    }

# UI Streamlit
st.title("💹 Kalkulator Profit/Loss Futures Crypto")

entry = st.number_input("📍 Entry Price", value=0.01, step=0.0001)
tp = st.number_input("🎯 Target Price (TP)", value=0.02, step=0.0001)
sl = st.number_input("🛑 Stop Loss (SL)", value=0.009, step=0.0001)
margin = st.number_input("💰 Margin (USDT)", value=10.0, step=1.0)
leverage = st.number_input("📈 Leverage (X)", value=10.0, step=1.0)
position = st.selectbox("📊 Jenis Posisi", ['long', 'short'])

if st.button("🔍 Hitung"):
    result = futures_pnl_calculator(entry, tp, sl, margin, leverage, position)
    st.subheader("📋 Hasil Perhitungan:")
    for k, v in result.items():
        st.write(f"**{k}**: {v}")
