import csv
import pickle
from inputvalidator import *

event_dates = { 
                20 : {  1914 : 'Начало Первой мировой войны',
                        1939 : 'Начало Второй мировой войны',
                        1994 : 'Принятие Конституции Республики Беларусь'
                        },
                14 : {  1385 : 'Кревская уния',
                        1392 : 'Островское соглашение'                        
                        },
                18 : {  1772 : 'Первый раздел Речи Посполитой',
                        1793 : 'Второй раздел Речи Посполитой',
                        1795 : 'Третий раздел Речи Посполитой' 
                        },
                16 : {  1529 : 'Издание I Статута ВКЛ',
                        1566 : 'Издание II Статута ВКЛ',
                        1588 : 'Издание III Статута ВКЛ'                    
                        }     
              }


class Serializer:
    def pickleSerialize(self, filename):
        with open(filename, 'wb') as pd:
            pickle.dump(event_dates, pd)
            
    def csvSerialize(self, filename):
        with open(filename, 'w', newline='') as cd:
            writer = csv.writer(cd)
            for century, event in event_dates.items():
                writer.writerow([century, event])

    def pickleDeserialize(self, filename):
        with open(filename, 'rb') as pd:
            data = pickle.load(pd)
        return data
    
    def csvDeserialize(self, filename):
        with open(filename, 'r', encoding='utf-8') as cd:
            reader = csv.reader(cd)
            data = dict(reader)
        return data

class EventDictActions:
    def __init__(self, event_dict: dict):
        self._eventsdict = event_dict

    def CenturyEventsList(self, century):
        for cent, dates in self._eventsdict.items():
            if cent == century:
                return dates
        return 'No events in this century'
    
class TaskFirst:
    @staticmethod
    def __call__():
        global event_dates
        event_dates = dict(sorted(event_dates.items()))

        file_serializer = Serializer()
        file_serializer.pickleSerialize('task1/pickle_file.txt')
        file_serializer.csvSerialize('task1/csv_file.csv')

        print(f"\033[92m Pickle deserealized data: \033[00m \n{file_serializer.pickleDeserialize('task1/pickle_file.txt')}")
        print(f"\033[92m CSV deserealized data: \033[00m \n{file_serializer.csvDeserialize('task1/csv_file.csv')}")

        action = EventDictActions(event_dates)
        centuryToFind = inputValidate("\033[1m Enter century: \033[00m", TYPES.INT)

        print(f"\033[92m Events: \033[00m \n{action.CenturyEventsList(centuryToFind)}")