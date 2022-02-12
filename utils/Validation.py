import inspect
from typing import Any, List, final
from .Error import Error

class Validation:
    """
    ### Validation class

    This object is intended to be a parent of any other object that needs validation properties, i.e, to be evaluated as valid or invalid.
    It not only provides a boolean evaluation, but also an error code and an error reason aimed to provide additional information of the object validation.

    -----
    Default error codes:
    101 - Variable with incorrect type.
    102 - Variable with incorrect value.
    103 - Variable does not fulfill a condition.
    """
    _valid: bool = True
    _errors: List[Error] = list()

    @property
    def valid(self) -> bool: return self._valid

    @property
    def errors(self) -> Error: return self._errors

    @property
    def errors_code(self) -> int: return [error.code for error in self._errors]

    @property
    def errors_reason(self) -> str: return [error.reason for error in self._errors]

    @property
    def errors_count(self) -> int: return len(self._errors)

    @final
    def get_error_by_code(self, code: int) -> Error or None:
        for _error in self._errors:
            if _error.code == code:
                return _error

        return None
    
    @final
    def get_error_by_tag(self, tag: str) -> Error or None:
        for _error in self._errors:
            if _error.tag == tag:
                return _error
        
        return None

    @final
    def status(self) -> str:
        """
        Returns a string of the object validation. This string is aimed to be informative only, which this method was developed for debugging purposes.
        """
        if self._valid:
            return f"Valid object."
        else:
            output = "###############################################################\n"
            output = output + f"Invalid object. Found {self.errors_count} errors."
            for e_index in range(len(self._errors)):
                output = output + f"\n{e_index}) Error {self._errors[e_index].code}: {self._errors[e_index].reason}"
            output = output + "\n###############################################################\n"
            return output
    
    @final
    def validate(self) -> None:
        """
        Once called, this method should evaluate the multiple validation conditions of a certain object and update its state.

        Initially, this function always sets the object as valid, and then executes the multiple conditions that will prove otherwise if any condition is not valid.

        Note: This function is NOT aimed to be overwritten. If you do, remember to call in the very first line this function.
        """
        self._clear_errors()
        self._validate()
    
    def _validate(self) -> None:
        """
        Function aimed to be overwritten by any child object. It should contain the multiple conditions to evaluate if an object is valid or not.
        """
        pass

    def _validate_type(self, var: Any, var_type: type, tag: str = None) -> bool:
        try:
            self._validate_type_exc(var, var_type)
            self._remove_error(tag)
            return True
        except TypeError:
            self._regist_error(101, f"Variable '{inspect.stack()[1][3]}' has incorrect type. Given/Expected: {type(var).__name__}/{var_type.__name__}", tag)
            return False
    
    def _validate_value(self, var: Any, var_value: Any, tag: str = None) -> bool:
        try:
            self._validate_value_exc(var, var_value)
            self._remove_error(tag)
            return True
        except ValueError:
            self._regist_error(102, f"Variable '{inspect.stack()[1][3]}' has incorrect value. Given/Expected: {var}/{var_value}", tag)
            return False
    
    def _validate_condition(self, var: Any, condition: Any, tag: str = None) -> bool:
        try:
            self._validate_condition_exc(var, condition)
            self._remove_error(tag)
            return True
        except (ValueError, TypeError):
            self._regist_error(102, f"Variable '{inspect.stack()[1][3]}' does not fulfill a condition.", tag)
            return False

    def _validate_type_exc(self, var: Any, var_type: type) -> None:
        if not isinstance(var, var_type): raise TypeError
    
    def _validate_value_exc(self, var: Any, var_value: Any) -> None:
        if not var == var_value: raise ValueError
    
    def _validate_condition_exc(self, var: Any, condition: Any) -> None:
        if not condition(var): raise ValueError
    
    def _regist_error(self, code: int, reason: str, tag: str = None) -> None:
        if not tag: tag = f"{inspect.stack()[2][3]}{inspect.stack()[1][3]}"
        error = Error(code, reason, tag)

        for _error in self._errors:
            if _error.tag == tag:
                # Updates the error
                _error = error
                return # Exits
        
        self._errors.append(error)

        # Updates the validation variable
        self._valid = False

    def _remove_error(self, tag: str = None) -> None:
        if not tag: tag = f"{inspect.stack()[2][3]}{inspect.stack()[1][3]}"

        # Removes the error if exists
        [self._errors.remove(_error) for _error in self._errors if _error.tag == tag]
        
        # Updates the validation variable
        if len(self._errors) == 0: self._valid = True
    
    def _clear_errors(self):
        self._errors.clear()
        self._valid = True
