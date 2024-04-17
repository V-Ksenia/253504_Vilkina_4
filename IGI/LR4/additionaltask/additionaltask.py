import pandas as pd

class TaskAdditional:
    @staticmethod
    def __call__():
        dtframe = pd.read_csv(r"C:\253504_Vilkina_4\IGI\LR4\additionaltask\Sleep_health_and_lifestyle_dataset.csv")
        print(f"Data Frame:\n{dtframe}")

        params = list(dtframe)
        print(params)

        for param in params:
            print(f"\033[1m \033[92m {param}: \033[00m")
            print(dtframe[param])

        max_Tournaments = dtframe['Heart Rate'].max()
        min_Tournaments = dtframe['Heart Rate'].min()

        mean_shot_power_max_Tournaments = dtframe[dtframe['Heart Rate'] == max_Tournaments]['Daily Steps'].mean()
        mean_shot_power_min_Tournaments = dtframe[dtframe['Heart Rate'] == min_Tournaments]['Daily Steps'].mean()

        print(mean_shot_power_max_Tournaments)
        print(mean_shot_power_min_Tournaments)
        ratio = mean_shot_power_max_Tournaments / mean_shot_power_min_Tournaments
        print(round(ratio, 2))

        mean_sleep = dtframe['Sleep Duration'].mean()
        print(mean_sleep)

        mean_activity_less_sleep = dtframe[dtframe['Sleep Duration'] < mean_sleep]['Physical Activity Level'].mean()
        print(round(mean_activity_less_sleep, 2))
if __name__ == '__main__':
    task6 = TaskAdditional()
    task6()