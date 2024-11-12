def validate_dna_input(dna_matrix: list) -> tuple[bool, str]:
    """Validate DNA matrix input"""
    if not isinstance(dna_matrix, list):
        return False, "DNA matrix must be a list"
    
    if not dna_matrix:
        return False, "DNA matrix cannot be empty"
    
    if not all(isinstance(row, str) for row in dna_matrix):
        return False, "All DNA matrix elements must be strings"
    
    return True, ""

def validate_dna_matrix(rows: list[str]):
    """
    Validates a DNA matrix for:
    - Non-empty input
    - Equal length rows
    - Valid DNA characters (A, T, C, G only)
    
    Returns None if valid, raises ValueError if invalid
    """
    if not rows:
        raise ValueError("Input matrix cannot be empty")
        
    valid_chars = set('ATCG')
    expected_length = len(rows[0])
    
    for i, row in enumerate(rows):
        # Check row length and characters in one pass
        if len(row) != expected_length:
            raise ValueError(f"Row {i} has length {len(row)}, expected {expected_length}. All rows must have the same length")
        
        invalid_chars = set(row) - valid_chars
        if invalid_chars:
            raise ValueError(f"Invalid characters {invalid_chars} found in row {i}. Only A, T, C, G are allowed")