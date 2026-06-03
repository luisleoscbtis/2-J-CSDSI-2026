import re

class Compiler:

    def compile(self, program):
        ast = self.pass1(program)
        ast = self.pass2(ast)
        return self.pass3(ast)

    def pass1(self, program):
        tokens = self._tokenize(program)
        self.tokens = tokens
        self.pos = 0
        self._expect('[')
        args = []
        while self._peek() != ']':
            args.append(self._consume())
        self._expect(']')
        self.args = args
        return self._parse_expression()

    def _tokenize(self, program):
        return re.findall(r'\[|\]|\(|\)|[+\-*/]|[a-zA-Z]+|\d+', program)

    def _peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def _consume(self):
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def _expect(self, tok):
        assert self._consume() == tok

    def _parse_expression(self):
        node = self._parse_term()
        while self._peek() in ('+', '-'):
            op = self._consume()
            b = self._parse_term()
            node = {'op': op, 'a': node, 'b': b}
        return node

    def _parse_term(self):
        node = self._parse_factor()
        while self._peek() in ('*', '/'):
            op = self._consume()
            b = self._parse_factor()
            node = {'op': op, 'a': node, 'b': b}
        return node

    def _parse_factor(self):
        tok = self._peek()
        if tok == '(':
            self._consume()
            node = self._parse_expression()
            self._expect(')')
            return node
        self._consume()
        if re.match(r'^\d+$', tok):
            return {'op': 'imm', 'n': int(tok)}
        else:
            return {'op': 'arg', 'n': self.args.index(tok)}

    def pass2(self, ast):
        op = ast['op']
        if op in ('+', '-', '*', '/'):
            a = self.pass2(ast['a'])
            b = self.pass2(ast['b'])
            if a['op'] == 'imm' and b['op'] == 'imm':
                result = {
                    '+': a['n'] + b['n'],
                    '-': a['n'] - b['n'],
                    '*': a['n'] * b['n'],
                    '/': int(a['n'] / b['n']),
                }[op]
                return {'op': 'imm', 'n': result}
            return {'op': op, 'a': a, 'b': b}
        return ast

    def pass3(self, ast):
        op = ast['op']
        if op == 'imm':
            return [f"IM {ast['n']}"]
        if op == 'arg':
            return [f"AR {ast['n']}"]
        op_map = {'+': 'AD', '-': 'SU', '*': 'MU', '/': 'DI'}
        return (
            self.pass3(ast['a']) +
            ['PU'] +
            self.pass3(ast['b']) +
            ['SW'] +
            ['PO'] +
            [op_map[op]]
        )