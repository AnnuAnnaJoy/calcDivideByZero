"""history"""
from calc.calculation.addition import Addition
from calc.calculation.multiplication import Multiplication
from calc.calculation.subtraction import Subtraction
from calc.calculator import Calculator


class History:
    """ This is the History class"""

    """calculator static property"""
    history = []

    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        """Adding the first result to the history array"""
        return History.history[0].get_result()

    @staticmethod
    def clear_history():
        """Clear history"""
        History.history.clear()
        return True

    @staticmethod
    def history_count():
        """Get the count of history History stored"""
        return len(History.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        """Adding the results to the history array"""
        History.history.append(calculation)
        return True

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        """Adding the last result to the history array"""
        # -1 gets the last item added to the list automatically
        # and you can expect it to have the get result method
        return History.history[-1].get_result()

    @staticmethod
    def get_last_calculation_object():
        """get last calculation"""
        return History.history[-1]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return History.history[num]

    @staticmethod
    def get_last_calculation_result_value():
        """get last calculation"""
        calculation = History.get_last_calculation_object()
        return calculation.get_result()

    @staticmethod
    def get_first_calculation():
        """get first calculation"""
        return History.history[0]

    @staticmethod
    def add_calculation(calculation):
        """ get a generic calculation from history"""
        return History.history.append(calculation)

    @staticmethod
    def add_addition_calculation(values):
        """create an addition and add object to history using factory method create"""
        History.add_calculation(Addition.create(values))
        # Get the result of the calculation
        return True

    @staticmethod
    def add_subtraction_calculation(values):
        """create a subtraction object to history using factory method create"""
        History.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation(values):
        """Add a multiplication object to history using factory method create"""
        History.add_calculation(Multiplication.create(values))
        return True
