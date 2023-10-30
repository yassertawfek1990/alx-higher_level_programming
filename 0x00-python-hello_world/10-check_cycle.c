#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - d
 * @list: linke
 * Return: 1
 */
int check_cycle(listint_t *list)
{
        listint_t *s = list;
        listint_t *f = list;

	while(f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
