import pandas as pd
from generaltask import GeneralTask

class TaskAdditional(GeneralTask):
    @staticmethod
    def __call__():
        dtframe = pd.read_csv(r"C:\253504_Vilkina_4\IGI\LR4\additionaltask\Sleep_health_and_lifestyle_dataset.csv")
        print(f"Data Frame:\n{dtframe}")

        params = list(dtframe)
        print(params)

        for param in params:
            print(f"\033[1m \033[92m {param}: \033[00m")
            print(dtframe[param])

        max_heart_rate = dtframe['Heart Rate'].max()
        min_heart_rate = dtframe['Heart Rate'].min()

        print(f"\033[1mМаксимальный сердечный ритм:\033[00m {max_heart_rate}\n\033[1mМинимальный сердечный ритм:\033[00m {min_heart_rate}")
        
        mean_daily_steps_max_heart_rate = dtframe[dtframe['Heart Rate'] == max_heart_rate]['Daily Steps'].mean()
        mean_daily_steps_min_heart_rate = dtframe[dtframe['Heart Rate'] == min_heart_rate]['Daily Steps'].mean()

        print(f"\033[1mСреднее число шагов с max сердечным ритмом:\033[00m {round(mean_daily_steps_max_heart_rate, 2)}\n\033[1mСреднее число шагов с min сердечным ритмом:\033[00m {round(mean_daily_steps_min_heart_rate, 2)}")
        
        ratio = mean_daily_steps_max_heart_rate / mean_daily_steps_min_heart_rate

        print(f"\033[92m\033[1mОтношение среднего числа шагов людей с наивысшим сердечным ритмом к среднему числу шагов с наименьшим ритмом:\033[00m {round(ratio, 2)}")

        mean_sleep = dtframe['Sleep Duration'].mean()
        print(f"\033[1mСредняя продолжительность сна:\033[00m {round(mean_sleep, 2)}")

        mean_activity_less_sleep = dtframe[dtframe['Sleep Duration'] < mean_sleep]['Physical Activity Level'].mean()
        print(f"\033[92m\033[1mАктивность людей, продолжительность сна которых не ниже среднего:\033[00m {round(mean_activity_less_sleep, 2)}")

if __name__ == '__main__':
    task6 = TaskAdditional()
    task6()