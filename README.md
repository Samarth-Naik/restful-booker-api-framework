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

Fixture scopes (function, module, session).

---------------------------------------------------------------
Interview Question

Q: Why use JSON Schema validation instead of individual assertions?

Answer:

JSON Schema validates the entire response structure, required fields, and data types in one place. It reduces repetitive assertions, improves maintainability, and clearly verifies the API contract.
----------------------------------------------------------------------------------
----schema validation
pip install jsonschema

    from jsonschema import validate
    from schemas.booking_schema import booking_schema

    validate(
        instance=response.json(),
        schema=booking_schema
)
------------------------------------------------------------
Smoke Testing

"Checking whether important things work."

✅ Correct.

A stronger interview answer would be:

Smoke testing is a small subset of critical test cases executed to verify that the application's core functionality is working and the build is stable enough for further testing.

Examples for your Restful Booker framework:

Health check (GET /ping)
Authentication (POST /auth)
Create booking (POST /booking)

If any of these fail, there's little point in running the remaining 200 tests.

Regression Testing

"Check if something is not broken after a fix."

✅ Correct.

A more complete answer:

Regression testing ensures that new code changes, bug fixes, or enhancements have not unintentionally broken existing functionality.

Example:

Developer fixes PATCH API.
You run the entire CRUD suite to ensure GET, POST, PUT, PATCH, and DELETE still work.
Sanity Testing

This one often confuses people.

Think of it like this:

Smoke → Is the whole application stable enough to test?
Sanity → Is the specific change working as expected?

Example:

Developer says:

"I fixed the Update Booking API."

Instead of running everything, you verify:

PUT works
PATCH still works
GET returns updated data

That's a sanity test.
------------------------------------------------------------------------------