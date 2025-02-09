import re

class SCIMToLDAPConverter:
    def __init__(self, scim_filter):
        self.scim_filter = scim_filter

    def convert(self):
        if not self._is_valid_scim_filter(self.scim_filter):
            raise ValueError("Invalid SCIM filter query")
        return self._convert_filter(self.scim_filter)

    def _is_valid_scim_filter(self, filter_str):
        # Enhanced validation for SCIM filter syntax
        pattern = re.compile(r'(\(*\w+\s+(eq|ne|co|sw|ew)\s+"[^"]+"\)*(\s+(and|or)\s+\(*\w+\s+(eq|ne|co|sw|ew)\s+"[^"]+"\)*)*)')
        return bool(pattern.fullmatch(filter_str.strip()))

    def _convert_filter(self, filter_str):
        filter_str = filter_str.strip()
        if filter_str.startswith('(') and filter_str.endswith(')'):
            filter_str = filter_str[1:-1].strip()

        if ' and ' in filter_str.lower():
            parts = self._split_filter(filter_str, 'and')
            return '(&' + ''.join([self._convert_filter(part) for part in parts]) + ')'
        elif ' or ' in filter_str.lower():
            parts = self._split_filter(filter_str, 'or')
            return '(|' + ''.join([self._convert_filter(part) for part in parts]) + ')'
        else:
            return self._convert_expression(filter_str)

    def _split_filter(self, filter_str, operator):
        parts = []
        depth = 0
        current_part = []
        for char in filter_str:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            elif depth == 0 and filter_str.lower().startswith(operator, len(current_part)):
                parts.append(''.join(current_part).strip())
                current_part = []
                continue
            current_part.append(char)
        parts.append(''.join(current_part).strip())
        return parts

    def _convert_expression(self, expression):
        match = re.match(r'(\w+)\s+(eq|ne|co|sw|ew)\s+"([^"]+)"', expression)
        if not match:
            raise ValueError(f"Invalid SCIM expression: {expression}")
        attr, operator, value = match.groups()
        if operator == 'eq':
            return f'({attr}={value})'
        elif operator == 'ne':
            return f'(!({attr}={value}))'
        elif operator == 'co':
            return f'({attr}=*{value}*)'
        elif operator == 'sw':
            return f'({attr}={value}*)'
        elif operator == 'ew':
            return f'({attr}=*{value})'
        else:
            raise ValueError(f"Unsupported SCIM operator: {operator}")
