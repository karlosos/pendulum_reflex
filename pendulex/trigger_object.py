class TriggerObject:
    def __init__(self, theta):
        self.theta = theta
        self.__triggered_flag = False

    def action(self):
        if not self.__triggered_flag:
            self.__triggered_flag = not self.__triggered_flag
            return 1
        return 0
