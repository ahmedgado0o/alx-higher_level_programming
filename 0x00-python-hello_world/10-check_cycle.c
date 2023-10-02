#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - checks the cycle
 * @list: list int
 * Return: 0 if ni and 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
