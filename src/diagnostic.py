

class Diagnostic:
    """
    @file diagnostic.py
    @brief Defines the Diagnostic class for car diagnostics.

    @class Diagnostic
    @brief Represents a diagnostic entry for a car.

    @var id
        Unique identifier for the diagnostic entry.
    @var type
        Type of diagnostic (e.g., error code, sensor reading).
    @var value
        Value associated with the diagnostic (e.g., numeric reading, status).

    @fn __init__(self, diagnostic_id, diagnostic_type, value)
        Initializes a Diagnostic object with the given id, type, and value.

    @param diagnostic_id
        Unique identifier for the diagnostic.
    @param diagnostic_type
        Type of diagnostic.
    @param value
        Value associated with the diagnostic.

    @fn __repr__(self)
        Returns a string representation of the Diagnostic object.
    """
    def __init__(self, diagnostic_id, diagnostic_type, value):
        self.id = diagnostic_id
        self.type = diagnostic_type
        self.value = value

    def __repr__(self):
        return f"Diagnostic(id={self.id}, type={self.type}, value={self.value})"