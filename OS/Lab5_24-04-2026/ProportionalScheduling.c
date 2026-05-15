#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int n, i, tickets[10], total = 0, sum = 0, win_ticket, winner;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        printf("P%d tickets: ", i + 1);
        scanf("%d", &tickets[i]);
        total += tickets[i];
    }

    srand(time(0));
    win_ticket = (rand() % total) + 1;
    printf("\nTotal Tickets: %d\nWinning Ticket: %d\n", total, win_ticket);

    for (i = 0; i < n; i++) {
        sum += tickets[i];
        if (win_ticket <= sum) {
            winner = i + 1;
            break;
        }
    }

    printf("Winner: Process P%d\n", winner);
    return 0;
}
/* Output:
Enter number of processes: 3
P1 tickets: 10
P2 tickets: 20
P3 tickets: 30

Total Tickets: 60
Winning Ticket: 35
Winner: Process P3
*/