# 실버3
def main():
    from collections import deque

    my_classes, my_mileage = map(int, input().split())

    max_success_result = 0
    application_info = []
    mileage_histories = []
    minimum_mileages = []

    for i in range(my_classes):
        applicants, maximum = map(int, input().split())
        application_info.append((applicants, maximum))

        mileage_history = sorted(list(map(int, input().split())), reverse=True)
        mileage_histories.append(mileage_history)
        pass

    for index, a_info in enumerate(application_info):
        applicants, maximum = a_info
        mileage_history = mileage_histories[index]
        minimum_mileage = 0

        if applicants < maximum:
            minimum_mileage = 1
        if applicants == maximum:
            minimum_mileage = mileage_history[applicants - 1]
        if applicants > maximum:
            minimum_mileage = mileage_history[maximum - 1]
        
        minimum_mileages.append(minimum_mileage)

    minimum_mileages.sort()

    for minimum_mileage in minimum_mileages:
        if my_mileage >= minimum_mileage:
            my_mileage -= minimum_mileage
            max_success_result += 1
        else:
            break
    
    
    print(max_success_result)
    pass

main()