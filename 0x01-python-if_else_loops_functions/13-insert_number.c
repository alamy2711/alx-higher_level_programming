#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *originHead = *head;
	listint_t *newNode, *tmp;

	if (head == NULL)
		return (NULL);

	newNode = malloc(sizeof(listint_t));

	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	
	if (*head == NULL)
	{
		newNode->next = NULL;
		*head = newNode;
		return (newNode);
	}

	if ((*head)->n > number)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}

	while (*head != NULL)
	{
		if ((*head)->next->n >= number)
		{
			tmp = (*head)->next;
			(*head)->next = newNode;
			newNode->next = tmp;
			break;
		}
		*head = (*head)->next;
	}

	*head = originHead;

	return (newNode);
}
