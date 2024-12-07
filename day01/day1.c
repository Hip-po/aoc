#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int left;
    int right;
    struct Node *next;
} Node;

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int calculate_total_distance(int *left, int *right, int size) {
    int total_distance = 0;
    for (int i = 0; i < size; i++) {
        total_distance += abs(left[i] - right[i]);
    }
    return total_distance;
}

int get_input(int **left, int **right) {
    char *line = NULL;
    size_t len = 0;
    int size = 0;
    Node *head = NULL, *tail = NULL;

    while (getline(&line, &len, stdin) != -1) {
        Node *new_node = (Node*)malloc(sizeof(Node));
        sscanf(line, "%d %d", &new_node->left, &new_node->right);
        new_node->next = NULL;
        if (tail) {
            tail->next = new_node;
        } else {
            head = new_node;
        }
        tail = new_node;
        size++;
    }
    free(line);

    *left = (int*)malloc(size * sizeof(int));
    *right = (int*)malloc(size * sizeof(int));

    Node *current = head;
    for (int i = 0; i < size; i++) {
        (*left)[i] = current->left;
        (*right)[i] = current->right;
        Node *temp = current;
        current = current->next;
        free(temp);
    }

    return size;
}

int calculate_similarity_score(int *left, int *right, int size) {
    int score = 0;
    for (int i = 0; i < size; i++) {
        int count = 0;
        for (int j = 0; j < size; j++) {
            if (left[i] == right[j]) {
                count++;
            }
        }
        score += left[i] * count;
    }
    return score;
}

int main(int ac, char **av) {
    int *left = NULL;
    int *right = NULL;

    int size = get_input(&left, &right);

    if (ac == 1 && strcmp(av[1], "1") == 0) {
        qsort(left, size, sizeof(int), compare);
        qsort(right, size, sizeof(int), compare);

        printf("Total distance: %d\n", calculate_total_distance(left, right, size));
    } else if (ac > 1 || strcmp(av[1], "2") == 0) {
        printf("Total similarity score: %d\n", calculate_similarity_score(left, right, size));
    } else {
        printf("Invalid argument\n");
    }

    free(left);
    free(right);
    return 0;
}
