Create a Virtual Environment
    python -m venv venv
Activate Venv
    .\venv\Scripts\Activate.ps1 ----since we are using powershell
Install packages
    pip install requests pytest pytest-html
Freeze requirements
    pip freeze > requirements.txt
Create pytest.ini
    [pytest]
    addopts = -v
----------------------------------------------------------------
🧠 Interview Question

Suppose I ask:

Why did you use dict for bookingdates instead of list?

A good answer would be:

"Because the API returns bookingdates as a JSON object containing checkin and checkout. When parsed by Python, a JSON object becomes a dictionary (dict), whereas a JSON array becomes a list."
-------------------------------------------------------------------
Interview Question

Q: When do you use json= and when do you use data= in the requests library?

Answer:

Use json= when the API expects a JSON request body. It automatically serializes the dictionary and sets Content-Type: application/json.
    Content-Type: application/json
Use data= when the API expects form data, such as application/x-www-form-urlencoded or multipart/form-data.
    Content-Type: application/x-www-form-urlencoded
-----------------------------------------------------------------
        conftest.py---contains fixtures

        Interview Question

Q: How is storing a token in a Pytest fixture different from storing it in a Postman environment variable?

A strong answer would be:

In Postman, I typically store the token in an environment variable so subsequent requests can reuse it. In Pytest, I use a fixture to generate the token and inject it into any test that needs it. This centralizes the authentication logic, reduces duplication, and makes the framework easier to maintain.

-------------------------------------------------------------------

