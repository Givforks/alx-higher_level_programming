#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome in c
 *
 * @head: the head address of the linked list
 *
 * Return: 1 if it's a palindrome, 0 else
 */

int is_palindrome(listint_t **head)
{
	listint_t *cur = *head;
	int tab[2048], k = 0, l = 0;

	if (*head)
	{
		while (cur)
		{
			tab[k] = cur->n;
			cur = cur->next;
			k++;
		}

		while (l < k / 2)
		{
			if (tab[l] == tab[k - l - 1])
				l++;
			else
				return (0);
		}
	}
	return (1);
}
