class QueryBuilder:
    @staticmethod
    def build(coverage_id, operations, output_format=None):
        query_parts = [f"for $c in ({coverage_id})"]
        expression = "$c"

        for operation in operations:
            if operation['type'] == 'subset':
                expression += f"[{operation['params']}]"
            elif operation['type'] in ['min', 'max', 'avg', 'count']:
                expression = f"{operation['type']}({expression})"
            elif operation['type'] == 'convert_celsius_to_kelvin':
                expression = f"({expression} + 273.15)"
            elif operation['type'] == 'on_the_fly_coloring':
                expression = f"switch {operation['params']}"
            elif operation['type'] == 'coverage_constructor':
                expression = operation['params']

        if output_format is not None:
            query_parts.append(f"return encode({expression}, \"{output_format}\")")
        else:
            query_parts.append(f"return {expression}")

        return " ".join(query_parts)
