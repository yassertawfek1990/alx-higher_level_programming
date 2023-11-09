#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints
 * @p: Pytho
 * Return: n
 */
void print_python_bytes(PyObject *p)
{
	char *st;
	long int s, j, l;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}
	s = ((PyVarObject *)(p))->ob_size;
	st = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", st);
	if (s >= 10)
		l = 10;
	else
		l = s + 1;
	printf("  first %ld bytes:", l);
	for (j = 0; j < l; j++)
		if (st[j] >= 0)
			printf(" %02x", st[j]);
		else
			printf(" %02x", 256 + st[j]);
	printf("\n");
	setbuf(stdout, NULL);
}
/**
 * pf - Printon
 * @p: Pyect
 * Return: norn
 */
void pf(PyObject *p)
{
	double v;
	char *n;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}
	v = ((PyFloatObject *)(p))->ob_fval;
	n = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
	printf("  value: %s\n", n);
	setbuf(stdout, NULL);
}
/**
 * print_python_list - Prin
 * @p: Pyth
 * Return: n
 */
void print_python_list(PyObject *p)
{
	long int s;
	long int j;
	PyListObject *l;
	PyObject *o;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}
	s = ((PyVarObject *)(p))->ob_size;
	l = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", l->allocated);
	for (j = 0; j < s; j++)
	{
		o = l->ob_item[j];
		printf("Element %ld: %s\n", i, ((o)->ob_type)->tp_name);
		if (PyBytes_Check(o))
			print_python_bytes(o);
		if (PyFloat_Check(o))
			print_python_float(o);
	}
	setbuf(stdout, NULL);
}
