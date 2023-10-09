#include <Python.h>

/**
 * print_python_list_info - Prints basic data about Python lists.
 * @p: A pointer to PyObject list.
 */
void print_python_list_info(PyObject *p)
{
    int listSize, allocation, element;
    PyObject *obj;

    listSize = Py_SIZE(p);
    allocation = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", listSize);
    printf("[*] Allocated = %d\n", allocation);

    for (element = 0; element < listSize; element++)
    {
        printf("Element %d: ", element);

        obj = PyList_GetItem(p, element);
        printf("%s\n", Py_TYPE(obj)->tp_name);
    }
}