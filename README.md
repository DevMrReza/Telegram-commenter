# Telegram Commenter Bot 🚀

A powerful, customizable Telegram bot designed to enhance engagement in channels by automatically replying to messages with random comments. With advanced admin controls and a user-friendly setup, this bot is perfect for automating community interactions.

---

## ✨ Features

- **Automatic Engagement**:  
  Automatically replies to messages in target channels with random comments to boost activity.  

- **Advanced Admin Controls**:  
  - Start or stop the bot dynamically.  
  - Add or remove comments from the pool with ease.  
  - View and manage the list of active comments directly via commands.

- **Lightweight & Efficient**:  
  Built with the robust `Telethon` library, ensuring smooth performance and scalability.  

- **Customizable & Secure**:  
  Fully customizable settings with secure admin-only access.

---

## 🛠️ Requirements

- **Python**: Version 3.7 or higher  
- **Telegram API Credentials**:  
  - Obtain `API ID` and `API Hash` from [my.telegram.org](https://my.telegram.org)  
- **Dependencies**:  
  - `Telethon` (Install via `pip install telethon`)

---

## 🚀 Installation & Setup

Follow these steps to set up the bot on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/DevMrReza/Telegram-commenter.git
cd Telegram-commenter


## 📝 Commands

| **Command**           | **Description**                                    |
|------------------------|----------------------------------------------------|
| `/comment on`         | Turn the bot on.                                   |
| `/comment off`        | Turn the bot off.                                  |
| `/add_comment [comment]` | Add a new comment to the list.                   |
| `/remove_comment [index]` | Remove a comment by its index.                  |
| `/list_comments`      | Display the current list of comments.              |
| `/help`               | Show the list of all available commands.           |

