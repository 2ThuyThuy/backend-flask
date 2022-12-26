user = {"username":"jose", "access_level":"guest"}

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return  func()
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function

@make_secure # validate
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

