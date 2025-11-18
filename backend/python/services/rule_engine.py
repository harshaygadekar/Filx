import json
from typing import List, Dict
from datetime import datetime
import sqlite3
from database.db import get_connection

class RuleEngine:
    def __init__(self):
        self.condition_operators = {
            'equals': lambda a, b: str(a) == str(b),
            'contains': lambda a, b: b in str(a),
            'startswith': lambda a, b: str(a).startswith(str(b)),
            'endswith': lambda a, b: str(a).endswith(str(b)),
            'gt': lambda a, b: float(a) > float(b),
            'lt': lambda a, b: float(a) < float(b),
            'in': lambda a, b: str(a) in str(b).split(','),
        }

    def load_rules(self) -> List[Dict]:
        conn = get_connection()
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
            except json.JSONDecodeError:
                continue

        conn.close()
        return rules

    def evaluate_condition(self, file_info: Dict, condition: Dict) -> bool:
        field = condition.get('field')
        operator = condition.get('operator')
        value = condition.get('value')

        file_value = file_info.get(field, '')

        if operator in self.condition_operators:
            try:
                return self.condition_operators[operator](file_value, value)
            except:
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

        import os
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
