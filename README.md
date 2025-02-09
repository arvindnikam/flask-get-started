# Flask Application

This is a simple Flask application with visit counting and redirection functionality.

## Requirements
- Python 3.x
- Flask

## Installation

1. Clone the repository:
   ```sh
   git clone git@github.com:arvindnikam/flask-get-started.git
   cd flask-get-started
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the application:
   ```sh
   flask run
   ```

## API Endpoints

### Root Endpoint
- `GET /`
  - Returns: "This thing works!"

### Visit Counter
- `GET /get_visits`
  - Returns the current number of visits.
- `GET /visit`
  - Increments the visit count and returns the updated value.
- `GET /set_visits/<visits>`
  - Sets the visit count to the provided value.
  - Returns an error if the value is not a valid integer.
- `GET /set_visits_with_validation/<int:visits>`
  - Sets the visit count with built-in Flask validation.

### URL Redirection
- `GET /goto/<domain>/path/<path:subpath>`
  - Redirects to the specified domain and subpath.
  - Example: `/goto/google.com/path/maps/place/Bengaluru` redirects to `https://google.com/maps/place/Bengaluru`.

## Running on a Different Port
By default, Flask runs on port 5000. You can change it in .env or by running:
```sh
flask run --port=5101
```

## License
This project is licensed under the MIT License.

