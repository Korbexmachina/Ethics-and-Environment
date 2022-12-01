class scenario:
    def __init__(self, body, option1, option2, option1_env, option1_money, option2_env, option2_money) -> None:
        """Initializes a new scenario

        Args:
            body (str): The body text for the scenario
            option1 (str): The first option
            option2 (str): The second option
            option1_impact (int): The impact that the first choice will have on the points total
            option2_impact (int): The impact that the second choice will have on the points total
        """
        self.body = body
        self.option1 = option1
        self.option2 = option2
        self.option1_impact = option1_env
        self.option1_impact = option1_money
        self.option2_impact = option2_env
        self.option2_impact = option2_money
    
    def __str__(self) -> None:
        """Prints the scenario, along with the options
        """
        print(self.body)
        print("\n---\n")
        print(f"Option 1: {self.option1}\nOption 2: {self.option2}")
        
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
