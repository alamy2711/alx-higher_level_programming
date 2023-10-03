#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: List to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *rabbit = list, *turtle = list;

	if (list == NULL)
		return (0);
	
	while (rabbit != NULL && turtle != NULL && rabbit != NULL)
	{
		rabbit = rabbit->next->next;
		turtle = turtle->next;

		if (rabbit == turtle)
			return (1);
	}

	return (0);
}
