// Day23.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <list>
#include <vector>

class Cup {
public:
    int value;
    int id; 

    Cup(int _value, int _id) {
        value = _value;
        id = _id;
    }
};

class Clock {
public:
    std::vector<Cup> clock = std::vector<Cup>();
    std::vector<Cup*> oneSmaller = std::vector<Cup*>();
    std::vector<Cup*> next = std::vector<Cup*>();

    Clock(int numberOfCups, std::vector<int> initialValues) {
        for (int index = 0; index < numberOfCups; index++) {
            if (index < initialValues.size()) {
                clock.push_back(Cup(initialValues[index], index));
                oneSmaller.push_back(NULL);
            }
            else {
                clock.push_back(Cup(index + 1, index));
                oneSmaller.push_back(NULL);
            }
        }

        for (int index = 0; index < numberOfCups; index++) {
            // add initialValues.size() + 1 !
            for (int other = 0; other < initialValues.size() + 1; other++) {
                if (index < initialValues.size() + 1) {
                    if (clock[index].value - 1 == clock[other].value) {
                        oneSmaller[index] = &clock[other];
                        break;
                    }
                    oneSmaller[index] = &clock.back();
                    //oneSmaller[index] = &clock[2];
                }
                else {
                    oneSmaller[index] = &clock[index - 1];
                }
            }
        }

        for (int index = 0; index < numberOfCups; index++) {
            if (index < numberOfCups - 1) {
                next.push_back(&clock[index + 1]);
            }
            else {
                next.push_back(&clock[0]);
            }
        }
    }
};

int main()
{
    std::vector<int> initialValues = { 8, 7, 2, 4, 9, 5, 1, 3, 6 };
    //std::vector<int> initialValues = { 3, 8, 9, 1, 2, 5, 4, 6, 7 };
    Clock clock = Clock(1000000, initialValues);

    Cup* current = &clock.clock[0];
    for (int iteration = 0; iteration < 10000001; iteration++) {
        Cup* currentPlusOne = clock.next[current->id];
        Cup* currentPlusTwo = clock.next[currentPlusOne->id];
        Cup* currentPlusThree = clock.next[currentPlusTwo->id];
        Cup* currentPlusFour = clock.next[currentPlusThree->id];

        Cup* minusOne = clock.oneSmaller[current->id];
       
        
        Cup* test = &clock.clock[0];
        
        /*for (int index = 0; index < 9; index++) {
            test = clock.next[test->id];
            std::cout << test->value << ",";
        }
        std::cout << std::endl;*/
        
        while (minusOne == currentPlusOne || minusOne == currentPlusTwo || minusOne == currentPlusThree) {
            if (minusOne == currentPlusOne) {
                minusOne = clock.oneSmaller[minusOne->id];
            }
            if (minusOne == currentPlusTwo) {
                minusOne = clock.oneSmaller[minusOne->id];
            }
            if (minusOne == currentPlusThree) {
                minusOne = clock.oneSmaller[minusOne->id];
            }
        }

        clock.next[currentPlusThree->id] = clock.next[minusOne->id];
        clock.next[current->id] = currentPlusFour;
        clock.next[minusOne->id] = currentPlusOne;
        

        if (!(iteration % 10000)) {
            std::cout << iteration << "\n";
        }

        current = clock.next[current->id];
    }

    Cup* pointer_1 = &clock.clock[6];
    Cup* pointer_next = clock.next[pointer_1->id];
    Cup* pointer_next_next = clock.next[pointer_next->id];

    std::cout << (long long) pointer_next->value * (long long) pointer_next_next->value;

    std::cout << "Hello World!\n";
}
