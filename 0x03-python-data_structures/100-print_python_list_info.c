
#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info -  function that print
 * @p: pyt
 */

void print_python_list_info(PyObject *p)
{
	long int x;
	long int s;
	PyListObject *l;
	PyObject *t;

	s = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", s);
	l = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", l->allocated);
	for (x = 0; x < s; x++)
	{
		t = PyList_GetItem(p, x);
		printf("Element %ld: %s\n", x, Py_TYPE(t)->tp_name);
	}
}
