# Password Manager 

A simple password management application with a graphical user interface, password generation, and JSON-based storage.

## 📌 Features
- Strong password generation
- Saving login credentials in `data.json`
- Searching for saved passwords
- Copying generated passwords to the clipboard

## 🔧 Requirements
- Python 3.8+
- Tkinter
- Pyperclip
- Dotenv

## 🛠 Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/PasswordManager.git
    cd PasswordManager
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file and add your email**:
    ```
    EMAIL=your_email@example.com
    ```

## 🚀 Running the Application

```sh
python main.py
```
