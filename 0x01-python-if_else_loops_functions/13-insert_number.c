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
	listint_t *newNode, *curr = *head;

	if (head == NULL)
		return (NULL);

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	if (curr == NULL)
	{
		newNode->next = NULL;
		curr = newNode;
		return (newNode);
	}

	if (curr->n > number)
	{
		newNode->next = curr;
		curr = newNode;
		return (newNode);
	}

	while (curr != NULL)
	{
		if (curr->next->n >= number)
		{
			newNode->next = curr->next;
			curr->next = newNode;
			return (newNode);
		}
		*head = (*head)->next;
	}
	newNode->next = NULL;
	curr->next = newNode;
	return (newNode);
}
