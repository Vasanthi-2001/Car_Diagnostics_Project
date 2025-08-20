class Diagnostic:
    def __init__(self, diagnostic_id, diagnostic_type, value):
        self.id = diagnostic_id
        self.type = diagnostic_type
        self.value = value

    def __repr__(self):
        return f"Diagnostic(id={self.id}, type={self.type}, value={self.value})"