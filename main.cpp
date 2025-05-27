#include <iostream>
#include <chrono>
#include "functions_lab11.h"

int main() {
    int choice;
    std::cout << "1 for first part | 2 for second part: ";
    std::cin >> choice;
    switch (choice) {
        case 1: {
            // func pow iteration and recursive
            double x;
            int n;

            std::cout << "Please enter real number not equal to zero: ";
            std::cin >> x;
            if (x == 0.0) {
                std::cout << "NUM SHOULDNT BE ZERO: ";
                return 1;
            }
            std::cout << "Please enter integer number: ";
            std::cin >> n;

            // время рекурсии
            auto start_rec = std::chrono::high_resolution_clock::now();
            double result_rec = PowRecursion(x, n);
            auto end_rec = std::chrono::high_resolution_clock::now();
            std::chrono::duration<double, std::micro> elapsed_seconds_rec = end_rec - start_rec;

            // время итерации
            auto start_iter = std::chrono::high_resolution_clock::now();
            double result_iter = PowIteration(x, n);
            auto end_iter = std::chrono::high_resolution_clock::now();
            std::chrono::duration<double, std::micro> elapsed_seconds_iter = end_iter - start_iter;


            std::cout << "Recursion - Pow(" << x << ", " << n << ") - is " << result_rec << " \n";
            std::cout << "Time of Recursion: " << elapsed_seconds_rec << " \n\n";

            std::cout << "Iteration - Pow(" << x << ", " << n << ") - is " << result_iter << " \n";
            std::cout << "Time of Iteration: " << elapsed_seconds_iter << " \n";
            break;
        }

        case 2: {
            /*
             * Написать программу, которая создает бинарное дерево, состоящее из целых чисел,
             * которые вводятся с клавиатуры. Затем программа выполняет преобразования в соответствии с номером варианта
             * и печатает все числа исходного и преобразованного бинарного дерева (или другой результат работы программы):
             *
            12) Находит число, ближайшее к среднему арифметическому минимального и максимального чисел в бинарном дереве.
             */
            TreeNode *root = nullptr;
            std::cout << "Enter integer nums for binary tree (0 to stop):\n";
            int number;
            while (std::cin >> number && number != 0) {
                root = insertNode(root, number);
            }
            std::cout << "Original tree (in order):\n";
            PrintInOrder(root);
            std::cout << "\n";

            int min_value = FindMin(root);
            int max_value = FindMax(root);
            double avg_value = (min_value + max_value) / 2.0;

            std::cout << "Minimum value: " << min_value << " \nMaximum value: " << max_value << " \n";
            std::cout << "Average value: " << avg_value << " \n";
            int closest = min_value;
            double min_diff = std::abs(min_value - avg_value);
            FindClosest(root, avg_value, closest, min_diff);

            std::cout << "Closest value is " << closest << " \n";
            FreeMemory(root);
            break;
        }
        default: {
            std::cout << "Please enter a valid choice.";
            break;

        }
    }
    return 0;
}
/*       5
       /   \
      3     8
     /     / \
    1     7  12*/