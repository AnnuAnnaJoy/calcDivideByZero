"""history"""


class History:
    """ This is the History class"""

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
        """Get the count of history calculator stored"""
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
