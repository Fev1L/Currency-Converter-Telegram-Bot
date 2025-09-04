# Currency Converter Telegram Bot

This is a Telegram bot that allows users to convert currencies directly in chat. It supports over 30 currencies, including USD, EUR, JPY, GBP, AUD, CAD, CNY, and more. After entering an amount, the user selects the currency to convert from and the currency to convert to.

## 🛠️ Technologies

* Python 3.x
* [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
* [CurrencyConverter](https://github.com/microservices-xyz/currency-converter)

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/Fev1L/Currency-Converter-Telegram-Bot.git
cd Currency-Converter-Telegram-Bot
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For Windows use `venv\Scripts\activate`
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Get a bot token from [BotFather](https://core.telegram.org/bots#botfather).

5. Create a `.env` file in the root directory and add:

```
TELEGRAM_TOKEN=your_telegram_bot_token
```

6. Run the bot:

```bash
python main.py
```

## 📱 How to Use

1. Start the bot in Telegram or press `/start`.
2. Enter the amount you want to convert.
3. Select the currency you want to convert from.
4. Select the currency you want to convert to.
5. Receive the converted amount with the correct currency symbols.

## ⚙️ Features

* Supports over 30 currencies.
* Interactive currency selection with inline buttons.
* Automatically shows currency symbols.
* Pagination for currency list ("More"/"Less" buttons).
* Limits the number of displayed currencies initially.

## 🧪 Testing

* For testing, you can use [pytest](https://docs.pytest.org/en/stable/).
* Test main functions such as currency conversion, user input handling, and Telegram API interaction.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
