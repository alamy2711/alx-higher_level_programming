#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: List's head
 * @number: Number to add
 *
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *tmp, *originHead = *head;

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
			*head = originHead;
			return (newNode);
		}
		*head = (*head)->next;
	}
	newNode->next = NULL;
	(*head)->next = newNode;
	*head = originHead;
	return (newNode);
}
