from typing import Tuple, Dict

class ResponseHelper:
    @staticmethod
    def default_success_response() -> Tuple[Dict[str, str], int]:
        return {'status': 'success'}, 200

    @staticmethod
    def error_response(e: Exception) -> Tuple[Dict[str, str], int]:
        return {'status': 'error', 'description': str(e)}, 500
