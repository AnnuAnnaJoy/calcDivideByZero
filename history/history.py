"""history"""
from calculator.calculator import Calculator


class History:
    """ This is the History class"""

    """calculator static property"""
    history = []

    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        """Adding the first result to the history array"""
        return Calculator.history[0].get_result()

    @staticmethod
    def clear_history():
        """Clear history"""
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        """Get the count of history calculator stored"""
        return len(Calculator.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        """Adding the results to the history array"""
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        """Adding the last result to the history array"""
        # -1 gets the last item added to the list automatically
        # and you can expect it to have the get result method
        return Calculator.history[-1].get_result()

    @staticmethod
    def get_last_calculation_object():
        """get last calculation"""
        return Calculator.history[-1]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculator.history[num]