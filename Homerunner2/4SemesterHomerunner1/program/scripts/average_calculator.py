import custom_exceptions
#import loadcells
from queue import Queue


#load = loadcells
queue = Queue(10)
threshold = 0.6
full_sum = 0
reset_queue = Queue(5)
test_weights = [10, 10, 10, 10, 10, 10.7]
weight_iterator = iter(test_weights)


# Lavet for testing årsager
# Henter en vægt fra loadcells.py or returnerer den i gram
#def get_weight_raw():
#    weight = load.get_weight_in_grams()
#    return weight

# Henter en vægt værdi fra loadcells.py
# Tilføjer værdien til queue og returnerer et afrundet
# gennemsnit af værdier på queue
def get_weight_number():
    #add_number(load.get_weight_in_kg())
    data = next(weight_iterator)
    add_number(data)
    return round(get_queue_average(), 1)


# Returnerer gennemsnit af værdier på queue
def get_queue_average():
    global full_sum
    global queue

    if queue.qsize() == 0:
        return 0
    return full_sum / queue.qsize()

#def weight_reset(weight_number):
  #  global queue
  #  global reset_queue

   # if reset_queue.full():
   #    for queue.qsize in queue:
   #         full_sum -= queue.get()
    #    return True
    #return False

# Tjekker om det aktuelle målte tal er for højt i
# forhold til gennemsnit af tal i queue
# Sammenligner nyeste målte tal med threshold
# kaster exception hvis tallet er for højt
def number_deviation_high(number: float):
    global queue
    global threshold

    #if queue.qsize() < queue.maxsize - 5:
    #    return
    avg = get_queue_average()
    if number > avg + threshold:
        raise custom_exceptions.number_deviation_high(number, avg)

# Tjekker om det aktuelle målte tal er for lavt i
# forhold til gennemsnit af tal i queue
# Sammenligner nyeste målte tal med threshold
# kaster exception hvis tallet er for lavt
def number_deviation_low(number: float):
    global queue
    global threshold
    global full_sum

    #if queue.qsize() < queue.maxsize - 5:
    #    return
    avg = get_queue_average()
    if number < avg - threshold:
        current_average = get_queue_average()
        #loadcells.reset()
        while queue.qsize() != 0:
            removed_value = queue.get()
            full_sum -= removed_value
            #load.reset()
        raise custom_exceptions.number_deviation_low(number, current_average)




# Tilføjer nyeste målte tal til queue, hvis tallet ikke er fejlagtigt
# De første 5 tal bliver tilføjet uanset hvad
# Hvis tallet er ok tilføjes det til queue og full_sum
# Hvis queue har nået maks størrelse vil det forreste tal blive slettet
def add_number(weight_number: float):
    global full_sum
    global queue

    try:
        if queue.qsize() >= queue.maxsize and queue.qsize() > 0:
            removed_value = queue.get()
            full_sum -= removed_value

        if queue.qsize() < 5:
            queue.put(weight_number)
            full_sum += weight_number
            return

        #weight_reset(weight_number)
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


# Lavet til testing, skal nok slettes
def show_queue():
    print("Queue tal: " + str(get_queue_average()))
    print("Queue str: " + str(queue.qsize()))
