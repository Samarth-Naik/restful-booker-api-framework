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

