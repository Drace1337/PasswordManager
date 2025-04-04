# Password Manager

Aplikacja do zarządzania hasłami z prostym interfejsem graficznym, generowaniem haseł i ich zapisywaniem w pliku JSON.

## 📌 Funkcje
- Generowanie silnych haseł
- Zapisywanie loginów i haseł w pliku `data.json`
- Wyszukiwanie zapisanych haseł
- Kopiowanie wygenerowanych haseł do schowka

## 🔧 Wymagania
- Python 3.8+
- Tkinter
- Pyperclip
- Dotenv

## 🛠 Instalacja

1. **Sklonuj repozytorium**:
    ```sh
    git clone https://github.com/yourusername/PasswordManager.git
    cd PasswordManager
    ```

2. **Utwórz wirtualne środowisko**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
    ```

3. **Zainstaluj zależności**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Utwórz plik `.env` i dodaj swój email**:
    ```
    EMAIL=your_email@example.com
    ```

## 🚀 Uruchamianie

```sh
python main.py
```

