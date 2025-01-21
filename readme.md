# Q-A-Platform


## Installation

To set up the Q-A-Platform locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/HariharanMan/Q-A-Platform.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd Q-A-Platform
   ```
3. **Set Up a Virtual Environment**:
   
   - For Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```
6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

