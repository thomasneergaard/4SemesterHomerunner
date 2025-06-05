from app import custom_exceptions
from queue import Queue

queue = Queue(10)
threshold = 0.6
full_sum = 0
reset_queue = Queue(5)
test_mode = True
if test_mode == False:
    import loadcells
    loadcells = loadcells
else:
    test_weights = [10, 10, 10, 10, 10, 10.7, 11, 12, 15, 11]
    weight_iterator = iter(test_weights)



def get_weight_number():
    if test_mode == False:
        add_number(loadcells.get_weight_in_kg())
    else:
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

    avg = get_queue_average()
    if number > avg + threshold:
        raise custom_exceptions.number_deviation_high(number, avg)

def number_deviation_low(number: float):
    global queue
    global threshold
    global full_sum

    avg = get_queue_average()
    if number < avg - threshold:
        if test_mode == False:
            loadcells.reset()
        while queue.qsize() != 0:
            removed_value = queue.get()
            full_sum -= removed_value
        raise custom_exceptions.number_deviation_low(number, avg)


def add_number(weight_number: float):
    global full_sum
    global queue

    try:
        if queue.qsize() < 5:
            queue.put(weight_number)
            full_sum += weight_number
            return

        if queue.qsize() >= queue.maxsize:
            removed_value = queue.get()
            full_sum -= removed_value

        number_deviation_high(weight_number)
        number_deviation_low(weight_number)

        queue.put(weight_number)
        full_sum += weight_number

    except custom_exceptions.number_deviation_high as e:
        print(f"Exception Occurred: {e.message} for tal {e.number}, gennemsnit {e.avg}. prv igen.")
    except custom_exceptions.number_deviation_low as e:
        print(f"Exception Occurred: {e.message} for tal {e.number}, gennemsnit {e.avg}. prv igen.")
    except ValueError:
        print("Ugyldigt input! Indtast venligst et tal.")


# Lavet til testing, skal nok slettes
def show_queue():
    print("Queue tal: " + str(get_queue_average()))
    print("Queue str: " + str(queue.qsize()))