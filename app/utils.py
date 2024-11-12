from app.validators import validate_dna_matrix

def process_dna_matrix(rows: list[str] ) -> dict:
    """
    Process a DNA matrix tofind sequences of 4 identical characters in all directions.
    
    Args:
        rows (list): List of strings, where each string represents a row of nucleotides
        
    Returns:
        dict: Dictionary containing analysis results and found sequences
    """
    
    validate_dna_matrix(rows)
    
    height = len(rows)
    width = len(rows[0])
    
    # Create a matrix NxN
    matrix = [list(row) for row in rows]
    
    def check_sequence(x, y, dx, dy):
        """
        Check if there's a sequence of 4 identical characters starting at (x,y) in direction (dx,dy)
        """
        # Check boundaries
        if (0 <= x + 3*dx < height and 0 <= y + 3*dy < width):
            # Get the sequence of characters in the direction
            chars = [matrix[x + i*dx][y + i*dy] for i in range(4)]
            if all(c == chars[0] for c in chars):
                return {
                    'char': chars[0],
                    'positions': [(x + i*dx, y + i*dy) for i in range(4)],
                    'direction': 'diagonal' if dx != 0 and dy != 0 else 'vertical' if dx != 0 else 'horizontal'
                }
        return None
    
    # Find all sequences
    sequences = []

    # I only need to check secuence to right, down and the diagonal right and left
    directions = [(0,1), (1,0), (1,1), (1,-1)]
    
    for i in range(height):
        for j in range(width):
            for dx, dy in directions:
                sequence = check_sequence(i, j, dx, dy)
                if sequence:
                    sequences.append(sequence)
    results = {
        'dimensions': (height, width),
        'matrix': rows,
        'sequences': sequences
    }
    return results