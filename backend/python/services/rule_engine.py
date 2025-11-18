import json
import os
import logging
from typing import List, Dict
from datetime import datetime
import sqlite3
from database.db import get_db_connection

logger = logging.getLogger(__name__)

class RuleEngine:
    def __init__(self):
        # BUGFIX: Add safe numeric comparison functions that handle type conversion errors
        def safe_gt(a, b):
            try:
                return float(a) > float(b)
            except (ValueError, TypeError):
                return False

        def safe_lt(a, b):
            try:
                return float(a) < float(b)
            except (ValueError, TypeError):
                return False

        self.condition_operators = {
            'equals': lambda a, b: str(a) == str(b),
            'contains': lambda a, b: b in str(a),
            'startswith': lambda a, b: str(a).startswith(str(b)),
            'endswith': lambda a, b: str(a).endswith(str(b)),
            'gt': safe_gt,
            'lt': safe_lt,
            'in': lambda a, b: str(a) in str(b).split(','),
        }

    def load_rules(self) -> List[Dict]:
        # BUGFIX: Use context manager to prevent connection leaks
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM rules WHERE enabled = 1')

            rules = []
            for row in cursor.fetchall():
                try:
                    rules.append({
                        'id': row[0],
                        'name': row[1],
                        'conditions': json.loads(row[2]) if row[2] else [],
                        'actions': json.loads(row[3]) if row[3] else {},
                    })
                except json.JSONDecodeError as e:
                    logger.warning(f"Failed to parse rule {row[0]}: {e}")
                    continue

        return rules

    def evaluate_condition(self, file_info: Dict, condition: Dict) -> bool:
        field = condition.get('field')
        operator = condition.get('operator')
        value = condition.get('value')

        file_value = file_info.get(field, '')

        if operator in self.condition_operators:
            try:
                return self.condition_operators[operator](file_value, value)
            except (ValueError, TypeError, AttributeError) as e:
                logger.debug(f"Condition evaluation error: {e}")
                return False

        return False

    def evaluate_rule(self, file_info: Dict, rule: Dict) -> bool:
        conditions = rule.get('conditions', [])

        if not conditions:
            return False

        for condition in conditions:
            if not self.evaluate_condition(file_info, condition):
                return False

        return True

    def generate_destination(self, file_info: Dict, rule: Dict, base_path: str) -> str:
        action = rule.get('actions', {})
        dest_template = action.get('destination', 'Organized')

        dest = dest_template
        dest = dest.replace('{extension}', file_info.get('extension', '').lstrip('.'))
        dest = dest.replace('{filename}', file_info.get('filename', ''))
        dest = dest.replace('{year}', datetime.now().strftime('%Y'))
        dest = dest.replace('{month}', datetime.now().strftime('%m'))
        dest = dest.replace('{category}', file_info.get('category', 'Other'))

        # BUGFIX: Import moved to top of file
        return os.path.join(base_path, dest)

    def generate_organization_plan(self, folder_path: str, files: List[Dict]) -> Dict:
        rules = self.load_rules()
        plan = {
            'total_files': len(files),
            'operations': [],
            'summary': {
                'to_move': 0,
                'duplicates': 0,
                'errors': 0,
            }
        }

        for file_info in files:
            for rule in rules:
                if self.evaluate_rule(file_info, rule):
                    destination = self.generate_destination(file_info, rule, folder_path)

                    plan['operations'].append({
                        'source': file_info['path'],
                        'destination': destination,
                        'rule_id': rule['id'],
                        'action': 'move',
                    })

                    plan['summary']['to_move'] += 1
                    break

        return plan

rule_engine = RuleEngine()
