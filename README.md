# **PredX: AI-Powered Trading SDK** 🚀  

![PredX SDK](https://img.shields.io/badge/Version-0.1.0-blue.svg)  
A Python SDK for interacting with **Prediction Markets & AI-powered Trading Systems**. PredX simplifies API calls for event creation, trading, user balances, and more.  

---

## ✨ **Features**  
✅ **Event Management**: Create & edit prediction markets  
✅ **Trading Automation**: Place market/limit orders effortlessly  
✅ **User Account Management**: Fetch token balances & withdraw USDC  
✅ **Built-in Authentication**: Secure API calls using private key-based auth  
✅ **Simple Integration**: Pythonic SDK design for seamless development  

---

## 📦 **Installation**  
Clone the repository and install the package:  
```sh
git clone https://github.com/Cointegrator/PredXAgent.git
cd PredXAgent
pip install .
```

---

## ⚡ **Quick Start**  
### **1️⃣ Set Up Your Private Key**  
Before running, set your **PRIVATE_KEY** in the environment:  
```sh
export PRIVATE_KEY="your_private_key_here"  # Mac/Linux
$env:PRIVATE_KEY="your_private_key_here"   # Windows (PowerShell)
```

### **2️⃣ Initialize an Agent**  
Create an agent instance to interact with the SDK:  
```python
from predx.agent.agent import Agent

agent = Agent(private_key="your_private_key_here")
print(f"Agent Address: {agent.get_agent_address()}")
```

### **3️⃣ Authenticate & Create an Event**  
```python
from predx.agent.event_agent import EventAgent

event_agent = EventAgent(private_key="your_private_key_here")
auth_token = event_agent.gen_auth_token("SEIV2_TEST")

event_data = {
    "bet_question": "Will Bitcoin reach $100K?",
    "bet_description": "A prediction market on Bitcoin's price movement.",
    "category_list": ["Crypto:Bitcoin"],
    "trade_time": "2025-01-27T07:10:45.893Z",
    "expire_time": "2025-02-13T08:00:00.000Z",
    "pre_trade_yes_price": 0.5,
    "pre_trade_no_price": 0.5,
    "pre_trade_total_share": 100000,
    "chain_name": "SEIV2_TEST",
    "language": "ENGLISH"
}

response = event_agent.create_event(event_data, auth_token=auth_token)
print("✅ Event Created:", response)
```

### **4️⃣ Place a Trade Order**  
```python
from predx.agent.trading_agent import TradingAgent

trading_agent = TradingAgent(private_key="your_private_key_here")
response = trading_agent.place_order(
    bet_key="1711364298281CmOkv6u",
    chain_name="SEIV2_TEST",
    price=50,
    share=1,
    operation=1,  # Buy
    order_mode="Market",
    is_yes=1,  # Yes side
    discount_rate=0,
    auth_token=auth_token
)
print("✅ Order Response:", response)
```

---

## 📌 **Running Example Scripts**  
After setting your private key, you can **quickly test the SDK** using the provided example scripts.  
Run any of the following:
```sh
python examples/create_event_example.py       # Create a new event
python examples/edit_event_example.py         # Edit an existing event
python examples/place_order_example.py        # Place a market order
python examples/get_token_balance_example.py  # Get token balance
python examples/trigger_withdraw_usdc_example.py  # Withdraw USDC
```

These scripts are located in the **`examples/`** folder and are designed for easy testing.  
You can modify the parameters in each file to experiment with different API calls.

---

## 📌 **Available API Methods**
### **Agent Authentication**
- `agent.get_agent_address()` – Returns the agent’s blockchain address.
- `agent.gen_auth_token(chain_name)` – Generates an authentication token for API calls.

### **Event Management**
- `event_agent.create_event(event_data, auth_token)` – Creates a new bet.
- `event_agent.edit_event(event_data, auth_token)` – Edits an existing bet.

### **Trading**
- `trading_agent.place_order(bet_key, chain_name, price, share, operation, order_mode, is_yes, discount_rate, auth_token)`
  - Places an order (Buy/Sell, Market/Limit).

### **User Balances & Withdrawals**
- `agent.get_token_balance(chain_name, auth_token)` – Fetches the user’s token balance.
- `agent.trigger_withdraw_usdc(chain_name, amount, auth_token)` – Withdraws USDC.

---

## 🛠 **Contributing**  
We welcome contributions! Please:  
1. Fork the repository  
2. Create a new branch:  
   ```sh
   git checkout -b feature-branch
   ```
3. Commit changes:  
   ```sh
   git commit -m "Add new feature"
   ```
4. Push to branch:  
   ```sh
   git push origin feature-branch
   ```
5. Open a **Pull Request** 🎉  

---

## 🔗 **Resources**  
- 📖 **Official Docs**: [Coming Soon]  
- 🛠 **API Reference**: https://predxagent.web.app  
- 📨 **Support**: Open an issue on GitHub  

---

## 🏆 **License**  
This project is licensed under **MIT License**.  

---

### **🚀 Start Building with PredX Today!**  
> _Your gateway to AI-powered trading & prediction markets._  
💡 **GitHub**: [repo-link](https://github.com/Cointegrator/PredXAgent.git)  




