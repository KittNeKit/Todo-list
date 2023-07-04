# Todo-list
This is a simple Todo List project implemented using Python and Django framework. The project allows users to create, manage, and track their tasks in a convenient way.

## Installation
1. Clone the repository:

```bash
git clone https://github.com/your-username/Todo-list
```
2. Change to the project's directory:
```bash
cd Todo-list
```
3. Сopy .env_sample file with your examples of env variables to your .env
file
4. Once you're in the desired directory, run the following command to create a virtual environment:
```bash
python3 -m venv venv
```
5. Activate the virtual environment:

On macOS and Linux:

```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```

4. Install the dependencies

```bash
pip install -r requirements.txt
```

5. Set up the database:

Run the migrations

```bash
python manage.py migrate
```

6. Start the development server

```bash
python manage.py runserver
```

7. Access the website locally at http://localhost:8000.


Enjoy!