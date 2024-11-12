from flask import jsonify, request
from app.database import update_stats, check_cache, update_cache, get_dna_stats
from app.validators import validate_dna_input
from app.utils import process_dna_matrix

def register_routes(app):
    @app.route('/mutant', methods=['POST'])
    def process_dna():
        """Process DNA sequence to determine if it's mutant"""
        data = request.json
        if not data or 'dna' not in data:
            return jsonify({"error": "No DNA matrix provided"}), 400

        dna_matrix = data['dna']
        
        # Validate input
        is_valid, error_message = validate_dna_input(dna_matrix)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        # Check cache
        cached_result = check_cache(dna_matrix)
        if cached_result is not None:
            return jsonify({"mutant": cached_result}), 200 if cached_result else 403

        try:
            result = process_dna_matrix(dna_matrix)
            is_mutant = len(result['sequences']) >= 1
            
            # Update cache and stats
            update_cache(dna_matrix, is_mutant)
            update_stats('mutant' if is_mutant else 'human')
            
            return jsonify({"mutant": is_mutant}), 200 if is_mutant else 403
        except Exception as e:
            app.logger.error(f"Error processing DNA: {str(e)}")
            return jsonify({"error": str(e)}), 500

    @app.route('/stats', methods=['GET'])
    def get_stats():
        """Get statistics about DNA checks"""
        try:
            stats = get_dna_stats()
            
            mutant_count = stats.get('mutant', 0)
            human_count = stats.get('human', 0)
            ratio = mutant_count / (human_count or 1)
            
            return jsonify({
                "count_mutant_dna": mutant_count,
                "count_human_dna": human_count,
                "ratio": round(ratio, 2)
            })
        except Exception as e:
            app.logger.error(f"Error getting stats: {str(e)}")
            return jsonify({"error": "Failed to retrieve statistics"}), 500
