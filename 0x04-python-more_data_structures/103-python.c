#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Print
 * @p: A PyObj
 */
void print_python_list(PyObject *p)
{
	int s;
	int a;
	int j;
	const char *t;
	PyListObject *l;
	PyVarObject *v;

	l = (PyListObject *)p;
	v = (PyVarObject *)p;
	s = v->ob_size;
	a = l->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", a);
	for (j = 0; j < s; j++)
	{
		t = l->ob_item[j]->ob_type->tp_name;
		printf("Element %d: %s\n", j, t);
		if (strcmp(t, "bytes") == 0)
			print_python_bytes(l->ob_item[j]);
	}
}

/**
 * print_python_bytes - Printxects.
 * @p: A PyOect.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char s;
	unsigned char j;
	PyBytesObject *b;
	PyVarObject *v;

	v = (PyVarObject *)p;
	b = (PyBytesObject *)p;
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", v->ob_size);
	printf("  trying string: %s\n", b->ob_sval);
	if (v->ob_size > 10)
		s = 10;
	else
		s = (v->ob_size + 1);
	printf("  first %d bytes: ", s);
	for (j = 0; j < s; j++)
	{
		printf("%02hhx", b->ob_sval[j]);
		if (j == (s - 1))
			printf("\n");
		else
			printf(" ");
	}
}
