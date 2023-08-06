#
# Product:   Macal
# Author:    Marco Caspers
# Date:      15-09-2022
#

from __future__ import annotations
import typing
import copy
from . import token
from . import types
from . import exceptions
from . import ast_function_definition
from . import variable

class ValueItem:
    def __init__(self) -> ValueItem:
        self.Value: typing.Any = None
        self.Type: types.VariableType = None
        self.Token: token.LexToken = token.LexToken.nullToken()


    # value is still a python value.
    def setFromMacal(self, tok: token.LexToken, type: types.VariableType, value: typing.Any) -> ValueItem:
        if tok is None:
            tok = token.LexToken.nullToken()
        self.Type = type
        self.Token = tok
        self.Value = value
        return self



    def setFromPython(self, tok: token.LexToken, value: typing.Any) -> ValueItem:
        if tok is None:
            tok = token.LexToken.nullToken()
        self.Type = self.getTypeFromPythonValue(value)
        self.Token = tok
        self.Value = self.fromPython(value).Value
        return self
   


    def getTypeFromPythonValue(self, value: typing.Any) -> types.VariableType:
        if value is None:
            return types.VariableTypes.Nil
        elif isinstance(value, str):
            return types.VariableTypes.String
        elif isinstance(value, int):
            return types.VariableTypes.Int
        elif isinstance(value, float):
            return types.VariableTypes.Float
        elif isinstance(value, bool):
            return types.VariableTypes.Bool
        elif isinstance(value, list):
            return types.VariableTypes.Array
        elif isinstance(value, dict):
            return types.VariableTypes.Record
        # this one is here for set return value from an external library.
        elif isinstance(value, variable.Variable):
            return types.VariableTypes.Variable
        # this one is here for set return value from an external library.
        elif isinstance(value, ast_function_definition.FunctionDefinition):
            return types.VariableTypes.Function
        else:
            raise exceptions.RuntimeError(f"getTypeFromPythonValue() for type {type(value)} Not implemented.", self.Token.Location, None)



    def fromPython(self, val: typing.Any):
        if val is None:
            ret = ValueItem()
            ret.Token = self.Token
            ret.Type = types.VariableTypes.Nil
            ret.Value = types.VariableTypes.Nil
            return ret
        elif isinstance(val, str):
            ret = ValueItem()
            ret.Token = self.Token
            ret.Type = types.VariableTypes.String
            ret.Value = val
            return ret
        elif isinstance(val, int):
            ret = ValueItem()
            ret.Token = self.Token
            ret.Type = types.VariableTypes.Int
            ret.Value = val
            return ret
        elif isinstance(val, float):
            ret = ValueItem()
            ret.Token = self.Token
            ret.Type = types.VariableTypes.Float
            ret.Value = val
            return ret
        elif isinstance(val, bool):
            ret = ValueItem()
            ret.Token = self.Token
            ret.Type = types.VariableTypes.Bool
            ret.Value = val
            return ret
        elif isinstance(val, dict):
            return self.__fromPythonDict(val)
        elif isinstance(val, list):
            return self.__fromPythonList(val)
        # this one is here for set return value from an external library.
        elif isinstance(val, variable.Variable):
            return val
        # this one is here for set return value from an external library.
        elif isinstance(val, ast_function_definition.FunctionDefinition):
            return val
        elif isinstance(val, ValueItem):
            print("Debug: ValueItem.fromPython(value) value is ValueItem, this is a bug that should be fix, take notes!")
            ret = val.clone()
        else:
            raise exceptions.RuntimeError(f"setValue() for type {type(val)} Not implemented.", self.Token.Location, None)



    def __fromPythonList(self, val: list) -> ValueItem:
        res = []
        for v in val:
            res.append(self.fromPython(v))
        ret = ValueItem()
        ret.Token = self.Token
        ret.Type = types.VariableTypes.Array
        ret.Value = res
        return ret



    def __fromPythonDict(self, val: dict) -> ValueItem:
        res = {}
        for (k, v) in val.items():
            res[k] = self.fromPython(v)
        ret = ValueItem()
        ret.Token = self.Token
        ret.Type = types.VariableTypes.Record
        ret.Value = res
        return ret



    def setValue(self, tok: token.LexToken, type: types.VariableType, filename: str) -> None:
        self.Token = tok
        self.Type = type
        if self.Type == types.VariableTypes.Int:
            self.Value = int(tok.Lexeme)
        elif self.Type == types.VariableTypes.Float:
            self.Value = float(tok.Lexeme)
        elif self.Type == types.VariableTypes.Bool:
            self.Value = tok.Lexeme == 'true'
        elif self.Type == types.VariableTypes.String:
            self.Value = tok.Lexeme
        elif self.Type == types.VariableTypes.Array:
            self.Value = tok.Lexeme
        elif self.Type == types.VariableTypes.Record:
            self.Value = tok.Lexeme
        elif self.Type == types.VariableTypes.Nil:
            self.Value = 'nil'
        else:
            raise exceptions.RuntimeError(f"Invalid value type ({self.Type}).", tok.Location, filename)



    def __repr__(self) -> str:
        return f'ValueItem(token={self.Token}, value={self.Value}, type={self.Type});'



    def __eq__(self, other: ValueItem) -> ValueItem:
        res = ValueItem()
        res.Type = types.VariableTypes.Bool
        res.Token = self.Token.Clone()
        res.Value = self.Value == other.Value
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res


    
    def __add__(self, other) -> ValueItem:
        res = ValueItem().setFromMacal(self.Token.Clone(), 
            types.VariableTypes.Float if self.Type == types.VariableTypes.Int and other.Type == types.VariableTypes.Float else self.Type,
            self.Value + other.Value)
        res.Token.Lexeme = f'{res.Value}'
        return res



    def __sub__(self, other: ValueItem):
        res = ValueItem().setFromMacal(self.Token.Clone(), 
            types.VariableTypes.Float if self.Type == types.VariableTypes.Int and other.Type == types.VariableTypes.Float else self.Type,
            self.Value - other.Value)
        res.Token.Lexeme = f'{res.Value}'
        return res



    def __mul__(self, other: ValueItem) -> ValueItem:
        res = ValueItem()
        res = ValueItem().setFromMacal(self.Token.Clone(), 
            types.VariableTypes.Float if self.Type == types.VariableTypes.Int and other.Type == types.VariableTypes.Float else self.Type,
            self.Value * other.Value)
        res.Token.Lexeme = f'{res.Value}'
        return res



    def __pow__(self, other: ValueItem) -> ValueItem:
        res = ValueItem()
        res = ValueItem().setFromMacal(self.Token.Clone(), 
            types.VariableTypes.Float if self.Type == types.VariableTypes.Int and other.Type == types.VariableTypes.Float else self.Type,
            self.Value ** other.Value)
        res.Token.Lexeme = f'{res.Value}'
        return res



    def __mod__(self, other: ValueItem) -> ValueItem:
        if other.Value == 0 or other.Value == 0.0:
            raise exceptions.RuntimeError(f"Division by zero.", other.Token.Location, None)
        res = ValueItem()
        res = ValueItem().setFromMacal(self.Token.Clone(), 
            types.VariableTypes.Int,
            self.Value % other.Value)
        res.Token.Lexeme = f'{res.Value}'
        return res



    def __truediv__(self, other: ValueItem) -> ValueItem:
        if other.Value == 0 or other.Value == 0.0:
            raise exceptions.RuntimeError(f"Division by zero.", other.Token.Location, None)
        res = ValueItem().setFromMacal(self.Token.Clone(), types.VariableTypes.Float, self.Value / other.Value)
        res.Token.Lexeme = f'{res.Value}'
        return res



    def __gt__(self, other: ValueItem) -> ValueItem:
        res = ValueItem().setFromMacal(self.Token.Clone(), types.VariableTypes.Bool, self.Value > other.Value)
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res
    


    def __lt__(self, other: ValueItem) -> ValueItem:
        res = ValueItem().setFromMacal(self.Token.Clone(), types.VariableTypes.Bool, self.Value < other.Value)
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res


    
    def __ge__(self, other: ValueItem) -> ValueItem:
        res = ValueItem().setFromMacal(self.Token.Clone(), types.VariableTypes.Bool, self.Value >= other.Value)
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res



    def __le__(self, other: ValueItem) -> ValueItem:
        res = ValueItem().setFromMacal(self.Token.Clone(), types.VariableTypes.Bool, self.Value <= other.Value)
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res



    def __ne__(self, other: ValueItem) -> ValueItem:
        res = ValueItem().setFromMacal(self.Token.Clone(), types.VariableTypes.Bool, self.Value != other.Value)
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res



    def __and__(self, other: ValueItem) -> ValueItem:
        res = ValueItem().setFromMacal(self.Token.Clone(), types.VariableTypes.Bool, self.Value and other.Value)
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res



    def __or__(self, other: ValueItem) -> ValueItem:
        res = ValueItem().setFromMacal(self.Token.Clone(), types.VariableTypes.Bool, self.Value or other.Value)
        res.Token.Lexeme = 'true' if res.Value else 'false'
        res.Token.Type = types.LexTokenTypes.Identifier
        return res


    
    def clone(self) -> ValueItem:
        return copy.deepcopy(self)


    def __str__(self) -> str:
        res = f'ValueItem(token={self.Token}, type={self.Type}, value='
        if self.Type == types.VariableTypes.Array:
            res = f'{res}[\n'
            for v in self.Value:
                res = f'{res}    {v}\n'
            res = f'{res}]);'
        elif self.Type == types.VariableTypes.Record:
            res = f'{res}{{\n'
            for (k,v) in self.Value.items():
                res = f'{res}    "{k}":{v}\n'
            res = f'{res}}});'
        else:
            res = f'{res}{self.Value});'
        return res
