#include <Python.h>

/**
 * print_python_list_info -  function that print
 * @p: pyt
 */

void print_python_list_info(PyObject *p)
{
	int x;
	int s;
	int a;
	PyObject *t;

	s = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", s);
	a = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", a);
	for (x = 0; x < s; x++)
	{
		printf("Element %d: ", x);
		t = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(t)->tp_name);
	}
}
