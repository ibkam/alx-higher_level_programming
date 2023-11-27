#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - check if a singly link list has a cycle
 * @list: head node
 * Return: 1 if there is a cycle or 0 if there is none
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;
	slow = fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return 1;
		}

	}
	return 0;
}
