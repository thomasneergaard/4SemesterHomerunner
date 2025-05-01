import custom_exceptions
import loadcells
from queue import Queue

#load = loadcells
queue = Queue(10)
queue_capacity = 10
threshold = 0.6
full_sum = 0
test_weights = [75.2, 76.0, 75.8, 76.5, 77.1]
weight_iterator = iter(test_weights)

#def get_weight_raw():
#    weight = load.get_weight_in_grams()
#    return weight


def get_weight_number():
    #add_number(load.get_weight_in_kg())
    data = next(weight_iterator)
    add_number(data)
    return round(get_queue_average(), 1)

def get_queue_average():
    global full_sum
    global queue

    if queue.qsize() == 0:
        return 0
    return full_sum / queue.qsize()

def number_deviation_high(number: float):
    global queue
    global threshold

    if queue.qsize() < queue_capacity - 1:
        return
    avg = get_queue_average()
    if number > avg + threshold:
        raise custom_exceptions.number_deviation_high(number, avg)

def number_deviation_low(number: float):
    global queue
    global threshold

    if queue.qsize() < queue_capacity - 1:
        return
    avg = get_queue_average()
    if number < avg - threshold:
        raise custom_exceptions.number_deviation_low(number, avg)

rules = {
    "high_deviation": number_deviation_low,
    "low_deviation": number_deviation_high
    }

def add_number(weight_number: float):
    global full_sum
    global queue
    global queue_capacity

    try:
        if queue.qsize() >= queue_capacity and queue.qsize() > 0:
            removed_value = queue.get()
            full_sum -= removed_value

        if queue.qsize() < 5:
            queue.put(weight_number)
            full_sum += weight_number
            return

        number_deviation_high(weight_number)
        number_deviation_low(weight_number)

        queue.put(weight_number)
        full_sum += weight_number

    except custom_exceptions.number_deviation_high as e:
        print(f"Exception Occurred: {e.message} for tal {e.number}, gennemsnit {e.avg}. Prøv igen.")
    except custom_exceptions.number_deviation_low as e:
        print(f"Exception Occurred: {e.message} for tal {e.number}, gennemsnit {e.avg}. Prøv igen.")
    except ValueError:
        print("Ugyldigt input! Indtast venligst et tal.")




def show_queue():
    print("Queue tal: " + str(get_queue_average()))
    print("Queue str: " + str(queue.qsize()))
