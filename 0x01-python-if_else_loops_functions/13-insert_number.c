#include "lists.h"

/**
 * insert_node - Inserst.
 * @head: A poin
 * @number: Th
 * Return: If 
 * */

listint_t *insert_node(listint_t **head, int number)
{
        listint_t *nd;
	listint_t *g;

	nd = *head;
        g = malloc(sizeof(listint_t));
        if (g == NULL)
                return (NULL);
        g->n = number;
        if (nd == NULL || nd->n >= number)
        {
                g->next = nd;
                *head = g;
                return (g);
        }
        while (nd && nd->next && nd->next->n < number)
                nd = nd->next;
        g->next = nd->next;
        nd->next = g;
        return (g);
}
