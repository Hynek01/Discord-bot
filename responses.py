import random
import sympy


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == "ping":  # Removed most of the returns for privacy reasons
        return ""

    # Add a help message that lists all available commands
    if p_message == "$help":
        help_message = "Available Commands:\n"
        help_message += "$calc - calculator\n"
        return help_message

    # Calculator command
    if p_message.startswith("$calc"):
        # Extract the mathematical expression after "$calc"
        expression = p_message[len("$calc") :].strip()
        try:
            # Use SymPy to evaluate the expression
            result = sympy.sympify(expression)
            return f"Result: {result}"
        except Exception as e:
            return f"Error: {str(e)}"
