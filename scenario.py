class Scenario:
    def __init__(self, body, option1, option2, option1_env, option1_money, option2_env, option2_money, face_name) -> None:
        """Initializzes a new scenario

        Args:
            body (str): The body text of the scenario
            option1 (str): The first option
            option2 (str): The second option
            option1_env (int): The impact of the first option on the environment variable
            option1_money (int): The impact of the first option on the money variable
            option2_env (int): The impact of the second option on the environment variable
            option2_money (int): The impact of the third option on the money variable
            face_name (str): The face and name of the character in the scenario
        """
        self.body = body
        self.option1 = option1
        self.option2 = option2
        self.option1_env = option1_env
        self.option1_money = option1_money
        self.option2_env = option2_env
        self.option2_money = option2_money
        self.face_name = face_name
    
    def __str__(self) -> str:
        """Returns a string representation of the scenario

        Returns:
            str: The string representation of the scenario
        """
        return f"{self.body}\n{self.face_name}\n---\nOption 1: {self.option1}\nOption 2: {self.option2}"
        
    def option1_picked(self, environment, money) -> tuple:
        """Adjusts the total number of points

        Args:
            points (int): The total number of points

        Returns:
            int: the new number of points after adding option1_impact to the total
        """
        return (environment + self.option1_env), (money + self.option1_money)
        
    def option2_picked(self, environment, money) -> tuple:
        """Adjusts the total number of points

        Args:
            points (int): The total number of points

        Returns:
            int: the new number of points after adding option2_impact to the total
        """
        return (environment + self.option2_env), (money + self.option2_money)
